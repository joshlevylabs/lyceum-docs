import http.server
import socketserver
import webbrowser
import os
import subprocess
import sys
import tempfile
import shutil

# Determine if running as a PyInstaller bundle
if getattr(sys, 'frozen', False):
    # Path to the directory containing the executable
    BASE_PATH = os.path.dirname(sys.executable)
    # Temporary directory where PyInstaller extracts bundled files
    RESOURCE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_PATH = BASE_PATH

PORT = 8004
DIRECTORY = "site"  # Serve the built site
MKDOCS_CONFIG = os.path.join(RESOURCE_PATH, "mkdocs.yml")
DOCS_DIR = os.path.join(RESOURCE_PATH, "docs")

def build_mkdocs():
    """Build the MkDocs site using the bundled config and docs."""
    try:
        # Create a temporary working directory
        temp_dir = tempfile.mkdtemp()
        # Copy mkdocs.yml and docs/ to the temp directory
        shutil.copy(MKDOCS_CONFIG, temp_dir)
        shutil.copytree(DOCS_DIR, os.path.join(temp_dir, "docs"))
        
        # Change to the temp directory and build the site
        os.chdir(temp_dir)
        result = subprocess.run(['mkdocs', 'build'], check=True, capture_output=True, text=True)
        print(result.stdout)
        
        # Copy the generated site/ back to BASE_PATH
        site_dir = os.path.join(temp_dir, "site")
        if os.path.exists(site_dir):
            shutil.copytree(site_dir, os.path.join(BASE_PATH, "site"), dirs_exist_ok=True)
    except subprocess.CalledProcessError as e:
        print(f"Error building MkDocs site: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'mkdocs' command not found. Please ensure MkDocs is installed on the system.")
        sys.exit(1)
    finally:
        # Clean up temp directory
        os.chdir(BASE_PATH)
        shutil.rmtree(temp_dir, ignore_errors=True)

# Ensure the site directory exists (build it if not)
site_path = os.path.join(BASE_PATH, DIRECTORY)
if not os.path.exists(site_path):
    print(f"'{DIRECTORY}' directory not found. Building the site...")
    build_mkdocs()
elif not os.listdir(site_path):  # If directory is empty
    print(f"'{DIRECTORY}' directory is empty. Building the site...")
    build_mkdocs()

# Custom handler to serve files from the site directory
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=site_path, **kwargs)

# Start the server and open the browser
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Lyceum API documentation at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()