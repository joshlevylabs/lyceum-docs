# Script to generate data-upload.md with proper Markdown formatting for Lyceum data upload

# Define each section as a string
title = "# Data Upload to Lyceum Platform\n\n"

description = (
    "This document provides a comprehensive guide for third parties to upload data to the Lyceum platform. "
    "The process involves preparing data in a specific JSON format, associating it with a group, handling units, "
    "and uploading it to an AWS S3 bucket while notifying the Lyceum API. This guide is based on the `FormLyceumDataUpload` "
    "C# script, which serves as a reference implementation.\n\n"
)

prerequisites = (
    "## Prerequisites\n\n"
    "Before initiating the upload process, ensure you have the following:\n\n"
    "- **Authentication Tokens:** Obtain an access token and a refresh token by authenticating with the Lyceum API. "
    "These are required for all API interactions. Refer to your authentication documentation for details.\n"
    "- **Session Title:** A unique title for the project or session being uploaded (e.g., \"MyProject\").\n"
    "- **Session Data:** The data to be uploaded, provided as a JSON string or file.\n"
    "- **Unit Mappings (Optional):** A dictionary mapping units in your data (e.g., \"Volts\") to Lyceum-compatible units "
    "(e.g., \"V\"). This can be provided programmatically or loaded from a file (e.g., `unit_mappings.json`).\n"
    "- **Environment Variables (Optional):**\n"
    "  - `LYCEUM_API_BASE`: The base URL for the Lyceum API (defaults to `https://api.thelyceum.io/api` if not set).\n"
    "  - `LYCEUM_BUCKET`: The S3 bucket name (defaults to `lyceum-prod` if not set).\n\n"
)

data_preparation = (
    "## Data Preparation\n\n"
    "The data must be structured as a JSON object and undergo specific transformations to meet Lyceum’s requirements.\n\n"
)

initial_json_structure = (
    "### Initial JSON Structure\n\n"
    "The input JSON should include the following key fields:\n\n"
    "- **GlobalProperties (Optional):** An object containing metadata key-value pairs (e.g., `\"Manufacturer\": \"ABC Corp\"`).\n"
    "- **CheckedData (Optional):** An array of objects representing measurement data to be processed.\n"
    "- **descriptor (Optional):** An array of metadata objects with `label` and `value` fields.\n\n"
    "**Example Input JSON:**\n"
    "```json\n"
    "{\n"
    "  \"GlobalProperties\": {\n"
    "    \"Manufacturer\": \"ABC Corp\",\n"
    "    \"Model\": \"XYZ\"\n"
    "  },\n"
    "  \"CheckedData\": [\n"
    "    {\n"
    "      \"Name\": \"Path1\",\n"
    "      \"Measurements\": [\n"
    "        {\n"
    "          \"Name\": \"FreqResponse\",\n"
    "          \"Results\": [\n"
    "            {\n"
    "              \"Name\": \"Amplitude\",\n"
    "              \"ResultValueType\": \"XY Values\",\n"
    "              \"ChannelCount\": 1,\n"
    "              \"Passed\": true,\n"
    "              \"XUnit\": \"Hz\",\n"
    "              \"YUnit\": \"dB\",\n"
    "              \"XValues\": [20, 20000],\n"
    "              \"YValuesPerChannel\": {\n"
    "                \"Ch1\": [0.1, 0.2]\n"
    "              }\n"
    "            }\n"
    "          ]\n"
    "        }\n"
    "      ]\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

step_1_add_project_name = (
    "### Step 1: Add Project Name\n\n"
    "Add a `ProjectName` field to the JSON root, using the session title provided.\n\n"
    "**Transformation:**\n"
    "```json\n"
    "{\n"
    "  \"ProjectName\": \"MyProject\",\n"
    "  \"GlobalProperties\": { /* ... */ },\n"
    "  \"CheckedData\": [ /* ... */ ]\n"
    "}\n"
    "```\n\n"
)

step_2_convert_global_properties = (
    "### Step 2: Convert Global Properties to Descriptors\n\n"
    "If `GlobalProperties` exists, convert it to a `descriptor` array where each property becomes an object with "
    "`label` and `value` fields. Remove the original `GlobalProperties` field.\n\n"
    "**Before:**\n"
    "```json\n"
    "{\n"
    "  \"GlobalProperties\": {\n"
    "    \"Manufacturer\": \"ABC Corp\",\n"
    "    \"Model\": \"XYZ\"\n"
    "  }\n"
    "}\n"
    "```\n\n"
    "**After:**\n"
    "```json\n"
    "{\n"
    "  \"descriptor\": [\n"
    "    {\"label\": \"Manufacturer\", \"value\": \"ABC Corp\"},\n"
    "    {\"label\": \"Model\", \"value\": \"XYZ\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

step_3_remove_unwanted_properties = (
    "### Step 3: Remove Unwanted Descriptor Properties\n\n"
    "Remove the following properties from the `descriptor` array if present:\n\n"
    "- SequenceName\n"
    "- ProjectDir\n"
    "- APxDir\n"
    "- Date\n"
    "- Day\n"
    "- Month\n"
    "- Year\n"
    "- Time\n"
    "- Hour\n"
    "- Minute\n"
    "- Second\n"
    "- Millisecond\n\n"
    "**Example:**\n\n"
    "**Before:**\n"
    "```json\n"
    "{\n"
    "  \"descriptor\": [\n"
    "    {\"label\": \"Manufacturer\", \"value\": \"ABC Corp\"},\n"
    "    {\"label\": \"Date\", \"value\": \"2023-10-01\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
    "**After:**\n"
    "```json\n"
    "{\n"
    "  \"descriptor\": [\n"
    "    {\"label\": \"Manufacturer\", \"value\": \"ABC Corp\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

step_4_update_descriptors = (
    "### Step 4: Update Descriptors with UUIDs\n\n"
    "Fetch descriptor metadata from the Lyceum API (`GET /project/metadata/`) and update the `descriptor` array. "
    "Replace `label` values with corresponding UUIDs or values from the API where applicable.\n\n"
    "**API Request:**\n"
    "```bash\n"
    "curl -X GET https://api.thelyceum.io/api/project/metadata/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\"\n"
    "```\n\n"
    "**Transformation Example:**\n\n"
    "**Before:**\n"
    "```json\n"
    "{\n"
    "  \"descriptor\": [\n"
    "    {\"label\": \"Manufacturer\", \"value\": \"ABC Corp\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
    "**After (assuming API provides UUIDs):**\n"
    "```json\n"
    "{\n"
    "  \"descriptor\": [\n"
    "    {\"label\": \"ABC Corp\", \"value\": \"uuid-from-api\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

step_5_process_checked_data = (
    "### Step 5: Process Checked Data\n\n"
    "If `CheckedData` exists, transform it into `ProcessedCheckedData`. This involves restructuring measurement results "
    "into a format with `Details`, `Units`, `Properties`, and `Data` sections.\n\n"
    "#### Process Overview\n\n"
    "- **Data Type:** Assume \"Measurement\" (hardcoded in the script).\n"
    "- **Device Label:** Extract from `descriptor` where `value` matches a specific UUID "
    "(e.g., \"9f7da84a-14f3-4407-90e2-40aad2ba81cb\"), or use a fallback.\n"
    "- **Transformation:** For each result in `CheckedData`, create a new object with:\n"
    "  - `Details`: Metadata like name, result type, and pass/fail status.\n"
    "  - `Units`: XUnit, YUnit, or MeterUnit based on `ResultValueType`.\n"
    "  - `Properties`: Additional metadata excluding specified keys.\n"
    "  - `Data`: Processed values with renamed channels.\n\n"
    "**Example Transformation:**\n\n"
    "**Before:**\n"
    "```json\n"
    "{\n"
    "  \"CheckedData\": [\n"
    "    {\n"
    "      \"Name\": \"Path1\",\n"
    "      \"Measurements\": [\n"
    "        {\n"
    "          \"Name\": \"FreqResponse\",\n"
    "          \"Results\": [\n"
    "            {\n"
    "              \"Name\": \"Amplitude\",\n"
    "              \"ResultValueType\": \"XY Values\",\n"
    "              \"ChannelCount\": 1,\n"
    "              \"Passed\": true,\n"
    "              \"XUnit\": \"Hz\",\n"
    "              \"YUnit\": \"dB\",\n"
    "              \"XValues\": [20, 20000],\n"
    "              \"YValuesPerChannel\": {\n"
    "                \"Ch1\": [0.1, 0.2]\n"
    "              }\n"
    "            }\n"
    "          ]\n"
    "        }\n"
    "      ]\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
    "**After:**\n"
    "```json\n"
    "{\n"
    "  \"ProcessedCheckedData\": [\n"
    "    {\n"
    "      \"Details\": {\n"
    "        \"Name\": \"Path1 - FreqResponse - Amplitude\",\n"
    "        \"ResultValueType\": \"XY Values\",\n"
    "        \"ChannelCount\": 1,\n"
    "        \"Passed\": true,\n"
    "        \"data_types\": \"Measurement\"\n"
    "      },\n"
    "      \"Units\": {\n"
    "        \"XUnit\": \"Hz\",\n"
    "        \"YUnit\": \"dB\"\n"
    "      },\n"
    "      \"Properties\": {},\n"
    "      \"Data\": {\n"
    "        \"XValues\": [20, 20000],\n"
    "        \"YValuesPerChannel\": {\n"
    "          \"DeviceLabel - Ch1\": [0.1, 0.2]\n"
    "        }\n"
    "      }\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
    "Remove the original `CheckedData` field after processing.\n\n"
)

data_preparation_section = (
    data_preparation + initial_json_structure + step_1_add_project_name +
    step_2_convert_global_properties + step_3_remove_unwanted_properties +
    step_4_update_descriptors + step_5_process_checked_data
)

group_association = (
    "## Group Association\n\n"
    "Associate the data with a group in the Lyceum system, either by using a saved group or selecting one via the API.\n\n"
)

fetch_groups = (
    "### Fetch Available Groups\n\n"
    "Send a GET request to `/organization/groups/` to retrieve available groups.\n\n"
    "**Request:**\n"
    "```bash\n"
    "curl -X GET https://api.thelyceum.io/api/organization/groups/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\"\n"
    "```\n\n"
    "**Response Example:**\n"
    "```json\n"
    "[\n"
    "  {\"id\": \"group_uuid1\", \"name\": \"Group1\"},\n"
    "  {\"id\": \"group_uuid2\", \"name\": \"Group2\"}\n"
    "]\n"
    "```\n\n"
)

select_group = (
    "### Select a Group\n\n"
    "- **Option 1: Saved Group:** Use a predefined group ID and name if available (e.g., from a config file).\n"
    "- **Option 2: User Selection:** Implement a selection mechanism (e.g., a dropdown) to choose a group from the API response.\n\n"
    "Append the selected group details to the JSON under `GroupDetails`.\n\n"
    "**Example:**\n"
    "```json\n"
    "{\n"
    "  \"GroupDetails\": {\n"
    "    \"group_name\": \"Group1\",\n"
    "    \"group_id\": \"group_uuid1\"\n"
    "  }\n"
    "}\n"
    "```\n\n"
)

group_association_section = group_association + fetch_groups + select_group

unit_handling = (
    "## Unit Handling\n\n"
    "Ensure units in `ProcessedCheckedData` are compatible with Lyceum’s unit system.\n\n"
)

fetch_unit_metadata = (
    "### Fetch Unit Metadata\n\n"
    "Retrieve unit metadata from the Lyceum API (`GET /project/metadata/`).\n\n"
    "**Request:**\n"
    "```bash\n"
    "curl -X GET https://api.thelyceum.io/api/project/metadata/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\"\n"
    "```\n\n"
    "**Response Example:**\n"
    "```json\n"
    "{\n"
    "  \"x_units\": [\n"
    "    {\"label\": \"Hz\", \"symbol\": \"Hz\", \"magnitude_symbol\": \"\"}\n"
    "  ],\n"
    "  \"y_units\": [\n"
    "    {\"label\": \"dB\", \"symbol\": \"dB\", \"magnitude_symbol\": \"\"}\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

apply_unit_mappings = (
    "### Apply Unit Mappings\n\n"
    "Map units in your data to Lyceum units using a provided dictionary. For example:\n\n"
    "- `\"Volts\"` → `\"V\"`\n\n"
    "**Transformation:**\n\n"
    "**Before:**\n"
    "```json\n"
    "{\n"
    "  \"ProcessedCheckedData\": [\n"
    "    {\n"
    "      \"Units\": {\n"
    "        \"YUnit\": \"Volts\"\n"
    "      }\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
    "**After (with mapping \"Volts\" → \"V\"):**\n"
    "```json\n"
    "{\n"
    "  \"ProcessedCheckedData\": [\n"
    "    {\n"
    "      \"Units\": {\n"
    "        \"YUnit\": \"V\"\n"
    "      }\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

replace_units_with_details = (
    "### Replace Units with Details\n\n"
    "Replace unit strings with full unit details from the API.\n\n"
    "**After:**\n"
    "```json\n"
    "{\n"
    "  \"ProcessedCheckedData\": [\n"
    "    {\n"
    "      \"Units\": {\n"
    "        \"YUnit\": {\n"
    "          \"label\": \"V\",\n"
    "          \"symbol\": \"V\",\n"
    "          \"magnitude_symbol\": \"\"\n"
    "        }\n"
    "      }\n"
    "    }\n"
    "  ]\n"
    "}\n"
    "```\n\n"
)

handle_unmatched_units = (
    "### Handle Unmatched Units\n\n"
    "For units not found in the metadata or mappings, implement a mechanism to:\n"
    "- Prompt the user to select a matching unit from available options.\n"
    "- Update the mappings and reapply them.\n\n"
)

unit_handling_section = (
    unit_handling + fetch_unit_metadata + apply_unit_mappings +
    replace_units_with_details + handle_unmatched_units
)

uploading_to_s3 = (
    "## Uploading to S3\n\n"
    "Upload the prepared JSON file to the Lyceum S3 bucket and notify the API.\n\n"
)

obtain_aws_credentials = (
    "### Obtain Temporary AWS Credentials\n\n"
    "Fetch credentials from the Lyceum API (`GET /account/get_aws_token/`).\n\n"
    "**Request:**\n"
    "```bash\n"
    "curl -X GET https://api.thelyceum.io/api/account/get_aws_token/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\"\n"
    "```\n\n"
    "**Response Example:**\n"
    "```json\n"
    "{\n"
    "  \"Credentials\": {\n"
    "    \"AccessKeyId\": \"your_access_key\",\n"
    "    \"SecretAccessKey\": \"your_secret_key\",\n"
    "    \"SessionToken\": \"your_session_token\"\n"
    "  }\n"
    "}\n"
    "```\n\n"
)

construct_s3_key = (
    "### Construct the S3 Object Key\n\n"
    "Use the following structure:\n\n"
    "```\n"
    "media/native-app-uploads/{project_name}/{unique_folder}/{unique_file_name}.json\n"
    "```\n\n"
    "- `{project_name}`: Value of `ProjectName` (e.g., \"MyProject\").\n"
    "- `{unique_folder}`: A unique identifier (e.g., a GUID).\n"
    "- `{unique_file_name}`: A timestamped name (e.g., \"MyProject_20231001120000.json\").\n\n"
    "**Example:**\n"
    "```\n"
    "media/native-app-uploads/MyProject/550e8400-e29b-41d4-a716-446655440000/MyProject_20231001120000.json\n"
    "```\n\n"
)

upload_file = (
    "### Upload the File\n\n"
    "Use an AWS S3 client with the temporary credentials to upload the JSON file to the bucket (default: `lyceum-prod`).\n\n"
    "**Pseudo-code:**\n"
    "```python\n"
    "s3_client = boto3.client(\n"
    "    's3',\n"
    "    aws_access_key_id=access_key_id,\n"
    "    aws_secret_access_key=secret_access_key,\n"
    "    aws_session_token=session_token,\n"
    "    region_name='us-west-1'\n"
    ")\n"
    "s3_client.upload_file('temp.json', 'lyceum-prod', 'media/native-app-uploads/MyProject/...')\n"
    "```\n\n"
)

notify_api = (
    "### Notify the Lyceum API\n\n"
    "Send a POST request to `/project/v2/upload/native/` with the upload details.\n\n"
    "**Payload:**\n"
    "```json\n"
    "{\n"
    "  \"file_url\": \"https://lyceum-prod.s3.amazonaws.com/media/native-app-uploads/MyProject/.../MyProject_20231001120000.json\",\n"
    "  \"v2_json_file_url\": \"https://lyceum-prod.s3.amazonaws.com/media/native-app-uploads/MyProject/.../MyProject_20231001120000.json\",\n"
    "  \"name\": \"MyProject\",\n"
    "  \"tags\": [],\n"
    "  \"descriptors\": [\n"
    "    {\"descriptor\": \"uuid-from-api\"},\n"
    "    {\"descriptor\": \"XYZ\"}\n"
    "  ],\n"
    "  \"groups\": [\"group_uuid1\"]\n"
    "}\n"
    "```\n\n"
    "**Request:**\n"
    "```bash\n"
    "curl -X POST https://api.thelyceum.io/api/project/v2/upload/native/ \\\n"
    "  -H \"Authorization: Bearer your_access_token\" \\\n"
    "  -H \"Content-Type: application/json\" \\\n"
    "  -d @payload.json\n"
    "```\n\n"
    "Ensure URLs are properly escaped.\n\n"
)

uploading_to_s3_section = (
    uploading_to_s3 + obtain_aws_credentials + construct_s3_key +
    upload_file + notify_api
)

error_handling = (
    "## Error Handling and Logging\n\n"
    "Implement robust error handling and logging to troubleshoot issues:\n\n"
    "- **Authentication Errors:** Handle token expiration and refresh.\n"
    "- **JSON Validation:** Validate data format before processing.\n"
    "- **Unit Mismatches:** Log and address unmatched units.\n"
    "- **S3 Upload Failures:** Retry or report errors.\n"
    "- **API Notification Failures:** Log response codes and messages.\n\n"
    "**Example Log Entries:**\n"
    "```\n"
    "✅ Data saved to temp.json\n"
    "❌ ERROR: Failed to fetch AWS credentials: 401 Unauthorized\n"
    "📡 Uploaded to S3: media/native-app-uploads/MyProject/...\n"
    "```\n\n"
)

final_notes = (
    "## Final Notes\n\n"
    "- **Security:** Securely handle AWS credentials and tokens.\n"
    "- **Validation:** Ensure all required fields are present and correctly formatted.\n"
    "- **Reference:** Consult the `FormLyceumDataUpload` C# script for detailed logic, especially for `CheckedData` processing.\n\n"
    "For further assistance, contact Lyceum support or refer to the script’s source code.\n"
)

# Combine all sections
full_content = (
    title + description + prerequisites + data_preparation_section +
    group_association_section + unit_handling_section + uploading_to_s3_section +
    error_handling + final_notes
)

# Write the content to data-upload.md with UTF-8 encoding to avoid encoding issues
with open("data-upload.md", "w", encoding="utf-8") as file:
    file.write(full_content)

# Print a confirmation message
print("data-upload.md has been generated successfully.")