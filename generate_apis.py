import json

# Load Swagger JSON
with open('swagger.json', 'r') as f:
    swagger_data = json.load(f)

# Extract general information
title = swagger_data['info']['title']
description = swagger_data['info']['description']
version = swagger_data['info']['version']
base_url = f"{swagger_data['schemes'][0]}://{swagger_data['host']}{swagger_data['basePath']}"

# Authentication
security_defs = swagger_data['securityDefinitions']
auth_methods = []
for name, details in security_defs.items():
    if details['type'] == 'apiKey':
        auth_methods.append(f"- **{name}**: API key in header: `{details['name']}`")
auth_section = "\n".join(auth_methods)

# Helper functions
def get_schema_details(schema, definitions):
    if '$ref' in schema:
        ref = schema['$ref'].split('/')[-1]
        return definitions[ref]
    return schema

def format_schema(schema, definitions, indent=0):
    if 'type' not in schema:
        return "N/A"
    schema_type = schema['type']
    if schema_type == 'object':
        properties = schema.get('properties', {})
        required = schema.get('required', [])
        prop_list = []
        for name, details in properties.items():
            prop_type = details.get('type', 'N/A')
            is_required = 'Required' if name in required else 'Optional'
            description = details.get('description', '')
            prop_list.append(f"  {'  ' * indent}- **{name}** ({prop_type}, {is_required}): {description}")
        return "\n".join(prop_list) if prop_list else "No properties defined"
    elif schema_type == 'array':
        items = schema.get('items', {})
        item_schema = get_schema_details(items, definitions)
        return f"Array of:\n{format_schema(item_schema, definitions, indent + 1)}"
    elif schema_type == 'string' and 'enum' in schema:
        enums = schema['enum']
        return f"Enum: {', '.join(map(str, enums))}"
    else:
        return schema_type

def format_parameters(parameters, definitions):
    if not parameters:
        return "None"
    param_list = []
    for param in parameters:
        name = param['name']
        in_location = param['in']
        required = 'Required' if param.get('required', False) else 'Optional'
        description = param.get('description', '')
        if in_location == 'body':
            schema = get_schema_details(param['schema'], definitions)
            schema_details = format_schema(schema, definitions)
            param_list.append(f"- **{name}** ({in_location}, {required}): {description}\n\n  **Schema:**\n{schema_details}")
        else:
            param_type = param.get('type', 'N/A')
            param_list.append(f"- **{name}** ({in_location}, {required}): {description} (Type: {param_type})")
    return "\n".join(param_list)

def format_responses(responses, definitions):
    response_list = []
    for code, details in responses.items():
        description = details.get('description', 'No description')
        schema = details.get('schema', {})
        if schema:
            schema_details = format_schema(get_schema_details(schema, definitions), definitions)
            response_list.append(f"- **{code}**: {description}\n\n  **Schema:**\n{schema_details}")
        else:
            response_list.append(f"- **{code}**: {description}")
    return "\n".join(response_list)

# Process paths by tags
definitions = swagger_data['definitions']
tags_dict = {}
for path, methods in swagger_data['paths'].items():
    for method, details in methods.items():
        if method == 'parameters':
            continue
        tags = details.get('tags', ['untagged'])
        for tag in tags:
            if tag not in tags_dict:
                tags_dict[tag] = []
            tags_dict[tag].append((path, method, details))

paths_section = ""
for tag, endpoints in tags_dict.items():
    paths_section += f"## {tag.capitalize()} Endpoints\n\n"
    for path, method, details in endpoints:
        operation_id = details.get('operationId', 'N/A')
        summary = details.get('summary', '')
        description = details.get('description', '')
        parameters = details.get('parameters', [])
        responses = details.get('responses', {})
        paths_section += f"### {method.upper()} {path}\n\n"
        if operation_id != 'N/A':
            paths_section += f"**Operation ID:** {operation_id}\n\n"
        if summary:
            paths_section += f"**Summary:** {summary}\n\n"
        if description:
            paths_section += f"**Description:** {description}\n\n"
        paths_section += "**Parameters:**\n"
        paths_section += format_parameters(parameters, definitions) + "\n\n"
        paths_section += "**Responses:**\n"
        paths_section += format_responses(responses, definitions) + "\n\n"

# Data Models
definitions_section = "## Data Models\n\n"
for name, schema in definitions.items():
    definitions_section += f"### {name}\n\n"
    definitions_section += format_schema(schema, definitions) + "\n\n"

# Combine all sections
markdown_content = f"""# {title}

{description}

**Version:** {version}

**Base URL:** {base_url}

## Authentication

{auth_section}

{paths_section}

{definitions_section}
"""

# Write to apis.md
with open("apis.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

print("apis.md has been generated successfully.")