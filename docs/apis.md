# Si6ma API



**Version:** v1

**Base URL:** https://api.thelyceum.io/api

## Authentication

- **Bearer**: API key in header: `Authorization`
- **Token**: API key in header: `Authorization`

## Account Endpoints

### GET /account/

**Operation ID:** account_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **first_name** (string, Optional): 
    - **last_name** (string, Optional): 
    - **email** (string, Optional): 
    - **profile_image** (string, Optional): 
    - **cover_image** (string, Optional): 
    - **following** (boolean, Optional): 
    - **is_verified** (boolean, Optional): 
    - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
    - **is_premium** (boolean, Optional): 

### POST /account/

**Operation ID:** account_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **password** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **password** (string, Required): 

### POST /account/check_availability/

**Operation ID:** account_check_availability

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **email** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **email** (string, Required): 

### POST /account/forgot_password/

**Operation ID:** account_forgot_password

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **email** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **email** (string, Required): 

### GET /account/get_aws_token/

**Operation ID:** account_get_aws_token

**Description:** API returns temporary credentials for webClient to upload files to s3

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **first_name** (string, Optional): 
    - **last_name** (string, Optional): 
    - **email** (string, Optional): 
    - **profile_image** (string, Optional): 
    - **cover_image** (string, Optional): 
    - **following** (boolean, Optional): 
    - **is_verified** (boolean, Optional): 
    - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
    - **is_premium** (boolean, Optional): 

### POST /account/invite/user/

**Operation ID:** account_invite_invite_user_to_organization

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **users** (array, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **users** (array, Required): 

### POST /account/login

**Operation ID:** account_login_create

**Description:** Takes a set of user credentials and returns an access and refresh JSON web
token pair to prove the authentication of those credentials.

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **email** (string, Required): 
  - **password** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **email** (string, Required): 
  - **password** (string, Required): 

### GET /account/me/

**Operation ID:** account_me

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **first_name** (string, Optional): 
    - **last_name** (string, Optional): 
    - **email** (string, Optional): 
    - **profile_image** (string, Optional): 
    - **cover_image** (string, Optional): 
    - **following** (boolean, Optional): 
    - **is_verified** (boolean, Optional): 
    - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
    - **is_premium** (boolean, Optional): 

### GET /account/min/

**Operation ID:** account_check_user_availability

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /account/resend_email_verification/

**Operation ID:** account_resend_email_verification_read

**Parameters:**
- **user_id** (query, Optional): User id (Type: boolean)

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **email** (string, Required): 

### POST /account/resend_email_verification/

**Operation ID:** account_resend_email_verification_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **email** (string, Required): 
- **user_id** (query, Optional): User id (Type: boolean)

**Responses:**
- **201**: 

  **Schema:**
  - **email** (string, Required): 

### POST /account/reset_password/

**Operation ID:** account_reset_password

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **token** (string, Required): 
  - **password** (string, Required): 
  - **uid** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **token** (string, Required): 
  - **password** (string, Required): 
  - **uid** (string, Required): 

### POST /account/token/refresh

**Operation ID:** account_token_refresh_create

**Description:** Takes a refresh type JSON web token and returns an access type JSON web
token if the refresh token is valid.

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **refresh** (string, Required): 
  - **access** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **refresh** (string, Required): 
  - **access** (string, Optional): 

### POST /account/verify_email_address/

**Operation ID:** account_verify_email_address

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **token** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **token** (string, Required): 

### GET /account/{id}/

**Operation ID:** account_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 
  - **following** (boolean, Optional): 
  - **is_verified** (boolean, Optional): 
  - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
  - **is_premium** (boolean, Optional): 

### PUT /account/{id}/

**Operation ID:** account_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 

### PATCH /account/{id}/

**Operation ID:** account_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 

### GET /account/{id}/follow/

**Operation ID:** account_follow

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 
  - **following** (boolean, Optional): 
  - **is_verified** (boolean, Optional): 
  - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
  - **is_premium** (boolean, Optional): 

### GET /account/{id}/follow_back/

**Operation ID:** account_follow_back

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 
  - **following** (boolean, Optional): 
  - **is_verified** (boolean, Optional): 
  - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
  - **is_premium** (boolean, Optional): 

## Categories Endpoints

### GET /categories/

**Operation ID:** categories_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **name** (string, Required): 
    - **description** (string, Optional): 

### POST /categories/

**Operation ID:** categories_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

### GET /categories/{id}/

**Operation ID:** categories_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

### PUT /categories/{id}/

**Operation ID:** categories_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

### PATCH /categories/{id}/

**Operation ID:** categories_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

### DELETE /categories/{id}/

**Operation ID:** categories_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Comments Endpoints

### GET /comments/

**Operation ID:** comments_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **content** (string, Required): 
    - **user** (string, Optional): 
    - **user_email** (string, Optional): 
    - **parent** (integer, Optional): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **replies** (string, Optional): 
    - **reactions** (array, Optional): 
    - **standard** (integer, Optional): 

### POST /comments/

**Operation ID:** comments_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### GET /comments/{id}/

**Operation ID:** comments_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### PUT /comments/{id}/

**Operation ID:** comments_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### PATCH /comments/{id}/

**Operation ID:** comments_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### DELETE /comments/{id}/

**Operation ID:** comments_delete

**Parameters:**
None

**Responses:**
- **204**: 

### POST /comments/{id}/react/

**Operation ID:** comments_react

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### GET /comments/{id}/reaction_history/

**Operation ID:** comments_reaction_history

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

## Component Endpoints

### GET /component/

**Operation ID:** component_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **name** (string, Required): 
    - **type** (string, Optional): 
    - **description** (string, Optional): 

### POST /component/

**Operation ID:** component_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

### GET /component/{id}/

**Operation ID:** component_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

### PUT /component/{id}/

**Operation ID:** component_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

### PATCH /component/{id}/

**Operation ID:** component_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

### DELETE /component/{id}/

**Operation ID:** component_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Configs Endpoints

### GET /configs/

**Operation ID:** configs_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **name** (string, Required): 
    - **slug** (string, Optional): 
    - **data_type** (string, Required): 

### POST /configs/

**Operation ID:** configs_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

### GET /configs/{id}/

**Operation ID:** configs_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

### PUT /configs/{id}/

**Operation ID:** configs_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

### PATCH /configs/{id}/

**Operation ID:** configs_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

### DELETE /configs/{id}/

**Operation ID:** configs_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Configuration Endpoints

### GET /configuration/

**Operation ID:** configuration_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **history_id** (integer, Optional): 
    - **history_date** (string, Required): 
    - **history_type** (string, Required): 
    - **history_user** (string, Optional): 
    - **name** (string, Required): 
    - **slug** (string, Optional): 
    - **data_type** (string, Required): 
    - **public** (boolean, Optional): 

### POST /configuration/

**Operation ID:** configuration_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

### GET /configuration/{id}/

**Operation ID:** configuration_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

### PUT /configuration/{id}/

**Operation ID:** configuration_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

### PATCH /configuration/{id}/

**Operation ID:** configuration_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

### DELETE /configuration/{id}/

**Operation ID:** configuration_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Constants Endpoints

### GET /constants/

**Operation ID:** constants_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **name** (string, Required): 
    - **slug** (string, Optional): 
    - **magnitude** (string, Optional): 
    - **magnitude_symbol** (string, Optional): 
    - **symbol** (string, Optional): 
    - **is_liner** (boolean, Optional): 
    - **is_decibels** (boolean, Optional): 

### POST /constants/

**Operation ID:** constants_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

### GET /constants/{id}/

**Operation ID:** constants_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

### PUT /constants/{id}/

**Operation ID:** constants_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

### PATCH /constants/{id}/

**Operation ID:** constants_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

### DELETE /constants/{id}/

**Operation ID:** constants_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Descriptors Endpoints

### GET /descriptors/

**Operation ID:** descriptors_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Equipment Endpoints

### GET /equipment/

**Operation ID:** equipment_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **name** (string, Required): 
    - **manufacturer** (string, Optional): 
    - **description** (string, Optional): 
    - **downloads** (string, Optional): 
    - **link** (string, Optional): 

### POST /equipment/

**Operation ID:** equipment_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

### GET /equipment/{id}/

**Operation ID:** equipment_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

### PUT /equipment/{id}/

**Operation ID:** equipment_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

### PATCH /equipment/{id}/

**Operation ID:** equipment_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

### DELETE /equipment/{id}/

**Operation ID:** equipment_delete

**Parameters:**
None

**Responses:**
- **204**: 

## File Endpoints

### GET /file/

**Operation ID:** file_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **user** (N/A, Optional): 
    - **groups** (array, Optional): 
    - **file_name** (string, Optional): 
    - **file** (string, Optional): 
    - **file_type** (string, Optional): 
    - **uploaded_at** (string, Optional): 

### POST /file/

**Operation ID:** file_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

### GET /file/{id}/

**Operation ID:** file_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (array, Optional): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 

### PUT /file/{id}/

**Operation ID:** file_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

### PATCH /file/{id}/

**Operation ID:** file_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

### DELETE /file/{id}/

**Operation ID:** file_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Notification Endpoints

### GET /notification/

**Operation ID:** notification_list

**Parameters:**
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)
- **q** (query, Optional): Coma-seperated ids (Type: string)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Organization Endpoints

### GET /organization/groups/

**Operation ID:** organization_groups_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)
- **o_m** (query, Optional):  (Type: string)
- **include** (query, Optional): Include groups in response, its UUID comma seperated. (Type: string)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### POST /organization/groups/

**Operation ID:** organization_groups_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **tags** (array, Optional): 
  - **members** (array, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **tags** (array, Optional): 
  - **members** (array, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

### GET /organization/groups/metadata/

**Operation ID:** organization_groups_metadata

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /organization/groups/{id}/

**Operation ID:** organization_groups_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **tags** (array, Required): 
  - **members** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **id** (string, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 
  - **joined** (boolean, Optional): 
  - **requested** (boolean, Optional): 
  - **is_public** (boolean, Optional): 

### PUT /organization/groups/{id}/

**Operation ID:** organization_groups_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

### PATCH /organization/groups/{id}/

**Operation ID:** organization_groups_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

### DELETE /organization/groups/{id}/

**Operation ID:** organization_groups_delete

**Parameters:**
None

**Responses:**
- **204**: 

### GET /organization/groups/{id}/accept/invitation/{invitation_id}/

**Operation ID:** organization_groups_accept_accept_group_invitations

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **name** (string, Optional): 
    - **group_name** (string, Required): 
    - **description** (string, Optional): 
    - **tags** (array, Optional): 
    - **members** (array, Optional): 
    - **image** (string, Optional): 
    - **image_url** (string, Optional): 
    - **is_public** (boolean, Optional): 
    - **approver** (string, Optional): 
    - **uploader** (string, Optional): 
    - **inviter** (string, Optional): 
    - **poster** (string, Optional): 

### PUT /organization/groups/{id}/add_member/

**Operation ID:** organization_groups_add_users_to_group

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **members** (array, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **members** (array, Required): 

### PATCH /organization/groups/{id}/change/role/{user_id}/

**Operation ID:** organization_groups_change_change_user_role_for_group

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **group_role** (string, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **group_role** (string, Required): 

### GET /organization/groups/{id}/invitations/

**Operation ID:** organization_groups_list_group_invitations

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /organization/groups/{id}/join/

**Operation ID:** organization_groups_join_group

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **name** (string, Optional): 
    - **group_name** (string, Required): 
    - **description** (string, Optional): 
    - **tags** (array, Optional): 
    - **members** (array, Optional): 
    - **image** (string, Optional): 
    - **image_url** (string, Optional): 
    - **is_public** (boolean, Optional): 
    - **approver** (string, Optional): 
    - **uploader** (string, Optional): 
    - **inviter** (string, Optional): 
    - **poster** (string, Optional): 

### GET /organization/groups/{id}/reject/invitation/{invitation_id}/

**Operation ID:** organization_groups_reject_reject_group_invitations

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **name** (string, Optional): 
    - **group_name** (string, Required): 
    - **description** (string, Optional): 
    - **tags** (array, Optional): 
    - **members** (array, Optional): 
    - **image** (string, Optional): 
    - **image_url** (string, Optional): 
    - **is_public** (boolean, Optional): 
    - **approver** (string, Optional): 
    - **uploader** (string, Optional): 
    - **inviter** (string, Optional): 
    - **poster** (string, Optional): 

### DELETE /organization/groups/{id}/user/{user}/

**Operation ID:** organization_groups_delete_group_user

**Parameters:**
None

**Responses:**
- **204**: 

### GET /organization/groups/{id}/user_list/

**Operation ID:** organization_groups_list_group_users

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)
- **group_role** (query, Optional): Group Role reference (Type: string)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /organization/groups/{id}/user_metadata/

**Operation ID:** organization_groups_user_meta_data

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Project Endpoints

### GET /project/

**Operation ID:** project_list

**Parameters:**
- **status** (query, Optional):  (Type: string)
- **projects__category__id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **groups__id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **data_type** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **descriptors__descriptor_id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)
- **for_user** (query, Optional): Projects of user (Type: uuid)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### POST /project/

**Operation ID:** project_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **file_url** (string, Required): 
  - **name** (string, Required): 
  - **units** (array, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **file_url** (string, Required): 
  - **name** (string, Required): 
  - **units** (array, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 

### POST /project/advance_search/

**Operation ID:** project_advance_search

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **key** (string, Required): 
  - **value** (string, Required): 
  - **is_negative** (boolean, Optional): 
  - **expression** (string, Optional): 
  - **operand** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **key** (string, Required): 
  - **value** (string, Required): 
  - **is_negative** (boolean, Optional): 
  - **expression** (string, Optional): 
  - **operand** (string, Optional): 

### GET /project/details/category/{project_id}/{category_id}/

**Operation ID:** project_details_device_details

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **tags** (array, Required): 
    - **categories** (string, Optional): 
    - **descriptors** (array, Required): 
    - **name** (string, Required): 
    - **status** (string, Optional): 
    - **file_type** (string, Optional): 
    - **file** (string, Optional): 
    - **data_type** (string, Optional): 
    - **groups** (array, Required): 
    - **limits** (array, Required): 
    - **updated_at** (string, Optional): 
    - **created_at** (string, Optional): 
    - **owner** (N/A, Required): 

### POST /project/details/multiple/

**Operation ID:** project_details_multiple_project_details

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **project_ids** (array, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **project_ids** (array, Required): 

### GET /project/details/{id}/

**Operation ID:** project_project_details

**Parameters:**
- **projects__device** (query, Optional):  (Type: string)
- **projects__category** (query, Optional):  (Type: string)

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **tags** (array, Required): 
    - **categories** (string, Optional): 
    - **descriptors** (array, Required): 
    - **name** (string, Required): 
    - **status** (string, Optional): 
    - **file_type** (string, Optional): 
    - **file** (string, Optional): 
    - **data_type** (string, Optional): 
    - **groups** (array, Required): 
    - **limits** (array, Required): 
    - **updated_at** (string, Optional): 
    - **created_at** (string, Optional): 
    - **owner** (N/A, Required): 

### GET /project/devices/

**Operation ID:** project_devices_list

**Parameters:**
- **project** (query, Optional):  (Type: string)
- **category** (query, Optional):  (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /project/devices/download/limits/{project_id}/

**Operation ID:** project_devices_download_download_limits

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **device** (N/A, Required): 
    - **x_units** (string, Required): 
    - **y_units** (string, Required): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **dimension_types** (string, Optional): 
    - **category** (string, Required): 
    - **project** (string, Required): 
    - **x_units_v2** (string, Optional): 
    - **y_units_v2** (string, Optional): 

### GET /project/devices/download/measurement/{project_id}/

**Operation ID:** project_devices_download_download_measurement

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **device** (N/A, Required): 
    - **x_units** (string, Required): 
    - **y_units** (string, Required): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **dimension_types** (string, Optional): 
    - **category** (string, Required): 
    - **project** (string, Required): 
    - **x_units_v2** (string, Optional): 
    - **y_units_v2** (string, Optional): 

### POST /project/devices/node/

**Operation ID:** project_devices_get_node_data

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **device** (N/A, Required): 
  - **x_units** (string, Required): 
  - **y_units** (string, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **dimension_types** (string, Optional): 
  - **category** (string, Required): 
  - **project** (string, Required): 
  - **x_units_v2** (string, Optional): 
  - **y_units_v2** (string, Optional): 
- **data_type** (query, Optional): Data Dimension types. (Type: string)

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **device** (N/A, Required): 
  - **x_units** (string, Required): 
  - **y_units** (string, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **dimension_types** (string, Optional): 
  - **category** (string, Required): 
  - **project** (string, Required): 
  - **x_units_v2** (string, Optional): 
  - **y_units_v2** (string, Optional): 

### GET /project/devices/node/descriptors/

**Operation ID:** project_devices_node_get_descriptors

**Parameters:**
- **projects** (query, Optional): Project UUID's must be comma seperated. (Type: string)

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **device** (N/A, Required): 
    - **x_units** (string, Required): 
    - **y_units** (string, Required): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **dimension_types** (string, Optional): 
    - **category** (string, Required): 
    - **project** (string, Required): 
    - **x_units_v2** (string, Optional): 
    - **y_units_v2** (string, Optional): 

### POST /project/limits/

**Operation ID:** project_create_limits

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **limits** (array, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **limits** (array, Required): 

### GET /project/metadata/

**Operation ID:** project_dropdown_metadata

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **status** (query, Optional):  (Type: string)
- **projects__category__id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **groups__id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **data_type** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **descriptors__descriptor_id** (query, Optional): Multiple values may be separated by commas. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (string, Optional): 
    - **tags** (array, Required): 
    - **groups** (array, Required): 
    - **clean_files** (array, Optional): 
    - **created_at** (string, Optional): 
    - **updated_at** (string, Optional): 
    - **serial_number** (integer, Optional): 
    - **readable_key** (string, Optional): 
    - **name** (string, Required): 
    - **file** (string, Optional): 
    - **v2_json_file** (string, Optional): 
    - **status** (string, Optional): 
    - **file_type** (string, Optional): 
    - **data_type** (string, Optional): 
    - **units** (object, Optional): 
    - **invalid_cells_action** (string, Optional): 
    - **is_public** (boolean, Optional): 
    - **metadata** (object, Optional): 
    - **source** (string, Optional): 
    - **template** (string, Optional): 
    - **owner** (string, Optional): 

### POST /project/statistics/

**Operation ID:** project_create_statistics

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **statistics** (array, Required): 
  - **data_type** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **statistics** (array, Required): 
  - **data_type** (string, Optional): 

### POST /project/v2/upload/

**Operation ID:** project_v2_create_v2

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **file_url** (string, Required): 
  - **v2_json_file_url** (string, Required): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **template** (N/A, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **file_url** (string, Required): 
  - **v2_json_file_url** (string, Required): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **template** (N/A, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 

### POST /project/v2/upload/native/

**Operation ID:** project_v2_upload_create_v2_native

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **file_url** (string, Required): 
  - **v2_json_file_url** (string, Required): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **template** (N/A, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **file_url** (string, Required): 
  - **v2_json_file_url** (string, Required): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **template** (N/A, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 

### GET /project/{id}/

**Operation ID:** project_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **clean_files** (array, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### PUT /project/{id}/

**Operation ID:** project_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **name** (string, Required): 
  - **tags** (array, Optional): 
  - **descriptors** (array, Optional): 
  - **groups** (array, Optional): 
  - **metadata** (object, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **name** (string, Required): 
  - **tags** (array, Optional): 
  - **descriptors** (array, Optional): 
  - **groups** (array, Optional): 
  - **metadata** (object, Optional): 

### PATCH /project/{id}/

**Operation ID:** project_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **name** (string, Required): 
  - **tags** (array, Optional): 
  - **descriptors** (array, Optional): 
  - **groups** (array, Optional): 
  - **metadata** (object, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **name** (string, Required): 
  - **tags** (array, Optional): 
  - **descriptors** (array, Optional): 
  - **groups** (array, Optional): 
  - **metadata** (object, Optional): 

### DELETE /project/{id}/

**Operation ID:** project_delete

**Parameters:**
None

**Responses:**
- **204**: 

### GET /project/{id}/download_file/{file_id}/

**Operation ID:** project_download_clean_data

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **clean_files** (array, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### GET /project/{id}/get_download_code/{file_id}/

**Operation ID:** project_download_cleaned_files_curl_and_shell

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **powershell** (string, Required): 
  - **curl** (string, Required): 

### GET /project/{id}/privileges/

**Operation ID:** project_project_access_details

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **clean_files** (array, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### GET /project/{id}/recreate_clean_data/

**Operation ID:** project_create_clean_data

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **clean_files** (array, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### GET /project/{project_id}/properties/

**Operation ID:** project_project_properties

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /project/{project_id}/properties/{id}/

**Operation ID:** project_project_properties_object

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Project_categories Endpoints

### GET /project_categories/

**Operation ID:** project_categories_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Project_category Endpoints

### GET /project_category/

**Operation ID:** project_category_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Project_descriptors Endpoints

### GET /project_descriptors/

**Operation ID:** project_descriptors_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

## Property Endpoints

### GET /property/

**Operation ID:** property_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### POST /property/

**Operation ID:** property_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **property_element** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **property_element** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 

### GET /property/brif_list/

**Operation ID:** property_brif_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /property/{id}/

**Operation ID:** property_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **property_element** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 

### PUT /property/{id}/

**Operation ID:** property_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **user** (string, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **user** (string, Required): 

### PATCH /property/{id}/

**Operation ID:** property_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **user** (string, Required): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **user** (string, Required): 

### DELETE /property/{id}/

**Operation ID:** property_delete

**Parameters:**
None

**Responses:**
- **204**: 

### POST /property/{property_pk}/element/

**Operation ID:** property_element_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

### PUT /property/{property_pk}/element/{id}/

**Operation ID:** property_element_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

### PATCH /property/{property_pk}/element/{id}/

**Operation ID:** property_element_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

### DELETE /property/{property_pk}/element/{id}/

**Operation ID:** property_element_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Request Endpoints

### POST /request/unit/

**Operation ID:** request_unit_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **type** (string, Optional): 
  - **symbol** (string, Optional): 
  - **approved** (boolean, Optional): 
  - **requested_by** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **type** (string, Optional): 
  - **symbol** (string, Optional): 
  - **approved** (boolean, Optional): 
  - **requested_by** (string, Optional): 

## Service Endpoints

### POST /service/

**Operation ID:** service_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **email** (string, Required): 
  - **message** (string, Required): 
  - **subject** (string, Required): 
  - **service_type** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **email** (string, Required): 
  - **message** (string, Required): 
  - **subject** (string, Required): 
  - **service_type** (string, Optional): 

## Session Endpoints

### GET /session/

**Operation ID:** session_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **name** (query, Optional):  (Type: string)
- **data_session_groups__group_id** (query, Optional):  (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### POST /session/

**Operation ID:** session_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

### GET /session/{id}/

**Operation ID:** session_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **data_session_groups** (array, Required): 
  - **data_session_user** (array, Required): 
  - **owner_name** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **data** (object, Optional): 
  - **project_ids** (object, Optional): 
  - **is_public** (boolean, Optional): 
  - **user** (string, Required): 
  - **projects** (array, Required): 

### PUT /session/{id}/

**Operation ID:** session_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

### PATCH /session/{id}/

**Operation ID:** session_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

### DELETE /session/{id}/

**Operation ID:** session_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Standards Endpoints

### GET /standards/

**Operation ID:** standards_list

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
Array of:
    - **id** (integer, Optional): 
    - **key** (string, Required): 
    - **status** (string, Optional): 
    - **title** (string, Required): 
    - **description** (string, Optional): 
    - **groups** (array, Optional): 
    - **equipment** (array, Optional): 
    - **components** (array, Optional): 
    - **categories** (array, Optional): 
    - **configurations** (array, Optional): 
    - **attachments** (array, Optional): 
    - **full_history** (string, Optional): 

### POST /standards/

**Operation ID:** standards_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

### GET /standards/{id}/

**Operation ID:** standards_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### PUT /standards/{id}/

**Operation ID:** standards_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

### PATCH /standards/{id}/

**Operation ID:** standards_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

### DELETE /standards/{id}/

**Operation ID:** standards_delete

**Parameters:**
None

**Responses:**
- **204**: 

### GET /standards/{id}/comments/

**Operation ID:** standards_comments_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### POST /standards/{id}/comments/

**Operation ID:** standards_comments_create

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

**Responses:**
- **201**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### GET /standards/{id}/full_history/

**Operation ID:** standards_full_history

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### GET /standards/{key}/{id}/

**Operation ID:** standards_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### PUT /standards/{key}/{id}/

**Operation ID:** standards_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### PATCH /standards/{key}/{id}/

**Operation ID:** standards_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### DELETE /standards/{key}/{id}/

**Operation ID:** standards_delete

**Parameters:**
None

**Responses:**
- **204**: 

## Template Endpoints

### GET /template/

**Operation ID:** template_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /template/brif_list/

**Operation ID:** template_brif_list

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **ordering** (query, Optional): Which field to use when ordering the results. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /template/{id}/

**Operation ID:** template_read

**Parameters:**
None

**Responses:**
- **200**: 

  **Schema:**
  - **id** (string, Optional): 
  - **owner** (N/A, Required): 
  - **project** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **template_data** (object, Optional): 
  - **name** (string, Optional): 
  - **groups** (array, Optional): 

### PUT /template/{id}/

**Operation ID:** template_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **name** (string, Optional): 
  - **groups** (array, Required): 
  - **id** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **name** (string, Optional): 
  - **groups** (array, Required): 
  - **id** (string, Optional): 

### PATCH /template/{id}/

**Operation ID:** template_partial_update

**Parameters:**
- **data** (body, Required): 

  **Schema:**
  - **name** (string, Optional): 
  - **groups** (array, Required): 
  - **id** (string, Optional): 

**Responses:**
- **200**: 

  **Schema:**
  - **name** (string, Optional): 
  - **groups** (array, Required): 
  - **id** (string, Optional): 

### DELETE /template/{id}/

**Operation ID:** template_delete

**Parameters:**
None

**Responses:**
- **204**: 

## User Endpoints

### GET /user/followed/

**Operation ID:** user_followed

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 

### GET /user/followers/

**Operation ID:** user_followers

**Parameters:**
- **search** (query, Optional): A search term. (Type: string)
- **limit** (query, Optional): Number of results to return per page. (Type: integer)
- **offset** (query, Optional): The initial index from which to return the results. (Type: integer)

**Responses:**
- **200**: 

  **Schema:**
  - **count** (integer, Required): 
  - **next** (string, Optional): 
  - **previous** (string, Optional): 
  - **results** (array, Required): 



## Data Models

### User

  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 
  - **following** (boolean, Optional): 
  - **is_verified** (boolean, Optional): 
  - **is_active** (boolean, Optional): Designates whether this user should be treated as active. Unselect this instead of deleting accounts.
  - **is_premium** (boolean, Optional): 

### AccountSignup

  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **password** (string, Required): 

### CheckUserAvailability

  - **email** (string, Required): 

### ForgotPasswordSerialzier

  - **email** (string, Required): 

### InviteUser

  - **users** (array, Required): 

### TokenObtainPair

  - **email** (string, Required): 
  - **password** (string, Required): 

### UserAvailability

  - **id** (string, Optional): 
  - **email** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **following** (boolean, Optional): 

### ResendUserEmailVerificaton

  - **email** (string, Required): 

### ResetPassword

  - **token** (string, Required): 
  - **password** (string, Required): 
  - **uid** (string, Required): 

### TokenRefresh

  - **refresh** (string, Required): 
  - **access** (string, Optional): 

### Token

  - **token** (string, Required): 

### UpdateUser

  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **cover_image** (string, Optional): 

### StandardCategory

  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 

### Reaction

  - **id** (integer, Optional): 
  - **reaction_type** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **created_at** (string, Optional): 
  - **comment** (integer, Required): 

### Comment

  - **id** (integer, Optional): 
  - **content** (string, Required): 
  - **user** (string, Optional): 
  - **user_email** (string, Optional): 
  - **parent** (integer, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **replies** (string, Optional): 
  - **reactions** (array, Optional): 
  - **standard** (integer, Optional): 

### Component

  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **type** (string, Optional): 
  - **description** (string, Optional): 

### ConfigTypes

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 

### ConfigTypeHistory

  - **history_id** (integer, Optional): 
  - **history_date** (string, Required): 
  - **history_type** (string, Required): 
  - **history_user** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 

### ConstantTypes

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **magnitude** (string, Optional): 
  - **magnitude_symbol** (string, Optional): 
  - **symbol** (string, Optional): 
  - **is_liner** (boolean, Optional): 
  - **is_decibels** (boolean, Optional): 

### DescriptorsList

  - **id** (string, Optional): 
  - **descriptor_id** (string, Required): 
  - **descriptor** (string, Required): 
  - **value** (string, Optional): 

### Equipment

  - **id** (integer, Optional): 
  - **name** (string, Required): 
  - **manufacturer** (string, Optional): 
  - **description** (string, Optional): 
  - **downloads** (string, Optional): 
  - **link** (string, Optional): 

### FileUploadUser

  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 

### FileUploadGroup

  - **name** (string, Optional): 
  - **id** (string, Optional): 

### UploadedFileList

  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (array, Optional): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 

### UploadedFile

  - **id** (integer, Optional): 
  - **user** (N/A, Optional): 
  - **groups** (object, Required): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Optional): 
  - **uploaded_at** (string, Optional): 
  - **file_url** (string, Optional): 

### Notifications

  - **_id** (string, Optional): 
  - **author** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **notification_category** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 

### GroupTags

  - **name** (string, Required): 
  - **slug** (string, Required): 

### GroupsList

  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **tags** (array, Required): 
  - **members** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **id** (string, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 
  - **joined** (boolean, Optional): 
  - **requested** (boolean, Optional): 
  - **is_public** (boolean, Optional): 

### Members

  - **user** (string, Required): 
  - **group_role** (string, Required): 

### NestedGroup

  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **tags** (array, Optional): 
  - **members** (array, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

### UpdateNestedGroup

  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 
  - **description** (string, Optional): 
  - **image** (string, Optional): 
  - **image_url** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **approver** (string, Optional): 
  - **uploader** (string, Optional): 
  - **inviter** (string, Optional): 
  - **poster** (string, Optional): 

### AddMemberToGroup

  - **members** (array, Required): 

### UpdateUserRoleForGroup

  - **group_role** (string, Required): 

### SafeUser

  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 

### GroupInvitations

  - **id** (string, Optional): 
  - **user** (N/A, Optional): 
  - **is_accepted** (boolean, Optional): 
  - **group_role** (string, Optional): 
  - **group** (string, Optional): 

### Tags

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Required): 

### ProjectClean

  - **id** (string, Optional): 
  - **file_name** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **file** (string, Optional): 
  - **project_file_type** (string, Optional): 

### Group

  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **group_name** (string, Required): 

### Limits

  - **id** (string, Optional): 
  - **limit** (object, Optional): 
  - **limit_types** (string, Optional): 
  - **x_units** (string, Optional): 
  - **y_units** (string, Optional): 
  - **dimension_types** (string, Optional): 

### ListProject

  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **categories** (string, Optional): 
  - **clean_files** (array, Optional): 
  - **groups** (array, Required): 
  - **limits** (array, Required): 
  - **owner** (N/A, Required): 
  - **can_delete** (boolean, Optional): 
  - **key** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 

### Units

  - **category** (string, Required): 
  - **index_column** (string, Required): 
  - **x_axis** (string, Required): 
  - **y_axis** (string, Required): 

### Descriptors

  - **project** (string, Optional): 
  - **descriptor** (string, Required): 
  - **value** (string, Optional): 

### DataIngestionUpload

  - **file_url** (string, Required): 
  - **name** (string, Required): 
  - **units** (array, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 

### Filter

  - **key** (string, Required): 
  - **value** (string, Required): 
  - **is_negative** (boolean, Optional): 
  - **expression** (string, Optional): 
  - **operand** (string, Optional): 

### ProjectDetail

  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **categories** (string, Optional): 
  - **descriptors** (array, Required): 
  - **name** (string, Required): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **file** (string, Optional): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **limits** (array, Required): 
  - **updated_at** (string, Optional): 
  - **created_at** (string, Optional): 
  - **owner** (N/A, Required): 

### MultipleProjectDetails

  - **project_ids** (array, Required): 

### Device

  - **id** (string, Optional): 
  - **name** (string, Required): 

### DevicesAndCategoryDevice

  - **id** (string, Optional): 
  - **device** (N/A, Required): 
  - **x_units** (string, Required): 
  - **y_units** (string, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **dimension_types** (string, Optional): 
  - **category** (string, Required): 
  - **project** (string, Required): 
  - **x_units_v2** (string, Optional): 
  - **y_units_v2** (string, Optional): 

### CreateLimits

  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **limits** (array, Required): 

### Project

  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **clean_files** (array, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### UnitsJSONSerialzier

  - **x_units** (string, Required): 
  - **y_units** (string, Required): 

### StatisticsNodeAndPrimaryNode

  - **name** (string, Required): 
  - **values** (array, Required): 

### Statistics

  - **categoryName** (string, Required): 
  - **units** (N/A, Required): 
  - **primaryNode** (N/A, Required): 
  - **nodes** (array, Required): 

### CreateUpdateStatistics

  - **id** (string, Optional): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **statistics** (array, Required): 
  - **data_type** (string, Optional): 

### TemplateData

  - **records** (array, Required): 
  - **plug** (object, Optional): 
  - **version** (string, Required): 

### TemplateIntermediate

  - **data** (N/A, Required): 
  - **extends** (string, Optional): 
  - **name** (string, Optional): 

### DataIngestionUploadV2

  - **file_url** (string, Required): 
  - **v2_json_file_url** (string, Required): 
  - **name** (string, Required): 
  - **tags** (array, Required): 
  - **descriptors** (array, Required): 
  - **data_type** (string, Optional): 
  - **groups** (array, Required): 
  - **is_public** (boolean, Optional): 
  - **template** (N/A, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 

### ProjectUpdate

  - **name** (string, Required): 
  - **tags** (array, Optional): 
  - **descriptors** (array, Optional): 
  - **groups** (array, Optional): 
  - **metadata** (object, Optional): 

### PowerShellAndCurl

  - **powershell** (string, Required): 
  - **curl** (string, Required): 

### PropertyBriefViews

  - **name** (string, Required): 
  - **id** (string, Optional): 

### PropertyElement

  - **id** (string, Optional): 
  - **unit** (N/A, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 

### PropertiesList

  - **id** (string, Optional): 
  - **property** (N/A, Required): 
  - **property_element** (N/A, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **value** (string, Optional): 
  - **category** (string, Required): 
  - **device** (string, Required): 
  - **project** (string, Required): 

### Category

  - **id** (string, Optional): 
  - **name** (string, Required): 

### Property

  - **id** (string, Optional): 
  - **property_element** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 

### PropertyCreateElement

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

### PropertyCreate

  - **id** (string, Optional): 
  - **property_element** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 

### UpdateProperty

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **user** (string, Required): 

### PropertyElementCreateUpdate

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **description** (string, Optional): 
  - **type** (string, Optional): 
  - **dimension** (string, Optional): 
  - **unit** (string, Optional): 

### UnitRequestCreate

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Optional): 
  - **type** (string, Optional): 
  - **symbol** (string, Optional): 
  - **approved** (boolean, Optional): 
  - **requested_by** (string, Optional): 

### ServiceRequest

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **email** (string, Required): 
  - **message** (string, Required): 
  - **subject** (string, Required): 
  - **service_type** (string, Optional): 

### DataSessionsGroup

  - **id** (string, Optional): 
  - **group** (string, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 

### DataSessionUsers

  - **id** (string, Optional): 
  - **user** (N/A, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 

### Sessions

  - **id** (string, Optional): 
  - **data_session_groups** (array, Required): 
  - **data_session_user** (array, Required): 
  - **owner_name** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **data** (object, Optional): 
  - **project_ids** (object, Optional): 
  - **is_public** (boolean, Optional): 
  - **user** (string, Required): 
  - **projects** (array, Required): 

### SessionsCreateUpdate

  - **id** (string, Optional): 
  - **data** (object, Optional): 
  - **name** (string, Required): 
  - **is_public** (boolean, Optional): 
  - **data_session_groups** (array, Optional): 
  - **data_session_user** (array, Optional): 

### StandardGroup

  - **id** (string, Optional): 
  - **name** (string, Optional): 
  - **description** (string, Optional): 

### Configuration

  - **id** (string, Optional): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **name** (string, Required): 
  - **slug** (string, Required): 
  - **data_type** (string, Required): 
  - **public** (boolean, Optional): 
  - **for_user** (string, Required): 

### StandardUploadedFile

  - **id** (integer, Optional): 
  - **file_name** (string, Optional): 
  - **file** (string, Optional): 
  - **file_type** (string, Required): 
  - **uploaded_at** (string, Optional): 
  - **user** (string, Optional): 
  - **groups** (array, Optional): 

### StandardRead

  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 
  - **full_history** (string, Optional): 

### StandardWrite

  - **id** (integer, Optional): 
  - **key** (string, Required): 
  - **status** (string, Optional): 
  - **title** (string, Required): 
  - **description** (string, Optional): 
  - **groups** (array, Optional): 
  - **equipment** (array, Optional): 
  - **components** (array, Optional): 
  - **categories** (array, Optional): 
  - **configurations** (array, Optional): 
  - **attachments** (array, Optional): 

### TemplateProject

  - **id** (string, Optional): 
  - **tags** (array, Required): 
  - **groups** (array, Required): 
  - **descriptors** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **serial_number** (integer, Optional): 
  - **readable_key** (string, Optional): 
  - **name** (string, Required): 
  - **file** (string, Optional): 
  - **v2_json_file** (string, Optional): 
  - **status** (string, Optional): 
  - **file_type** (string, Optional): 
  - **data_type** (string, Optional): 
  - **units** (object, Optional): 
  - **invalid_cells_action** (string, Optional): 
  - **is_public** (boolean, Optional): 
  - **metadata** (object, Optional): 
  - **source** (string, Optional): 
  - **template** (string, Optional): 
  - **owner** (string, Optional): 

### TemplateViews

  - **id** (string, Optional): 
  - **owner** (N/A, Required): 
  - **project** (array, Required): 
  - **created_at** (string, Optional): 
  - **updated_at** (string, Optional): 
  - **template_data** (object, Optional): 
  - **name** (string, Optional): 
  - **groups** (array, Optional): 

### TemplateBriefViews

  - **name** (string, Optional): 
  - **id** (string, Optional): 

### TemplateUpdate

  - **name** (string, Optional): 
  - **groups** (array, Required): 
  - **id** (string, Optional): 

### SafeUserFollowers

  - **id** (string, Optional): 
  - **first_name** (string, Optional): 
  - **last_name** (string, Optional): 
  - **email** (string, Optional): 
  - **profile_image** (string, Optional): 
  - **followed_back** (boolean, Optional): 


