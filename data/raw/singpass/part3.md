> This is part 3 of 3 of the full documentation (pages 201–205 of 205).
> The content is paginated: fetch every part to see all of it.
> Previous part: https://docs.developer.singpass.gov.sg/docs/llms-full.txt/1
> Page index: https://docs.developer.singpass.gov.sg/docs/llms.txt

> Agents can also search and read this documentation through its [MCP server](https://docs.developer.singpass.gov.sg/docs/~gitbook/mcp).

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
This site has an agentic ask interface you may use to query the documentation dynamically by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://docs.developer.singpass.gov.sg/docs/index.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

---

# .well-known Endpoints


# OpenID Discovery Endpoint

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Responses from this endpoint can and should be cached for at least 1 hour, and NOT retrieved for each OIDC/Auth2 operation. Cache-Control headers on the response indicate a possible policy.

{% hint style="info" %}
If you are using an off-the-shelf OIDC client to integrate with Singpass, you will probably only need to specify our Issuer URL.

OIDC Discovery URLs in general may be derived by concatenating the string `/.well-known/openid-configuration` to the Issuer URL.
{% endhint %}

## Curl request

```bash
$ curl 'https://stg-id.singpass.gov.sg/.well-known/openid-configuration' -i -X GET \
    -H 'Accept: application/json'
```

## HTTP request

```http
GET /.well-known/openid-configuration HTTP/1.1
Accept: application/json
Host: stg-id.singpass.gov.sg
```

## HTTP response

```http
HTTP/1.1 200 OK
Cache-Control: max-age=21600, must-revalidate, no-transform, public
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Thu, 26 Sep 2024 03:38:09 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 1125

{
  "issuer" : "https://stg-id.singpass.gov.sg",
  "authorization_endpoint" : "https://stg-id.singpass.gov.sg/auth",
  "jwks_uri" : "https://stg-id.singpass.gov.sg/.well-known/keys",
  "response_types_supported" : [ "code" ],
  "scopes_supported" : [ "openid" ],
  "subject_types_supported" : [ "public" ],
  "claims_supported" : [ "nonce", "aud", "iss", "sub", "exp", "iat" ],
  "grant_types_supported" : [ "authorization_code", "urn:openid:params:grant-type:ciba" ],
  "token_endpoint" : "https://stg-id.singpass.gov.sg/token",
  "token_endpoint_auth_methods_supported" : [ "private_key_jwt" ],
  "token_endpoint_auth_signing_alg_values_supported" : [ "ES256", "ES384", "ES512" ],
  "id_token_signing_alg_values_supported" : [ "ES256" ],
  "id_token_encryption_alg_values_supported" : [ "ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW" ],
  "id_token_encryption_enc_values_supported" : [ "A256CBC-HS512" ],
  "backchannel_authentication_endpoint" : "https://stg-id.singpass.gov.sg/bc-auth",
  "backchannel_token_delivery_modes_supported" : [ "poll" ],
  "userinfo_endpoint" : "https://stg-id.singpass.gov.sg/userinfo"
}
```

## **HTTPie request**

```bash
$ http GET 'https://stg-id.singpass.gov.sg/.well-known/openid-configuration' \
    'Accept:application/json'
```

## Request body

```
```

## Response body

```json
{
  "issuer": "https://stg-id.singpass.gov.sg",
  "authorization_endpoint": "https://stg-id.singpass.gov.sg/auth",
  "jwks_uri": "https://stg-id.singpass.gov.sg/.well-known/keys",
  "response_types_supported": ["code"],
  "scopes_supported": ["openid"],
  "subject_types_supported": ["public"],
  "claims_supported": ["nonce", "aud", "iss", "sub", "exp", "iat"],
  "grant_types_supported": [
    "authorization_code",
    "urn:openid:params:grant-type:ciba"
  ],
  "token_endpoint": "https://stg-id.singpass.gov.sg/token",
  "token_endpoint_auth_methods_supported": ["private_key_jwt"],
  "token_endpoint_auth_signing_alg_values_supported": [
    "ES256",
    "ES384",
    "ES512"
  ],
  "id_token_signing_alg_values_supported": ["ES256"],
  "id_token_encryption_alg_values_supported": [
    "ECDH-ES+A256KW",
    "ECDH-ES+A192KW",
    "ECDH-ES+A128KW"
  ],
  "id_token_encryption_enc_values_supported": ["A256CBC-HS512"],
  "backchannel_authentication_endpoint": "https://stg-id.singpass.gov.sg/bc-auth",
  "backchannel_token_delivery_modes_supported": ["poll"],
  "userinfo_endpoint": "https://stg-id.singpass.gov.sg/userinfo"
}
```

## Response fields

| Path                                               | Type     | Description                                                                                                                                                                                                                                  |
| -------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issuer`                                           | `String` | URL (identity) of the issuer.                                                                                                                                                                                                                |
| `authorization_endpoint`                           | `String` | URL of the OP’s OAuth 2.0 Authorization Endpoint.                                                                                                                                                                                            |
| `jwks_uri`                                         | `String` | URL of the OP’s JSON Web Key Set.                                                                                                                                                                                                            |
| `response_types_supported`                         | `Array`  | JSON array containing a list of the OAuth 2.0 response\_type values that OP supports.                                                                                                                                                        |
| `scopes_supported`                                 | `Array`  | JSON array containing a list of the OAuth 2.0 scope values that OP supports.                                                                                                                                                                 |
| `subject_types_supported`                          | `Array`  | JSON array containing a list of the Subject Identifier types that this OP supports.                                                                                                                                                          |
| `claims_supported`                                 | `Array`  | JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for.                                                                                                                     |
| `grant_types_supported`                            | `Array`  | JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.                                                                                                                                                       |
| `token_endpoint`                                   | `String` | URL of the OP’s OAuth 2.0 Token Endpoint. This contains the signing key(s) the RP uses to validate signatures from the OP.                                                                                                                   |
| `token_endpoint_auth_methods_supported`            | `Array`  | JSON array containing a list of Client Authentication methods supported by this Token Endpoint.                                                                                                                                              |
| `token_endpoint_auth_signing_alg_values_supported` | `Array`  | JSON array containing a list of the JWS signing algorithms (alg values) supported by the Token Endpoint for the signature on the JWT used to authenticate the Client at the Token Endpoint for the private\_key\_jwt authentication methods. |
| `id_token_signing_alg_values_supported`            | `Array`  | JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                                  |
| `id_token_encryption_alg_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                               |
| `id_token_encryption_enc_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (enc values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                               |
| `backchannel_token_delivery_modes_supported`       | `Array`  | JSON array containing supported backchannel delivery modes.                                                                                                                                                                                  |
| `backchannel_authentication_endpoint`              | `String` | URL of the OP’s Backchannel Authentication Endpoint.                                                                                                                                                                                         |
| `userinfo_endpoint`                                | `String` | URL of the OP’s UserInfo Endpoint.                                                                                                                                                                                                           |

<br>


# JWKS Endpoint

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Singpass signs all JWTs issued during the authentication process using its ASP signing key. Integrating parties can validate the JWT signatures by acquiring the signing public key from a **JSON Web Key Set (JWKS)** endpoint.

This endpoint will return one or more public keys in [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) form. The correct JWK to use for signature validation will have its `use` attribute as `sig` (to indicate that it is a signing key), and its `kid` value should match the one found in the JWT under validation.

Public keys returned from this endpoint could be in random sequence or rotated for security enhancement. For more information, please refer to [Caching and key rotation](#caching-and-key-rotation) section.

## Curl request

```bash
$ curl 'https://stg-id.singpass.gov.sg/.well-known/keys' -i -X GET \
    -H 'Accept: application/json'
```

## HTTP request

```http
GET /.well-known/keys HTTP/1.1
Accept: application/json
Host: stg-id.singpass.gov.sg
```

## HTTP response

```http
HTTP/1.1 200 OK
Cache-Control: max-age=21600, must-revalidate, no-transform, public
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Thu, 26 Sep 2024 03:38:09 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Content-Type: application/json
Content-Length: 697

{
  "keys" : [ {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "eckey-test-secondary",
    "x" : "9bRoLZyZeV49dMVYauCapuZJ7g8ae8e0vWERXr77OT8",
    "y" : "o6lIAyvlmjV7qkGLlLkPIoKHc9VQxSXWgZ-xnboPuuU"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "eckey-test",
    "x" : "MW_NF3jr-Fjn8RMg7_ewHfc4VBNJJUnn_gGht3Y-Aeo",
    "y" : "hqdPsdwc8FHpPl47VInEgK2F3and2P_0AnR2q92o4M0"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "alias/test-sp-auth-api-id-token-signing-key-kms-asymmetric-key-alias",
    "x" : "wit9gl-WpjLzgpNmpf4RP8UHLDHzqq1HHhQPmGCALdY",
    "y" : "oFVT90ZGZdkw8Ok-G9MvsE1SUhh1N0I78LFrprrIHx8"
  } ]
}
```

## HTTPie request

```bash
$ http GET 'https://stg-id.singpass.gov.sg/.well-known/keys' \
    'Accept:application/json'
```

## Request body

```http
```

## Response body

```json
{
  "keys": [
    {
      "kty": "EC",
      "use": "sig",
      "crv": "P-256",
      "kid": "eckey-test-secondary",
      "x": "9bRoLZyZeV49dMVYauCapuZJ7g8ae8e0vWERXr77OT8",
      "y": "o6lIAyvlmjV7qkGLlLkPIoKHc9VQxSXWgZ-xnboPuuU"
    },
    {
      "kty": "EC",
      "use": "sig",
      "crv": "P-256",
      "kid": "eckey-test",
      "x": "MW_NF3jr-Fjn8RMg7_ewHfc4VBNJJUnn_gGht3Y-Aeo",
      "y": "hqdPsdwc8FHpPl47VInEgK2F3and2P_0AnR2q92o4M0"
    },
    {
      "kty": "EC",
      "use": "sig",
      "crv": "P-256",
      "kid": "alias/test-sp-auth-api-id-token-signing-key-kms-asymmetric-key-alias",
      "x": "wit9gl-WpjLzgpNmpf4RP8UHLDHzqq1HHhQPmGCALdY",
      "y": "oFVT90ZGZdkw8Ok-G9MvsE1SUhh1N0I78LFrprrIHx8"
    }
  ]
}
```

## Caching and key rotation

> IMPORTANT: Responses from this endpoint, or individual keys from inside the JWKS can and should be cached for at least 1 hour, and NOT retrieved for each JWT validation. Cache-Control headers on the response indicate a possible policy.

For varying reasons, keys used for signing can and will be rotated/changed with no defined schedule, and at the full discretion of NDI. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different `kid` value. The new `kid` value will be reflected in all the new JWTs signed by NDI. In such cases, cached copies of NDI public keys must be refreshed by re-invoking the JWKS endpoint.

If the validation of the NDI signature fails, re-fetch from the JWKS endpoint once for that validation.

Please read through the list of **DON’Ts** below:

* Do not assume the position of a signing key among the list of the returned keys.
* Do not validate NDI signatures using a hardcoded public key OR `kid`. Always determine the correct key (for signature verification) by inspecting the `kid` from the JWS header, and use it to retrieve the public key from our JWKS endpoint.
* Do not cache only 1 key. Caching should be done for the entire JWKS.


# Error Response

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Singpass APIs are RESTful in design and communicate classes of errors based on the **HTTP status code**. The status code should be used to determine if the error is caused by consumer or provider. Consumers should log the HTTP status code along with the `id` and/or `trace_id` of the error.

<table><thead><tr><th width="191">HTTP Status</th><th>Description</th></tr></thead><tbody><tr><td>4xx</td><td><p>Errors caused by API consumer. You can expect codes such as 400, 401, 403, 404 etc. if incorrect requests are made to APIs.</p><p>Example: <strong>400 Bad Request due to invalid/missing request arguments</strong></p></td></tr><tr><td>5xx</td><td><p>Errors caused by API provider or its dependencies. You can expect codes such as 500, 502, 503 etc if there is an issue on Singpass or its dependencies.</p><p>Example: <strong>500: Internal Server Error due to some kind of programming error.</strong></p></td></tr></tbody></table>

Example: Invalid Request Parameters

```http
HTTP/1.1 400 Bad Request
Connection: keep-alive
Cache-Control: no-cache, no-store, must-revalidate
Transfer-Encoding: chunked
Content-Type: application/json
Date: Thu, 26 Sep 2024 03:36:41 GMT
Content-Length: 190

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "CLIENT_SIDE_ERROR",
  "error_description" : "This is an invalid request.",
  "trace_id" : "66f4d6c93a23476106150eb7c40d7dc9"
}
```

Example: Server Error

```http
HTTP/1.1 500 Internal Server Error
Cache-Control: no-cache, no-store, must-revalidate
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Thu, 26 Sep 2024 03:36:41 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 192

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "SERVER_SIDE_ERROR",
  "error_description" : "An unexpected error occurred.",
  "trace_id" : "66f4d6c97ef952fbff9f2d20f6b826f9"
}
```

| Path                | Type                             | Description                                                                                                                                                                                                                                                                                               |
| ------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | `String`                         | The unique identifier for this error/request. Please log this identifier for support and debugging purposes.                                                                                                                                                                                              |
| `trace_id`          | `String InstanceOfAssertFactory` | (Optional) An auxiliary id for request correlation across services. Please also log this identifier for operational support and debugging purposes.                                                                                                                                                       |
| `error`             | `String`                         | Error code representing broad class of error; likely to be one of CLIENT\_SIDE\_ERROR, ARGUMENTS\_NOT\_VALID, SERVER\_SIDE\_ERROR, TOO\_MANY\_REQUESTS. However, specific error codes can be returned for some endpoints, in which case you may find more details in the documentation for that endpoint. |
| `error_description` | `String`                         | Returns human readable general information about the reason for the error. Note that due to security reasons; detailed information is unlikely to be available in this message.                                                                                                                           |


# Contact

If you have any other queries, please go to [partnersupport.singpass.gov.sg](http://partnersupport.singpass.gov.sg/) and submit a request.


