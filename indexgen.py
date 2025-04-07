# Script to generate index.md with proper Markdown formatting for Lyceum API documentation

# Define each section as a string with Markdown formatting
title = "# Lyceum API Documentation\n\n"

introduction = (
    "## Introduction\n\n"
    "Welcome to the Lyceum API documentation. This API provides a powerful interface for interacting with the Lyceum platform, "
    "enabling seamless data management and integration capabilities.\n\n"
)

purpose = (
    "## Purpose\n\n"
    "The Lyceum API is designed to facilitate:\n"
    "- **Data Upload**: Efficiently upload and manage data on the Lyceum platform.\n"
    "- **Authentication**: Securely authenticate and manage user sessions.\n"
    "- **Integration**: Integrate Lyceum functionalities into third-party applications.\n\n"
)

features = (
    "## Features\n\n"
    "- **Token-based Authentication**: Secure access to API endpoints.\n"
    "- **Data Handling**: Support for uploading and processing various data formats.\n"
    "- **Group Management**: Associate data with specific groups for organized access.\n"
    "- **Unit Handling**: Ensure data compatibility with Lyceum's unit system.\n"
    "- **S3 Integration**: Upload data directly to AWS S3 with temporary credentials.\n\n"
)

getting_started = (
    "## Getting Started\n\n"
    "To begin using the Lyceum API, please refer to the following sections:\n"
    "- [Authentication](authentication.md): Learn how to authenticate and obtain access tokens.\n"
    "- [API Endpoints](apis.md): Explore the available API endpoints and their usage.\n"
    "- [Data Upload](data-upload.md): Understand the process for uploading data to the platform.\n\n"
)

contact = (
    "## Contact\n\n"
    "For support or inquiries, please contact us at [support@thelyceum.io](mailto:support@thelyceum.io).\n"
)

# Combine all sections into a single string
full_content = (
    title + introduction + purpose + features + getting_started + contact
)

# Write the content to index.md with UTF-8 encoding to avoid encoding issues
with open("index.md", "w", encoding="utf-8") as file:
    file.write(full_content)

# Print a confirmation message
print("index.md has been generated successfully.")