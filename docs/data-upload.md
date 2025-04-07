# Data Upload to Lyceum Platform

This document provides a comprehensive guide for third parties to upload data to the Lyceum platform. The process involves preparing data in a specific JSON format, associating it with a group, handling units, and uploading it to an AWS S3 bucket while notifying the Lyceum API. This guide is based on the `FormLyceumDataUpload` C# script, which serves as a reference implementation.

## Prerequisites

Before initiating the upload process, ensure you have the following:

- **Authentication Tokens:** Obtain an access token and a refresh token by authenticating with the Lyceum API. These are required for all API interactions. Refer to your authentication documentation for details.
- **Session Title:** A unique title for the project or session being uploaded (e.g., "MyProject").
- **Session Data:** The data to be uploaded, provided as a JSON string or file.
- **Unit Mappings (Optional):** A dictionary mapping units in your data (e.g., "Volts") to Lyceum-compatible units (e.g., "V"). This can be provided programmatically or loaded from a file (e.g., `unit_mappings.json`).
- **Environment Variables (Optional):**
  - `LYCEUM_API_BASE`: The base URL for the Lyceum API (defaults to `https://api.thelyceum.io/api` if not set).
  - `LYCEUM_BUCKET`: The S3 bucket name (defaults to `lyceum-prod` if not set).

## Data Preparation

The data must be structured as a JSON object and undergo specific transformations to meet Lyceum’s requirements.

### Initial JSON Structure

The input JSON should include the following key fields:

- **GlobalProperties (Optional):** An object containing metadata key-value pairs (e.g., `"Manufacturer": "ABC Corp"`).
- **CheckedData (Optional):** An array of objects representing measurement data to be processed.
- **descriptor (Optional):** An array of metadata objects with `label` and `value` fields.

**Example Input JSON:**
```json
{
  "GlobalProperties": {
    "Manufacturer": "ABC Corp",
    "Model": "XYZ"
  },
  "CheckedData": [
    {
      "Name": "Path1",
      "Measurements": [
        {
          "Name": "FreqResponse",
          "Results": [
            {
              "Name": "Amplitude",
              "ResultValueType": "XY Values",
              "ChannelCount": 1,
              "Passed": true,
              "XUnit": "Hz",
              "YUnit": "dB",
              "XValues": [20, 20000],
              "YValuesPerChannel": {
                "Ch1": [0.1, 0.2]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

### Step 1: Add Project Name

Add a `ProjectName` field to the JSON root, using the session title provided.

**Transformation:**
```json
{
  "ProjectName": "MyProject",
  "GlobalProperties": { /* ... */ },
  "CheckedData": [ /* ... */ ]
}
```

### Step 2: Convert Global Properties to Descriptors

If `GlobalProperties` exists, convert it to a `descriptor` array where each property becomes an object with `label` and `value` fields. Remove the original `GlobalProperties` field.

**Before:**
```json
{
  "GlobalProperties": {
    "Manufacturer": "ABC Corp",
    "Model": "XYZ"
  }
}
```

**After:**
```json
{
  "descriptor": [
    {"label": "Manufacturer", "value": "ABC Corp"},
    {"label": "Model", "value": "XYZ"}
  ]
}
```

### Step 3: Remove Unwanted Descriptor Properties

Remove the following properties from the `descriptor` array if present:

- SequenceName
- ProjectDir
- APxDir
- Date
- Day
- Month
- Year
- Time
- Hour
- Minute
- Second
- Millisecond

**Example:**

**Before:**
```json
{
  "descriptor": [
    {"label": "Manufacturer", "value": "ABC Corp"},
    {"label": "Date", "value": "2023-10-01"}
  ]
}
```

**After:**
```json
{
  "descriptor": [
    {"label": "Manufacturer", "value": "ABC Corp"}
  ]
}
```

### Step 4: Update Descriptors with UUIDs

Fetch descriptor metadata from the Lyceum API (`GET /project/metadata/`) and update the `descriptor` array. Replace `label` values with corresponding UUIDs or values from the API where applicable.

**API Request:**
```bash
curl -X GET https://api.thelyceum.io/api/project/metadata/ \
  -H "Authorization: Bearer your_access_token"
```

**Transformation Example:**

**Before:**
```json
{
  "descriptor": [
    {"label": "Manufacturer", "value": "ABC Corp"}
  ]
}
```

**After (assuming API provides UUIDs):**
```json
{
  "descriptor": [
    {"label": "ABC Corp", "value": "uuid-from-api"}
  ]
}
```

### Step 5: Process Checked Data

If `CheckedData` exists, transform it into `ProcessedCheckedData`. This involves restructuring measurement results into a format with `Details`, `Units`, `Properties`, and `Data` sections.

#### Process Overview

- **Data Type:** Assume "Measurement" (hardcoded in the script).
- **Device Label:** Extract from `descriptor` where `value` matches a specific UUID (e.g., "9f7da84a-14f3-4407-90e2-40aad2ba81cb"), or use a fallback.
- **Transformation:** For each result in `CheckedData`, create a new object with:
  - `Details`: Metadata like name, result type, and pass/fail status.
  - `Units`: XUnit, YUnit, or MeterUnit based on `ResultValueType`.
  - `Properties`: Additional metadata excluding specified keys.
  - `Data`: Processed values with renamed channels.

**Example Transformation:**

**Before:**
```json
{
  "CheckedData": [
    {
      "Name": "Path1",
      "Measurements": [
        {
          "Name": "FreqResponse",
          "Results": [
            {
              "Name": "Amplitude",
              "ResultValueType": "XY Values",
              "ChannelCount": 1,
              "Passed": true,
              "XUnit": "Hz",
              "YUnit": "dB",
              "XValues": [20, 20000],
              "YValuesPerChannel": {
                "Ch1": [0.1, 0.2]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

**After:**
```json
{
  "ProcessedCheckedData": [
    {
      "Details": {
        "Name": "Path1 - FreqResponse - Amplitude",
        "ResultValueType": "XY Values",
        "ChannelCount": 1,
        "Passed": true,
        "data_types": "Measurement"
      },
      "Units": {
        "XUnit": "Hz",
        "YUnit": "dB"
      },
      "Properties": {},
      "Data": {
        "XValues": [20, 20000],
        "YValuesPerChannel": {
          "DeviceLabel - Ch1": [0.1, 0.2]
        }
      }
    }
  ]
}
```

Remove the original `CheckedData` field after processing.

## Group Association

Associate the data with a group in the Lyceum system, either by using a saved group or selecting one via the API.

### Fetch Available Groups

Send a GET request to `/organization/groups/` to retrieve available groups.

**Request:**
```bash
curl -X GET https://api.thelyceum.io/api/organization/groups/ \
  -H "Authorization: Bearer your_access_token"
```

**Response Example:**
```json
[
  {"id": "group_uuid1", "name": "Group1"},
  {"id": "group_uuid2", "name": "Group2"}
]
```

### Select a Group

- **Option 1: Saved Group:** Use a predefined group ID and name if available (e.g., from a config file).
- **Option 2: User Selection:** Implement a selection mechanism (e.g., a dropdown) to choose a group from the API response.

Append the selected group details to the JSON under `GroupDetails`.

**Example:**
```json
{
  "GroupDetails": {
    "group_name": "Group1",
    "group_id": "group_uuid1"
  }
}
```

## Unit Handling

Ensure units in `ProcessedCheckedData` are compatible with Lyceum’s unit system.

### Fetch Unit Metadata

Retrieve unit metadata from the Lyceum API (`GET /project/metadata/`).

**Request:**
```bash
curl -X GET https://api.thelyceum.io/api/project/metadata/ \
  -H "Authorization: Bearer your_access_token"
```

**Response Example:**
```json
{
  "x_units": [
    {"label": "Hz", "symbol": "Hz", "magnitude_symbol": ""}
  ],
  "y_units": [
    {"label": "dB", "symbol": "dB", "magnitude_symbol": ""}
  ]
}
```

### Apply Unit Mappings

Map units in your data to Lyceum units using a provided dictionary. For example:

- `"Volts"` → `"V"`

**Transformation:**

**Before:**
```json
{
  "ProcessedCheckedData": [
    {
      "Units": {
        "YUnit": "Volts"
      }
    }
  ]
}
```

**After (with mapping "Volts" → "V"):**
```json
{
  "ProcessedCheckedData": [
    {
      "Units": {
        "YUnit": "V"
      }
    }
  ]
}
```

### Replace Units with Details

Replace unit strings with full unit details from the API.

**After:**
```json
{
  "ProcessedCheckedData": [
    {
      "Units": {
        "YUnit": {
          "label": "V",
          "symbol": "V",
          "magnitude_symbol": ""
        }
      }
    }
  ]
}
```

### Handle Unmatched Units

For units not found in the metadata or mappings, implement a mechanism to:
- Prompt the user to select a matching unit from available options.
- Update the mappings and reapply them.

## Uploading to S3

Upload the prepared JSON file to the Lyceum S3 bucket and notify the API.

### Obtain Temporary AWS Credentials

Fetch credentials from the Lyceum API (`GET /account/get_aws_token/`).

**Request:**
```bash
curl -X GET https://api.thelyceum.io/api/account/get_aws_token/ \
  -H "Authorization: Bearer your_access_token"
```

**Response Example:**
```json
{
  "Credentials": {
    "AccessKeyId": "your_access_key",
    "SecretAccessKey": "your_secret_key",
    "SessionToken": "your_session_token"
  }
}
```

### Construct the S3 Object Key

Use the following structure:

```
media/native-app-uploads/{project_name}/{unique_folder}/{unique_file_name}.json
```

- `{project_name}`: Value of `ProjectName` (e.g., "MyProject").
- `{unique_folder}`: A unique identifier (e.g., a GUID).
- `{unique_file_name}`: A timestamped name (e.g., "MyProject_20231001120000.json").

**Example:**
```
media/native-app-uploads/MyProject/550e8400-e29b-41d4-a716-446655440000/MyProject_20231001120000.json
```

### Upload the File

Use an AWS S3 client with the temporary credentials to upload the JSON file to the bucket (default: `lyceum-prod`).

**Pseudo-code:**
```python
s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name='us-west-1'
)
s3_client.upload_file('temp.json', 'lyceum-prod', 'media/native-app-uploads/MyProject/...')
```

### Notify the Lyceum API

Send a POST request to `/project/v2/upload/native/` with the upload details.

**Payload:**
```json
{
  "file_url": "https://lyceum-prod.s3.amazonaws.com/media/native-app-uploads/MyProject/.../MyProject_20231001120000.json",
  "v2_json_file_url": "https://lyceum-prod.s3.amazonaws.com/media/native-app-uploads/MyProject/.../MyProject_20231001120000.json",
  "name": "MyProject",
  "tags": [],
  "descriptors": [
    {"descriptor": "uuid-from-api"},
    {"descriptor": "XYZ"}
  ],
  "groups": ["group_uuid1"]
}
```

**Request:**
```bash
curl -X POST https://api.thelyceum.io/api/project/v2/upload/native/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

Ensure URLs are properly escaped.

## Error Handling and Logging

Implement robust error handling and logging to troubleshoot issues:

- **Authentication Errors:** Handle token expiration and refresh.
- **JSON Validation:** Validate data format before processing.
- **Unit Mismatches:** Log and address unmatched units.
- **S3 Upload Failures:** Retry or report errors.
- **API Notification Failures:** Log response codes and messages.

**Example Log Entries:**
```
✅ Data saved to temp.json
❌ ERROR: Failed to fetch AWS credentials: 401 Unauthorized
📡 Uploaded to S3: media/native-app-uploads/MyProject/...
```

## Final Notes

- **Security:** Securely handle AWS credentials and tokens.
- **Validation:** Ensure all required fields are present and correctly formatted.
- **Reference:** Consult the `FormLyceumDataUpload` C# script for detailed logic, especially for `CheckedData` processing.

For further assistance, contact Lyceum support or refer to the script’s source code.
