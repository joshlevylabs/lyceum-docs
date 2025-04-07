# Script to generate authentication.md with proper Markdown formatting

# Define each section as a string
title = "# Authentication\n\n"

description = (
    "The Lyceum API uses token-based authentication. To access protected endpoints, "
    "you must obtain an access token by logging in with your credentials. The access "
    "token is short-lived, and a refresh token is provided to obtain a new access token "
    "without re-entering credentials.\n\n"
)

base_url = (
    "## Base URL\n\n"
    "All API endpoints are relative to a base URL. The default base URL is "
    "`https://api.thelyceum.io/api`. However, this can be overridden by setting the "
    "`LYCEUM_API_BASE` environment variable. Ensure you use the correct base URL for "
    "your environment.\n\n"
)

# Login Section
login = (
    "## Login\n\n"
    "To authenticate and obtain access and refresh tokens, send a POST request to "
    "`/account/login` with your email and password.\n\n"
)

login_request = (
    "### Request\n\n"
    "- **Method:** POST\n"
    "- **URL:** `/account/login`\n"
    "- **Headers:**\n"
    "  - `Content-Type: application/json`\n"
    "- **Body:**\n"
    "```json\n"
    "{\n"
    "  \"email\": \"your_email@example.com\",\n"
    "  \"password\": \"your_password\"\n"
    "}\n"
    "```\n\n"
)

login_response = (
    "### Response\n\n"
    "- **Status Code:** 200 OK\n"
    "- **Body:**\n"
    "```json\n"
    "{\n"
    "  \"access\": \"your_access_token\",\n"
    "  \"refresh\": \"your_refresh_token\"\n"
    "}\n"
    "```\n\n"
)

login_examples = (
    "### Examples\n\n"
    "#### cURL\n\n"
    "```bash\n"
    "curl -X POST https://api.thelyceum.io/api/account/login \\\n"
    "  -H \"Content-Type: application/json\" \\\n"
    "  -d '{\"email\": \"your_email@example.com\", \"password\": \"your_password\"}'\n"
    "```\n\n"
    "#### Python\n\n"
    "```python\n"
    "import requests\n\n"
    "url = \"https://api.thelyceum.io/api/account/login\"\n"
    "data = {\"email\": \"your_email@example.com\", \"password\": \"your_password\"}\n"
    "headers = {\"Content-Type\": \"application/json\"}\n"
    "response = requests.post(url, json=data, headers=headers)\n"
    "print(response.json())\n"
    "```\n\n"
    "#### JavaScript\n\n"
    "```javascript\n"
    "fetch(\"https://api.thelyceum.io/api/account/login\", {\n"
    "  method: \"POST\",\n"
    "  headers: {\n"
    "    \"Content-Type\": \"application/json\"\n"
    "  },\n"
    "  body: JSON.stringify({\n"
    "    email: \"your_email@example.com\",\n"
    "    password: \"your_password\"\n"
    "  })\n"
    "})\n"
    ".then(response => response.json())\n"
    ".then(data => console.log(data));\n"
    "```\n\n"
)

login_errors = (
    "### Common Error Responses\n\n"
    "- **400 Bad Request:** Invalid request format or missing fields (e.g., email or password not provided).\n"
    "- **401 Unauthorized:** Incorrect email or password.\n\n"
)

login_section = login + login_request + login_response + login_examples + login_errors

# Token Refresh Section
token_refresh = (
    "## Token Refresh\n\n"
    "To obtain a new access token when the current one expires, send a POST request to "
    "`/account/token/refresh` with your refresh token.\n\n"
)

token_refresh_request = (
    "### Request\n\n"
    "- **Method:** POST\n"
    "- **URL:** `/account/token/refresh`\n"
    "- **Headers:**\n"
    "  - `Content-Type: application/json`\n"
    "- **Body:**\n"
    "```json\n"
    "{\n"
    "  \"refresh\": \"your_refresh_token\"\n"
    "}\n"
    "```\n\n"
)

token_refresh_response = (
    "### Response\n\n"
    "- **Status Code:** 200 OK\n"
    "- **Body:**\n"
    "```json\n"
    "{\n"
    "  \"access\": \"new_access_token\"\n"
    "}\n"
    "```\n\n"
)

token_refresh_examples = (
    "### Examples\n\n"
    "#### cURL\n\n"
    "```bash\n"
    "curl -X POST https://api.thelyceum.io/api/account/token/refresh \\\n"
    "  -H \"Content-Type: application/json\" \\\n"
    "  -d '{\"refresh\": \"your_refresh_token\"}'\n"
    "```\n\n"
    "#### Python\n\n"
    "```python\n"
    "import requests\n\n"
    "url = \"https://api.thelyceum.io/api/account/token/refresh\"\n"
    "data = {\"refresh\": \"your_refresh_token\"}\n"
    "headers = {\"Content-Type\": \"application/json\"}\n"
    "response = requests.post(url, json=data, headers=headers)\n"
    "print(response.json())\n"
    "```\n\n"
    "#### JavaScript\n\n"
    "```javascript\n"
    "fetch(\"https://api.thelyceum.io/api/account/token/refresh\", {\n"
    "  method: \"POST\",\n"
    "  headers: {\n"
    "    \"Content-Type\": \"application/json\"\n"
    "  },\n"
    "  body: JSON.stringify({\n"
    "    refresh: \"your_refresh_token\"\n"
    "  })\n"
    "})\n"
    ".then(response => response.json())\n"
    ".then(data => console.log(data));\n"
    "```\n\n"
)

token_refresh_errors = (
    "### Common Error Responses\n\n"
    "- **400 Bad Request:** Invalid or missing refresh token.\n"
    "- **401 Unauthorized:** Refresh token is expired or invalid.\n\n"
)

token_refresh_section = (
    token_refresh + token_refresh_request + token_refresh_response +
    token_refresh_examples + token_refresh_errors
)

# User Information Section
user_info = (
    "## User Information\n\n"
    "To retrieve user details, including verification status, send a GET request to "
    "`/account/me/` with the access token in the Authorization header.\n\n"
)

user_info_request = (
    "### Request\n\n"
    "- **Method:** GET\n"
    "- **URL:** `/account/me/`\n"
    "- **Headers:**\n"
    "  - `Authorization: Bearer your_access_token`\n\n"
)

user_info_response = (
    "### Response\n\n"
    "- **Status Code:** 200 OK\n"
    "- **Body:**\n"
    "```json\n"
    "{\n"
    "  \"id\": \"user_id\",\n"
    "  \"email\": \"your_email@example.com\",\n"
    "  \"is_verified\": true\n"
    "}\n"
    "```\n"
    "*Note: Additional fields may be present in the response.*\n\n"
)

user_info_examples = (
    "### Examples\n\n"
    "#### cURL\n\n"
    "```bash\n"
    "curl -X GET https://api.thelyceum.io/api/account/me/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\"\n"
    "```\n\n"
    "#### Python\n\n"
    "```python\n"
    "import requests\n\n"
    "url = \"https://api.thelyceum.io/api/account/me/\"\n"
    "headers = {\"Authorization\": \"Bearer your_access_token\"}\n"
    "response = requests.get(url, headers=headers)\n"
    "print(response.json())\n"
    "```\n\n"
    "#### JavaScript\n\n"
    "```javascript\n"
    "fetch(\"https://api.thelyceum.io/api/account/me/\", {\n"
    "  method: \"GET\",\n"
    "  headers: {\n"
    "    \"Authorization\": \"Bearer your_access_token\"\n"
    "  }\n"
    "})\n"
    ".then(response => response.json())\n"
    ".then(data => console.log(data));\n"
    "```\n\n"
)

user_info_errors = (
    "### Common Error Responses\n\n"
    "- **401 Unauthorized:** Access token is missing, invalid, or expired.\n"
    "- **403 Forbidden:** User lacks permission to access this resource.\n\n"
)

verification_status = (
    "### Verification Status\n\n"
    "The `is_verified` field in the response indicates whether the user’s account is "
    "verified. Some API endpoints or features may require verification. If "
    "`is_verified` is `false`, access to certain functionalities may be restricted.\n\n"
)

user_info_section = (
    user_info + user_info_request + user_info_response + user_info_examples +
    user_info_errors + verification_status
)

# Notes Section
notes = (
    "## Notes\n\n"
    "- **Token Storage:** The script uses a `SecureStorage` class to encrypt and store "
    "tokens locally. In your application, ensure tokens are stored securely (e.g., "
    "encrypted storage or secure keychains) to prevent unauthorized access.\n"
    "- **Environment Variables:** The script supports pre-filling credentials via "
    "`LYCEUM_LOGIN_USERNAME` and `LYCEUM_LOGIN_PASSWORD` environment variables, "
    "though these are optional.\n"
    "- **Additional Headers:** The script sets `Cache-Control` and `User-Agent` headers "
    "for the `/account/me/` request. These are not strictly required for basic "
    "authentication but may be included for compatibility or caching control if needed.\n"
)

# Combine all sections
full_content = (
    title + description + base_url + login_section + token_refresh_section +
    user_info_section + notes
)

# Write the content to authentication.md
with open("authentication.md", "w") as file:
    file.write(full_content)

# Optional: Print a message to confirm
print("authentication.md has been generated successfully.")