# Authentication

The Lyceum API uses token-based authentication. To access protected endpoints, you must obtain an access token by logging in with your credentials. The access token is short-lived, and a refresh token is provided to obtain a new access token without re-entering credentials.

## Base URL

All API endpoints are relative to a base URL. The default base URL is `https://api.thelyceum.io/api`. However, this can be overridden by setting the `LYCEUM_API_BASE` environment variable. Ensure you use the correct base URL for your environment.

## Login

To authenticate and obtain access and refresh tokens, send a POST request to `/account/login` with your email and password.

### Request

- **Method:** POST
- **URL:** `/account/login`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
```json
{
  "email": "your_email@example.com",
  "password": "your_password"
}
```

### Response

- **Status Code:** 200 OK
- **Body:**
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### Examples

#### cURL

```bash
curl -X POST https://api.thelyceum.io/api/account/login \
  -H "Content-Type: application/json" \
  -d '{"email": "your_email@example.com", "password": "your_password"}'
```

#### Python

```python
import requests

url = "https://api.thelyceum.io/api/account/login"
data = {"email": "your_email@example.com", "password": "your_password"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)
print(response.json())
```

#### JavaScript

```javascript
fetch("https://api.thelyceum.io/api/account/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    email: "your_email@example.com",
    password: "your_password"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Common Error Responses

- **400 Bad Request:** Invalid request format or missing fields (e.g., email or password not provided).
- **401 Unauthorized:** Incorrect email or password.

## Token Refresh

To obtain a new access token when the current one expires, send a POST request to `/account/token/refresh` with your refresh token.

### Request

- **Method:** POST
- **URL:** `/account/token/refresh`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
```json
{
  "refresh": "your_refresh_token"
}
```

### Response

- **Status Code:** 200 OK
- **Body:**
```json
{
  "access": "new_access_token"
}
```

### Examples

#### cURL

```bash
curl -X POST https://api.thelyceum.io/api/account/token/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

#### Python

```python
import requests

url = "https://api.thelyceum.io/api/account/token/refresh"
data = {"refresh": "your_refresh_token"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)
print(response.json())
```

#### JavaScript

```javascript
fetch("https://api.thelyceum.io/api/account/token/refresh", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    refresh: "your_refresh_token"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Common Error Responses

- **400 Bad Request:** Invalid or missing refresh token.
- **401 Unauthorized:** Refresh token is expired or invalid.

## User Information

To retrieve user details, including verification status, send a GET request to `/account/me/` with the access token in the Authorization header.

### Request

- **Method:** GET
- **URL:** `/account/me/`
- **Headers:**
  - `Authorization: Bearer your_access_token`

### Response

- **Status Code:** 200 OK
- **Body:**
```json
{
  "id": "user_id",
  "email": "your_email@example.com",
  "is_verified": true
}
```
*Note: Additional fields may be present in the response.*

### Examples

#### cURL

```bash
curl -X GET https://api.thelyceum.io/api/account/me/ \
  -H "Authorization: Bearer your_access_token"
```

#### Python

```python
import requests

url = "https://api.thelyceum.io/api/account/me/"
headers = {"Authorization": "Bearer your_access_token"}
response = requests.get(url, headers=headers)
print(response.json())
```

#### JavaScript

```javascript
fetch("https://api.thelyceum.io/api/account/me/", {
  method: "GET",
  headers: {
    "Authorization": "Bearer your_access_token"
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

### Common Error Responses

- **401 Unauthorized:** Access token is missing, invalid, or expired.
- **403 Forbidden:** User lacks permission to access this resource.

### Verification Status

The `is_verified` field in the response indicates whether the user's account is verified. Some API endpoints or features may require verification. If `is_verified` is `false`, access to certain functionalities may be restricted.

## Notes

- **Token Storage:** The script uses a `SecureStorage` class to encrypt and store tokens locally. In your application, ensure tokens are stored securely (e.g., encrypted storage or secure keychains) to prevent unauthorized access.
- **Environment Variables:** The script supports pre-filling credentials via `LYCEUM_LOGIN_USERNAME` and `LYCEUM_LOGIN_PASSWORD` environment variables, though these are optional.
- **Additional Headers:** The script sets `Cache-Control` and `User-Agent` headers for the `/account/me/` request. These are not strictly required for basic authentication but may be included for compatibility or caching control if needed.
