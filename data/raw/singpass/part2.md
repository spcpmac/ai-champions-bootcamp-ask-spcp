> This is part 2 of 3 of the full documentation (pages 101–200 of 205).
> The content is paginated: fetch every part to see all of it.
> Previous part: https://docs.developer.singpass.gov.sg/docs/llms-full.txt
> Next part: https://docs.developer.singpass.gov.sg/docs/llms-full.txt/2
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

# How to Onboard our API

This information is for onboarding onto Sign V3. Do note that we are no longer supporting new requests to onboard onto Sign V1.

{% hint style="success" %}
**Onboarding for Sign V3 is open.** Please follow the steps below to onboard via the Singpass Developer Portal.
{% endhint %}

## Onboarding Steps

{% stepper %}
{% step %}

### Before you start (Prerequisites)

#### Get Access to Singpass Developer Portal (SDP)

* Sign with Singpass integrations are managed via SDP
* 👉 [How to get access to developer.singpass.gov.sg](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/obtaining-access-to-the-singpass-developer-portal-sdp)

#### Download Singpass Staging App ([guide here](https://docs.developer.singpass.gov.sg/docs/testing/testing-with-singpass-app))

* You need a Singpass Staging App to test that your application is successfully redirecting users to the Sign portal, and that they can sign with their Singpass app.

#### Gather information about your use case

* Description of use case and estimated transaction volume
* Sample of document(s) to be signed
  {% endstep %}

{% step %}

### Design & UX Setup

#### Download the Sign with Singpass button

* The Sign button is available to download in 2 sizes here.

{% file src="/files/n5X7FvyMnJZp4ZJi5ZAk" %}

* If you want to customise the Sign button e.g. change the button font to your brand font, please consult the section [UX Guidelines](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/ux-guidelines#implementing-the-sign-with-singpass-button) in our [UX Guidelines](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/ux-guidelines)on how to implement the button in your application

#### Prepare your application details

You can define the **App Name** and **Logo** that will be displayed to users on our Sign portal. Logos must meet the following requirements:

* PNG format
* Square (1:1 ratio) dimension
* Min size: 256px by 256px
* Max size: 512px by 512px in size.

*Note: **Entity Name** cannot be changed, it is based on the UEN associated with your Singpass Developer Portal account.*

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-d0fe4223fe48cd3103e2ed7b2b33323210dfa952%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Prepare your user journey

As part of your app creation in the **production** environment, you are required to submit a User Journey that illustrates how your digital service will use the Sign with Singpass API.

{% file src="/files/gkRvthnek88TEkjgEiDJ" %}
{% endstep %}

{% step %}

### Technical Integration

Set up the following resources in your own staging environment:

* [**Webhook URL**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook)
* [**JWKS URL**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/jwks-specification)
* [**Redirect URL**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/redirect-from-sign-with-singpass)
  {% endstep %}

{% step %}

### Request for Staging access

1. Log onto [Singpass Developer Portal](https://developer.singpass.gov.sg)
2. Toggle to the **Staging Environment**
3. Click "**New App"** and select "Sign with Singpass"
4. Enter in the details you have prepared in Steps 1-3

If you encounter any issues, please submit a request at [partnersupport.singpass.gov.sg](http://partnersupport.singpass.gov.sg/).
{% endstep %}

{% step %}

### Test your staging integration

Once you have received access to the endpoints, we recommend performing these tasks:

* [ ] Check that you can [initiate a signing request](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request)
* [ ] Complete a signing request (with your Staging Singpass app) and check that your application's webhook is successfully called
* [ ] Retrieve the signed document from the [webhook call](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook)
* [ ] Check that you can call the [get signing result endpoint](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/get-signing-result)
* [ ] (Upon smooth integration) Take screenshots of your end-to-end flow to complete the user journey document
  {% endstep %}

{% step %}

### Request for Production Access

Once your staging implementation is complete and you are ready to go live:

1. Log onto [Singpass Developer Portal](https://developer.singpass.gov.sg)
2. Ensure you have done the following:
   1. Agreed to the Singpass Services Agreement ([instructions here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/consent-to-singpass-service-agreement))
   2. Updated your billing contact details ([instructions here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/updating-billing-contact-information))
3. Toggle to the **Production Environment**
4. Click "**New App"** and select "Sign with Singpass"
5. Enter in the details you have prepared for your **production** application
6. Once your **production app has been approved**, you can start testing and using your integration.

{% hint style="warning" %}
⏳ Note: Production App approval may take up to 2 weeks. Please plan your rollout timeline accordingly.
{% endhint %}
{% endstep %}
{% endstepper %}


# API Documentation


# Sign V3

V3 continues our mission to enhance the convenience and security of digital signing in Singapore. It significantly reduces technical complexity, ensuring faster and safer implementation, and provides greater access to digital signing to businesses and citizens across various aspects of their lives.

## Change log

<table><thead><tr><th width="118.1431884765625">Date</th><th>Changes</th></tr></thead><tbody><tr><td>2 June 2025</td><td><p><strong>V3.0</strong></p><p>Initial version</p></td></tr><tr><td>14 August 2025</td><td>Added acceptable PDF dimensions</td></tr><tr><td>7 Oct 2025</td><td><p><strong>V3.2</strong></p><p>Released PDF viewer within Sign Portal; support for multiple signing locations by the same signer within the document, and option for RP to specify an intended signer; and returning of signer information to the RP's webhook.</p></td></tr><tr><td>21 Oct 2025</td><td>Update PDF requirements that it must not be hybrid-referenced</td></tr><tr><td>15 Jan 2026</td><td><strong>Cancel Sign Request:</strong> New feature to allow Relying Parties (RPs) to cancel an initiated sign request<br><strong>Increased limit for multiple signing locations:</strong> Support for up to 20 locations per signing request</td></tr></tbody></table>

## High-level integration flow

Relying Parties (RPs) will send us the document, and then redirect the user to our Sign portal to perform the signing. Sign will then notify the RP of a successful signing via their webhook, from which RPs can retrieve the signed document.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-bd52d21ba5aacb3fe300206273d5646d507f74ca%2Fsign_v3.jpg?alt=media" alt=""><figcaption><p>Sign V3 High-level integration flow</p></figcaption></figure>

RPs are expected to implement the following steps referenced from the diagram above:

<table><thead><tr><th width="62.7664794921875">Step</th><th width="106.00433349609375">Component</th><th width="264.38543701171875">Summary</th><th>Specifications</th></tr></thead><tbody><tr><td>1</td><td>Backend</td><td>Send raw document to Sign with Singpass and get <code>signing_url</code></td><td><a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request">Initiate Sign Request</a></td></tr><tr><td>2</td><td>Frontend</td><td>Redirect user to Sign with Singpass</td><td>Redirect user to the <a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal">Sign Portal</a> via the <code>signing_url</code> retuned in step 1. RP should follow <a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/ux-guidelines">UX Guidelines</a> to render the "Sign with Singpass" button.</td></tr><tr><td>3.1</td><td>Frontend</td><td>Accept redirect from Sign with Singpass</td><td><a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/redirect-from-sign-with-singpass">Redirect From Sign with Singpass</a></td></tr><tr><td>3.2</td><td>Backend</td><td>Accept success signing webhook</td><td><a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook">Accept Success Signing Webhook</a></td></tr><tr><td>4</td><td>Backend</td><td>Get signing result</td><td><a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/get-signing-result">Get Signing Result</a></td></tr><tr><td>5</td><td>Backend</td><td>Download signed document</td><td>N/A. Just fetch the signed document from <code>signed_doc_url</code></td></tr><tr><td>0</td><td>Backend</td><td>JWKS specifications</td><td><a data-mention href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/jwks-specification">JWKS Specification</a></td></tr></tbody></table>

## Production and staging URLs

**Staging Base URL:** <https://staging.sign.singpass.gov.sg/api/v3>

**Production Base URL:** <https://app.sign.singpass.gov.sg/api/v3>

## Developer tools

{% hint style="warning" %}
These tools are open-source community projects and are not officially supported or maintained by the Sign team. We welcome contributions to improve them. Their inclusion here does not imply endorsement or preference by the Sign team.
{% endhint %}

### Demo App

[Sign V3 Demo App](https://github.com/singpass/sign-v3-demo-app) is a reference implementation that demonstrates how RPs can integrate with V3. It helps partners explore the API and conduct early-stage integration testing.

### Mockpass

[**Mockpass**](https://github.com/opengovsg/mockpass) is an open-source mock server that stubs various Singpass APIs, including the **Sign v3** signing flow. It is designed for local development, CI and low environment testing, enabling fast, repeatable, and secure integration without relying on staging infrastructure.

### Sign Location helper

[Sign Location Helper](https://github.com/singpass/sign-location-helper) is a fully client-side browser-based tool for visually determining signature coordinates within a PDF document. It allows users to upload a PDF, place and drag signature boxes, and copy normalised `(x, y, page)` values for use in Sign v3. Ideal for RPs experimenting signature placement.

<br>


# Initiate Sign Request

This endpoint allows RP to initiate a signing session by sending the raw PDF document. The service processes the document to set up a signing transaction and returns a unique sign request identifier along with a signing URL to redirect users to in order for them to perform the signing.

## Implementation Notes

1. Each signing session allows for **one user** to affix **up to 20 signatures** within **one PDF document.**
2. RPs may optionally **specify the intended signer** by providing their NRIC
   1. If specified, only this individual will be able to view and sign the document
   2. If left blank, the document will be "locked" to the first user who accesses it, and no other users will be able to access or sign it. If another user needs to access the document instead, RPs must initiate a new signing session.
3. All signing sessions must be initiated via the [Singpass button](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/ux-guidelines#implementing-the-sign-with-singpass-button) and not through providing any redirect links directly to the user.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-d7eb48f4ad2cbe9b35ea42052f86a29f7ae78e4b%2Fimage%20(53).png?alt=media" alt=""><figcaption><p>Sign with Singpass button</p></figcaption></figure>

3. Each signing session has a validity of **30 mins**. RPs should only initiate a request when the application is ready to redirect the user to the Sign portal to perform the signing.

## **Path**

<mark style="color:green;">`POST`</mark> `/sign-requests`

## **Headers**

| Name          | Value                      |
| ------------- | -------------------------- |
| Content-Type  | `application/octet-stream` |
| Authorization | `<token>`                  |

## **Authorization token**

RPs should sign the signature parameter into a JWT token as authorization token.

**Token Type:** Standard JWT ([JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519))

{% hint style="info" %}
You can use the free tool <https://jwt.io/> to verify if your token is signed properly.
{% endhint %}

RPs should specify the payload based on whether they require one or multiple signatures from the user. RPs can also increase the security of the signing session by specifying the identity of the individual who can view and sign the document using the `signer_uin_hash` field.

**Note:** Multiple signatures will still only be performed by *one* user. If you require multiple *different* users to sign the same document, you must iteratively start a new signing session with the signed output of the previous user's signing session.

{% tabs %}
{% tab title="Single Signature" %}
**Use Case:** If you only require the user to sign on one location within the document.

**Payload:**

* `x` & `y`: Coordinates for placing the signature. The values should be ≥ 0 and <1, with a maximum precision of four decimal places. See detailed explanation in [#how-to-set-signing-coordinates](#how-to-set-signing-coordinates "mention")
* `page`: The page number for placing the signature. Starting from 1.
* `doc_name`: The name of the document. This will be shown to the user.
* `client_id`: Your application's registered client ID.
* `signer_uin_hash` : (Optional) A SHA256 hash of the user's NRIC in uppercase. If specified, only this user will be able to view and sign the document. Refer to [Sign Portal User Journey](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal#negative-flows) for error flows your user might see after logging in.
* `redirect_uri` : The URL your user will be redirected to upon success/error. It must match against your redirect\_uri(s) registered on Singpass Developer Portal.
* `jti`: Standard JWT ID, a unique identifier for the JWT, must be a UUID.
* `iat` & `exp`: Standard Issued At / Expiration timestamp of JWT. Must issued within 2 minutes.

**Example:**

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsImtpZCI6InBUaHpVbl9JNVJXZzcyQWEyUzI1LXhoRG0wRzBNWjNSN3FpWUdyYmVmT0EifQ.eyJkb2NfbmFtZSI6ImR1bW15LnBkZiIsImNsaWVudF9pZCI6ImxvY2FsLXRlc3QiLCJqdGkiOiJhOWIxYjU4MS1lYjY3LTRkZWEtODBhYy02NTViMWFhZmQ0NzEiLCJ4IjowLCJ5IjowLCJwYWdlIjoxLCJyZWRpcmVjdF91cmkiOiJodHRwczovL3JlZGlyZWN0LmNvbS9yZWRpcmVjdCIsImlhdCI6MTc3NDkzOTEyOCwiZXhwIjoxNzc0OTM5MjQ4fQ.gyXThRwkXNxypcrFv8PPvS7sfPoTMW-rMK-ntvgc17YNmLpTXQqRdyFIT8jUK0J2fpmEwZfsnROBIdzkOZyF0g
```

{% endcode %}
{% endtab %}

{% tab title="Multiple Signatures" %}
**Use Case:** If you require the same user to sign on multiple locations within the same document.

**Payload:**

* `sign_locations` : an array of up to 20 signature locations. Each location is an object containing `x` ,`y` , and `page` . See detailed explanation in [#how-to-set-signing-coordinates](#how-to-set-signing-coordinates "mention")
* `doc_name`: The name of the document. This will be shown to the user.
* `client_id`: Your application's registered client ID.
* `signer_uin_hash` : (Optional) A SHA256 hash of the user's NRIC in uppercase. If specified, only this user will be able to view and sign the document. Refer to [Sign Portal User Journey](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal#negative-login-flows) for error flows your user might see after logging in.
* `redirect_uri` : The URL your user will be redirected to upon success/error. It must match against your redirect\_uri(s) registered on Singpass Developer Portal.
* `jti`: Standard JWT ID, a unique identifier for the JWT, must be a UUID.
* `iat` & `exp`: Standard Issued At / Expiration timestamp of JWT. Must issued within 2 minutes.

{% hint style="warning" %}
Please note that we will reject the request if there are overlapping signatures detected.
{% endhint %}

**Example:**

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsImtpZCI6InBUaHpVbl9JNVJXZzcyQWEyUzI1LXhoRG0wRzBNWjNSN3FpWUdyYmVmT0EifQ.eyJkb2NfbmFtZSI6ImR1bW15LnBkZiIsImNsaWVudF9pZCI6ImxvY2FsLXRlc3QiLCJqdGkiOiI0NDE2ZDY2MS0xZmMxLTQ4MjItYWM4ZS00YzZmODhhYjI2MTIiLCJzaWduX2xvY2F0aW9ucyI6W3sieCI6MCwieSI6MCwicGFnZSI6MX0seyJ4IjowLjUsInkiOjAuNSwicGFnZSI6MX1dLCJyZWRpcmVjdF91cmkiOiJodHRwczovL3JlZGlyZWN0LmNvbS9yZWRpcmVjdCIsImlhdCI6MTc3NDkzOTE1OCwiZXhwIjoxNzc0OTM5Mjc4fQ.zQnogAwVAEabwqlw5gOaKJDR_dRn8qwjdmvWmkxQU2Sy8cHmzbhTo-BJLv2r8vp17jPl7dk-hDmCOMw8gwj5xQ
```

{% endcode %}
{% endtab %}
{% endtabs %}

## **Body**

Raw binary PDF content

### PDF Requirements

* PDF must be less than 10 MB in size.
* PDF must have less than 100 pages.
* PDF must be unencrypted.
* PDF must not contain JavaScript or Hide actions. Both can change what the document displays after it has been signed.
* PDF must not be a hybrid-reference PDF
  * for example, this can happen if you export a PDF from Word using the option **“Best for electronic distribution and accessibility.”**
* If the PDF contains existing signature(s):
  * These signatures should fulfil the requirements of a PAdES signature (minimally B-T).\
    *Note: Signatures created with Sign will automatically fulfil these requirements*
  * These signatures should not overlap with the x-y coordinates given.
* The dimension allowed for each page are as follows:
  * Minimum width: 220pt or 300px
  * Minimum height: 60pt or 80px
  * Maximum width and height: 3370pt or 4490px
  * Ratio between width and height must be less than 2. e.g. 300px x 1000px document will not be accepted, even though it is within the acceptable range of width and height.

### Privacy

The PDF document is held temporarily during the signing process and purged when no longer needed.

## **Sample request**

```sh
curl 'https://staging.sign.singpass.gov.sg/api/v3/sign-requests' \
  -H 'authorization: XXX' \
  -H 'content-type: application/octet-stream' \
  --data 'file=@path_to_your_test.pdf'
```

## **Response**

{% tabs %}
{% tab title="Created (201)" %}
The signing URL will bring the signer to the [Sign Portal](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal) where they will perform the signing.

```json
{
  "request_id": "signv3-01961944-5491-785a-baf2-edea694ae61a",
  "signing_url": "https://staging.sign.singpass.gov.sg/?token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ24tc3RnLTAxIn0.eyJyZXF1ZXN0X2lkIjoic2lnbnYzLTAxOTYxOTQ0LTU0OTEtNzg1YS1iYWYyLWVkZWE2OTRhZTYxYSIsImlhdCI6MTc0NDE4MDYzMCwiZXhwIjoxNzQ0MTgyNDMwfQ.UGBmPO2IHUKxyMO9ZjpGt_NuhHqbBTz2IuFmYcHFzi0slw3K1V-XpIfVqW8ua3PGoWf52jNPBH2lkPhcz69r6A",
  "exchange_code": "37994734-1d76-4d27-b5f0-96dd1504cf67"
}
```

{% hint style="info" %}
`signing_url` will only be valid for **30 minutes** upon issuance. RPs are expected to create sign requests on demand upon signing.

We may change the format of`signing_url` at any point of time.
{% endhint %}

{% hint style="warning" %}
`exchange_code` should be treated as a secret as it will be used to [get the signing result](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/get-signing-result). Please **do not** share the code or put in your application logs.
{% endhint %}
{% endtab %}

{% tab title="Invalid File Error (400)" %}
There may be a few scenarios under which you will receive a 400 error:

* `CONTENT_TOO_LARGE`: File size has exceeded 10 MB
* `BAD_SIGN_LOCATION`: The signature coordinates could be out of bounds, overlapping other forms or in a page that is non existent.
* `INVALID_PDF`: The PDF file in the request may be corrupted or set with MDP permissions that restrict further signing.
* `CLIENT_SIDE_ERROR`: A catch-all error for bad input values (for e.g. a number when a string is expected, or if redirect\_uri does not exists in the list of registered redirect\_uris)

```json
{
  "error": "BAD_SIGN_LOCATION",
  "error_description": "Signature field is out of bounds",
  "id": "ca21bb57-8255-46f0-b2f4-80613768ea6e",
  "trace_id": "7755321139078968799"
}
```

{% endtab %}

{% tab title="Auth Token Error (401)" %}

```json
{
  "error": "UNAUTHORIZED",
  "error_description": "Unauthorized.",
  "error_details": "JWT validation failed",
  "id": "ca21bb57-8255-46f0-b2f4-80613768ea6e",
  "trace_id": "7755321139078968799"
}
```

{% endtab %}

{% tab title="Server error (500)" %}

```json
{
  "error": "SERVER_SIDE_ERROR",
  "error_description": "Something went wrong.",
  "id": "ca21bb57-8255-46f0-b2f4-80613768ea6e",
  "trace_id": "7755321139078968799"
}
```

{% endtab %}
{% endtabs %}

## How to set signing coordinates

When starting a sign request, define the signature position using the `x` and `y` parameters in the JWT payload. These coordinates are percentage-based and relative to the PDF's dimensions, starting from the bottom left corner.

* **y**: Vertical position (0 to 1), where 0 is the bottom and 1 is the top.
* **x**: Horizontal position (0 to 1), where 0 is the left and 1 is the right.

We will not accept coordinates where a signature cannot be placed due to being outside the page boundaries. The **signature size is fixed at 60x225 points**, regardless of the PDF size.

| Example                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>✅ <strong>x = 0, y = 0</strong></p><p>The bottom-left corner of the signature is positioned at the bottom-left corner of the document.</p>                                                                                                               | <img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1e3aab48f9fbbdd73993ff3426382adb1f13de9e%2FAcrobat%202025-04-09%2015.25.51.png?alt=media" alt="" data-size="original">                    |
| <p>✅ <strong>x = 0.5, y = 0.5</strong></p><p>The bottom-left corner of the signature is positioned in the center of the document.</p>                                                                                                                       | <img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-aacade55265347b5f800a48db3a2690dd3737af0%2FTP%20Screenshot%202025-04-09%20at%2015.28.20%402x.png?alt=media" alt="" data-size="original">  |
| <p>🚫 <strong>x = 1, y = 1</strong></p><p>Error: Signature will be out of page area</p>                                                                                                                                                                     |                                                                                                                                                                                                                                                                                      |
| <p>🚫 <strong>x = 0.00001, y = 0.00001</strong></p><p>Error: Coordinates can only be specified up to 4 decimal places.</p>                                                                                                                                  |                                                                                                                                                                                                                                                                                      |
| <p>⚠️ <strong>x = 0, y = 0</strong><br>Signature will appear cropped if the PDF has been set to a coordinate other than (0,0). This is usually not the default behaviour for PDFs, and you can check this at Page Box / Media box settings of your PDF.</p> | <img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-71bcf194cba69e67277cf4fcef753e3134e59060%2FScreenshot%202025-09-02%20at%2010.23.57%E2%80%AFAM.png?alt=media" alt="" data-size="original"> |


# Redirect From Sign with Singpass

After completing the digital signing process on the Sign portal, the user will be redirected back to the RP’s application. The redirection uses the pre-registered URL set during [**onboarding**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/how-our-api-works) and includes key query parameters, allowing the RP to track and finalise the transaction.

## Additional Query Parameters

* **request\_id:** Match the sign request id returned during the initiate sign request API.
* **status:** Either `success` or `cancelled`, RP must check the actual signing status from [webhook](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook) or [get signing result API](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/get-signing-result)
  * `success`: user is being redirected back to RP after successfully completing the signing
  * `cancelled`: user is being redirected back to RP after being identified as a [non-intended signer](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal#non-intended-signers)

{% hint style="warning" %}
The query parameters will be changed soon.
{% endhint %}

**Example**

```sh
# Given pre-registed recirect_uri is https://rp.com/sign-redirect
https://rp.com/sign-redirect?request_id=signv3-01961988-8b77-7a86-9641-5f2507965c04&status=success
```

<details>

<summary>Can I provide more than 1 redirect URL for my application?</summary>

We only accept one redirect URL per application onboarded. When we send the user back to your application, we will include the `request_id` in the query parameters, which you can then use to redirect the user back to whichever page on your application you deem necessary.

</details>


# Accept Success Signing Webhook

Upon successful signing, Sign will notify the relying party (RP) via a webhook. The RP must implement and expose a webhook endpoint on their server to receive this notification. The webhook will inform the RP that a signing transaction has been successfully completed and provide the URL to download the signed document.

## Path

A <mark style="color:green;">`POST`</mark> request to the webhook URL that was provided to us during your [onboarding](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/how-our-api-works).

## **Body**

A JSON object with only 1 field `token` .

```json
{
  "token": "xxxx"
}
```

The token is a standard [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519) with payload:

* `request_type`: Always `signed_doc_url`
* `signed_doc_url`: Where you can download the signed document. This link will expire after 2 minutes.
* `request_id`: Same as the request id returned during initiate sign request
* `signer_info` : an object containing the following information:
  * `signer_name` : Name of the signer as per the user cert CN
  * `signer_partial_uinfin` : The last 4 alphanumerical value of the signer's NRIC
  * `signed_at` : Unix timestamp in milliseconds of when the user completed the sign request.
* `iat` & `exp`: Standard Issued At / Expiration timestamp of JWT. The expiry of the token is set to 2 minutes. The `signed_doc_url` will expire within the `exp` as well.

{% hint style="danger" %}
RP are required to implement token validation by fetching the [JWKS Specification](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/jwks-specification#sign-with-singpass-jwks), and verify the signature, expiration, and claims contained in the JWT.
{% endhint %}

{% hint style="danger" %}
RP are required to download the document **immediately** as the `signed_doc_url` will expire in 2 minutes. We do not recommend RP to send the `signed_doc_url` to user for the same reason.
{% endhint %}

**Example:**

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNpZ24tZGV2LTAxIn0.eyJzaWduZWRfZG9jX3VybCI6Imh0dHBzOi8vZGV2LnNpZ24uc2luZ3Bhc3MuZ292LnNnL3NpZ25lZC90ZXN0LXNpZ25lZC1wZGYtaWQ_RXhwaXJlcz0xNzU4NjE2MDM0JktleS1QYWlyLUlkPUsyQUUwQzdLRkhNODJOJlNpZ25hdHVyZT1EZ1FBY0V-ZjhWT2xJTmUybkYtWFlKYVJTMXQ2RzQ5ckcyZnJKUzJVT29wbDR6SnpmcH5-flBhRHFoaH52RzBxanVJQjFjOFg1QWtrdG15NkNRcDNPN2QwNHBmN1RnZm5ZaW5pakJLT3Z3Ui1KdEpjOUFzcGx2VzJ0NUQzNXBRbjFyLVFNVURrOUFQYUJRVWh4eX4wNTE0RDN4bXBoS2hidmFXeUN5QXBEaWRlLUlYelo3QzVRMWxpUDNVQ1JiLUxsdWpKLU4xUUZTaWN5dnNmNWhjanRQVUw5Tk5GRG5OdFlYR2U1Y29pOX5kZ0lramNQbEZzS29KdTBkS3UtbzA2UDhEMFhzeExkTllrRjlnY051bVBiOHNxOXE1ZjhkVHNBUUIwNnhFMmp3dVhmaTR5eG8yalRQTmczRGhxeWxiTi1aWkkwWjJrQk8tM0U3bHROQXliVUFfXyIsInNpZ25lcl9pbmZvIjp7InNpZ25lcl9uYW1lIjoiVXNlciBTMzE3Njc0OUQiLCJzaWduZXJfcGFydGlhbF91aW5maW4iOiI3NDlEIiwic2lnbmVkX2F0IjoxNzU4NjE1OTEzNTY3fSwiZXhwIjoxNzU4NjE2MDMzfQ.xxx
```

{% endcode %}

## Response

It is sufficient to respond with only 2XX HTTP status code without any response body.

## Retry Settings <a href="#retry-settings" id="retry-settings"></a>

Singpass will perform automated retries of webhook calls in the case of timeouts or certain errors.

```
Per try timeout: 2s
Delay between each retry: 2s
Max attempts: 3
```

{% hint style="danger" %}
RP are required to respond to the webhook request within **2 seconds.**
{% endhint %}

## **IP Address**

We strive to maintain consistent egress IPs, but please note that they are subject to change with short notice.

* **Staging:**
  * 54.169.20.186
* **Production:**
  * 18.143.229.39
  * 54.179.76.90
  * 3.0.39.45


# Get Signing Result

This endpoint allows the relying party (RP) to actively query the signing results and obtain the signed document after completion.

{% hint style="info" %}
It is **not recommended to use this endpoint for status polling** as the [webhook](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook) is more efficient. RPs do not need to invoke this API if the success signing webhook was captured.
{% endhint %}

## **Path**

<mark style="color:green;">`GET`</mark> `/sign-requests/:request_id/signed-doc`

## **Headers**

| Name          | Value              |
| ------------- | ------------------ |
| Content-Type  | `application/json` |
| Authorization | `<token>`          |

## **Authorization token**

RP should sign the signature parameter into a JWT token as authorization token.

* **Token Type:** Standard JWT ([JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519))
* **Payload:**
  * `exchange_code`: The exchange\_code returned when initiate sign request.
  * `jti`: Standard JWT ID, a unique identifier for the JWT, must be a UUID.
  * `iat` & `exp`: Standard Issued At / Expiration timestamp of JWT. Must issued within 2 minutes.

Example:

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsImtpZCI6IjEyMDUwMzM5LWUzNTktNGUyYy04YTc2LWY0Nzk0MDZmZDliMyJ9.eyJleGNoYW5nZV9jb2RlIjoiY2JlNzM3MWMtZjExMC00OTEzLWE3YmQtNjQwOTk0YjA4MDczIiwianRpIjoiY2IyYTk5NmQtZjk3ZS00YzJiLWE5ZDAtZDM0NzgxNzhjY2RmIiwiaWF0IjoxNzQ3Mzc3NzIyLCJleHAiOjE3NDczNzc4NDJ9.ZLQTMnSiqRfFE1w2jDjQgOVDKWY2Fv-HTSn976dZXmt2FVNMEzOfTdV8qCWnw8mOE5aJzIi2DQyIDZqwKAFJ4Q
```

{% endcode %}

## **Body**

Empty

## **Response**

{% tabs %}
{% tab title="Signed (200)" %}

```json
{
    "signed_doc_url": "XXXX",
    "signer_info": 
        {
            "signer_name": <Name as per the CN in the user certifiate>,
            "signer_partial_uinfin": "123A",
            "signed_at": <Timestamp of the user completing the sign request>
        }
    "exp": 1744190335
}
```

* `signed_doc_url`: Where you can download the signed document.
* `signer_info` : an object containing the following information:
  * `signer_name` : Name of the signer as per the user cert CN
  * `signer_partial_uinfin` : The last 4 alphanumerical value of the signer's NRIC
  * `signed_at` : Unix timestamp in milliseconds of when the user completed the sign request.
* `exp`: Expiration time (in UNIX second) of `signed_doc_url` .

{% hint style="danger" %}
Similar to the [successful signing webhook](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/accept-success-signing-webhook), the `signed_doc_url`will only be valid for 2 minutes. RPs should download the document immediately for their own application. We do not recommend forwarding this URL to the user.
{% endhint %}
{% endtab %}

{% tab title="Error (400)" %}
There may be a few scenarios under which you will receive a 400 error:

* `DOCUMENT_NOT_SIGNED`: The user has not signed the document yet and the request has not expired yet
* `REQUEST_EXPIRED`: The request has expired without the user signing the document.
* `SIGNED_ACCESS_EXPIRED`: The document has been signed, but can no longer be retrieved via this endpoint as the 1h access period has passed.

```json
{
    "id": "91934263-3ad0-4f2d-afb6-441b2e256b64",
    "trace_id": "1747520091621739744",
    "error": "DOCUMENT_NOT_SIGNED",
    "error_description": "Document is not signed yet."
}
```

{% endtab %}

{% tab title="Auth Token Error (401)" %}

```json
{
  "error": "UNAUTHORIZED",
  "error_description": "Unauthorized.",
  "error_details": "JWT validation failed",
  "id": "ca21bb57-8255-46f0-b2f4-80613768ea6e",
  "trace_id": "7755321139078968799"
}
```

{% endtab %}

{% tab title="Server Error (500)" %}

```json
{
  "error_description": "Something went wrong.",
  "id": "ca21bb57-8255-46f0-b2f4-80613768ea6e",
  "trace_id": "7755321139078968799"
}
```

{% endtab %}
{% endtabs %}

## **Sample request**

```sh
curl 'https://staging.sign.singpass.gov.sg/api/v3/sign-requests/<request_id>/signed_doc' \
  -H 'Authorization: <auth_token>'
```


# JWKS Specification

## JWKS Endpoint requirements for RP

The client must provide the public key(s) during onboarding by hosting the JWKS on a publicly accessible URL. This endpoint must be compatible with Singpass's [#jwks-url-service-level-expectations](#jwks-url-service-level-expectations "mention"). These public keys will be used to verify the signature of the token in [Initiate Sign Request](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request) and [Get Signing Result](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/get-signing-result).

RP are allowed to provide multiple keys on the JWKS url.

{% hint style="info" %}
[mkjwk.org](https://mkjwk.org/) is a useful open-source tool to generate different types of JWK for signing and encryption; compliant with Singpass's broad requirements on structure. While we **DO NOT** suggest this as a secure way to generate your *real* keypair (including private key); this can be a useful tool to understand how JWK works; and how it is represented for signing and encryption purposes; while you are reviewing against our supported algorithms below.
{% endhint %}

### **Key requirements:**

* Must have key `use` of value `sig` per [rfc7517#section-4.2](https://tools.ietf.org/html/rfc7517#section-4.2)
* Must contain a key ID in the standard `kid` field per [rfc7517#section-4.5](https://tools.ietf.org/html/rfc7517#section-4.5)
  * Will be used by Singpass to select the relevant key to verify the client assertion
* Must be an EC key, with curves: `P-256`, `P-384` or `P-521` *(NIST curves, aka `secp256r1`, `secp384r1`, `secp521r1` respectively)*

### **Example**

```json
{
    "keys": [
        {
            "kty": "EC",
            "use": "sig",
            "crv": "P-256",
            "kid": "6X_-_oLSH0DQLtz16o-NTKcm0lG0J-VDGHOz6tPx0Jc",
            "x": "1tR88zrGoPUV-Fr4bh_9NR-mDhC9rLswDp85hkbKBT0",
            "y": "1vYh1M53NK_b7l9Y-1FgCENOp6Fl9StVVLr3KqK_Ka8",
            "alg": "ES256"
        }
    ]
}
```

### **Key Rotation Best Practices**

Our server caches the key for <mark style="color:red;">**1 hour**</mark>. When performing key rotation, do ensure that:

* New key should be added to the JWKS at least 1 hour before it is used to sign new JWTs.
* Old key must remain available for at least 1 hour after stop signing with it, ensuring that previously issued JWTs can still be validated.

### Service Level Expectations <a href="#jwks-url-service-level-expectations" id="jwks-url-service-level-expectations"></a>

Sign requires that any JWKS is published on an endpoint that:

* Is served behind HTTPS on port `443` using a TLS server certificate issued by a standard *publicly verifiable CA issuer* (no private CAs), with *complete cert chain* presented by the server.
* Is publicly accessible
  * No IP whitelisting: Singpass does not publish or guarantee the IP addresses used to fetch your JWKS, and they may change without notice. A JWKS contains only public keys and is safe to expose publicly.
  * No mTLS or other custom HTTP header requirements outside standard HTTP headers such as `Content-Type`, `Accept`.
* Is able to respond in a timely fashion with respect to the below configuration.
  * Per try timeout: 3s
  * Max attempts: 3
  * Cache duration for retrieved JWKS: 1h

> Note: While the above is a technical requirement; the user experience of your users may be affected if we are unable to retrieve your JWKS in a timely fashion upon our cache expiry due to slower token exchanges with your backend. We recommend aiming for this response to be as fast as possible based on an in-memory cache; or simple static asset retrieval.

## Sign with Singpass JWKS

RP can verify the signature of a JWT from Sign with Singpass by acquiring the signing public key from this endpoint. More information about a JSON Web Key (JWK) endpoint can be found [here](https://tools.ietf.org/html/rfc7517).

Public keys returned from this endpoint could be in random sequence or rotated for security enhancement.

### URLs

<table><thead><tr><th width="178">Environment</th><th width="576">URL</th></tr></thead><tbody><tr><td>Staging</td><td><a href="https://static.staging.sign.singpass.gov.sg/.well-known/keys.json">https://static.staging.sign.singpass.gov.sg/.well-known/keys.json</a></td></tr><tr><td>Production</td><td><a href="https://static.app.sign.singpass.gov.sg/.well-known/keys.json">https://static.app.sign.singpass.gov.sg/.well-known/keys.json</a></td></tr></tbody></table>

### Cache and key rotation

For varying reasons, keys used for signing can and will be rotated/changed with **no defined schedule**, and at the full discretion of Singpass. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different `kid` value. The new `kid` value will be reflected in all the new JWTs signed by Singpass. In such cases, cached copies of Singpass public keys must be refreshed by re-invoking the JWKS endpoint.

If the validation of the Singpass signature fails, re-fetch from the JWKS endpoint once for that validation.

{% hint style="danger" %}
Please read through the list of **DON’Ts** below:

* Do not assume the position of a signing key among the list of the returned keys.
* Do not validate Singpass signatures using a hardcoded public key. Always determine the correct key (for signature verification) by inspecting the `kid` from the JWS header, and use it to retrieve the public key from our JWKS endpoint.
* Do not cache only 1 key. Caching should be done for the entire JWKS.
  {% endhint %}


# Sign Portal User Journey

This page outlines what your users will see on the Sign portal when you direct them to the URL provided in the [Initiate Sign Request](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request) response.

## Happy Flow

This is the main user journey that your users will experience.

*If the interactive demo below does not work, please see the* [*step-by-step illustration here*](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/sign-portal/sign-portal)*.*

{% embed url="<https://app.arcade.software/share/tZAyhjFHyu5FvIEiUcEC>" %}

## Negative Flows

There may be instances where your users may encounter error screens when using the Sign Portal

### Non-intended signers

<div data-full-width="true"><figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-674370cd87e32c9f414135847f1c1ffb495a1423%2FNo%20Access%20page.png?alt=media" alt="Error screen if the user is not the intended signer" width="563"><figcaption><p>Error screen if the user is not the intended signer</p></figcaption></figure></div>

RPs can specify which user is the intended signer by providing a hash of the user's NRIC when creating a sign request. If an RP includes this specification, after the user performs the login, they will see the above error screen.

* The user will not be able to view and sign the document
* The error message will tell the user to contact the RP directly for help.
* The only action the user will be allowed to do is to "Leave Sign Portal". This button will be linked to the RP's redirect URL.

{% hint style="info" %}
Note: The user will see that they have performed the login step **successfully** on their mobile's Singpass App. However, the Sign Portal page will thereafter show this error screen.
{% endhint %}

{% hint style="warning" %}
It is RP's responsibility to provide the **correct** NRIC in the **appropriate** format when creating sign requests. [See the documentation here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request).
{% endhint %}

### Expired or Incorrect Links

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-a5e77bb571606a3bc59c29a1f0289fad6f31e3ae%2FLink%20Invalid%20page.png?alt=media" alt="" width="563"><figcaption><p>Error screen if the user visits a signing request that has already expired or the link is invalid</p></figcaption></figure>

The link provided is **valid for 30 minutes**. If the link has expired, users will not be able to log in to view and sign the document. Instead, user will see a generic error screen when they attempt to access the portal.

The same error screen will be shown if users access the portal with an incorrect link (e.g. due to typos).

## Commonly Asked Questions

<details>

<summary>Why does the user have to scan QR code twice? What’s the difference?</summary>

The first QR code is to verify the user's identity with Singpass and log in to the Sign portal. **If you have specified in the** [**Initiate Sign Request**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request) **parameters the NRIC of the user who can access the document, only that user would be able to perform a successful log in.** This will ensure that any sensitive contents within the document are not exposed to unintended users.

The second QR code (which comes with a 4-digit reference code) is for the user to sign the document.

</details>

<details>

<summary>What is the reference code for during the signing?</summary>

The purpose of the reference code is to allow users to verify that they are signing the correct document, when the code on their Singpass App matches that which is shown in the Sign Portal.

</details>

<details>

<summary>What happens if a user rejects the signing on their Singpass App?</summary>

If the user **rejects** the signing (Clicks 'Reject' in Step 8), the Sign Portal will continue to stay in 'pending sign' mode. Users will have to (i) refresh the Portal to get a new QR code or (ii) return back to the organization's webpage to restart the process.

</details>

<details>

<summary>Why can’t the user log in?</summary>

The user might not be able to log in if i) you [specified an intended signer](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request#authorization-token) for the document that is not them, or ii) you did not specify a signer, but someone else has logged into the portal to access the document before them.

</details>

<details>

<summary>Why can’t the user sign?</summary>

The user will not be able to sign if i) you [specified an intended signer](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request#authorization-token) for the document that is not them, ii) the document has already been signed, or iii) an unexpected error occurred.

</details>


# Step-by-step User Journey

#### 1. By clicking the "Sign with Singpass" button on your portal, the user will be redirected to Singpass signing portal.

The following elements in the sample image below will be replaced with information provided to us during your [onboarding](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/how-our-api-works):

* "*Login PDF Viewer Client*" will be replaced with your display name provided
* Your organisation's logo will be displayed beside the display name, instead of the placeholder image

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-6efde817523494b96be5f3dc61911683872ec418%2FFrame%201%20\(2\).png?alt=media)

#### 2. The user is required to verify their identity with Singpass before they can view the document. They will do this by performing a Singpass Log In with their Singpass App.

![](https://image.mux.com/0224WrueMbF3tqP456inX99UnYphFtFXLMSsOcfMiN8k/animated.gif?start=0\&end=3.933333\&width=640\&fps=30)

![](https://image.mux.com/ScS6tro518ZEOnRgBZRCNzzc11J018EwANJafdJzvePM/animated.gif?start=0\&end=5.553333\&width=640\&fps=30)

#### 3. Upon successful authentication, the user can begin reviewing the document.

The document name ("dummy.pdf") will be taken from the `doc_name` parameter provided in the payload when [initiating the sign request](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3/initiate-sign-request).

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-8f6eb8ddfdc12786d7cf0db7fc505f9f1e4000fa%2FFrame%204%20\(1\).png?alt=media)

#### 4. In the field navigation panel, the user can easily locate the fields in the document that require their signature.

This panel is on the right of the desktop screen. For mobile users, it will be at the bottom.

![](https://image.mux.com/uwfDWl013eitl2uAY84VrhNwQ8RggeGVRLwROzrNZKsA/animated.gif?start=16.271\&end=18.351\&width=640\&fps=30)

#### 5. The user must review each field by clicking/tapping on them.

For mobile, the user can also tap the 'Mark as reviewed' button to review each field.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-ad1f3ea65b11b3035f204f49b017ee4511aaab18%2FFrame%206.png?alt=media\&token=bac981a6-0c8f-4aaf-800c-0b8b3d7ce289)

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-b80fff81c22e7acbcb248b87e791234d06c52cb6%2FFrame%207.png?alt=media\&token=590eb054-67bd-4aa5-a5fa-cd4f5324c094)

#### 6. The Sign button becomes active once all fields are reviewed.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-31e3ffb5d905cf04a6968a8406b439ca95d321cd%2FFrame%208.png?alt=media\&token=4c33c981-0fde-44b7-991b-9d5c90220b35)

#### 7. When the Sign button is clicked, the user will be shown a QR code, which they should scan with their Singpass App on their mobile device.

It will also display a **match reference code** ("9736" in the example below)

![](https://image.mux.com/sxQ4Weh5QO52fv15FsE9v1OEX9sqd8kIa4Q5p8nKDcQ/animated.gif?start=0\&end=3.533333\&width=640\&fps=30)

#### 8. On their Singpass App, the user will select Approve or Reject.

They can also check the **Match reference code** to ensure they are signing the right document.

![](https://image.mux.com/UJdgGDYCYEahtauHU4JTdtpwiDRbuYAaOveW7eKtTzA/animated.gif?start=0\&end=4.8\&width=640\&fps=30)

#### 9. Document is successfully signed! At this point, the user can return to your portal, or view their signed document first.

The user can view their signed document by clicking 'View Signed Document'.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-cc2438356ab3bd32ec71b3041a2cada72a2bb2a9%2FFrame%209.png?alt=media\&token=c3ec038d-f8f1-4fea-888d-d8cb179189e4)

#### 10. At this point, the user can check signature details for added transparency and peace of mind.

The user will return to your portal by clicking 'Leave Sign Portal' as the final step, to complete the rest of the process (if any).

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1349b634a9ea637c45e08e99c776060f5a371301%2FFrame%2010.png?alt=media\&token=45733a26-6d08-4550-aef8-55d50e766b09)


# Cancel Sign Request

This endpoint allows RP to initiate a cancellation to a sign request. RP can cancel any active or expired sign requests created by them.

A cancellation request will be rejected if **any** of the following conditions are met:

* The user has already initiated a sign session (clicked *Proceed to Sign* and signing QR code is shown)
* The document has already been signed
* The sign request has already been cancelled

### Path <a href="#path" id="path"></a>

<mark style="color:green;">`POST`</mark> `/sign-requests/cancel`

### Headers <a href="#headers" id="headers"></a>

| Name          | Value            |
| ------------- | ---------------- |
| Content-Type  | application/json |
| Authorization | \<token>         |

## Authorization token

RP should sign the signature parameter into a JWT token as authorization token.

* **Token Type:** Standard JWT ([JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519))
* **Payload:**
  * `request_id`: Same as the request id returned during initiate sign request
  * `client_request`: Your application's registered client ID
  * `iat` & `exp`: Standard Issued At / Expiration timestamp of JWT. Must issued within 2 minutes.

Example:

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsImtpZCI6InBUaHpVbl9JNVJXZzcyQWEyUzI1LXhoRG0wRzBNWjNSN3FpWUdyYmVmT0EifQ.eyJjbGllbnRfaWQiOiJ0ZXN0LWNsaWVudC1pZCIsInJlcXVlc3RfaWQiOiJzaWdudjMtMDE5OWNjOWMtOGI3Yy03MGRmLWIyOWItMzk4NDNhMTBjMzMyIiwiaWF0IjoxNzYwMDc0NDkxLCJleHAiOjE3NjAwNzQ2MTF9.-mf63KNiCCKNuVgAwn7OL4Lv7vnZ9fvPT5Pm2lCWQn36k6SK5jkBm8Iwonr0Yg5cTb1Jf2T1DK5aG_1VzYkqig
```

{% endcode %}

## Body

Empty

## Response

{% tabs %}
{% tab title="Cancelled (200)" %}

* `200 OK` Sign request successfully cancelled
  {% endtab %}

{% tab title="Active Session (400)" %}

```
{
  'error': 'ACTIVE_SESSION_ONGOING'
  'error_description': 'Request cannot be cancelled due to an active sign session'
}
```

* The user has already initiated a sign session (clicked *Proceed to Sign*)
* RP will not be able to cancel and will receive `400 Bad Request`
  {% endtab %}

{% tab title="Request Signed (400)" %}

```
{
  'error': 'DOCUMENT_ALREADY_SIGNED'
  'error_description': 'Document has already been signed'
}
```

* The document has already been signed
* RP will not be able to cancel and will receive `400 Bad Request`
  {% endtab %}

{% tab title="Request Cancelled (400)" %}

```
{
  'error': 'REQUEST_ALREADY_CANCELLED'
  'error_description': 'Document has already been cancelled'
}
```

* The sign request has already been cancelled
* RP will not be able to cancel and will receive `400 Bad Request`
  {% endtab %}

{% tab title="Invalid Request ID" %}

```
{
  'error': 'CLIENT_SIDE_ERROR'
  'error_description': 'No record found'
}
```

* If the request\_id is invalid or not found, RP will receive `400 Bad Request` .
  {% endtab %}
  {% endtabs %}

### Sample Request <a href="#sample-request" id="sample-request"></a>

```sh
curl -X POST http://staging.sign.singpass.gov.sg/api/v3/sign-requests/cancel \
  -H "Authorization: eyJhbGciOiJFUzI1NiIsImtpZCI6InBUaHpVbl9JNVJXZzcyQWEyUzI1LXhoRG0wRzBNWjNSN3FpWUdyYmVmT0EifQ.eyJjbGllbnRfaWQiOiJ0ZXN0LWNsaWVudC1pZCIsInJlcXVlc3RfaWQiOiJzaWdudjMtMDE5OWNjOWMtOGI3Yy03MGRmLWIyOWItMzk4NDNhMTBjMzMyIiwiaWF0IjoxNzYwMDc0NDkxLCJleHAiOjE3NjAwNzQ2MTF9.-mf63KNiCCKNuVgAwn7OL4Lv7vnZ9fvPT5Pm2lCWQn36k6SK5jkBm8Iwonr0Yg5cTb1Jf2T1DK5aG_1VzYkqig" \
  -H "Content-Type: application/json"

```


# Sign V1

Last Updated: 2 June 2025

{% hint style="warning" %}
We are no longer accepting requests to onboard Sign V1. Please refer to the [latest documentation for V3](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3) instead.
{% endhint %}

## Changelog

<table><thead><tr><th width="174">Date</th><th>Changes</th></tr></thead><tbody><tr><td>30 Sep 2024</td><td><ul><li>Introduction of <a href="#authenticating-via-json-web-token"><mark style="color:blue;">JWT as the preferred authentication mech</mark></a><mark style="color:blue;">anism</mark></li><li>Deprecation of Basic Authentication</li></ul></td></tr><tr><td>11 Nov 2024</td><td>Added IP addresses for whitelisting</td></tr><tr><td>5 Mar 2025</td><td>Update to <a href="#qr-code-deeplinking-specifications">QR Code deeplinking specifications</a> to support new staging app</td></tr><tr><td>27 May 2025</td><td>Update to <a data-mention href="#other-dsap-requirements">#other-dsap-requirements</a></td></tr><tr><td>2 June 2025</td><td>Updated to indicate that <a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3">V3 is released</a>; onboarding for v1 no longer supported</td></tr></tbody></table>

## Introduction <a href="#introduction" id="introduction"></a>

The guide provide a clear illustration of the web-based application programming interfaces (API) for the use of Document Signing Application Providers (DSAP). Described here are the necessary APIs that DSAPs must invoke to facilitate a document signing process for a Singpass user.

## Document Signing Flow Diagram <a href="#document-signing-flow-diagram" id="document-signing-flow-diagram"></a>

An overview of the document signing flow and the interactions between DSAP, Singpass and other dependencies.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-bfc92b93ba3ab2010e86ac8357ae7c0ca38beb8b%2Fimage%20(26).png?alt=media" alt=""><figcaption><p>Document signing flow</p></figcaption></figure>

## Staging and Production URLs <a href="#staging-and-production-urls" id="staging-and-production-urls"></a>

**Disclaimer:** The domains used in the sample requests in the API specs below may not be accurate for your environment. Please choose the correct one from the table below that suits your testing needs.

| Environment    | Domain                                          | Access Mechanism                                                                                                                                                     |
| -------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Staging**    | <https://staging.sign.singpass.gov.sg/api/v1/*> | <ul><li>SSL</li><li>Basic Authentication (Deprecated)</li><li>JWT <a href="https://docs.sign.singpass.gov.sg/#authenticating-via-json-web-token">(New)</a></li></ul> |
| **Production** | <https://app.sign.singpass.gov.sg/api/v1/*>     | <ul><li>SSL</li><li>Basic Authentication (Deprecated)</li><li>JWT <a href="https://docs.sign.singpass.gov.sg/#authenticating-via-json-web-token">(New)</a></li></ul> |

{% hint style="warning" %}
You must not do "cert pinning" or create any form of dependency to the **leaf** TLS certificates of the above domains. Singpass reserves the right to rotate its TLS leaf certificate without prior notice to partners.

mTLS is no longer required. We will ignore all incoming mTLS client authentication.
{% endhint %}

#### JWKS URLs

<table><thead><tr><th width="192">Environment</th><th>Domain</th><th>Access Mechanism</th></tr></thead><tbody><tr><td><strong>Staging</strong></td><td><a href="https://static.staging.sign.singpass.gov.sg/.well-known/keys.json">https://static.staging.sign.singpass.gov.sg/.well-known/keys.json</a></td><td>SSL</td></tr><tr><td><strong>Production</strong></td><td><a href="https://static.app.sign.singpass.gov.sg/.well-known/keys.json">https://static.app.sign.singpass.gov.sg/.well-known/keys.json</a></td><td>SSL</td></tr></tbody></table>

{% hint style="warning" %}
Please note that there may be more than one key appearing in the JWKS, and DSAPs must use the `kid` value to identify the right key.
{% endhint %}

## DSAP Server Certificate <a href="#dsap-server-certificate" id="dsap-server-certificate"></a>

The webhook server must be configured to present the full certificate chain to Singpass when Singpass invokes the notification webhook endpoints. This can be verified using a tool like [SSL Labs](https://www.ssllabs.com/). Please note that your cert should not be a self-signed certificate.

Additionally, server certificates presented must minimally conform to the following requirements:<br>

<table><thead><tr><th width="192">Requirement</th><th>RSA Certs</th><th>ECC Certs</th></tr></thead><tbody><tr><td><strong>Required Public Key dimensions</strong></td><td><p>>= 2048 bits</p><p>>= 3072 bits (recommended)</p></td><td>>= 256-bit based on curves <code>P-256</code>, <code>P-384</code> or <code>P-521</code> <em>(NIST curves, aka <code>secp256r1</code>, <code>secp384r1</code>, <code>secp521r1</code> respectively)</em></td></tr><tr><td><strong>X.509 v3 extension KeyUsage</strong></td><td>digitalSignature, keyEncipherment</td><td>digitalSignature</td></tr><tr><td><strong>X509 v3 extension ExtendedKeyUsage</strong></td><td>serverAuth</td><td>serverAuth</td></tr></tbody></table>

## General Error Response <a href="#general-error-response" id="general-error-response"></a>

DSS APIs are RESTful in design and communicate classes of errors based on the **Http Status** code. The status code should be used to determine if the error is caused by consumer or provider. Consumers should log the HTTP status code along with the `id` and/or `trace_id` of the error.

<table><thead><tr><th width="338">HTTP Status Code</th><th>Description</th><th data-hidden>RSA Certs</th></tr></thead><tbody><tr><td><strong>4XX</strong></td><td><p>Errors caused by API consumer. You can expect codes such as 400, 401, 403, 404 etc if incorrect requests are made to APIs.</p><p>Example: <strong>400: Invalid/missing request arguments</strong></p></td><td><p>>= 2048 bits</p><p>>= 3072 bits (recommended)</p></td></tr><tr><td><strong>5XX</strong></td><td><p>Errors caused by DSS or its dependencies. You can expect codes such as 500, 502, 503 etc if there is an issue on DSS or its dependencies.</p><p>Example: <strong>500: Internal Server Error due to some kind of programming error.</strong></p></td><td>digitalSignature, keyEncipherment</td></tr></tbody></table>

#### **Example: Invalid Request Parameters**

```
HTTP/1.1 400 Bad Request
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Cache-Control: no-cache, no-store, must-revalidate
Transfer-Encoding: chunked
Content-Type: application/json
Date: Tue, 24 Sep 2024 02:30:42 GMT
Content-Length: 190

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "CLIENT_SIDE_ERROR",
  "error_description" : "This is an invalid request.",
  "trace_id" : "66f22452fb051066bf30f8002a3c5e4a"
}
```

#### **Example: Server Error**

```
HTTP/1.1 500 Internal Server Error
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Cache-Control: no-cache, no-store, must-revalidate
Transfer-Encoding: chunked
Content-Type: application/json
Date: Tue, 24 Sep 2024 02:30:42 GMT
Content-Length: 192

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "SERVER_SIDE_ERROR",
  "error_description" : "An unexpected error occurred.",
  "trace_id" : "66f22452d4ed47e5b4fbb870813ab8eb"
}
```

### Description of fields <a href="#description-of-fields" id="description-of-fields"></a>

<table><thead><tr><th width="192">Path</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td>String</td><td>The unique identifier for this error/request. Please log this identifier for support and debugging purposes.</td></tr><tr><td><code>trace_id</code></td><td>String</td><td>(Optional) An auxiliary id for request correlation across services. Please also log this identifier for operational support and debugging purposes.</td></tr><tr><td><code>error</code></td><td>String</td><td>Error code representing broad class of error. See Error Codes for the list of possible error codes that can be returned and what they represent.</td></tr><tr><td><code>error_description</code></td><td>String</td><td>Returns human readable general information about the reason for the error. Note that due to security reasons; detailed information is unlikely to be available in this message.</td></tr></tbody></table>

### Error Codes<br>

<table><thead><tr><th width="338">Error Code</th><th>Description</th><th data-hidden>RSA Certs</th></tr></thead><tbody><tr><td><code>CLIENT_SIDE_ERROR</code></td><td>Generic error code for an invalid request.</td><td><p>>= 2048 bits</p><p>>= 3072 bits (recommended)</p></td></tr><tr><td><code>SERVER_SIDE_ERROR</code></td><td>Generic error code for an error that occurred in Singpass.</td><td>digitalSignature, keyEncipherment</td></tr><tr><td><code>UNAUTHORIZED</code></td><td>Authorization header value is invalid.</td><td></td></tr><tr><td><code>MISSING_AUTHORIZATION</code></td><td>Authorization header was required but not found.</td><td></td></tr><tr><td><code>ARGUMENTS_NOT_VALID</code></td><td>Some request parameters are invalid.</td><td></td></tr><tr><td><code>SIGN_REF_NOT_FOUND</code></td><td>Requested sign ref is invalid or has already expired.</td><td></td></tr><tr><td><code>MULTIPLE_ASSERTION_HEADER</code></td><td>Multiple DSS assertion headers.</td><td></td></tr><tr><td><code>ASSERTION_NOT_VALID</code></td><td>DSS assertion header is invalid.</td><td></td></tr><tr><td><code>JWKS_URL_NOT_FOUND</code></td><td>DSAP JWKS URL is not found.</td><td></td></tr><tr><td><code>CLIENT_JWKS_ERROR</code></td><td>Unable to fetch DSAP JWKS or DSAP JWKS is invalid.</td><td></td></tr></tbody></table>

## Document Signing endpoints invoked by DSAP <a href="#document-signing-endpoints-invoked-by-dsap" id="document-signing-endpoints-invoked-by-dsap"></a>

The API in this sections are endpoints invoked by DSAPs at various part of the DSS flow.

* /doc-signing-sessions
* /doc-signing-sessions/\<sign\_ref>/hash
* /.well-known/keys.json

### Authenticating via Basic Authentication (Deprecated)

{% hint style="warning" %}
This is deprecated in favour of [authenticating via JSON Web Tokens.](https://docs.sign.singpass.gov.sg/#authenticating-via-json-web-token-recommended)
{% endhint %}

For all DSS APIs except the JWKS endpoint, DSAPs will need to authenticate themselves using their base64-encoded `client_id` and `client_secret` via the [basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#Basic_authentication_scheme) scheme in the following format:

```
Authorization: Basic <client_id>:<client_secret>
```

### Authenticating via JSON Web Token <a href="#authenticating-via-json-web-token" id="authenticating-via-json-web-token"></a>

DSAPs are to use JSON Web Token (JWT) assertion for authentication when calling the DSS APIs.

```
X-Dss-Assertion: <jwt_assertion>
```

#### Structure of JWT

#### Sample JWT

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJwLXRlc3QtMDEifQ.eyJpc3MiOiJtb2NrQ2xpZW50SWQiLCJzdWIiOiJtb2NrQ2xpZW50SWQiLCJhdWQiOiJodHRwczovL3N0YWdpbmcuc2lnbi5zaW5ncGFzcy5nb3Yuc2ciLCJpYXQiOjE3Mjc2NjUwMzcsImV4cCI6MTcyNzY2NTYzNywianRpIjoiN2Q2NDdmNTMtZDEzOC00YjUxLWIxZDgtZGM2OWQ1NmNhNDAxIn0.iF9WH09CW1zhOhaSH37Faaw6kw7dbUMx2yuIAW9tD7p50ixUWIBTswvwxkutIPFY4zGFxcjrV4USwBfxpe28RA
```

{% endcode %}

**Decoded JWT Header**

```
{
  "alg": "ES256",
  "typ": "JWT",
  "kid": "rp-test-01"
}
```

| Parameter | Type   |                                                                                             |
| --------- | ------ | ------------------------------------------------------------------------------------------- |
| `alg`     | String | Algorithm used in the JWT. Acceptable values are: `ES256`, `ES384`, `ES512`                 |
| `typ`     | String | Acceptable value: `JWT`                                                                     |
| `kid`     | String | The Key ID used for the JWT. This value must correspond to a key in the DSAP JWKS endpoint. |

#### Decoded JWT Body

```
{
  "iss": "mockClientId",
  "sub": "mockClientId",
  "aud": "https://staging.sign.singpass.gov.sg",
  "iat": 1727665037,
  "exp": 1727665637,
  "jti": "7d647f53-d138-4b51-b1d8-dc69d56ca401"
}
```

| Parameter | Type   | Description                                                                                                                                                                                                                                                |
| --------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `iss`     | String | Use the ClientID provided by Singpass                                                                                                                                                                                                                      |
| `sub`     | String | Use the ClientID provided by Singpass                                                                                                                                                                                                                      |
| `aud`     | String | <p>The DSS domain that will be accepting the JWT.<br><br>Value:<br>Staging: <https://staging.sign.singpass.gov.sg><br>Production:<br><https://app.sign.singpass.gov.sg></p>                                                                                |
| `iat`     | Number | A Unix timestamp in seconds indicating the date and time when the JWT was issued.                                                                                                                                                                          |
| `exp`     | Number | A Unix timestamp in seconds indicating the date and time when the JWT will expire. Max expiry allowed is`600` seconds from `iat`                                                                                                                           |
| `jti`     | String | A random string that must be regenerated for **each JWT** to prevent replay attacks. Singpass will cache and reject all duplicate `jti` that is sent within a preset period. As such, DSAPs are advised to use a UUID-v4 value when populating this value. |

**DSAP JWKS Endpoint**

Singpass will attempt to retrieve the public key from the DSAP JWKS endpoint in order to verify the JWT. This endpoint is provided during onboarding and is tied to the DSAP Client ID.

Singpass will only accept JWT signed by EC key. DSAP JWKS should have at least 1 EC key.

#### Sample JWKS Endpoint

```
{
  "keys": [
    {
      "kty": "EC",
      "x": "FuIv2xuY0coivK-MRg01T3_JHUMEtFHdpjj8AuxCPLA",
      "y": "N6pMWRTjPzsBdUTyLrhX7tftfx4IWxvL3z1s9PoxQlE",
      "crv": "P-256",
      "use": "sig",
      "kid": "sign-prod-01"
    }
  ]
}
```

| Parameter | Type   | Description                                                                                                                         |
| --------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `kty`     | String | Key Type Acceptable value: `EC`                                                                                                     |
| `x`       | String | X-Coordinate This is the X-coordinate of the elliptic curve point, which is a component of the public key. It is base64url-encoded. |
| `y`       | String | Y-Coordinate This is the Y-coordinate of the elliptic curve point, which is a component of the public key. It is base64url-encoded. |
| `crv`     | Number | Curve Name                                                                                                                          |
| `use`     | Number | Public Key Use. Acceptable value: `sig`                                                                                             |
| `kid`     | String | Key ID. Singpass will search for the `kid` that was specified in the JWT for verification.                                          |
| `alg`     | String | \[Optional] Algorithm                                                                                                               |

DSAPs are to put the JWT in the request header with the key `X-Dss-Assertion` when calling all DSS APIs.

{% hint style="info" %}
For existing DSAP that are currently using Basic Authentication, DSAPs can continue to use the `Authorization` header when calling DSS APIs. DSS APIs will first detect if `X-Dss-Assertion` exists in the header before falling back to `Authorization`. Existing DSAPs are advised to start preparing for the change to JWT early.
{% endhint %}

### `POST /doc-signing-sessions` <a href="#post-doc-signing-sessions" id="post-doc-signing-sessions"></a>

DSAPs can call this endpoint to start a document signing session. On success, a unique signing reference value - `sign_ref` - is included in the response object. The `sign_ref` is the primary identifier of a signing session used in all exchanges between Singpass and DSAP.

DSAPs have to specify a **client notification token** when initialising a session. Singpass will specify this token in an `Authorization` header for subsequent calls to the DSAP notification webhook endpoints.

{% hint style="info" %}
A document signing session is only valid for a short amount of time. The expiry of a signing session can be found via the `expires_at` response field. When a sign session expires, Singpass will delete it from storage and calls to [<mark style="color:blue;">/doc-signing-sessions/\<sign-ref>/hash</mark>](#post-doc-signing-sessions-less-than-sign-ref-greater-than-hash) will result in a `SIGN_REF_NOT_FOUND` error. Also, any attempts to scan a doc signing QR code or sign a doc hash will fail.

Please note that **Singpass will not notify DSAPs** when the signing session expires. It is recommended to make use of the aforementioned expires\_at response field to coordinate the session expiry between Singpass and DSAPs.
{% endhint %}

#### Request and Response Structure

**Sample Curl Request&#x20;**<mark style="color:red;">**(Deprecated)**</mark>

```
$ curl 'https://staging.sign.singpass.gov.sg/api/v1/doc-signing-sessions' -i -u 'client_id:client_secret' -X POST \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{"tenant_id":"some_tenant_id","client_notification_token":"client_notification_token"}' \
    --cert client.crt --key client.key
```

**Sample Curl Request&#x20;**<mark style="color:red;">**(New)**</mark>

```
$ curl 'https://staging.sign.singpass.gov.sg/api/v1/doc-signing-sessions' -i -X POST \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'X-Dss-Assertion: <jwt-assertion>' \
    -d '{"tenant_id":"some_tenant_id","client_notification_token":"client_notification_token"}' \
    --cert client.crt --key client.key
```

#### Sample HTTP Request <mark style="color:red;">(Deprecated)</mark>

```
POST /doc-signing-sessions HTTP/1.1
Accept: application/json
Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=
Content-Type: application/json
Host: staging.sign.singpass.gov.sg
Content-Length: 86

{"tenant_id":"some_tenant_id","client_notification_token":"client_notification_token"}
```

#### **Sample HTTP Request&#x20;**<mark style="color:red;">**(New)**</mark>

```
POST /doc-signing-sessions HTTP/1.1
Accept: application/json
X-Dss-Assertion: <jwt-assertion>
Content-Type: application/json
Host: staging.sign.singpass.gov.sg
Content-Length: 86

{"tenant_id":"some_tenant_id","client_notification_token":"client_notification_token"}
```

**Sample Response**

{% code overflow="wrap" %}

```
HTTP/1.1 200 OK
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Cache-Control: no-cache, no-store, must-revalidate
Transfer-Encoding: chunked
Content-Type: application/json
Date: Tue, 24 Sep 2024 02:30:17 GMT
Content-Length: 181

{"sign_ref":"4b1b5241-9594-4e98-b9e3-7f53b73e3fcc","expires_at":1727145019,"qr_code":{"payload":"https://app.singpass.gov.sg/docsign?sign_ref=4b1b5241-9594-4e98-b9e3-7f53b73e3fcc"}}// Some code
```

{% endcode %}

**Request Body**

| Name                        | Type   | Description                                                                                                                                                                                                                  |
| --------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_notification_token` | String | <p>A token provided by the DSAP to be used by Singpass when invoking the DSAP’s webhook endpoint.</p><p>Allowed Characters: Alphanumeric, underscore ( \_ ), dash ( - ), and whitespace</p><p>Max length: 255 characters</p> |
| `tenant_id`                 | String | <p>The identifier of the tenant of the DSAP client using the doc signing service.</p><p>Allowed Characters: Alphanumeric, underscore ( \_ ), dash ( - ), and whitespace</p><p>Max length: 255 characters</p>                 |

{% hint style="info" %}
The value of the `tenant_id` is not the signer's identity. Rather, it is an unique identifier for the DSAP's corporate customers that we can refer to in case of any anomaly detected. If you are not reselling your service to a third party, you can reuse the DSAP name provided during onboarding as the `tenant_id`.

For example: If ABC Bank goes through DSAP to reach DSS, then `tenant_id` must be a unique identifier of ABC Bank. However, if ABC Bank is directly integrated with DSS, then `tenant_id` can be just `ABC Bank`.
{% endhint %}

#### **Request Headers**

| Name              | Description                                                                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization`   | <p><mark style="color:red;">(Deprecated)</mark></p><p>The DSAP’s client id and client secret in http basic authentication scheme format.</p><p>Not required if DSAP is using JWT to authenticate</p> |
| `X-Dss-Assertion` | <p><mark style="color:red;">(New)</mark></p><p>JWT issued by the DSAP for authentication.</p>                                                                                                        |

#### **Request Headers**

| Name              | Description                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization`   | <p><mark style="color:red;">(Deprecated)</mark></p><p>The DSAP’s client id and client secret in http basic authentication scheme format.</p><p>Not required if DSAP is using JWT to authenticate.</p> |
| `X-Dss-Assertion` | <p><mark style="color:red;">(New)</mark></p><p>JWT issued by the DSAP for authentication.</p>                                                                                                         |

#### **Response Body**

| Parameter Description | Type   |                                                                                                                                                                                                                                                                           |
| --------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sign_ref`            | String | The primary identifier of a signing session used in all exchanges between Singpass and DSAP.                                                                                                                                                                              |
| `qr_code.payload`     | String | The QR payload containing the sign ref in a format understood by SingPass Mobile (SPM). DSAPs are expected to encode and display this as a QR code for SPM users to scan. Refer to the UX Guide provided in the developer package for the QR code display specifications. |
| `expires_at`          | Number | A Unix timestamp in seconds indicating the date and time when the `sign_ref` will expire.                                                                                                                                                                                 |

{% hint style="info" %}
Please note that `sign_ref` should not be treated as a UUID-v4, and the length of the `sign_ref` may vary from time to time.
{% endhint %}

{% hint style="warning" %}
The host of the URL in `qr_code.payload` in staging environment will change to stg-app.singpass.gov.sg after 18 Mar 2025.
{% endhint %}

#### Error Responses

Please refer to [General Error Response.](#general-error-response)

### `POST /doc-signing-sessions/<sign-ref>/hash` <a href="#post-doc-signing-sessions-less-than-sign-ref-greater-than-hash" id="post-doc-signing-sessions-less-than-sign-ref-greater-than-hash"></a>

DSAPs must use this endpoint to send the document hash, document name, and challenge code to Singpass. Singpass will then forward the document information and challenge code to the user for verification and signing.

The DSAP must invoke this API only after it has received the user’s digital signing certificate through its notification webhook endpoint. See **Steps 6, 7 and 8** of the [flow diagram](#document-signing-flow-diagram) for more details about what DSAPs need to do before invoking this endpoint.

#### **Request and Response Structure**

#### **Sample Curl Request&#x20;**<mark style="color:red;">**(Deprecated)**</mark>

```
$ curl 'https://staging.sign.singpass.gov.sg/api/v1/doc-signing-sessions/c6258905-c196-4465-9182-4d95e0163e96/hash' -i -u 'client_id:client_secret' -X POST \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
  "challenge_fqdn" : "signing-partner.gov.sg",
  "doc_name" : "signable-document.pdf",
  "nonce" : "bxUoQ4XiThs0oR19arXcaHpj+lm+i0BPta4YeTXkLXX=",
  "app_launch_url" : "com.example.dsap://home",
  "doc_hash" : "6AC7637DA92C76385F95A92C7617E591A8F6DF8F74F37EF8DB7E25E648E1DB7E",
  "challenge_code" : "1567"
}' \
    --cert client.crt --key client.key
```

#### **Sample Curl Request&#x20;**<mark style="color:red;">**(New)**</mark>

```
$ curl 'https://staging.sign.singpass.gov.sg/api/v1/doc-signing-sessions/c6258905-c196-4465-9182-4d95e0163e96/hash' -i -X POST \
    -H 'Accept: application/json' \
    -H 'Content-Type: application/json' \
    -H 'X-Dss-Assertion: <jwt-assertion>' \
    -d '{
  "challenge_fqdn" : "signing-partner.gov.sg",
  "doc_name" : "signable-document.pdf",
  "nonce" : "bxUoQ4XiThs0oR19arXcaHpj+lm+i0BPta4YeTXkLXX=",
  "app_launch_url" : "com.example.dsap://home",
  "doc_hash" : "6AC7637DA92C76385F95A92C7617E591A8F6DF8F74F37EF8DB7E25E648E1DB7E",
  "challenge_code" : "1567"
}' \
    --cert client.crt --key client.key
```

**Sample HTTP Request&#x20;**<mark style="color:red;">**(Deprecated)**</mark>

```
POST /doc-signing-sessions/c6258905-c196-4465-9182-4d95e0163e96/hash HTTP/1.1
Authorization: Basic Y2xpZW50X2lkOmNsaWVudF9zZWNyZXQ=
Accept: application/json
Content-Type: application/json
Host: staging.sign.singpass.gov.sg
Content-Length: 309

{
  "challenge_fqdn" : "signing-partner.gov.sg",
  "doc_name" : "signable-document.pdf",
  "nonce" : "bxUoQ4XiThs0oR19arXcaHpj+lm+i0BPta4YeTXkLXX=",
  "app_launch_url" : "com.example.dsap://home",
  "doc_hash" : "6AC7637DA92C76385F95A92C7617E591A8F6DF8F74F37EF8DB7E25E648E1DB7E",
  "challenge_code" : "1567"
}
```

#### **Sample HTTP Request&#x20;**<mark style="color:red;">**(New)**</mark>

```
POST /doc-signing-sessions/c6258905-c196-4465-9182-4d95e0163e96/hash HTTP/1.1
Accept: application/json
X-Dss-Assertion: <jwt-assertion>
Content-Type: application/json
Host: staging.sign.singpass.gov.sg
Content-Length: 309

{
  "challenge_fqdn" : "signing-partner.gov.sg",
  "doc_name" : "signable-document.pdf",
  "nonce" : "bxUoQ4XiThs0oR19arXcaHpj+lm+i0BPta4YeTXkLXX=",
  "app_launch_url" : "com.example.dsap://home",
  "doc_hash" : "6AC7637DA92C76385F95A92C7617E591A8F6DF8F74F37EF8DB7E25E648E1DB7E",
  "challenge_code" : "1567"
}
```

#### **Sample HTTP Response**

```
HTTP/1.1 200 OK
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Date: Tue, 24 Sep 2024 02:30:20 GMT
```

#### Path Parameters

| Parameter  | Description                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------- |
| `sign_ref` | The primary identifier of a signing session used in all exchanges between Singpass and DSAP |

#### **Request Body**

```
{
  "challenge_fqdn" : "signing-partner.gov.sg",
  "doc_name" : "signable-document.pdf",
  "nonce" : "bxUoQ4XiThs0oR19arXcaHpj+lm+i0BPta4YeTXkLXX=",
  "app_launch_url" : "com.example.dsap://home",
  "doc_hash" : "6AC7637DA92C76385F95A92C7617E591A8F6DF8F74F37EF8DB7E25E648E1DB7E",
  "challenge_code" : "1567"
}

```

#### **Request Fields**

<table><thead><tr><th width="207">Parameter</th><th width="154">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>doc_name</code></td><td>String</td><td><p>The name of the document to be signed by the user. Do note that this value will be displayed to the user, so it is recommended to use a human-readable name.</p><p>Length must be between 1 and 255</p></td></tr><tr><td><code>doc_hash</code></td><td>String</td><td><p>The hash of the document to be signed by the user. Refer to <a href="https://docs.sign.singpass.gov.sg/#document-hash-specifications">Document Hash Specifications</a> for more details.</p><p>Length must be 64</p></td></tr><tr><td><code>challenge_code</code></td><td>String</td><td><p>A set of characters used by the user to visually verify the signing session between the Singpass App and the DSAP website.</p><p>Length must be 4. Numerical values are recommended.</p></td></tr><tr><td><code>nonce</code></td><td>String</td><td>Singpass-generated random string sent to the DSAP's webhook endpoint during user certificate notification.</td></tr><tr><td><code>challenge_fqdn</code></td><td>String</td><td><p>The domain name of the webpage displaying the QR code. This will be displayed to the user on the Singpass app.</p><p>Length must be between 1-255</p></td></tr><tr><td><code>app_launch_url</code></td><td>String</td><td><p>(Optional) This adds the possibility for the user to be redirected back to the provided App Link after they successfully authorize themselves on the Singpass App. The value passed here should be the App Link registered with Apple’s App Store and/or Google’s Play Store.</p><p>Max length allowed is 255 characters.</p></td></tr></tbody></table>

#### **Request Headers**

<table><thead><tr><th width="375">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>Authorization</code></td><td><p><mark style="color:red;">(Deprecated)</mark></p><p>The DSAP’s client id and client secret in http basic authentication scheme format. Not required if DSAP is using JWT to authenticate</p></td></tr><tr><td><code>X-Dss-Assertion</code></td><td><p><mark style="color:red;">(New)</mark></p><p>JWT issued by the DSAP for authentication.</p></td></tr></tbody></table>

**Response Body**

There is no body in the response for successful API call.

#### **Error Response**

If Singpass fails to find the requested `sign_ref` (e.g. due to expiry), this API will return a `HTTP 400` error, and an accompanying `SIGN_REF_NOT_FOUND`error code in the response body.

For other errors, please refer to [General Error Response.](#general-error-response)

### `GET /.well-known/keys.json`

Integrating parties can verify the signature of a JWT from Singpass by acquiring the signing public key from this endpoint. More information about a JSON Web Key (JWK) endpoint can be found [here](https://tools.ietf.org/html/rfc7517).

Public keys returned from this endpoint could be in random sequence or rotated for security enhancement. For more information, please refer to [Caching and key rotation.](#caching-and-key-rotation)

#### Request and Response Structure

#### **Sample Curl Request**

```
$ curl 'https://static.staging.sign.singpass.gov.sg/.well-known/keys.json' -i -X GET
```

#### **Sample HTTP Request**

```
GET /.well-known/keys.json HTTP/1.1
Host: static.staging.sign.singpass.gov.sg
```

#### **Sample HTTP Response**

```
HTTP/1.1 200 OK
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
Cache-Control: max-age=21600, must-revalidate, no-transform, public
Content-Type: application/json
Content-Length: 436
Date: Tue, 24 Sep 2024 02:30:00 GMT

{
  "keys" : [ {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "ndi_dss_signer_02",
    "x" : "ObZ0BvgODnkQqMK5OjBWn5V6DCWlEhICwC7UuXxs-Vw",
    "y" : "c9CjVC779_rvOWMwbh4cE4Jx3bcfKe_20WVDtZYc_Ns"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "ndi_dss_signer",
    "x" : "dL8zGIrEMDfwlMxsd_uYqNbjq6PUHaswudG5lMJlcyI",
    "y" : "f2mU8Q2eE1pUsN37ktEHTf3n0u1u_2N7VRRus-3u4Z0"
  } ]
}
```

#### Request Body

There is no request body for this API call.

#### **Response Body**

```
{
  "keys" : [ {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "ndi_dss_signer_02",
    "x" : "ObZ0BvgODnkQqMK5OjBWn5V6DCWlEhICwC7UuXxs-Vw",
    "y" : "c9CjVC779_rvOWMwbh4cE4Jx3bcfKe_20WVDtZYc_Ns"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "ndi_dss_signer",
    "x" : "dL8zGIrEMDfwlMxsd_uYqNbjq6PUHaswudG5lMJlcyI",
    "y" : "f2mU8Q2eE1pUsN37ktEHTf3n0u1u_2N7VRRus-3u4Z0"
  } ]
}
```

#### Caching and Key Rotation

{% hint style="warning" %}
Responses from this endpoint, or individual keys from inside the JWKS can and should be cached for at least 1 hour, and NOT retrieved for each JWT validation. Cache-Control headers on the response indicate a possible policy.
{% endhint %}

For varying reasons, keys used for signing can and will be rotated/changed with no defined schedule, and at the full discretion of Singpass. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different `kid` value. The new `kid` value will be reflected in all the new JWTs signed by Singpass. In such cases, cached copies of Singpass public keys must be refreshed by re-invoking the JWKS endpoint.

If the validation of the Singpass signature fails, re-fetch from the JWKS endpoint once for that validation.

Please read through the list of **DON’Ts** below:

* Do not assume the position of a signing key among the list of the returned keys.
* Do not validate Singpass signatures using a hardcoded public key OR `kid`. Always determine the correct key (for signature verification) by inspecting the `kid` from the JWS header, and use it to retrieve the public key from our JWKS endpoint.
* Do not cache only 1 key. Caching should be done for the entire JWKS.

## DSAP Notification Webhook Endpoint <a href="#dsap-notification-webhook-endpoint" id="dsap-notification-webhook-endpoint"></a>

### Usage <a href="#usage" id="usage"></a>

Singpass will inform DSAP of various events that happen during the document signing process. To facilitate this, DSAPs must implement and expose a webhook endpoint to accept information from Singpass.

{% hint style="info" %}
The DSAP’s webhook is the main and only mechanism for Singpass to notify the DSAP of the events that happen in the signing flow. DSAPs cannot poll or query Singpass to get the state of the user’s doc signing session. See the Session expiry section for details on how session expiry should be handled.
{% endhint %}

Singpass will call the webhook endpoint to inform of the following events:

1. User certificate notification - To send the user’s certificate (See Step 6 of flow diagram).
2. Document hash signature notification - To send the user’s document hash signature (See Step 14 of flow diagram).
3. Webhook error notification - To inform DSAP of any errors encountered during the webhook calls above.

{% hint style="warning" %}
Please note that for all calls to the webhook endpoint, DSAPs are expected to respond `HTTP 200` to the webhook calls immediately, before any significant processing is performed on the request. This is to keep low latencies on the user-facing APIs that are dependent on the webhook calls and give a better overall experience to Singpass users.
{% endhint %}

### Specifications

* The webhook must accept the `POST` HTTP method.
* It should expect a [JSON Web Tokens (JWT)](https://tools.ietf.org/html/rfc7519) in the request body.
* It should authenticate incoming calls using the [Bearer authentication scheme](https://tools.ietf.org/html/rfc6750), accepting only the `client_notification_token` given to Singpass during session initialisation.
* For non-repudiation purposes, Singpass will sign all JWTs sent to DSAPs webhook with its signing key. DSAPs can retrieve the corresponding public keys for verification from [/.well-known/keys.json.](#get-.well-known-keys.json)
* Singpass will perform automated retries of webhook requests if it encounters timeouts and on certain errors. See the webhook Retry Settings for more details.
* It is sufficient for DSAPs to respond with an HTTP status code without any response body for this endpoint.

### IP Address Whitelisting

Singpass will call your webhook endpoints from these IP addresses, which you may choose to whitelist.

| Staging       | Production    |
| ------------- | ------------- |
| 54.169.20.186 | 18.143.229.39 |
|               | 54.179.76.90  |
|               | 3.0.39.45     |

### Request and Response Structure <a href="#request-and-response-structure-3" id="request-and-response-structure-3"></a>

#### **Sample Curl Request**

{% code overflow="wrap" %}

```
$ curl 'https://<dsap_domain_url>/dsap/webhook' -i -X POST \
    -H 'Authorization: Bearer <client_notification_token>' \
    -H 'Content-Type: application/json' \
    -d '{"token":"eyJraWQiOiJuZGlfZHNzX3NpZ25lciIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzaWduX3JlZiI6IjU2MTYzZTg5LWEyMzItNDUwMi1hNDRmLWUyMjI1MTJiYTFhZCIsInJlcXVlc3RfdHlwZSI6InVzZXJfY2VydCIsImV4cCI6MTcyNzE0NTE1MiwidXNlcl9jZXJ0IjoiTUlJQnJUQ0NBVEtnQXdJQkFnSUNBK2N3Q2dZSUtvWkl6ajBFQXdNd05URUxNQWtHQTFVRUJoTUNVMGN4RERBS0JnTlZCQW9NQTA1RVNURVlNQllHQTFVRUF3d1BkR1Z6ZEVCdVpHa3VaMjkyTG5Obk1CNFhEVEl3TURZd016QTNNalF5TjFvWERUSXdNRFl3TXpBM01qWXdOMW93VERFdE1Dc0dBMVVFQlJNa09HRmtPREExWW1VdE56Z3pOQzAwWWpZNExXRmxZek10Tm1NNE5UUTNObVpsWWpFeE1Sc3dHUVlEVlFRRERCSlRNREF3TURBd01Ea2dTbTlvYmlCRWIyVXdkakFRQmdjcWhrak9QUUlCQmdVcmdRUUFJZ05pQUFSb2FRWUVTQWpaUzBISnJwY1g1bWpRZlFzT0RaQ0s1WW1ybFdJejFyaXp3dzRBWEQ5bzRkdFJVZHBNOStGQWtlM2NreFlpWmM5SzJoYXZZdVRLLy9kM09KRzlFVHlyZ0VsVXRoV1c2R2FCZEZzV1pnRHMvenMzRkhyMFJvTThYLzB3Q2dZSUtvWkl6ajBFQXdNRGFRQXdaZ0l4QUw5WUl1M3hZMnY5YndiL2NoUWdPN0p6YnJxOGd0aTJOVmFoc0Q3Sk5kOUErOFJKcmR5QlRGZlpSMDA0elYzNk9RSXhBTzVZVHFYUWdydys1UFpXWjZSYWV3VkRKbjdEeXdYUUpiZXk3WnJ5MjdlZDdoeHNZYVQ5QlBBNElvNll5MmhHS1E9PSIsImlhdCI6MTcyNzE0NTAzMiwibm9uY2UiOiI5NjBiYzY5Yy1lY2M5LTRlOWEtODY4Yy04OTkyNTgwYjUyNTcifQ.ERUp7x8yEYZkdJEDU3z_0IZNYb0MdKknaoYYZXjQ8X4Dh29qtAP39W4N3dGJu_vvhYbtSjXX-JgXEINsMj8rtkkULZWsRXN8GTPalFTFc6l00_Kx09SLiha6Lc-UevED"}'
```

{% endcode %}

#### Sample HTTP Request

{% code overflow="wrap" %}

```
POST /dsap/webhook HTTP/1.1
Authorization: Bearer <client_notification_token>
Content-Type: application/json
Host: <dsap_domain_url>:443
Content-Length: 1215

{"token":"eyJraWQiOiJuZGlfZHNzX3NpZ25lciIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzaWduX3JlZiI6IjU2MTYzZTg5LWEyMzItNDUwMi1hNDRmLWUyMjI1MTJiYTFhZCIsInJlcXVlc3RfdHlwZSI6InVzZXJfY2VydCIsImV4cCI6MTcyNzE0NTE1MiwidXNlcl9jZXJ0IjoiTUlJQnJUQ0NBVEtnQXdJQkFnSUNBK2N3Q2dZSUtvWkl6ajBFQXdNd05URUxNQWtHQTFVRUJoTUNVMGN4RERBS0JnTlZCQW9NQTA1RVNURVlNQllHQTFVRUF3d1BkR1Z6ZEVCdVpHa3VaMjkyTG5Obk1CNFhEVEl3TURZd016QTNNalF5TjFvWERUSXdNRFl3TXpBM01qWXdOMW93VERFdE1Dc0dBMVVFQlJNa09HRmtPREExWW1VdE56Z3pOQzAwWWpZNExXRmxZek10Tm1NNE5UUTNObVpsWWpFeE1Sc3dHUVlEVlFRRERCSlRNREF3TURBd01Ea2dTbTlvYmlCRWIyVXdkakFRQmdjcWhrak9QUUlCQmdVcmdRUUFJZ05pQUFSb2FRWUVTQWpaUzBISnJwY1g1bWpRZlFzT0RaQ0s1WW1ybFdJejFyaXp3dzRBWEQ5bzRkdFJVZHBNOStGQWtlM2NreFlpWmM5SzJoYXZZdVRLLy9kM09KRzlFVHlyZ0VsVXRoV1c2R2FCZEZzV1pnRHMvenMzRkhyMFJvTThYLzB3Q2dZSUtvWkl6ajBFQXdNRGFRQXdaZ0l4QUw5WUl1M3hZMnY5YndiL2NoUWdPN0p6YnJxOGd0aTJOVmFoc0Q3Sk5kOUErOFJKcmR5QlRGZlpSMDA0elYzNk9RSXhBTzVZVHFYUWdydys1UFpXWjZSYWV3VkRKbjdEeXdYUUpiZXk3WnJ5MjdlZDdoeHNZYVQ5QlBBNElvNll5MmhHS1E9PSIsImlhdCI6MTcyNzE0NTAzMiwibm9uY2UiOiI5NjBiYzY5Yy1lY2M5LTRlOWEtODY4Yy04OTkyNTgwYjUyNTcifQ.ERUp7x8yEYZkdJEDU3z_0IZNYb0MdKknaoYYZXjQ8X4Dh29qtAP39W4N3dGJu_vvhYbtSjXX-JgXEINsMj8rtkkULZWsRXN8GTPalFTFc6l00_Kx09SLiha6Lc-UevED"}
```

{% endcode %}

#### Sample HTTP Response

```
HTTP/1.1 200 OK
Date: Tue, 24 Sep 2024 02:30:32 GMT
Connection: close
```

#### **Request Body**

{% code overflow="wrap" %}

```
{"token":"eyJraWQiOiJuZGlfZHNzX3NpZ25lciIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJzaWduX3JlZiI6IjU2MTYzZTg5LWEyMzItNDUwMi1hNDRmLWUyMjI1MTJiYTFhZCIsInJlcXVlc3RfdHlwZSI6InVzZXJfY2VydCIsImV4cCI6MTcyNzE0NTE1MiwidXNlcl9jZXJ0IjoiTUlJQnJUQ0NBVEtnQXdJQkFnSUNBK2N3Q2dZSUtvWkl6ajBFQXdNd05URUxNQWtHQTFVRUJoTUNVMGN4RERBS0JnTlZCQW9NQTA1RVNURVlNQllHQTFVRUF3d1BkR1Z6ZEVCdVpHa3VaMjkyTG5Obk1CNFhEVEl3TURZd016QTNNalF5TjFvWERUSXdNRFl3TXpBM01qWXdOMW93VERFdE1Dc0dBMVVFQlJNa09HRmtPREExWW1VdE56Z3pOQzAwWWpZNExXRmxZek10Tm1NNE5UUTNObVpsWWpFeE1Sc3dHUVlEVlFRRERCSlRNREF3TURBd01Ea2dTbTlvYmlCRWIyVXdkakFRQmdjcWhrak9QUUlCQmdVcmdRUUFJZ05pQUFSb2FRWUVTQWpaUzBISnJwY1g1bWpRZlFzT0RaQ0s1WW1ybFdJejFyaXp3dzRBWEQ5bzRkdFJVZHBNOStGQWtlM2NreFlpWmM5SzJoYXZZdVRLLy9kM09KRzlFVHlyZ0VsVXRoV1c2R2FCZEZzV1pnRHMvenMzRkhyMFJvTThYLzB3Q2dZSUtvWkl6ajBFQXdNRGFRQXdaZ0l4QUw5WUl1M3hZMnY5YndiL2NoUWdPN0p6YnJxOGd0aTJOVmFoc0Q3Sk5kOUErOFJKcmR5QlRGZlpSMDA0elYzNk9RSXhBTzVZVHFYUWdydys1UFpXWjZSYWV3VkRKbjdEeXdYUUpiZXk3WnJ5MjdlZDdoeHNZYVQ5QlBBNElvNll5MmhHS1E9PSIsImlhdCI6MTcyNzE0NTAzMiwibm9uY2UiOiI5NjBiYzY5Yy1lY2M5LTRlOWEtODY4Yy04OTkyNTgwYjUyNTcifQ.ERUp7x8yEYZkdJEDU3z_0IZNYb0MdKknaoYYZXjQ8X4Dh29qtAP39W4N3dGJu_vvhYbtSjXX-JgXEINsMj8rtkkULZWsRXN8GTPalFTFc6l00_Kx09SLiha6Lc-UevED"}
```

{% endcode %}

#### **Request Fields**

| Name    | Type   | Description                                                                                                            |
| ------- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| `token` | String | The signed JWT containing standard and custom claims that describe a user or error event of a digital signing session. |

#### **Request Headers**

| Name            | Description                                                                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | Bearer token authentication credentials. The token value is equal to the `client_notification_token` provided by the DSAP during session initialization. |

#### **Response Body**

There is no body in the response for this API call.

#### Request `token` structure

As mentioned previously, the request body `token` field is a JWT signed by Singpass, which can be verified by DSAPs.

#### **JWT Header (User Certificate)**

```
{
  "kid" : "ndi_dss_signer",
  "typ" : "JWT",
  "alg" : "ES256"
}
```

#### **JWT Claims (User Certificate)**

{% code overflow="wrap" %}

```
{
  "sign_ref" : "56163e89-a232-4502-a44f-e222512ba1ad",
  "request_type" : "user_cert",
  "exp" : 1727145152,
  "user_cert" : "MIIBrTCCATKgAwIBAgICA+cwCgYIKoZIzj0EAwMwNTELMAkGA1UEBhMCU0cxDDAKBgNVBAoMA05ESTEYMBYGA1UEAwwPdGVzdEBuZGkuZ292LnNnMB4XDTIwMDYwMzA3MjQyN1oXDTIwMDYwMzA3MjYwN1owTDEtMCsGA1UEBRMkOGFkODA1YmUtNzgzNC00YjY4LWFlYzMtNmM4NTQ3NmZlYjExMRswGQYDVQQDDBJTMDAwMDAwMDkgSm9obiBEb2UwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAARoaQYESAjZS0HJrpcX5mjQfQsODZCK5YmrlWIz1rizww4AXD9o4dtRUdpM9+FAke3ckxYiZc9K2havYuTK//d3OJG9ETyrgElUthWW6GaBdFsWZgDs/zs3FHr0RoM8X/0wCgYIKoZIzj0EAwMDaQAwZgIxAL9YIu3xY2v9bwb/chQgO7Jzbrq8gti2NVahsD7JNd9A+8RJrdyBTFfZR004zV36OQIxAO5YTqXQgrw+5PZWZ6RaewVDJn7DywXQJbey7Zry27ed7hxsYaT9BPA4Io6Yy2hGKQ==",
  "iat" : 1727145032,
  "nonce" : "960bc69c-ecc9-4e9a-868c-8992580b5257"
}
```

{% endcode %}

#### **Description of Claims (User Certificate)**

<table><thead><tr><th width="251">Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sign_ref</code></td><td>String</td><td>The primary identifier of a signing session used in all exchanges between Singpass and DSAP.</td></tr><tr><td><code>user_cert</code></td><td>String</td><td>The user's digital signing certificate in base64-encoded DER format.</td></tr><tr><td><code>iat</code></td><td>Number</td><td>A Unix timestamp in seconds indicating the date and time when the JWT was issued.</td></tr><tr><td><code>exp</code></td><td>Number</td><td>A Unix timestamp in seconds indicating the date and time when the JWT will expire.</td></tr><tr><td><code>nonce</code></td><td>String</td><td>A randomly generated string used to associate this user certificate notification to a document hash callback . This nonce must be included in the subsequent document hash callback request from DSAP.</td></tr><tr><td><code>request_type</code></td><td>String</td><td>Value to indicate the type of the request, value is <code>user_cert</code>.</td></tr></tbody></table>

#### **Description of Claims (Document Hash Signature)**

| Parameter            | Type   | Description                                                                                                                                                          |
| -------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sign_ref`           | String | The primary identifier of a signing session used in all exchanges between Singpass and DSAP.                                                                         |
| `doc_hash`           | String | The hash of the document to be signed by the user. Refer to [Document Hash Specifications](#document-hash-specifications) for more details.                          |
| `iat`                | Number | A Unix timestamp in seconds indicating the date and time when the JWT was issued.                                                                                    |
| `exp`                | Number | A Unix timestamp in seconds indicating the date and time when the JWT will expire.                                                                                   |
| `doc_hash_signature` | String | The signature of the document hash, signed by the user. Refer to [Document Hash Signature Specifications](#document-hash-signature-specifications) for more details. |
| `request_type`       | String | Value to indicate the type of the request, value is `signed_doc_hash`.                                                                                               |

#### **Description of Claims (Error)**

| Parameter           | Type   | Description                                                                                                                   |
| ------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `sign_ref`          | String | The primary identifier of a signing session used in all exchanges between Singpass and DSAP.                                  |
| `error`             | String | Error code representing an error, e.g. `CLIENT_NOTIFICATION_FAILED`                                                           |
| `iat`               | Number | A Unix timestamp in seconds indicating the date and time when the JWT was issued.                                             |
| `exp`               | Number | A Unix timestamp in seconds indicating the date and time when the JWT will expire.                                            |
| `error_description` | String | Returns human readable general information about the reason for the error.                                                    |
| `request_type`      | String | Value to indicate the type of the request, value is `error`.                                                                  |
| `ndi_request_id`    | String | A randomly generated ID that can be used to correlate requests between Singpass and DSAP. This ID is unique per user request. |

### Retry Settings <a href="#retry-settings" id="retry-settings"></a>

Singpass will retry on any connection errors, client timeout and the following http response codes returned from the DSAP webhook endpoint:

* 502 - BAD\_GATEWAY
* 503 - SERVICE\_UNAVAILABLE
* 504 - GATEWAY\_TIMEOUT

Singpass is using the following configuration for retry strategy:

```
Total timeout across all attempts: 5s
Per try timeout: 2s
Min back off: 500ms
Max attempts: 3
```

### Error Response

The DSAP webhook API must follow RESTful conventions and communicate errors by returning a proper error response and with a corresponding HTTP status code, following the structure indicated below. All fields are mandatory.

#### Response Fields

| Parameter           | Type   | Description                                                                                                                                 |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | String | A randomly generated ID that can be used to correlate requests between Singpass and DSAP. This ID is unique per user request.               |
| `error`             | String | Error code representing an error. Must be one of the values from the list of [v](#valid-error-codes)[alid error codes.](#valid-error-codes) |
| `error_description` | String | Returns human readable general information about the reason for the error.                                                                  |

#### **Sample Error Response**

```
{
  "id" : "1234",
  "error" : "SIGN_REF_NOT_FOUND",
  "error_description" : "The requested sign ref does not exist."
}
```

### Valid Error Codes <a href="#valid-error-codes" id="valid-error-codes"></a>

| Error                | Expected Http Status |                                                                                                                                                                          |
| -------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `SIGN_REF_NOT_FOUND` | 400                  | To be returned if the sign ref in the request is unknown or expired.                                                                                                     |
| `INVALID_REQUEST`    | 400                  | A catch all indicating an invalid request parameter from DSS. Eg. invalid client notification token, invalid user cert, invalid doc hash signature, etc.                 |
| `SERVER_ERROR`       | 5XX                  | <p>A catch all for any other errors that occurred in the DSAP.</p><p>Singpass will retry on 502, 503 and 504. Refer to <a href="#retry-settings">Retry Settings.</a></p> |

## Other DSAP Requirements <a href="#other-dsap-requirements" id="other-dsap-requirements"></a>

DSAPs are expected to verify the validity of the user’s certificate status against National Certificate Authority (NCA).

{% hint style="info" %}
Singpass only validates the expiry, signature and signer of the certificate against the NCA Root and Intemediary CAs.
{% endhint %}

* DSAPs must use [Online Certificate Status Protocol (OCSP)](https://tools.ietf.org/html/rfc6960) to do the status verification against NCA. The OCSP response must be embedded in the signed document.
* DSAPs shall not send unknown OCSP requests (e.g. unknown OCSP certificate serial number or unknown CA Hash name).
* Cryptographic algorithms: DSAP shall ensure that the default cryptographic algorithms used in its systems and during the Digital Signing Process are as follows:
  * Digital Signature Algorithms: ECDSA (key size with 256 bits or more);
  * ECC Curves: NIST P-256, P-384, P-521;
  * Hash Algorithms: SHA-2 (256/384/512).
* The [Certificate Revocation List (CRL) file](https://www.nca.gov.sg/SNICA-G1.crl) size is **large** so we do not recommend using [CRL](https://tools.ietf.org/html/rfc5280#section-6.3) to verify the cert status to avoid large signed document file sizes.

## Document Hash Specifications

DSAPs are expected to use the received user cert and generate a document hash that can later be digitally signed (locally) to form a [PAdES-LTV/LTA](https://www.etsi.org/deliver/etsi_ts/102700_102799/10277804/01.01.02_60/ts_10277804v010102p.pdf) compliant signature.

The document hash should be **SHA256 hashed** and **hex-encoded** before sending to Singpass.

## Document Hash Signature Specifications <a href="#document-hash-signature-specifications" id="document-hash-signature-specifications"></a>

The document hash is locally signed by the user’s digital identity, verified by Singpass and then sent to the DSAP.

The signature follows the [**ASN.1/DER format**](https://www.cryptosys.net/pki/manpki/pki_ecchexformat.html) and will be **hex-encoded**.

{% hint style="info" %}
The document hash is not re-hashed during signing.
{% endhint %}

DSAPs are expected to then generate a [PAdES-LTV/LTA](https://www.etsi.org/deliver/etsi_ts/102700_102799/10277804/01.01.02_60/ts_10277804v010102p.pdf) compliant signature using this.

## UI/UX Specifications

DSAPs should follow the UX Guide provided in the developer package given during onboarding when displaying the QR code and/or challenge code to the users on their webpage.

### QR Code deeplinking specifications <a href="#qr-code-deeplinking-specifications" id="qr-code-deeplinking-specifications"></a>

To support mobile users, DSAPs are also required to render the QR code with the mobile app links (deep links) following the format below.

**For production:**

<table data-full-width="false"><thead><tr><th width="170">Platform</th><th width="580"></th></tr></thead><tbody><tr><td>Android</td><td><code>intent://app.singpass.gov.sg/docsign?sign_ref=&#x3C;sign-ref>#Intent;scheme=https;package=sg.ndi.sp;S.browser_fallback_url=https://app.singpass.gov.sg/docsign;end</code></td></tr><tr><td>iOS</td><td><code>https://app.singpass.gov.sg/docsign?sign_ref=&#x3C;sign-ref></code></td></tr></tbody></table>

**For staging:**

<table data-full-width="false"><thead><tr><th width="170">Platform</th><th width="580"></th></tr></thead><tbody><tr><td>Android</td><td><code>intent://stg-app.singpass.gov.sg/docsign?sign_ref=&#x3C;sign-ref>#Intent;scheme=https;package=sg.ndi.sp.dev;S.browser_fallback_url=https://stg-app.singpass.gov.sg/docsign;end</code></td></tr><tr><td>iOS</td><td><code>https://stg-app.singpass.gov.sg/docsign?sign_ref=&#x3C;sign-ref></code></td></tr></tbody></table>

{% hint style="danger" %}
The new staging domain `stg-app.singpass.gov.sg` will only take effect from 18 Mar 2025. In the meantime, RP must use `app.singpass.gov.sg` for both staging and production.
{% endhint %}

## Frequently Asked Questions (FAQs) <a href="#frequently-asked-questions-faqs" id="frequently-asked-questions-faqs"></a>

**Question: Since the** [<mark style="color:blue;">**user cert notification**</mark>](#dsap-notification-webhook-endpoint) **webhook is defined as asynchronous and non-blocking, are there any constraints on when a DSAP should invoke the** [<mark style="color:blue;">**/doc-signing-sessions/\<sign-ref>/hash endpoint**</mark>](#post-doc-signing-sessions-less-than-sign-ref-greater-than-hash)**?**

Answer: Yes. The agreed average response time between the start of the [<mark style="color:blue;">user cert notification</mark>](#dsap-notification-webhook-endpoint) webhook and the invocation of the hash endpoint must be 8 seconds. This 8-second interval correlates to the period that an end-user has to wait after scanning the QR (till he/she receives a "Signing Challenge"). While waiting for the "Signing Challenge" (which is provided by a DSAP), the end-user will encounter a loading/ spinner screen.<br>

**Question: Are DSAPs allowed to cache an end-user’s public X.509 Certificate beyond the TTL of a signing-session (`sign_ref`) to cater for better user experience?**

Answer: Although it is technically possible for DSAPs to cache an end-user’s public certificate beyond the TTL of a signing-session (`sign_ref`), Singpass does not condone such a practice as it infringes Data Protection Policies. i.e. Lack of end-user’s consent in providing his/her personal information to a third-party site/application (<https://www.singpass.gov.sg/singpass/common/privacystatement>).

The [<mark style="color:blue;">/doc-signing-sessions/\<sign-ref>/hash endpoint</mark>](#post-doc-signing-sessions-less-than-sign-ref-greater-than-hash) will proceed to reject any requests of such nature if an invalid signing-reference ID (`sign_ref`) is provided. Repeated attempts to guess a signing-reference ID (sign\_ref) will be logged and recognised by Singpass as a malicious security event.


# User Journey (V1)

{% stepper %}
{% step %}

### On the organisation's webpage, click / tap on the 'Sign' button

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-a0154ad2e6f463ba351d4179f0c06ab2d7909fac%2FSafari%20(Catalina)%20-%20Light.png?alt=media" alt=""><figcaption><p>Sample organisation's webpage</p></figcaption></figure>
{% endstep %}

{% step %}

### Scan the QR code with your Singpass App

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1a4c761006ea3b1ef9ed09ac3b6c3031bd1a5b88%2FScan%20QR.png?alt=media" alt=""><figcaption><p>Screen showing QR (Desktop &#x26; Mobile views)</p></figcaption></figure>
{% endstep %}

{% step %}

### Approve or Reject on your Singpass App:

Check that the reference codes on your desktop and mobile screens are the same.

Tap *Approve* to sign the document, or *Reject* to cancel the signing.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-65ea26ab37bf9f17c8dc34502cab0ed450e5f6a7%2FConsent%20(3).png?alt=media" alt=""><figcaption><p>Screens shown after QR is scanned (Desktop &#x26; Mobile views)</p></figcaption></figure>
{% endstep %}

{% step %}

### Signing complete!

Return to the organisation's webpage to complete the rest of the process (if any).

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-a4c49d3ffa8cec203c9366febad16cf58c6bb22b%2FDocumentSigned%20(2).png?alt=media" alt=""><figcaption><p>Successful signing (Desktop &#x26; Mobile views)</p></figcaption></figure>
{% endstep %}
{% endstepper %}

## You may have some questions...

<details>

<summary>What is the reference code for during the signing?</summary>

The purpose of the reference code is to allow users to verify that they are signing the correct document, when the code on their Singpass App matches that which is shown on the organisation's webpage.

</details>

<details>

<summary>How can I download my document after signing?</summary>

You may return to the organisation who has sent you this document for the signed copy.

</details>


# Transaction Signing

## Transaction Signing API Specifications

This document outlines the technical specifications for the **Singpass Transaction Signing API**, designed to enable secure and seamless transaction signing for applications integrating with Singpass. It details the API endpoints, authentication mechanisms, request/response structures, and security protocols to ensure integrity, confidentiality, and user trust.

This specification serves as a guide for developers and system integrators to facilitate smooth implementation and interoperability.

## Flow Diagram

Refer to this diagram for an overview of the transaction signing flow and the interactions between RP, Singpass and other dependencies.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-5e884ae4964efcc71cdf54311d78257fb7bf5223%2Fimage%20(1)%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

RPs are expected to implement the following steps referenced from the flow diagram above:

<table><thead><tr><th width="105">Step(s)</th><th width="140">Component</th><th>Summary</th><th width="247">Specifications</th></tr></thead><tbody><tr><td>1</td><td>Frontend</td><td>Retrieve Singpass transaction signing javascript (Singpass JS)</td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/transaction-signing/embedding-singpass-js">Embedding Singpass JS</a></td></tr><tr><td>2</td><td>Frontend</td><td>Initialise a transaction signing session via Singpass JS</td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/transaction-signing/init-transaction-signing">Init Transaction Signing</a></td></tr><tr><td>6</td><td>Backend</td><td>After receiving the sign code, invoke Singpass API to exchange it for the user-signed transaction hash</td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/transaction-signing/exchange-transaction-signature">Exchange Transaction Signature</a></td></tr></tbody></table>


# Embedding Singpass JS

We provide a **core JavaScript library** (Singpass JS) to enable seamless integration with the Singpass Digital Signing Service (DSS). It facilitates transaction signing workflows for Relying Party (RP) applications, covering steps **2.1 to 5.3** in the flow diagram.

**Key Functionalities**

* **Initialisation**: Singpass JS is initialised in the RP’s frontend to set up the transaction signing process.
* **Session Management**: Starts the signing session with transaction details (Step 2.1).
* **QR Code Rendering**: Generates and displays the QR code for the user to scan via SingPass Mobile App (Step 2.2).
* **Status Handling**: Tracks user actions, returning the CHALLENGED status when the QR code is scanned (Step 3.2).
* **Success Confirmation**: Confirms the signed challenge response and returns the success status with the sign code (Step 5.3).

RPs shall embed this Javascript in your front end application.

## **URLs**

<table><thead><tr><th width="178">Environment</th><th width="576">URL</th></tr></thead><tbody><tr><td>Staging</td><td><p><a href="https://static.staging.sign.singpass.gov.sg/static/ndi_txn_sign.js">https://static.staging.sign.singpass.gov.sg/static/ndi_txn_sign.js</a><br>OR</p><p><a href="https://stg-id.singpass.gov.sg/static/ndi_txn_sign.js">https://stg-id.singpass.gov.sg/static/ndi_txn_sign.js</a> <mark style="color:red;">(Deprecated)</mark></p></td></tr><tr><td>Production</td><td><a href="https://static.app.sign.singpass.gov.sg/static/ndi_txn_sign.js">https://static.app.sign.singpass.gov.sg/static/ndi_txn_sign.js</a><br>OR<br><a href="https://id.singpass.gov.sg/static/ndi_txn_sign.js">https://id.singpass.gov.sg/static/ndi_txn_sign.js</a> <mark style="color:red;">(Deprecated)</mark></td></tr></tbody></table>

{% hint style="warning" %}
You **must provide your frontend origin** during onboarding to allow communication with us.
{% endhint %}

## Content Security Policy (CSP) Requirements <a href="#content_security_policy_csp_requirements" id="content_security_policy_csp_requirements"></a>

This section is important if the RP’s website (where Singpass JS is embedded) uses a Content Security Policy (CSP) header. For Singpass JS to fully function, please ensure that the following CSP attributes are set/added:

* `script-src` [`https://*.singpass.gov.sg`](https://*.singpass.gov.sg/)`;`
* `connect-src` [`https://*.singpass.gov.sg`](https://*.singpass.gov.sg/)`;`
* `style-src` [`https://*.singpass.gov.sg`](https://*.singpass.gov.sg/)`;`
* `img-src` [`https://*.singpass.gov.sg`](https://*.singpass.gov.sg/) `data:;`
* `font-src` [`https://fonts.gstatic.com`](https://fonts.gstatic.com/)`;`

Sample CSP header:

{% code overflow="wrap" %}

```
content-security-policy: default-src 'self'; script-src 'self' https://*.singpass.gov.sg; connect-src'self' https://*.singpass.gov.sg; style-src 'self' https://*.singpass.gov.sg; img-src 'self' https://*.singpass.gov.sg data:; font-src https://fonts.gstatic.com;
```

{% endcode %}

{% hint style="info" %}
It is not necessary to set/add any CSP attributes if the **RP’s website does not use a CSP header** or has **less strict policies** for all the attributes mentioned above.
{% endhint %}

## UI dimensions <a href="#ui_dimensions" id="ui_dimensions"></a>

The HTML elements will be rendered in a rectangular area with a fixed size with these dimensions, depending on the mode specified via the `additionalOptions` parameter:

| Mode                                 | Dimensions (width by height) |
| ------------------------------------ | ---------------------------- |
| Basic QR with no additional elements | 298px by 367px               |
| QR with download link                | 298px by 416px               |

{% hint style="danger" %}
The RP must allot a minimum space according to these dimensions for the transaction signing UI element to be rendered properly.
{% endhint %}

## UI Reference <a href="#ui_reference" id="ui_reference"></a>

For RP’s reference, this section displays the screens that Singpass JS renders during the transaction signing process. RPs can refer to these screens to get a better idea of how integrating with Singpass JS will look like on their website.

The green border indicates the [`minimum expected size of the DOMElementID`](#ui_dimensions) provided by the RP.

<table><thead><tr><th width="355">Description</th><th>Screen</th></tr></thead><tbody><tr><td>Session initialisation success</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-45576507e03d7ce73dba4b29fca2dcf2fe257f2f%2Fimage%20(6).png?alt=media" alt=""></td></tr><tr><td>User scanned the QR code using SPM</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-2497665fa3c2c8f20b6e393e9e0570c397ce87c8%2Fimage%20(7).png?alt=media" alt="" data-size="original"></td></tr><tr><td>Session expired (Before QR code was scanned)</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-41dcabb360123866d659da1361e1b587d127ad1b%2Fimage%20(8).png?alt=media" alt="" data-size="original"></td></tr><tr><td>Session expired (After QR code was scanned)</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1421e156ae97a2b0ff0507ff649f7c81ea589d34%2Fimage%20(9).png?alt=media" alt="" data-size="original"></td></tr><tr><td>Retryable error occurred<br><br>Users are only allowed to retry up to 1 time. This is to prevent excessive retries on the Singpass server because automated retries are already in place for such API calls.</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-e328e5e50ecbfdd8e3a8d8dd58d1de61ecc4b7fe%2Fimage%20(10).png?alt=media" alt="" data-size="original"></td></tr><tr><td><p>Unretryable error occurred<br></p><p>Examples of possible scenarios:</p><ul><li>Error occurred when invoking transactionParamsSupplier</li><li>Pre-flight checks have failed (ie. RP invoked .initTxnSigning() with invalid parameters)</li><li>Retries exhausted Malformed response from Singpass server, which cannot be recovered by retrying</li><li>Client side errors returned from Singpass server</li><li>In the situation where a corresponding erroneous HTTP status code is received, it will be displayed in brackets.</li></ul></td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-64df3a1e6f67de92b17ee92bb1154d692e02d0bf%2Fimage%20(11).png?alt=media" alt="" data-size="original"></td></tr><tr><td>Service unavailable. This screen will be displayed if transaction signing service is toggled off on Singpass.</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-65277a16a569e631c6da91b10cbe1de3fac46ec9%2Fimage%20(12).png?alt=media" alt="" data-size="original"></td></tr><tr><td><p>Browser unsupported.<br><br>This screen will be displayed if the end-user’s browser/user-agent is not supported by Singpass JS.</p><p><br>Singpass JS supports recent versions of major browsers, including but not limited to Chrome, Firefox, Edge, Safari, SamsungBrowser and IE 11.</p></td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-54e7df72b4177a9eb0440acba97b4ca7b3199a13%2Fimage%20(13).png?alt=media" alt="" data-size="original"></td></tr><tr><td>Transaction Cancelled. This screen will be displayed if RP invoked .cancelTxnSigningSession()</td><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-864f0e681ea722e750a9aca30f01dbf6625b7bf4%2Fimage%20(14).png?alt=media" alt="" data-size="original"></td></tr></tbody></table>


# Init Transaction Signing

RPs should invoke this function to start a transaction signing session with Singpass. This is the only function that needs to be invoked by the RP for every transaction signing session.

{% code overflow="wrap" %}

```js
initTxnSigning(DOMElementID, clientParams, transactionParamsSupplier, onError, additionalOptions)
```

{% endcode %}

Behind the scenes, Singpass JS will coordinate the required backend API calls to create a new session and renders the UI screens accordingly as users progress through the signing process.

Firstly, Singpass JS will perform pre-flight checks to validate the function method parameters and ensure that the end-user’s browser/user-agent is supported by Singpass JS.

Next, Singpass JS will call the `/txn-signing-sessions` endpoint that is exposed on the Singpass backend to initiate the transaction signing flow.

Upon successful invocation of this function and the session initiation by Singpass, a QR code will be generated and displayed for the user to scan with the Singpass app (SPM) and proceed with the transaction.

At the same time, Singpass JS will call the `/status` endpoint, which is a long-polling connection to the Singpass backend. This endpoint reacts to user actions in the SPM app, i.e. "user scanned" and "user authorised".

{% hint style="info" %}
Wrap the invocation of `initTxnSigning` in a **try-catch block**, in case of any unforeseen errors.\
RPs can choose to default to an alternate authorisation mechanism in such error cases.
{% endhint %}

## **Following up after redirection**

Once the user has successfully scanned and authorised the transaction using SPM, Singpass JS will redirect the end-user’s browser/user-agent to the RP’s registered `redirect_uri` along with the `code` and `state` parameters.

Once redirected, the RP’s backend **should invoke the /txn-signatures** endpoint to retrieve the user’s transaction hash signature and complete the transaction signing flow.

Sample redirect location upon successful transaction signing

{% code overflow="wrap" %}

```
https://partner.txnsign.gov.sg/redirect?code=v2-BYE9fSQpDXCM0tlcI0yHwkwiff3bNy09n%2F703h4rmZI%3D&state=ewoidXNlciI6ImEiLAoic2Vzc2lvbiI6IjEyMyIsCiJyYW5kb20iOiJ4eXoiCn0=
```

{% endcode %}

## **Method Parameters**

**`DOMElementID`** `string`

Represents [the unique ID of the Document Object Model (DOM) Element](https://developer.mozilla.org/en-US/docs/Web/API/Element/id) where Singpass JS will render the transaction signing UI elements (QR code, text, images) on.

{% hint style="info" %}
The DOM element should be **empty**; Singpass JS will clear it before rendering any UI assets.
{% endhint %}

{% hint style="info" %}
See [UI dimensions](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/transaction-signing/embedding-singpass-js#ui_dimensions) for the minimum size required of this element.
{% endhint %}

**`clientParams`** `object: { clientId, redirectUri }`

* **`clientId`** `string`

  The client identifier that was assigned by Singpass during RP registration.
* **`redirectUri`** `string`

  The URL that Singpass JS will eventually redirect the user to after the user completes the signing process using SPM. This value will be validated against the RP’s `redirect_uri` that was specified during RP registration.

***

**`transactionParamsSupplier`** `function: () ⇒ object: {state, nonce, txnInfo}`

This function will be invoked by Singpass to retrieve the necessary session parameters from the RP’s backend everytime a new sign session is to be initialised.

{% hint style="danger" %}
Singpass JS may invoke this function **multiple times** (eg. when the user clicks on the Singpass-rendered retry button to re-initialise another session due to an unforeseen error or session expiry). RPs should ensure that a **new** set of values (`txnInfo`, `state`, `nonce`) is returned on each invocation as these values are expected to be session-based.
{% endhint %}

{% hint style="danger" %}
RPs should ensure that they perform **automated retries on any network calls** made during this function invocation because Singpass **JS will not retry** on any failures arising from this function invocation.
{% endhint %}

This function can either be an `async` function **OR** a standard function that returns a `Promise` object that resolves to an object containing the following structure:

* **`state`** `string`

  A session-based, unique, and non-guessable value that RP’s backend should generate per transaction signing session.<br>

  As part of threat modelling, Singpass JS requests for the state parameter to mitigate replay attacks against the RP’s redirect uri. This parameter serves the same purpose as the [OAuth 2.0’s `state` parameter](https://tools.ietf.org/html/rfc6749#section-4.1.1).<br>

  It should have a **maximum of 255 characters** and **must match `regexp` pattern of `[A-Za-z0-9/_\-=.]`**.
* **`nonce`** `string`

  A session-based, unique, and non-guessable value that the RP’s backend should generate per transaction signing session.

  As part of threat modelling, Singpass JS requests for the nonce parameter to mitigate MITM attacks against the `/txn-signatures` endpoint. This parameter serves the same purpose as the [OIDC 1.0’s `nonce` parameter](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest).

  It should have a **maximum of 255 characters**. We recommend that you use a hex-encoded random number such as `java.security.SecureRandom` or `UUIDv4`.
* **`txnInfo`** `string`

  A signed JWT that contains the transaction information that the user would sign on using SPM. The structure of the JWT and how it will be validated by Singpass is detailed in the Structure of [`txnInfo` JWT section.](#structure-of-txninfo-jwt)

**Sample `transactionParamsSupplier` Implementation**

{% code overflow="wrap" %}

```javascript
const initiateSessionOnBackend = async () => {
  // Replace the below with an `await`ed call to initiate a session on your backend
  // which will generate state+nonce+txnInfo values.
  // Keep in mind to put in place automated retries, because Singpass will not retry on
  // any errors coming from this function invocation.

  //e.g
  return { state: "dummySessionState", nonce: "dummySessionNonce", txnInfo: "dummyTxnInfo" };
}

const transactionParamsSupplier = async () => {
  const backendSession = await initiateSessionOnBackend();
  return {
    state: backendSession.state,
    nonce: backendSession.nonce,
    txnInfo: backendSession.txnInfo
  };
};
```

{% endcode %}

***

**`onError`** `function: (errorId, message) ⇒ {}`

A callback function that will be invoked by Singpass JS upon certain error events.

On error events, you can expect the appropriate error screens to be rendered on the provided `DOMElementID` parameter.

The function must accept the following parameters:

* **`errorId`** `string`

  An Singpass-generated unique identifier for the error/request. If present, it can be used for debugging the error in Singpass.
* **`message`** `string`

  A short description of the error that occurred. Possible values:

  | Error Code                 | Description                                                                  |
  | -------------------------- | ---------------------------------------------------------------------------- |
  | `invalid_request`          | General client side errors, eg. an API call returned a 400 bad request error |
  | `status_subscription_fail` | The status subscription API call that Singpass JS makes has failed           |
  | `sign_session_expired`     | The current signing session has expired                                      |
  | `service_unavailable`      | Transaction signing service is toggled off at Singpass                       |
  | `txn_signing_fail`         | Catch all for unhandled/unknown errors                                       |
  | `txn_signing_cancelled`    | The current signing session is cancelled                                     |

**Sample `onError` implementation**

{% code overflow="wrap" %}

```javascript
const onError = (errorId, message) => {
  // Can be any custom implementation to handle the error

  // eg.
  console.log(`onError. errorId:${errorId} message:${message}`);
};
```

{% endcode %}

***

**`additionalOptions`** `object`

Optional configuration to customise additional behaviour:

* **`renderDownloadLink`** `string` (Optional)

  Whether to render a link to download the Singpass app. Defaults to false if not specified. The link appears below the QR area. Clicking the link opens the Singpass app webpage in a new tab/window.

|   | These additional UI elements will change the height of the rendered UI. See UI dimensions for the expected heights of the UI for the different modes. |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |

* **`appLaunchUrl`** `boolean` (Optional)

  Intended for mobile apps which embed this javascript and render a QR code. This adds the possibility for the user to be redirected back to the provided App Link after they successfully authorize themselves on the Singpass Mobile App. The value passed here should be the App Link registered with Apple’s App Store and/or Google’s Play Store.

  * Please note that opting into this would mean the relying party is required to be able to initialize auth, i.e generate the QR code, both with and without the appLaunchUrl. This is to ensure the Singpass App only triggers App Links when desired.

| Authenticating From                       | appLaunchUrl Param |
| ----------------------------------------- | ------------------ |
| Relying Party website                     | Do not include     |
| Relying Party website on a mobile browser | Do not include     |
| Relying Party mobile app                  | Can Include        |

* Sample `additionalOptions` implementation:

```
{
  renderDownloadLink: boolean,
  appLaunchUrl: string
}
```

## **Returns**

`initTxnSigning` returns a `string` that may be one of the following values:

* `SUCCESSFUL`

  Pre-flight checks were successful, and you can expect a QR code to be rendered. In case of unforeseen errors (eg. API errors during initialisation), a generic error screen will be rendered with the corresponding erroneous HTTP code, and the `onError` callback will be invoked.
* `FAILED`

  Pre-flight checks failed due to missing or malformed input parameters. If a valid `DOMElementID` is provided, a generic error screen will be rendered suggesting the user to opt for alternative authorization mechanisms. The `onError` callback will **NOT** be invoked.
* `NO_OP`

  Input method parameters are valid but pre-flight checks have determined that Singpass JS will not run on the end-user’s browser/user-agent. If a valid `DOMElementID` is provided, an error screen will be rendered indicating the unsupported browser/user-agent. The onError callback will **NOT** be invoked.

**Sample HTML invoking `.initTxnSigning()`**

{% code overflow="wrap" %}

```html
<html>
<script src="https://stg-id.singpass.gov.sg/static/ndi_txn_sign.js"></script>
<script>
  async function init() {
    const transactionParamsSupplier = async () => {
      const backendSession = await initiateSessionOnBackend();
      return {
        state: backendSession.state,
        nonce: backendSession.nonce,
        txnInfo: backendSession.txnInfo
      };
    };

    const onError = (errorId, message) => {
      console.log(`onError. errorId:${errorId} message:${message}`);
    };

    const initTxnSigningResponse = window.NDI.initTxnSigning(
      'singpass-qr',
      {
        clientId: 'T5sM5a53Yaw3URyDEv2y9129CbElCN2F',
        redirectUri: 'https://partner.gov.sg/redirect'
      },
      transactionParamsSupplier,
      onError,
      {
        renderDownloadLink: true,
        appLaunchUrl:'https://partner.gov.sg' // Replace with your iOS/Android App Link
      }
    );

    console.log('initTxnSigning: ', initTxnSigningResponse);
}
</script>
<body onload="init()">
<div id="singpass-qr"></div>
</body>
</html>
```

{% endcode %}

## **Structure of `txnInfo` JWT**

The `txnInfo` returned by the RP-provided `transactionParamsSupplier` function described above should wrap the required transaction information.

This is a standard signed JWT in [compact serialization format](https://tools.ietf.org/html/rfc7515#section-3.1).

Sample Signed JWT

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im1vY2stY2xpZW50LWVzMjU2LTEifQ.eyJleHAiOjE2MTQ2NTk1MDAsImlzcyI6IlQ1c001YTUzWWF3M1VSeURFdjJ5OTEyOUNiRWxDTjJGIiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL3R4bi1zaWduaW5nLXNlc3Npb25zIiwidHhuX2lkIjoidHJhbnNhY3Rpb25faWRlbnRpZmllciIsInR4bl9pbnN0cnVjdGlvbnMiOiJ1cGRhdGUgYmFuayBhY2NvdW50IGZyb20geHh4IHRvIHl5eSIsInR4bl9oYXNoIjoiYTRlNTlhNDBmODM2MjA0NDVlODk1ODcxZTU5Njg5NTcwZWQ2YjY0OTdkMzE1OTYxYTlkNDNmNDRkNDE4NzU4YiIsImlhdCI6MTYxNDY1OTM5Nywic3ViIjoiMWMwY2VlMzgtM2E4Zi00ZjhhLTgzYmMtN2EwZTRjNTlkNmE5In0.JTR09Ou6xBqo1nH19rTzrXyz4aW01_1JeMd6dcEFBJOAFAaVol3erfHvH6hDzA6m5RgfBfO-El6zQODY7o9uig
```

{% endcode %}

| Parameters                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Header** - standard JWS Headers. Refer to <https://tools.ietf.org/html/rfc7515#section-4>.                                                          | <p><code>type</code> - Must be "JWT"<br><br><code>alg</code> - Must be an ECDSA-based algorithm. See complete list <a href="https://tools.ietf.org/html/rfc7518#section-3.4">here</a>.<br><br><code>kid</code> - The key id indicating the key used to sign the JWT</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Payload** - standard registered claims alongside custom claims highlighted in **bold**. Refer to <https://tools.ietf.org/html/rfc7519#section-4.1>. | <p><code>iat</code> - A Unix timestamp in seconds indicating the date and time when the JWT was issued. Must be at most 2 minutes from the current time.<br><br><code>exp</code> - A Unix timestamp in seconds indicating the date and time when the JWT will expire. Must not be greater than two minutes from <code>iat</code>.<br><br><code>sub</code> - (optional) The user’s Singpass ID (in UUIDv4 format) if available.<br><br><strong><code>txn\_id</code></strong> - The unique ID of the transaction generated by the RP.<br><br><strong><code>txn\_instructions</code></strong> - Human-readable instructions that the user can read and consent on. Any sensitive information must be masked.<br><br><strong><code>txn\_hash</code></strong> - Hashed value of the combined <code>txn\_id</code> and <code>txn\_instructions</code> claims in the format: <code>\<txn\_id>:\<txn\_instructions></code>. Must be <strong>SHA256 hashed and hex-encoded</strong>.</p> |
| **Signature**                                                                                                                                         | Standard [JWT signature](https://tools.ietf.org/html/rfc7515#section-3.3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**JWT Validation**

Singpass backend will validate the signature of the signed JWT using the RP’s JWKS endpoint that was provided during registration.

{% hint style="info" %}
Singpass caches the keys found in the RP’s JWKS endpoint for **one hour**.\
\
When the RP’s signing keypair needs to be rotated, new keypairs must use a **different key id (`kid`)** value to ensure that consumers (e.g. Singpass) of the keys do not use a stale version of the public key in their caches.
{% endhint %}

## `.cancelTxnSigningSession()` <a href="#cancel_txn_signing_session" id="cancel_txn_signing_session"></a>

This function does **not** require any method parameters, and it also does **not** return anything.

Upon invocation, all ongoing API calls (if any) made by `.initTxnSession()` will be aborted. A [screen](https://stg-id.singpass.gov.sg/docs/txn-signing/js#ui_cancelled) indicating that the transaction has been cancelled is rendered, and there will be no UI changes thereafter.

If a valid [`onError`](https://stg-id.singpass.gov.sg/docs/txn-signing/js#on_error_callback) callback is provided, then it will be invoked with the following parameters:\
`onError(errorId: '', message: 'txn_signing_cancelled')`

{% hint style="info" %}
We recommend invoking this function when a **transaction has been cancelled by the user** (eg. when the transaction modal is closed) to ensure that the transaction is aborted properly.\
It is safe to invoke this method regardless of the session’s state (ie. whether the session is active or in an erroneous state).
{% endhint %}


# Exchange Transaction Signature

This section describes the process where the Relying Party (RP) backend exchanges the **sign code** received from the Singpass for the **user's digital signature**. This step finalises the transaction signing workflow, ensuring the transaction is securely signed and validated.

## Exchange signature API

### URLs

<table><thead><tr><th width="165">Environment</th><th width="176">Access Mechanism</th><th>URL</th></tr></thead><tbody><tr><td>Staging</td><td>mTLS</td><td>https://stg-id.singpass.gov.sg:8443/txn-signatures<br><mark style="color:red;">(Deprecated)</mark></td></tr><tr><td>Staging</td><td>TLS</td><td><a href="https://staging.sign.singpass.gov.sg/api/v1/txn-signatures">https://staging.sign.singpass.gov.sg/api/v1/txn-signatures</a></td></tr><tr><td>Production</td><td>mTLS</td><td>https://id.singpass.gov.sg:8443/txn-signatures<br><mark style="color:red;">(Deprecated)</mark></td></tr><tr><td>Production</td><td>TLS</td><td><a href="https://app.sign.singpass.gov.sg/api/v1/txn-signatures">https://app.sign.singpass.gov.sg/api/v1/txn-signatures</a></td></tr></tbody></table>

### Client Authentication

RPs are required to authenticate themselves by specifying a signed JWT via the `Authorization` header.

**JWT header**

The following standard JWS headers need to be included. Refer to [Jose Header RFC](https://tools.ietf.org/html/rfc7515#section-4) for more details about what each header presents.

**JWT claims**

The following claims need to be present.

<table><thead><tr><th width="146">Path</th><th width="145">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>sub</code></td><td><code>String</code></td><td>The Client ID generated during transaction signing replying party registration.</td></tr><tr><td><code>sign_code</code></td><td><code>String</code></td><td>The Singpass generated code that was returned to the RP via the RP’s redirect URI (specified in the <code>sign_code</code> query parameter).</td></tr><tr><td><code>iat</code></td><td><code>Number</code></td><td>The time at which the JWT was issued.</td></tr></tbody></table>

Claims example

```json
{
  "sign_code": "aRpFkeEbdOSBaeY7aGIk0rkvb90yr9nezLM4cMLOuVc=",
  "iat": 1598238992,
  "sub": "4iHWBHNNrYcXKKMOvk3bIE3CYAQnQ84V"
}
```

### Request

**Request headers**

Should include the Authorization token descibed in [Client Authentication](#client-authentication).

**Request body**

Request body shall be a json object with the sign\_code parameter.

```json
{"sign_code":"wOU1mqb7XICjhdTUgl73"}
```

**Example request**

{% code overflow="wrap" %}

```http
POST https://app.sign.singpass.gov.sg/api/v1/txn-signatures HTTP/1.1
Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJhdWQiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy90eG4tc2lnbmF0dXJlcyIsInN1YiI6Im5kaV9yZWdpc3RlcmVkX2NsaWVudF9pZCIsInNpZ25fY29kZSI6IndPVTFtcWI3WElDamhkVFVnbDczIiwiaXNzIjoibmRpX3JlZ2lzdGVyZWRfY2xpZW50X2lkIiwiZXhwIjoxNzM0MzM4Nzc4LCJpYXQiOjE3MzQzMzg3MTh9.1s2vk5I7o1cPYu2Djbf5qVLO4NmruwgI_L2rVqU7Q3q_b_TclSA4ue637OsiCoLTxMC9g5zDDIEjlz3hykBAq4o9jPOhMu4HsBFsiaz9IYmP2OkNnx3kMxBUxeqKZUxz
Content-Type: application/json

{"sign_code":"wOU1mqb7XICjhdTUgl73"}
```

{% endcode %}

### Response

The response is a JWT signed by Singpass wrapped in a json response.

Example:

{% code overflow="wrap" %}

```json
{"token":"eyJraWQiOiJuZGlfZHNzX3NpZ25lciIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJhdWQiOiJodHRwczovL2F1ZGllbmNlLm9yaWdpbiIsInN1YiI6IjZlNjc2NjU0LTViYjQtNDIyNy1iYTFhLWYzMDU5ZTIyNWYyMCIsInR4bl9oYXNoX3NpZ25hdHVyZSI6IjZhYzc2MzdkYTkyYzc2Mzg1Zjk1YTkyYzc2MTdlNTkxYThmNmRmOGY3NGYzN2VmOGRiN2UyNWU2NDhlMWRiN2UiLCJ0eG5faGFzaCI6IjZhYzc2MzdkYTkyYzc2Mzg1Zjk1YTkyYzc2MTdlNTkxYThmNmRmOGY3NGYzN2VmOGRiN2UyNWU2NDhlMWRiN2UiLCJpc3MiOiJodHRwczovL2NsaWVudC5yZWRpcmVjdC5vcmlnaW4iLCJleHAiOjE3MzQzMzg4MzUsImlhdCI6MTczNDMzODcxNSwibm9uY2UiOiJjZWJhUTRYaVRoczBvUDA4YXJYY0JRcGordnkraTBCUHRhNFllVFhrTEVFPSJ9.vVZxJrZoUoloLzjvCwB8-Cg0yVxlBRQmGDcGrxNy_Owr8n_NV_sy7oQI0FMzLd4XcGBNfhIdLKBuycQIOZCVWPUU6qrhZFVORfjOCyJc10BvtB3_inOP8drRkHb4Q1o5"}
```

{% endcode %}

#### Token JWT structure

**Headers**

The following standard JWS headers will be included. Refer to [Jose Header RFC](https://tools.ietf.org/html/rfc7515#section-4) for more details about what each header presents.

Header Example

```json
{
  "kid" : "abcd",
  "typ" : "JWT",
  "alg" : "ES256"
}
```

**Claims**

The following claims will be returned.

<table><thead><tr><th width="240">Path</th><th width="123">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>iss</code><br><mark style="color:red;">(Deprecated)</mark></td><td><code>String</code></td><td>The principal that issued the JWT. <a href="https://tools.ietf.org/html/rfc7519#section-4.1.1">https://tools.ietf.org/html/rfc7519#section-4.1.1</a><br></td></tr><tr><td><code>sub</code></td><td><code>String</code></td><td>The user’s Singpass user id signed the transaction. <a href="https://tools.ietf.org/html/rfc7519#section-4.1.2">https://tools.ietf.org/html/rfc7519#section-4.1.2</a></td></tr><tr><td><code>iat</code></td><td><code>Number</code></td><td>The time at which the JWT was issued. <a href="https://tools.ietf.org/html/rfc7519#section-4.1.6">https://tools.ietf.org/html/rfc7519#section-4.1.6</a></td></tr><tr><td><code>exp</code></td><td><code>Number</code></td><td>The expiration time on or after which the JWT MUST NOT be accepted by Singpass for processing. Additionally, Singpass will not accept tokens with an <code>exp</code> longer than 2 minutes since <code>iat</code>. <a href="https://tools.ietf.org/html/rfc7519#section-4.1.4">https://tools.ietf.org/html/rfc7519#section-4.1.4</a></td></tr><tr><td><code>nonce</code></td><td><code>String</code></td><td>The value passed by the signing partner during the init session API call</td></tr><tr><td><code>txn_hash_signature</code></td><td><code>String</code></td><td>The hex-encoded user signature over the <code>txn_hash</code></td></tr><tr><td><code>txn_hash</code></td><td><code>String</code></td><td>The SHA-256 hash of the <code>txn_id</code> and <code>txn_instructions</code> field calculated in this manner: <code>sha256(&#x3C;txn_id>:&#x3C;txn_instructions></code>). Encoded in hexadecimal.</td></tr></tbody></table>

Claims Example

{% code overflow="wrap" %}

```json
{
  "sub" : "6e676654-5bb4-4227-ba1a-f3059e225f20",
  "txn_hash_signature" : "6ac7637da92c76385f95a92c7617e591a8f6df8f74f37ef8db7e25e648e1db7e",
  "txn_hash" : "6ac7637da92c76385f95a92c7617e591a8f6df8f74f37ef8db7e25e648e1db7e",
  "exp" : 1734338835,
  "iat" : 1734338715,
  "nonce" : "cebaQ4XiThs0oP08arXcBQpj+vy+i0BPta4YeTXkLEE="
}
```

{% endcode %}

**Signature**

Standard JWT signature, RP **MUST** validate the signature with [Singpass public keys.](#fetch-our-public-keys)

### Error handling

Singpass APIs are RESTful in design and communicate classes of errors based on the **Http Status** code. The status code should be used to determine if the error is caused by consumer or provider. Consumers should log the HTTP status code along with the `id` and/or `trace_id` of the error.

<table><thead><tr><th width="165">Http Status</th><th>Description</th></tr></thead><tbody><tr><td>4xx</td><td><p>Errors caused by API consumer. You can expect codes such as 400, 401, 403, 404 etc if incorrect requests are made to APIs.</p><p>Example: <strong>400: Invalid/missing request arguments</strong></p></td></tr><tr><td>5xx</td><td><p>Errors caused by API provider or its dependencies. You can expect codes such as 500, 502, 503 etc if there is an issue on Singpass or its dependencies.</p><p>Example: <strong>500: Internal Server Error due to some kind of programming error.</strong></p></td></tr></tbody></table>

**Error response json**

<table><thead><tr><th width="230">Path</th><th width="101">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>id</code></td><td><code>String</code></td><td>The unique identifier for this error/request. Please log this identifier for support and debugging purposes.</td></tr><tr><td><code>trace_id</code></td><td><code>String</code></td><td>(Optional) An auxiliary id for request correlation across services. Please also log this identifier for operational support and debugging purposes.</td></tr><tr><td><code>error</code></td><td><code>String</code></td><td>Error code representing broad class of error. See <a href="https://stg-id.singpass.gov.sg/docs/txn-signing/api#api_error_codes">Error Codes</a> for the list of possible error codes that can be returned and what they represent.</td></tr><tr><td><code>error_description</code></td><td><code>String</code></td><td>Returns human readable general information about the reason for the error. Note that due to security reasons; detailed information is unlikely to be available in this message.</td></tr></tbody></table>

**Error codes**

| Error Code            | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| `CLIENT_SIDE_ERROR`   | Generic error code for an invalid request.                 |
| `SERVER_SIDE_ERROR`   | Generic error code for an error that occurred in Singpass. |
| `UNAUTHORIZED`        | Authorisation header value is invalid.                     |
| `ARGUMENTS_NOT_VALID` | Some request parameters are invalid.                       |

Example: Invalid Request Parameters

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "CLIENT_SIDE_ERROR",
  "error_description" : "This is an invalid request.",
  "trace_id" : "675fe8742c6442a7c0a1f3d1643ff9af"
}
```

## Fetch our public keys

Integrating parties can verify the signature of a JWT from Singpass by acquiring the signing public key from this endpoint. More information about a JSON Web Key (JWK) endpoint can be found [here](https://tools.ietf.org/html/rfc7517).

Public keys returned from this endpoint could be in random sequence or rotated for security enhancement.

### URLs

<table><thead><tr><th width="178">Environment</th><th width="576">URL</th></tr></thead><tbody><tr><td>Staging</td><td><p><a href="https://static.staging.sign.singpass.gov.sg/.well-known/keys.json">https://static.staging.sign.singpass.gov.sg/.well-known/keys.json</a><a href="https://static.staging.sign.singpass.gov.sg/.well-known/keys.json"><br></a>OR</p><p><a href="https://stg-id.singpass.gov.sg/.well-known/digital-signing-keys">https://stg-id.singpass.gov.sg/.well-known/digital-signing-keys</a> <mark style="color:red;">(Deprecated)</mark></p></td></tr><tr><td>Production</td><td><a href="https://static.app.sign.singpass.gov.sg/.well-known/keys.json">https://static.app.sign.singpass.gov.sg/.well-known/keys.json</a><a href="https://static.app.sign.singpass.gov.sg/.well-known/keys.json"><br></a>OR<br><a href="https://id.singpass.gov.sg/.well-known/digital-signing-keys">https://id.singpass.gov.sg/.well-known/digital-signing-keys</a> <mark style="color:red;">(Deprecated)</mark></td></tr></tbody></table>

### Cache and key rotation

For varying reasons, keys used for signing can and will be rotated/changed with **no defined schedule**, and at the full discretion of Singpass. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different `kid` value. The new `kid` value will be reflected in all the new JWTs signed by Singpass. In such cases, cached copies of Singpass public keys must be refreshed by re-invoking the JWKS endpoint.

If the validation of the Singpass signature fails, re-fetch from the JWKS endpoint once for that validation.

{% hint style="danger" %}
Please read through the list of **DON’Ts** below:

* Do not assume the position of a signing key among the list of the returned keys.
* Do not validate Singpass signatures using a hardcoded public key OR `kid`. Always determine the correct key (for signature verification) by inspecting the `kid` from the JWS header, and use it to retrieve the public key from our JWKS endpoint.
* Do not cache only 1 key. Caching should be done for the entire JWKS.
  {% endhint %}


# UX Guidelines

This section contains important UX guidelines to ensure signers are well-guided through their signing journey.

* [Adding sufficient signature placeholder space in your document](#add-sufficient-signature-placeholder-space-in-your-document)
* [Upload your app logo](#upload-your-app-logo)
* [Implementing the Sign with Singpass button](#implementing-the-sign-with-singpass-button)
* [Presenting Sign with other signing options](#presenting-sign-with-other-signing-options)

## **Add sufficient signature placeholder space in your document**

On a regular A4 document, a Sign with Singpass signature will take up an area of 7.78cm x 2.12cm (294 x 80 pixels).

When preparing a PDF of the unsigned document, clearly demarcate the placements of the signatures and **mark a sufficient area (at least 3.12 x 7.98cm) for the signature placeholders to appear.** This ensures that the document's content will not be obscured by the digital signature.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-820afa8e8e61e11f1f8f3b1da98008f665a03fef%2FPlaceholder%20ref.png?alt=media" alt=""><figcaption><p>Example of a clearly demarcated signature area in the document (size annotations are not required)</p></figcaption></figure>

For ease, you may copy the placeholder sample from this Word document to use in your own document:

{% file src="/files/q5jScpCblUvy3ZzGKFdA" %}

<details>

<summary>How do I define the location on the document where my user's signature should appear?</summary>

When initiating a sign request to our API, you are required to send us the coordinates of the desired location for your user's signature to appear.

You can use our [Sign Location Helper](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3#sign-location-helper) to experiment with signature placement and copy the `(x, y, page)` values for use in Sign v3.

</details>

## Upload your app logo

Your organisation's logo will be displayed in various places like the Login screen and Singpass app. This helps users identify your organisation when they are transacting with you.

### App logo requirement

When uploading your logo, ensure that they meet the following requirements:

* **File format**: PNG (transparent background)
* **Dimension**: 256px by 256px to 512px by 512px
* **File size**: Up to 200KB
* **Aspect Ratio**: Square (1:1 ratio)
* **No padding**: The logo should fill the entire canvas with no surrounding whitespace. Padding is applied automatically and does not need to be included in your upload.

### Example of logo

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1f5ad361226deb39a3873ec6cbe2484b2da01fd0%2FDocs_%20App%20Logo.png?alt=media" alt=""><figcaption></figcaption></figure>

Note:

* For Singpass Login screen: Changes will take effect from 1 Jul 2026.
* For Singpass app: Logo changes will only be reflected once users update to the latest app version, from late Jul 2026 onwards.

## Implementing the Sign with Singpass button

{% hint style="danger" %}
**All signing sessions must be initiated via the Singpass button** and not through providing any redirect links directly to the user.
{% endhint %}

#### You can download the Sign button in 2 sizes here:

{% file src="/files/n5X7FvyMnJZp4ZJi5ZAk" %}

#### Otherwise, please adhere to the following guidelines to create the Sign button.

* [Singpass button types](#singpass-button-types)
* [Font usage for button label](#font-usage-for-button-label)
* [Aria labels for screen readers](#accessibility-aria-labels-for-screen-readers)
* [Singpass logo size](#singpass-logo-size)
* [Button colour](#button-colour)
* [Border stroke](#border-stroke)
* [Border radius](#border-radius)
* [Hover state](#hover-state)
* [Width and height](#width-and-height)
* [Loading state](#loading-state)

\
**Singpass logo download:**

You can also use the following Singpass logo for your online and print materials

{% file src="/files/oSoNXQPBlIAQXYCZkHVB" %}

#### **Singpass button types**

By default, use the white fill button to pair it with your service’s interface. Alternatively, you may use the red fill button if it’s suitable.

* White-filled button: **#FFFFFF**
* Red-filled button: **#F4333D**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-0c5730a994abdd86aabb54877c2fb212acb26694%2FBg.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Font usage for button label**

By default, please use **Poppins at 16px** size. Alternatively, you may use your brand’s typeface. San serif is highly recommended for this button to better match the Singpass logo.

Download Poppins Bold on [Google fonts](https://fonts.google.com/specimen/Poppins).

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-f2c99718abbc22742991942c37e5263fb48d9de4%2FBg-1.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Accessibility: Aria labels for screen readers**

Please ensure that the **Singpass logo has a aria-label** to ensure that screen readers will read it as “Sing pass” to avoid it reading out the entire word as ‘S-i-n-g-p-a-s-s’.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-650ff023000ce0e1d68e6387908e817b099a65ac%2Faria.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Singpass logo size**

**Match the x-height of the label** as close as possible to ensure visual balance and proportion.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-83b8a40f8eed7b7d912746028c41136b75c99d1e%2FGroup%207812%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Button colour**

To ensure brand recognition and consistency, use the **white-filled** or **red-filled** buttons as stated below. Avoid using colours other than white-filled or red-filled buttons.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-f16d1f72a02977e13c3731dc0abccb848fbc6227%2FGroup%207813.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Border stroke**

When using the white-filled button, please ensure to adhere to the specs stated below.

* Border colour: **#C8C9CC**
* Border width: **1px**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-740b9a7c7809e606162ec7cafdc8d81d2fce957e%2FBg-2.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Border radius**

Ensure that the border radius of Singpass button matches your button.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-03fa80778351710e70f0d1240afd8d55cf3034c7%2FGroup%207814.png?alt=media&amp;token=ae5dcedb-614c-40f7-9e99-87c9f9d5bd52" alt=""><figcaption></figcaption></figure>

#### **Hover state**

Please adhere to the following colours, and avoid using another hover state styling.

* White-filled button hover colour: **#F5F5F7**
* Red-filled button hover colour: **#B0262D**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-801d3aa2f457546926e6acae218a1f5a6fe86cff%2FGroup%207815.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Width and height**

Please ensure that the Singpass button visually matches your primary button with the following:

* Width: **Fill to match your primary button width**
* Height: **Match your button height**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-bc6067b81a66c78f22c07cc40118e8cebc1d2bd2%2FGroup%207816.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Loading state**

Please ensure that the button has a loading state as follows. The loading state should appear for the duration of time after the user clicks the button and is waiting to be redirected to the Sign portal.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-7e9658d95813b104b9fc0aa8486ddd25f35cd1f9%2FLoading%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

## Presenting Sign with other signing options

**If users are given multiple options to sign**, with Sign as one of the options, we recommend positioning Sign as the preferred signing choice, and including the following liner to inform users of the security benefit of using Sign with Singpass:

> *By signing with Singpass, you create secure digital signatures that are highly resistant to forgery and tampering.*

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-7b8dac1493c464b3a54450d96df1efc2c93c5d69%2FMultiple%20sign%20options.png?alt=media" alt=""><figcaption><p>Example demonstrating how this liner can be included</p></figcaption></figure>


# User Journey Illustration

Relying Parties (RPs) who wish to use Sign with Singpass in their production environments will also have to submit a **user journey illustration.** Please fill in the following template before uploading it into the onboarding form.

{% file src="/files/H5S3QYj2eyjKrpJJRfOn" %}

{% hint style="success" %}
Please also ensure that your user journey design adheres to our [UX Guidelines](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/ux-guidelines)
{% endhint %}


# Digital Signing Partners

You may also choose to contact the following Digital Signing Partners who have experience integrating Sig&#x6E;**:**

{% hint style="info" %}
Alternatively, you may **directly** integrate with Sign with Singpass APIs by submitting on [onboarding request here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/onboard).
{% endhint %}

<table data-view="cards" data-full-width="true"><thead><tr><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>DocuSign</strong><br>Docusign brings agreements to life. Over 1.5 million customers and more than a billion people in over 180 countries use Docusign solutions to accelerate the process of doing business and simplify people’s lives.</td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-37ac9bbf66c27fd6862840abfa017c389f3c3610%2FDocusign%20banner.png?alt=media">Docusign banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/docusign">Docusign</a></td></tr><tr><td><strong>Kofax</strong><br>Kofax enables organisations to Work Like Tomorrow™—today. Kofax’s Intelligent Automation software platform and solutions digitally transform document intensive workflows.</td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-e1edf7cd3eaea0e3b3e4d017d587916a62e70dcc%2FTungsten%20Auto%20banner.png?alt=media">Tungsten Auto banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/tungsten-automation">Tungsten Automation</a></td></tr><tr><td><strong>Tessaract Technologies Pte Ltd</strong><br>Tessaract.io is an all-in-one enterprise management system for professionals built on a cloud-native architecture, readily accessible on all smart devices.</td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-24f79bc15dbe9f4e46b9ce3badec57a847b7ccee%2FTessaract%20banner.png?alt=media">Tessaract banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/tessaract-technologies-pte-ltd">Tessaract Technologies Pte Ltd</a></td></tr><tr><td><strong>Netrust Pte Ltd</strong><br>Netrust is Asia’s first public Certification Authority (CA) and Singapore's first IMDA-accredited CA since 2001 which provides individuals, business and government organizations with a complete online identification and security infrastructure to enable secure electronic transactions.</td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-3ddb1e170c00a6c11f20a879d5729e7438d4689d%2FNetrust%20banner.png?alt=media">Netrust banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/netrust-pte-ltd">Netrust Pte Ltd</a></td></tr><tr><td><strong>Modus Consulting</strong><br>Modus Consulting enables organisations to develop digital document frameworks and orchestrations, starting with intelligent data capture via "Dynamic Interactive PDFs" to back-office submission and orchestrations.</td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-03daaa16aeb0dd0a28be08c169b99c55e30e7344%2FNDISign%20banner.png?alt=media">NDISign banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/modus-consulting">Modus Consulting</a></td></tr><tr><td><p><strong>Redoc.co by Real Estate Doc Pte Ltd.</strong></p><p>Redoc.co, by Real Estate Doc, is the cloud-based Revenue and Contract Management software for Sales-Driven and Real Estate Businesses.</p></td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-7a92a497835fbfa64f1ae7057994990808e2c000%2FRedoc%20banner.png?alt=media">Redoc banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/redoc.co-by-real-estate-doc-pte-ltd.">Redoc.co by Real Estate Doc Pte Ltd.</a></td></tr><tr><td><p><strong>CrimsonLogic</strong></p><p>For more than 30 years, we have partnered with governments across the world. Together as their trusted partner, we deliver value to citizens and businesses through sustainable Digital Transformation.</p></td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c7c9b3dc6d70b2f3e68f1f3028db3f2763bba6a3%2FCrimsonLogic%20banner.png?alt=media">CrimsonLogic banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/crimsonlogic">CrimsonLogic</a></td></tr><tr><td><p><strong>Zoho Sign</strong></p><p>Zoho Sign is a complete digital signature app for business signatories. It helps organisations to sign, send, and manage documents from anywhere and at anytime.</p></td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-3f34ff424c7876f5d7579e40609cb6447035bbd7%2FZoho%20banner.png?alt=media">Zoho banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/zoho-sign">Zoho Sign</a></td></tr><tr><td><p><strong>Securemetric Technology Pte. Ltd.</strong></p><p>SigningCloud is a SaaS based digital signature solution for you to sign, assign &#x26; manage documents signature in one place.</p></td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c7d33da11560a1f02b4fbe693608cd0c384f786a%2FSigning%20Cloud%20banner.png?alt=media">Signing Cloud banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/securemetric-technology-pte.-ltd.">Securemetric Technology Pte. Ltd.</a></td></tr><tr><td><p><strong>Rently Pte. Ltd.</strong></p><p>Rently is the new revolutionary mobile application that digitalises the entire property renting process and it is now integrated with Sign with Singpass.</p></td><td><a href="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-18eaa338b287d7e91499826a0605ea0c1aebb092%2FRently%20banner.png?alt=media">Rently banner.png</a></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners/rently-pte.-ltd.">Rently Pte. Ltd.</a></td></tr></tbody></table>


# Docusign

## **About Docusign**

Docusign brings agreements to life. Over 1.5 million customers and more than a billion people in over 180 countries use Docusign solutions to accelerate the process of doing business and simplify people’s lives.

With intelligent agreement management, Docusign unleashes business-critical data that is trapped inside of documents. Until now, these were disconnected from business systems of record, costing businesses time, money, and opportunity.

Using Docusign IAM, companies can create, commit, and manage agreements with solutions created by the #1 company in e-signature and contract lifecycle management (CLM).

To find out more, click [here](https://www.docusign.com/).

## **Contact**

**Sales Email Address**

* <apac@docusign.com>

**Singapore Hotline**

* +800 1206 719

**Sydney Hotline**

* +61 2 9392 1998

**US Hotline**

* +1 877 720 2040


# Tungsten Automation

## **About Tungsten Automation**

Kofax enables organisations to Work Like Tomorrow™—today. Kofax’s Intelligent Automation software platform and solutions digitally transform document intensive workflows. Customers realise greater agility and resiliency by combining Kofax’s process orchestration, cognitive capture, RPA, output management, analytics and mobile capabilities to speed time-to-value and increase competitiveness, growth and profitability while mitigating compliance risk.

Kofax SignDoc® included in Kofax Intelligent Automation software platform enables trustworthy, secure and convenient paperless signing for a wide variety of functions including customer and employee onboarding, procurement, account management, service documentation, payroll and finance.

To find out more, click [here](https://www.kofax.com/).

***

## Contact

**Enquiry Email Address**

* <SSR.APAC@kofax.com>

**Singapore Hotline**

* +65 6278 7662


# OneSpan

## **About OneSpan**

OneSpan enables financial institutions, government departments and other organisations to succeed by making bold advances in their digital transformation. OneSpan establishes trust in people’s identities, the devices they use, and the transactions that shape their lives. More than 10,000 customers, including over half of the top 100 global banks, rely on OneSpan solutions to protect their most important relationships and business processes. From digital onboarding to fraud mitigation to workflow management, OneSpan’s unified Trusted Identity platform reduces costs, accelerates customer acquisition, and increases customer satisfaction.

To find out more, click [here](https://www.onespan.com/).

***

## Contact

**Contact**

**Enquiry Email Address**

* <info@onespan.com>

**Singapore Hotline**

* +65 6323 0906


# Tessaract Technologies Pte Ltd

## **About Tessaract Technologies Pte Ltd**

Tessaract.io is an all-in-one enterprise management system for professionals built on a cloud-native architecture, readily accessible on all smart devices. Tessaract.io keeps track of workflows, schedules and billings from initial execution to eventual completion. Tessaract.io's automation features include one-click workflow generation, automated document creation and digital signing, client engagement and notifications, and an integrated full-fledge accounting software that allows for e-invoicing.

To find out more, click [here](https://tessaract.io/).

***

## **Contact**

**Cherilyn**

* <cherilyn@tessaract.io> +65 8692 0222


# Netrust Pte Ltd

## **About Netrust Pte Ltd**

Established in 1997, Netrust is Asia’s first public Certification Authority (CA) and Singapore's first IMDA-accredited CA since 2001 which provides individuals, business and government organizations with a complete online identification and security infrastructure to enable secure electronic transactions. Netrust also delivers professional services including security consulting, PKI deployment and custom application development.

Netrust issues digital certificates for online applications including secure access to government applications, Internet banking, supply chain management, virtual private networks and secure access to intranet portals. Parties can rely on Netrust certificates for evidentiary presumption and users are assured of the legality and security of their transactions.

To find out more, click [here](https://www.netrust.net/).

***

## **Contact**

**Enquiry Email Address**

* <infoline@netrust.net>

**Singapore Hotline**

* +65 6212 1388


# Modus Consulting

## About Modus Consulting

Modus Consulting enables organisations to develop digital document frameworks and orchestrations, starting with intelligent data capture via "Dynamic Interactive PDFs" to back-office submission and orchestrations. NDISign enables a fully digital document workflow. With no printing and wet signing required, organisations can realise the true value of the fully digital document workflow.

This on-premise solution allows for customised branding of the experience interface with a platform-agnostic approach and the most straightforward signing ceremony with only two clicks on the interface - one for selecting the document and one for getting it back.

To find out more, click [here](https://www.modus.sg/).

***

## **Contact**

**Enquiry Email Address**

* <info@modus.sg>

**Singapore Hotline**

* +65 6673-9853


# Redoc.co by Real Estate Doc Pte Ltd.

## **About Redoc.co by Real Estate Doc Pte Ltd.**

Redoc.co, by Real Estate Doc, is the cloud-based Revenue and Contract Management software for Sales-Driven and Real Estate Businesses.

Designed and developed for Salespersons and Sales-driven organisations, Redoc.co digitalises and automates workflow, converting deals faster from quotation to closure.

To find out more, click [here](https://redoc.co/).

***

**Contact**

**Enquiry Email Address**

* <enquiries@realestatedoc.co>
* <ivan.lim@realestatedoc.co>
* <eugene.lee@realestatedoc.co>

**Hotline**

* +65 9180 1197


# CrimsonLogic

## **About CrimsonLogic**

For more than 30 years, we have partnered with governments across the world. Together as their trusted partner, we deliver value to citizens and businesses through sustainable Digital Transformation.

To find out more, click [here](https://www.crimsonlogic.com/).

***

## **Contact**

**Enquiry Email Address**

* <sales@crimsonlogic.com>

**Singapore Hotline**

* (65) 6887 7888


# Zoho Sign

## About Zoho Sign

Zoho Sign is a complete digital signature app for business signatories. It helps organisations to sign, send, and manage documents from anywhere and at anytime.

Say goodbye to the traditional method of signing documents with pen and paper. With Zoho Sign, you can reduce the document turnaround time, save costs on printing and mailing, and automate mundane tasks.

Zoho Sign readily integrates with more than 50+ popular apps, including Zoho CRM, Dropbox, HubSpot, Microsoft Teams, Google Workplace, and much more. In addition, our powerful APIs and mobile SDKs help businesses to connect Zoho Sign with their existing in-house applications.

Sign paperless and go green with Zoho Sign.

To find out more, click [here](https://www.zoho.com/sign).

***

## **Contact**

**Enquiry Email Address**

* <support@zohosign.com>

**Singapore Hotline**

* +65 6723 1040

**US Hotline**

* +1 877 834 4428


# Securemetric Technology Pte. Ltd.

## **About Securemetric Technology Pte. Ltd.**

SigningCloud is a SaaS based digital signature solution for you to sign, assign & manage documents signature in one place. We have simplified the document signing process by automating your document delivery. SigningCloud tracks progress by checking each signer’s status. Notifications and reminders will be sent to related parties to keep everyone on the same page. You’ll be able to spend less time tracking down signatures and devote more time to other mission-critical tasks. SigningCloud uses state-of-the-art cryptography algorithms to ensure confidentiality and integrity of all signed documents.

To find out more, click [here](https://www.signingcloud.com/).

***

## Contact

**Enquiry Email Address**

* <helpdesk@signingcloud.com>


# Rently Pte. Ltd.

## **About Rently Pte. Ltd.**

Rently is the new revolutionary mobile application that digitalises the entire property renting process and it is now integrated with Sign with Singpass. Rently is the safest and fastest way to draft and sign rental contracts. It helps tenants, landlords and real estate agents save time and streamline communication beyond contract signature. Rently believes that technology can break the hassle of renting properties and bring a new paperless and scam-free experience for everyone.

To find out more, click [here](https://www.rently.sg/).

***

## **Contact**

Enquiry Email Address

* <support@rently.sg>


# Support

## Enquiries

If you have any questions or encounter any issues, please don’t hesitate to raise a support ticket at <https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new>

## Feedback

Have feedback or a feature request? Let us know at <https://go.gov.sg/sign-feedback>


# Guiding Principles

## <mark style="color:red;">What you see is what you sign</mark>

* As a trusted partner of Sign with Singpass, you should always ensure that the user gets to see what they sign before they proceed to sign the document.
* You should never use this system to misrepresent intended documents which your user plans to sign.

## <mark style="color:red;">PDPA & Applicable Regulations</mark>

* Protect, retain and transfer data retrieved according to the Personal Data Protection Act (PDPA), relevant industry regulations and applicable legislation.

## <mark style="color:red;">Lawful purposes</mark>

Use Sign with Singpass for lawful purposes only. Singpass reserves the right to terminate the integration if Sign with Singpass is used for any unlawful purpose.


# Quick Start

## CIBA Onboarding Guide&#x20;

### Overview

CIBA (Client-Initiated Backchannel Authentication) onboarding is currently available only to **Government agencies** and is assessed on a case-by-case basis.

### Typical CIBA Flow

For a call-centre use case:

1. A call-centre agent verifies the caller’s identity
2. The agent initiates a CIBA request via Singpass
3. A push notification is sent to the user’s Singpass app
4. The user reviews and approves the request
5. The transaction proceeds upon successful authentication

### Onboarding Steps

#### 1. Create a Staging App

Create a staging app via the Singpass Developer Portal (SDP): <https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/create-staging-app&#x20>;

Configuration:

* Select openid as the only scope
* Use dummy values for fields not applicable (e.g. Site URL, Redirect URL)
* Configure your JWKS endpoint

#### 2. Submit Use Case for Assessment

Share the following details via Partner Support:

* Description of your CIBA use case
  * When is CIBA triggered?
  * Why is CIBA required?
* Expected monthly transaction volume
* Systems that will integrate with Singpass

#### 3. Evaluation by Singpass

The Singpass Product and Security teams will assess:

* Alignment with CIBA policy
* Authentication assurance requirements
* User journey and risk controls
* Availability of fallback flows

> We may follow up with clarifications during this stage.

#### 4. Whitelisting & Testing

If the use case is approved:

* Your use case will be whitelisted
* Your team can proceed with testing in staging

#### 5. Production Setup

Once testing is complete:

1. Submit a Production App Request via SDP
2. Indicate that the app is for CIBA
3. Include your User Journey (UJ)
4. Singpass will whitelist your client ID for CIBA usage


# Step-up Authentication using Push Notifications

Client-Initiated Backchannel Authentication (CIBA)

{% hint style="warning" %}
Onboarding for CIBA is only for Government agencies and on a case-by-case basis. &#x20;
{% endhint %}

## Introduction

This guide illustrates the Step-up Authentication (Push Notifications) Flow and the APIs that Relying Parties (RP) need to integrate with.

The Step-up authentication feature can be employed in use-cases where RPs require their users to perform an additional layer of authentication before proceeding on with a **high-risk transaction**. This kind of authentication is done by triggering a push notification to the user’s Singpass Mobile Application.

RPs who are looking to opt-in for Step-up Authentication are required to integrate with Singpass operating in the **Client-initiated Backchannel Authentication (CIBA) Poll Mode** (see [CIBA specs](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html#rfc.section.7)). Refer to this diagram for an overview of the CIBA authentication flow between an RP, Singpass and its dependencies.

<figure><img src="https://4204905545-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FE7FCbKTvZEx7uI8INZXT%2Fuploads%2FAjF2OPRhkzjBzKHje75F%2Fimage.png?alt=media&amp;token=994c3461-0d5d-463e-9f59-c4d87a2e8bf5" alt=""><figcaption><p>CIBA Authentication Flow between RP, Singpass and its dependencies</p></figcaption></figure>


# Backchannel Authentication Endpoint

As mentioned previously, the Step-up Authentication (Push Notifications) flow is implemented over the CIBA Poll mode flow.

This endpoint allows RPs to make an authentication request to begin a CIBA session with Singpass for a given user identifier. When initiation is successful, the RP will receive an auth session identifier which should be used for the subsequent CIBA steps.

Details about the user identifier is detailed in the `login_hint` field under the [Request Parameters](#form-parameters) section below.

## Client Authentication <a href="#client_authentication" id="client_authentication"></a>

To initiate the CIBA flow, RPs must authenticate itself with Singpass using client assertion JWT.

Refer to [this section](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/client-initiated-backchannel-authentication-ciba/step-up-authentication-using-push-notifications/token-endpoint#client-authentication-client-assertion-jwt) for the structure of assertion JWT.

## Backchannel Authentication Request and Response <a href="#backchannel_authentication_request_and_response" id="backchannel_authentication_request_and_response"></a>

### **Curl request**

```bash
$ curl 'https://stg-id.singpass.gov.sg/bc-auth' -i -X POST \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1' \
    -d 'client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJjbGllbnRJZCJ9.9STntUMUIaSSqe9fSET28n5szfM7VjD98ElfpVQtEhl5S8bnwKm2GpCsvMGhhzCifEP8uJyyjylFGhXOra2EderNpp3yrVHePlhIiB1nhVcXPYL1wng0iWJ85kk-PcZb&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&scope=openid&login_hint=178478de-fed7-4c03-a75e-e68c44d0d5f0'
```

### **Form parameters**

| Parameter               | Description                                                                                                                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_assertion`      | The jwt used for authorization                                                                                                                                |
| `client_assertion_type` | The type of grant being requested. This MUST be set to `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`                                               |
| `login_hint`            | A hint to the OpenID Provider regarding the end-user for whom authentication is being requested. Must be in upper case NRIC format or lower case UUID format. |
| `scope`                 | Supported value is `openid`.                                                                                                                                  |

### **HTTP request**

```http
POST /bc-auth HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1
Host: stg-id.singpass.gov.sg
Content-Length: 355

client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJjbGllbnRJZCJ9.9STntUMUIaSSqe9fSET28n5szfM7VjD98ElfpVQtEhl5S8bnwKm2GpCsvMGhhzCifEP8uJyyjylFGhXOra2EderNpp3yrVHePlhIiB1nhVcXPYL1wng0iWJ85kk-PcZb&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&scope=openid&login_hint=178478de-fed7-4c03-a75e-e68c44d0d5f0
```

### **HTTP response**

```http
HTTP/1.1 200 OK
Cache-Control: no-cache, no-store, must-revalidate
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Fri, 14 Feb 2025 01:38:24 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 82

{
  "auth_req_id" : "a167061f-1dfc-47a4-9537-eb7a4247619e",
  "expires_in" : 300
}
```

### **HTTPie request**

```bash
$ http --form POST 'https://stg-id.singpass.gov.sg/bc-auth' \
    'client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJjbGllbnRJZCJ9.9STntUMUIaSSqe9fSET28n5szfM7VjD98ElfpVQtEhl5S8bnwKm2GpCsvMGhhzCifEP8uJyyjylFGhXOra2EderNpp3yrVHePlhIiB1nhVcXPYL1wng0iWJ85kk-PcZb' \
    'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
    'scope=openid' \
    'login_hint=178478de-fed7-4c03-a75e-e68c44d0d5f0'
```

### **Request body**

```x-www-form-urlencoded
client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJjbGllbnRJZCJ9.9STntUMUIaSSqe9fSET28n5szfM7VjD98ElfpVQtEhl5S8bnwKm2GpCsvMGhhzCifEP8uJyyjylFGhXOra2EderNpp3yrVHePlhIiB1nhVcXPYL1wng0iWJ85kk-PcZb&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&scope=openid&login_hint=178478de-fed7-4c03-a75e-e68c44d0d5f0
```

### **Response body**

```json
{
  "auth_req_id" : "a167061f-1dfc-47a4-9537-eb7a4247619e",
  "expires_in" : 300
}
```

### **Response fields**

| Path          | Type     | Description                                                                                                                                                 |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_req_id` | `String` | ID given in the start of the OIDC CIBA flow that should be used to reference this authentication session.                                                   |
| `expires_in`  | `Number` | A JSON number with a positive integer value indicating the expiration time of the "auth\_req\_id" in seconds since the authentication request was received. |

### **Error Responses**

The table below shows the list of common error codes that may be returned for this endpoint.

| Error Code        | Description                                                                 |
| ----------------- | --------------------------------------------------------------------------- |
| `unknown_user_id` | No active valid Singpass App (mobile) user available for given login\_hint. |
| `access_denied`   | End-user is an SFA user and is not authorised to authenticate into this RP. |
| `invalid_client`  | RP failed client assertion authentication.                                  |
| `invalid_request` | Invalid request parameters.                                                 |
| `invalid_scope`   | The scope requested is not valid.                                           |


# Token Endpoint

Endpoint to obtain an ID token. The ID token is a signed JWT that contains user information in the sub claim, and is signed by Singpass Auth. RPs will be able to verify the ID token’s JWT signature with our JWKS endpoint.

For the Step-up authentication flow, only the following grant(s) is supported:

* `urn:openid:params:grant-type:ciba`

In the below sections, we are going to describe the API contract.

## Client-Initiated Backchannel Authentication (CIBA) Grant <a href="#client_initiated_backchannel_authentication_ciba_grant" id="client_initiated_backchannel_authentication_ciba_grant"></a>

This grant type allows the RP to obtain an ID token for the user indicated by the `login_hint` parameter that was provided during initiation. This is only allowed for `confidential` RPs.

Currently, Singpass only supports **Poll** mode, which means that RPs need to poll the token endpoint at regular intervals until they receive an ID token or receive certain error codes (see [Error Responses](#error-responses)).

| Important | RPs should **NOT** send two overlapping token requests with the same `auth_req_id`. RPs should always wait until receiving the response to the previous request before sending out the next request. |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Note | It is recommended for RPs to wait for at least **30s** for a response before trying again. |
| ---- | ------------------------------------------------------------------------------------------ |

### **Client Authentication - Client Assertion JWT**

RPs must authenticate themselves using **Client Assertion JWT**.

In this authentication mechanism, the RP is required to present an assertion JWT in the request body. Singpass will then verify this JWT against a JWK provided by the RP during onboarding.

This method of authentication relies on PKI and eradicates the need to keep and transfer secrets. You may refer to [this RFC spec documentation](https://tools.ietf.org/html/rfc7523#section-2.2) for more details.

#### **Assertion JWT Structure**

The RP is required to generate an assertion JWT that has the following header and claims, and is signed with the JWK that was provided during onboarding.

**JWT Header**

The header **must include `alg` and `typ`**.

The supported `alg` types are:

* `ES256`
* `ES384`
* `ES512`.

This must match the `alg` value in the signing key used to sign the assertion (if the signing JWK specifies `alg` explicitly).

The header should also include `kid` of the signing key to help identify which of the RP’s signing keys was used, though this is not mandatory. If omitted, we will test against all known signing keys when attempting to verify the signature.

example

```json
{
  "typ" : "JWT",
  "alg" : "ES256",
  "kid" : "rp_key_01"
}
```

**JWT Claims**

| Path  | Type     | Description                                                                                                                                                                                                                                                     |
| ----- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sub` | `String` | This should be `client_id` of the registered client.                                                                                                                                                                                                            |
| `aud` | `String` | The recipient that the JWT is intended for. This must match the `issuer` field in the response of the OpenID discovery endpoint (<https://id.singpass.gov.sg/.well-known/openid-configuration>). e.g. [https://id.singpass.gov.sg](https://id.singpass.gov.sg/) |
| `iss` | `String` | This should be `client_id` of the registered client.                                                                                                                                                                                                            |
| `iat` | `Number` | The time at which the JWT was issued. <https://tools.ietf.org/html/rfc7519#section-4.1.6>                                                                                                                                                                       |
| `exp` | `Number` | The expiration time on or after which the JWT MUST NOT be accepted by Singpass for processing. Additionally, Singpass will not accept tokens with an `exp` longer than 2 minutes since `iat`. <https://tools.ietf.org/html/rfc7519#section-4.1.4>               |

### **Request / Response Structure**

#### **Curl request**

```bash
$ curl 'https://stg-id.singpass.gov.sg/token' -i -X POST \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1' \
    -d 'client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&auth_req_id=9f7e4f01-45cc-4eed-84c2-f7f58233f7fa&client_assertion=eyJraWQiOiJzaWdJZCIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJpTUJ3MlhkR2VHanRYRVl4TURoT1RxUnN5a000dHRaZiIsInN1YiI6ImlNQncyWGRHZUdqdFhFWXhNRGhPVHFSc3lrTTR0dFpmIiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnIiwiZXhwIjoxNzM5NDk3MjY4LCJpYXQiOjE3Mzk0OTcxNDh9.8LhU6OSaZhZqJ90T2i6S1ay-Ir_mbw_PXOvjI49BhtR--3A2F3WgLoiNesDHFVCSzz7uv4NoiQqGWxn5C0hdWA&grant_type=urn%3Aopenid%3Aparams%3Agrant-type%3Aciba'
```

#### **Form parameters**

| Parameter               | Description                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| `auth_req_id`           | Authentication request id.                                                                  |
| `grant_type`            | The type of grant being requested. This must be set to `urn:openid:params:grant-type:ciba`. |
| `client_assertion_type` | This MUST be set to `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`                |
| `client_assertion`      | A JWT identifying the client.                                                               |

#### **HTTP request**

```http
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1
Host: stg-id.singpass.gov.sg
Content-Length: 557

client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&auth_req_id=9f7e4f01-45cc-4eed-84c2-f7f58233f7fa&client_assertion=eyJraWQiOiJzaWdJZCIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJpTUJ3MlhkR2VHanRYRVl4TURoT1RxUnN5a000dHRaZiIsInN1YiI6ImlNQncyWGRHZUdqdFhFWXhNRGhPVHFSc3lrTTR0dFpmIiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnIiwiZXhwIjoxNzM5NDk3MjY4LCJpYXQiOjE3Mzk0OTcxNDh9.8LhU6OSaZhZqJ90T2i6S1ay-Ir_mbw_PXOvjI49BhtR--3A2F3WgLoiNesDHFVCSzz7uv4NoiQqGWxn5C0hdWA&grant_type=urn%3Aopenid%3Aparams%3Agrant-type%3Aciba
```

#### **HTTP response**

```http
HTTP/1.1 200 OK
Expires: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
X-XSS-Protection: 0
Pragma: no-cache
X-Frame-Options: DENY
Date: Fri, 14 Feb 2025 01:39:09 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 446

{"token_type":"Bearer","id_token":"eyJraWQiOiJuZGlfc3RnXzAxIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJhdWQiOiJpTUJ3MlhkR2VHanRYRVl4TURoT1RxUnN5a000dHRaZiIsInN1YiI6InM9Uzg4MjkzMTRCLHU9MWMwY2VlMzgtM2E4Zi00ZjhhLTgzYmMtN2EwZTRjNTlkNmE5IiwiYW1yIjpbInB3ZCIsInN3ayJdLCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2ciLCJleHAiOjE3Mzk0OTc3NDgsImlhdCI6MTczOTQ5NzE0OH0.BxXLysNFj7TKZBydqXICOCzLzQyylt_Gde18_lSLq4ZcWNz8TY3ZGT_DXU5dWkBEJ4OSaDcEfpxpwNdd-MeEDA"}
```

#### **Request body**

```x-www-form-urlencoded
client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&auth_req_id=9f7e4f01-45cc-4eed-84c2-f7f58233f7fa&client_assertion=eyJraWQiOiJzaWdJZCIsInR5cCI6IkpXVCIsImFsZyI6IkVTMjU2In0.eyJpc3MiOiJpTUJ3MlhkR2VHanRYRVl4TURoT1RxUnN5a000dHRaZiIsInN1YiI6ImlNQncyWGRHZUdqdFhFWXhNRGhPVHFSc3lrTTR0dFpmIiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnIiwiZXhwIjoxNzM5NDk3MjY4LCJpYXQiOjE3Mzk0OTcxNDh9.8LhU6OSaZhZqJ90T2i6S1ay-Ir_mbw_PXOvjI49BhtR--3A2F3WgLoiNesDHFVCSzz7uv4NoiQqGWxn5C0hdWA&grant_type=urn%3Aopenid%3Aparams%3Agrant-type%3Aciba
```

#### **Response body**

```json
{"token_type":"Bearer","id_token":"eyJraWQiOiJuZGlfc3RnXzAxIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJhdWQiOiJpTUJ3MlhkR2VHanRYRVl4TURoT1RxUnN5a000dHRaZiIsInN1YiI6InM9Uzg4MjkzMTRCLHU9MWMwY2VlMzgtM2E4Zi00ZjhhLTgzYmMtN2EwZTRjNTlkNmE5IiwiYW1yIjpbInB3ZCIsInN3ayJdLCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2ciLCJleHAiOjE3Mzk0OTc3NDgsImlhdCI6MTczOTQ5NzE0OH0.BxXLysNFj7TKZBydqXICOCzLzQyylt_Gde18_lSLq4ZcWNz8TY3ZGT_DXU5dWkBEJ4OSaDcEfpxpwNdd-MeEDA"}
```

#### **Response fields**

| Path         | Type     | Description                                                                                                                                                                                                                                                                       |
| ------------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `token_type` | `String` | The type of token being requested, Bearer only so far.                                                                                                                                                                                                                            |
| `id_token`   | `String` | The ID token with relevant claims in JWT format signed by the ASP. Note that the example response body shows a JWS (3-part structure separated by dots), but the format will differ for a JWS in JWE (5-part structure). See below for more details about the ID token structure. |

#### **Error Responses**

The table below shows the list of common error codes that may be returned for this endpoint. RPs must take note to only re-poll the token endpoint for scenarios as specified below.

| Important | Note that only the `error` field in the JSON response should be used to determine the error scenario. Do NOT use the `error_description` field to determine the error scenario. Singpass reserves the right to change the content of the `error_description` field without prior notice to RPs. |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

| Error code (returned in `error` field) | Error scenario                                                          | Can perform re-poll? |
| -------------------------------------- | ----------------------------------------------------------------------- | -------------------- |
| `authorization_pending`                | The session is still pending as the end-user has not authenticated yet. | **Yes**              |
| `access_denied`                        | End-user rejected the authentication via SP mobile app.                 | No                   |
| `expired_token`                        | The authentication session has expired or is not found.                 | No                   |
| `unauthorized_client`                  | RP is not authorized to perform this flow.                              | No                   |
| `invalid_client`                       | RP failed client assertion authentication.                              | No                   |
| `invalid_grant`                        | -                                                                       | No                   |
| `invalid_request`                      | -                                                                       | No                   |
| `server_error`                         | -                                                                       | No                   |

### **ID Token Structure**

The format and structure of the issued ID Token will vary depending on the client’s profile as specified in this table below:

| Client Profile                            | `sub` Claim Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | ID token format                                                                                                |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `direct`                                  | UUID only (eg. `u=32af8b7d-ad1d-4c25-8dc7-0a981b533000`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | JWS                                                                                                            |
| `direct_pii_allowed`                      | <p><strong>Regular NRIC holders</strong>: NRIC and UUID (eg. <code>s=S1234567A,u=32af8b7d-ad1d-4c25-8dc7-0a981b533000</code>)<br></p><p><strong>Singpass Foreign Account (SFA) holders</strong>: Singpass User ID (UID), Foreigner ID (FID), Country-of-Issuance (COI) and UUID (eg. <code>s=Y7613265T,fid=G730Z-H5P96,coi=DE,u=e2af740e-25b4-4b19-b527-494670952cb0</code>)<br></p><p>This class of users were previously known as "Foreign Unique Account" or "Singpass Foreign Unique Account" users. Only designated relying parties are able to have SFA users authenticate & complete token exchange.</p> | <p>JWS in JWE (encrypted with client’s JWK)</p><p>See section below for more details about the JWE format.</p> |
| `bridge` (special case internal use only) | NRIC and UUID (eg. `s=S1234567A,u=32af8b7d-ad1d-4c25-8dc7-0a981b533000`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | JWS                                                                                                            |

#### **Overview of a JWS in JWE**

An encrypted ID token will returned from the `/token` endpoint is a JWS in JWE that is in compact serialization form. It has the following structure:

* JWE Header
* Encrypted Key
* Initialization Vector
* Encrypted Payload (if decrypted, this would be the Base64 encoded form of a [JWS ID Token](#overview-of-a-jws))
* Authentication Tag

See <https://datatracker.ietf.org/doc/html/rfc7516#section-3.1> for more details.

**JWE Header**

The JWE will contain these standard headers. Refer to <https://tools.ietf.org/html/rfc7515#section-4> for more information about each header.

Note: Relying parties should use the `kid` field in the header to determine which key Singpass used for encryption.

example

```json
{
	"kid": "client_01",
	"cty": "JWT",
	"enc": "A256CBC-HS512",
	"alg": "ECDH-ES+A256KW"
}
```

#### **Overview of a JWS**

The [JWS](https://tools.ietf.org/html/rfc7515) ID token returned from the `/token` endpoint is in compact serialization form. A JWS has the following structure.

* JWS Header
* Payload (containing claims)
* Signature

**JWS Header**

The JWS ID token will contain these standard headers. Refer to <https://tools.ietf.org/html/rfc7515#section-4> for more information about each header.

example

```json
{
  "kid" : "ndi_stg_01",
  "typ" : "JWT",
  "alg" : "ES256"
}
```

**JWT Claims**

The JWS ID token will contain the following claims.

example

```json
{
  "aud" : "iMBw2XdGeGjtXEYxMDhOTqRsykM4ttZf",
  "sub" : "s=S8829314B,u=1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9",
  "amr" : [ "pwd", "swk" ],
  "iss" : "https://stg-id.singpass.gov.sg",
  "exp" : 1739497748,
  "iat" : 1739497148
}
```

| Path  | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sub` | `String` | The principal that is the subject of the JWT. Contains a comma-separated, key=value mapping that identifies the user; possibly including multiple alternate IDs representing the user. The keys included vary by the profile of the OIDC client, and the user type, however the minimal format is `u=<UUID>` where UUID represents the user’s globally unique identifier. <https://tools.ietf.org/html/rfc7519#section-4.1.2> |
| `aud` | `String` | The client\_id of the relying party. <https://tools.ietf.org/html/rfc7519#section-4.1.3>                                                                                                                                                                                                                                                                                                                                      |
| `iss` | `String` | The principal that issued the JWT. <https://tools.ietf.org/html/rfc7519#section-4.1.1>                                                                                                                                                                                                                                                                                                                                        |
| `iat` | `Number` | The time at which the JWT was issued. <https://tools.ietf.org/html/rfc7519#section-4.1.6>                                                                                                                                                                                                                                                                                                                                     |
| `exp` | `Number` | The expiration time on or after which the JWT MUST NOT be accepted for processing. Defaults to 10 minutes since "iat". <https://tools.ietf.org/html/rfc7519#section-4.1.4>                                                                                                                                                                                                                                                    |
| `amr` | `Array`  | Authentication method references. Example values are `["face"]`, `["fv"]`, `["fv-alt"]`, `["otp"]`, `["pwd","fv"]`, `["pwd","otp-email"]`, `["pwd","sms"]`, `["pwd","swk"]`, `["pwd"]`, `["sso"]`. Note that this list is non-exhaustive, and Singpass reserves the right to introduce new values without prior notice to RPs.                                                                                                |

## Client JWK Requirements <a href="#client_jwk_requirements" id="client_jwk_requirements"></a>

Clients are expected to provide public keys to Singpass in the [JWK](https://tools.ietf.org/html/rfc7517) format. These public keys will be used in the following (non-exhaustive) scenarios:

* Signature JWK used to verify the signature of the [client assertion JWT](#client-authentication-client-assertion-jwt) presented during token request.
* Encryption JWK used to [encrypt an ID token](#id-token-structure) which contains the user’s PII.

The client must provide the public key(s) during onboarding, and they can do so only via **ONE** of the following forms:

* Provide a JWKS in a JSON format.
* Host the JWKS on a publicly accessible URL. This endpoint must be compatible with Singpass' [service level expectations](#jwks-url-service-level-expectations).

Signing key is always required for both `direct` and `direct_pii_allowed` clients. Encryption key is only required for `direct_pii_allowed` clients. `direct_pii_allowed` clients must ensure that the provided JWKS or the resource returned by the JWKS URL contains both the signing and encryption keys.

| Tip | [mkjwk.org](https://mkjwk.org/) is a useful open-source tool to generate different types of JWK for signing and encryption; compliant with Singpass' broad requirements on structure. While we **DO NOT** suggest this as a secure way to generate your *real* keypair (including private key); this can be a useful tool to understand how JWK works; and how it is represented for signing and encryption purposes; while you are reviewing against our supported algorithms below. |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### **JWK for signing**

The signing JWK will be used to verify the [client assertion JWT](#client-authentication-client-assertion-jwt) provided during `/token` request, thereby authenticating the client.

Clients are allowed to provide multiple signature keys in the JWKS / hosted on the JWKS url provided during client creation.

The signature JWK should have the following attributes:

* Must have key `use` of value `sig` per [rfc7517#section-4.2](https://tools.ietf.org/html/rfc7517#section-4.2)
* Must contain a key ID in the standard `kid` field per [rfc7517#section-4.5](https://tools.ietf.org/html/rfc7517#section-4.5)
  * Will be used by Singpass to select the relevant key to verify the client assertion
* Must be an EC key, with curves: `P-256`, `P-384` or `P-521` *(NIST curves, aka `secp256r1`, `secp384r1`, `secp521r1` respectively)*

Example EC signing key using P-256 and a timestamped key Id

```json
{
    "kty": "EC",
    "use": "sig",
    "kid": "sig-2021-01-15T12:09:06Z",
    "crv": "P-256",
    "x": "Tjm2thouQXSUJSrKDyMfVGe6ZQRWqCr0UgeSbNKiNi8",
    "y": "8BuGGu519a5xczbArHq1_iVJjGGBSlV5m_FGBJmiFtE"
}
```

#### **Key Rotation**

Relying parties can **rotate** their signing keys in a self-driven manner. To do this with **zero downtime** the Relying party must

* support use of **JWKS URLs** and be onboarded as such
* ensure their replacement signing key has a different key ID (`kid`) to the original key
* ensure their replacement signing key matches the other cryptographic key requirements

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                 |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new signing key pair (`K2`) supported for signing.                                                           |
| T0            | Relying party **adds** public key `K2` to its JWKS endpoint (and leaves `K1` on the endpoint)                                          |
| T0 - T+1 hour | Singpass' cache will expire, and re-retrieves the relying party’s published keys from their JWKS endpoint which now includes `K2`      |
| > T+1 hour    | Relying party changes their system to start signing client assertions using the new signing key `K2`                                   |
| Clean Up      | Post-validation, relying party can remove key `K1` from their JWKS endpoint when they are comfortable their new signing key is working |

### **JWK for encryption**

The encryption JWK will be used to [encrypt ID tokens](#id-token-structure) requested from the `/token` endpoint.

Singpass will select the strongest available, supported encryption key from either a **local JWKS**, or **JWKS URL** to encrypt returned ID tokens for those relying parties who require any PII in the ID token.

The encryption JWK must have the following attributes:

* Must have key `use` of value `enc` per [rfc7517#section-4.2](https://tools.ietf.org/html/rfc7517#section-4.2)
* Must contain a key ID in the standard `kid` field per [rfc7517#section-4.5](https://tools.ietf.org/html/rfc7517#section-4.5)
  * The key ID will be specified in the returned JWE header so that clients can pick the right key for decryption
* Must have key type (`kty`) of `EC`
* Must specify the appropriate key encryption `alg` the relying party wants Singpass to use, consistent with the key type/curve (`kty`), and meet the requirements below on allowed `alg`/`curve`/key sizes, consistent with [RFC7518 - JSON Web Algorithm specification](https://tools.ietf.org/html/rfc7518#section-4.1)

| Key Type (`kty`)                 | EC                                                                                                                          |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Status                           | **Required** for new Relying Parties                                                                                        |
| Key encryption algorithm (`alg`) | <p>ECDH-ES+A128KW<br>ECDH-ES+A192KW<br>ECDH-ES+A256KW</p>                                                                   |
| Curve (`crv`)                    | <p>P-256 <em>(NIST, aka secp256r1)</em><br>P-384 <em>(NIST, aka secp384r1)</em><br>P-521 <em>(NIST, aka secp521r1)</em></p> |

Example EC encryption key using P-256 and a timestamped key Id; asking us to encrypt the CEK using ECDH-ES+A128KW

```json
{
    "kty": "EC",
    "use": "enc",
    "kid": "enc-2021-01-15T12:09:06Z",
    "crv": "P-256",
    "x": "xom6kD54yfXRPvMFVYFlVjUKzmNhz7wf0DP_2h9kXtY",
    "y": "lrh8C9c8-SBJTm1FcfqLkj2AnHtaxpnB1qsN6PiFFJE",
    "alg": "ECDH-ES+A128KW"
}
```

#### **Key Preference**

If the relying party exposes *multiple supported encryption keys*, Singpass will select the key to use for encrypting tokens based on the following logic:

1. prefer any EC key (`kty`) matching the above requirements
2. prefer EC keys with stronger `crv` (curve) *above* EC keys with weaker curve
3. prefer EC keys with stronger `alg` key wrapping *above* weaker ones
4. otherwise pick the first compatible key we find

#### **Key Rotation**

Relying parties can **rotate** their encryption keys in a self-driven manner. To do this with **zero downtime** the Relying party must

* support use of **JWKS URLs** and be onboarded as such
* have the ability to decrypt tokens produced with either **one of two** different encryption keys based on either
  * selecting the correct decryption key by its key ID (`kid`)
  * trial-and-error decryption against multiple keys in a collection
* ensure their replacement key matches the other cryptographic key requirements noted above

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                                         |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new encryption key pair (`K2`) supported for decryption. The existing key pair (`K1`) is still available for decryption of ID tokens |
| T0            | Relying party **removes** public key `K1` and **adds** public key `K2` on its JWKS endpoint                                                                    |
| T0 - T+1 hour | Singpass' caches will expire at any (indeterminate) time within this period, and start encrypting tokens with new encryption key `K2`.                         |
| T0 - T+1 hour | Relying party may be receiving tokens encrypted with either `K1` or `K2` keys throughout this period; and must be able to decrypt either.                      |
| > T+1 hour    | Relying party can remove support for decrypting with the previous `K1` key                                                                                     |

### **JWKS URL Service Level Expectations**

Singpass requires that any JWKS is published on an endpoint that

* is served behind HTTPS on port `443` using a TLS server certificate issued by a standard *publicly verifiable CA issuer* (no private CAs), with *complete cert chain* presented by the server
* is publicly accessible (no IP whitelisting, mTLS or other custom HTTP header requirements outside standard HTTP headers such as `Content-Type`, `Accept`)
* is able to respond in a timely fashion with respect to the below configuration

| Per try timeout                   | 3s |
| --------------------------------- | -- |
| Max attempts                      | 3  |
| Cache duration for retrieved JWKS | 1h |

| Note | While the above is a technical requirement; the user experience of your users may be affected if we are unable to retrieve your JWKS in a timely fashion upon our cache expiry due to slower token exchanges with your backend. We recommend aiming for this response to be as fast as possible based on an in-memory cache; or simple static asset retrieval. |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

If Singpass fails to retrieve a valid JWKS from the provided URL after cache expiry, the relying party’s token exchange will fail with an OAuth2/OIDC `invalid_client` error in these circumstances:

* if *client assertions* are used, and we are unable to validate the relying party’s assertion using their signing key
* if *encryption of returned ID tokens* is required, and we are unable to retrieve the relying party’s preferred encryption key


# .well-known Endpoints

## OpenID discovery endpoint <a href="#openid_discovery_endpoint" id="openid_discovery_endpoint"></a>

Responses from this endpoint can and should be cached for at least 1 hour, and NOT retrieved for each OIDC/OAuth2 operation. Cache-Control headers on the response indicate a possible policy.

### **Curl request**

```bash
$ curl 'https://stg-id.singpass.gov.sg/.well-known/openid-configuration' -i -X GET \
    -H 'Accept: application/json'
```

### **HTTP request**

```http
GET /.well-known/openid-configuration HTTP/1.1
Accept: application/json
Host: stg-id.singpass.gov.sg
```

### **HTTP response**

```http
HTTP/1.1 200 OK
Cache-Control: max-age=21600, must-revalidate, no-transform, public
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Fri, 14 Feb 2025 01:38:28 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 1349

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
  "userinfo_endpoint" : "https://stg-id.singpass.gov.sg/userinfo",
  "userinfo_signing_alg_values_supported" : [ "ES256" ],
  "userinfo_encryption_alg_values_supported" : [ "ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW" ],
  "userinfo_encryption_enc_values_supported" : [ "A256GCM" ]
}
```

### **HTTPie request**

```bash
$ http GET 'https://stg-id.singpass.gov.sg/.well-known/openid-configuration' \
    'Accept:application/json'
```

### **Request body**

```none
```

### **Response body**

```json
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
  "userinfo_endpoint" : "https://stg-id.singpass.gov.sg/userinfo",
  "userinfo_signing_alg_values_supported" : [ "ES256" ],
  "userinfo_encryption_alg_values_supported" : [ "ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW" ],
  "userinfo_encryption_enc_values_supported" : [ "A256GCM" ]
}
```

### **Response fields**

| Path                                               | Type     | Description                                                                                                                                                                                                                                 |
| -------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `issuer`                                           | `String` | URL (identity) of the issuer                                                                                                                                                                                                                |
| `authorization_endpoint`                           | `String` | URL of the OP’s OAuth 2.0 Authorization Endpoint                                                                                                                                                                                            |
| `jwks_uri`                                         | `String` | URL of the OP’s JSON Web Key Set                                                                                                                                                                                                            |
| `response_types_supported`                         | `Array`  | JSON array containing a list of the OAuth 2.0 response\_type values that OP supports                                                                                                                                                        |
| `scopes_supported`                                 | `Array`  | JSON array containing a list of the OAuth 2.0 scope values that OP supports                                                                                                                                                                 |
| `subject_types_supported`                          | `Array`  | JSON array containing a list of the Subject Identifier types that this OP supports                                                                                                                                                          |
| `claims_supported`                                 | `Array`  | JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for                                                                                                                     |
| `grant_types_supported`                            | `Array`  | JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports.                                                                                                                                                      |
| `token_endpoint`                                   | `String` | URL of the OP’s OAuth 2.0 Token Endpoint. This contains the signing key(s) the RP uses to validate signatures from the OP.                                                                                                                  |
| `token_endpoint_auth_methods_supported`            | `Array`  | JSON array containing a list of Client Authentication methods supported by this Token Endpoint.                                                                                                                                             |
| `token_endpoint_auth_signing_alg_values_supported` | `Array`  | JSON array containing a list of the JWS signing algorithms (alg values) supported by the Token Endpoint for the signature on the JWT used to authenticate the Client at the Token Endpoint for the private\_key\_jwt authentication methods |
| `id_token_signing_alg_values_supported`            | `Array`  | JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                                 |
| `id_token_encryption_alg_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                              |
| `id_token_encryption_enc_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (enc values) supported by the OP for the ID Token to encode the Claims in a JWT.                                                                                              |
| `backchannel_token_delivery_modes_supported`       | `Array`  | JSON array containing supported backchannel delivery modes                                                                                                                                                                                  |
| `backchannel_authentication_endpoint`              | `String` | URL of the OP’s Backchannel Authentication Endpoint                                                                                                                                                                                         |
| `userinfo_endpoint`                                | `String` | URL of the OP’s UserInfo Endpoint                                                                                                                                                                                                           |
| `userinfo_signing_alg_values_supported`            | `Array`  | JSON array containing a list of the JWS signing algorithms (alg values) supported by the UserInfo Endpoint to encode the Claims in a JWT.                                                                                                   |
| `userinfo_encryption_alg_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (alg values) supported by the UserInfo Endpoint to encode the Claims in a JWT.                                                                                                |
| `userinfo_encryption_enc_values_supported`         | `Array`  | JSON array containing a list of the JWE encryption algorithms (enc values) supported by the UserInfo Endpoint to encode the Claims in a JWT.                                                                                                |

## JWKS endpoint <a href="#jwks_endpoint" id="jwks_endpoint"></a>

NDI signs all JWTs issued during the authentication process using its ASP signing key. Integrating parties can validate the JWT signatures by acquiring the signing public key from a **JSON Web Key Set (JWKS)** endpoint.

This endpoint will return one or more public keys in [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) form. The correct JWK to use for signature validation will have its `use` attribute as `sig` (to indicate that it is a signing key), and its `kid` value should match the one found in the JWT under validation.

Public keys returned from this endpoint could be in random sequence or rotated for security enhancement. For more information, please refer to [Caching and key rotation](#caching-and-key-rotation) section.

### **Curl request**

```bash
$ curl 'https://stg-id.singpass.gov.sg/.well-known/keys' -i -X GET \
    -H 'Accept: application/json'
```

### **HTTP request**

```http
GET /.well-known/keys HTTP/1.1
Accept: application/json
Host: stg-id.singpass.gov.sg
```

### **HTTP response**

```http
HTTP/1.1 200 OK
Cache-Control: max-age=21600, must-revalidate, no-transform, public
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Fri, 14 Feb 2025 01:38:28 GMT
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
    "kid" : "eckey-test",
    "x" : "Nf4-Nc2_hC5pg1Pr274P6YN1cZNZHZRUm8sccBYQBFU",
    "y" : "I2whYvPaxHocMfJ5ob67Ow9uk_TksTCQQ_x-DN9oMeo"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "eckey-test-secondary",
    "x" : "qfdyc_f2hxS_4-76Z9WH9itB_S49Q3vsoJTxOBJpXmQ",
    "y" : "gSdCGVcqx4_l8hgKh_nJAOn2F52tDKyvQPLfDZoi1bI"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "alias/test-sp-auth-api-id-token-signing-key-kms-asymmetric-key-alias",
    "x" : "1TsrYH0vsifCBY2ZzeXHm-e53jndsoRzaiBRuAyMd8o",
    "y" : "sdMKEjilloz3eUH8dBI_d_gF07TSJzhr3tYa_qLdLqw"
  } ]
}
```

### **HTTPie request**

```bash
$ http GET 'https://stg-id.singpass.gov.sg/.well-known/keys' \
    'Accept:application/json'
```

### **Request body**

```none
```

### **Response body**

```json
{
  "keys" : [ {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "eckey-test",
    "x" : "Nf4-Nc2_hC5pg1Pr274P6YN1cZNZHZRUm8sccBYQBFU",
    "y" : "I2whYvPaxHocMfJ5ob67Ow9uk_TksTCQQ_x-DN9oMeo"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "eckey-test-secondary",
    "x" : "qfdyc_f2hxS_4-76Z9WH9itB_S49Q3vsoJTxOBJpXmQ",
    "y" : "gSdCGVcqx4_l8hgKh_nJAOn2F52tDKyvQPLfDZoi1bI"
  }, {
    "kty" : "EC",
    "use" : "sig",
    "crv" : "P-256",
    "kid" : "alias/test-sp-auth-api-id-token-signing-key-kms-asymmetric-key-alias",
    "x" : "1TsrYH0vsifCBY2ZzeXHm-e53jndsoRzaiBRuAyMd8o",
    "y" : "sdMKEjilloz3eUH8dBI_d_gF07TSJzhr3tYa_qLdLqw"
  } ]
}
```

### **Caching and key rotation**

| Important | Responses from this endpoint, or individual keys from inside the JWKS can and should be cached for at least 1 hour, and NOT retrieved for each JWT validation. Cache-Control headers on the response indicate a possible policy. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For varying reasons, keys used for signing can and will be rotated/changed with no defined schedule, and at the full discretion of NDI. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different `kid` value. The new `kid` value will be reflected in all the new JWTs signed by NDI. In such cases, cached copies of NDI public keys must be refreshed by re-invoking the JWKS endpoint.

If the validation of the NDI signature fails, re-fetch from the JWKS endpoint once for that validation.

Please read through the list of **DON’Ts** below:

* Do not assume the position of a signing key among the list of the returned keys.
* Do not validate NDI signatures using a hardcoded public key OR `kid`. Always determine the correct key (for signature verification) by inspecting the `kid` from the JWS header, and use it to retrieve the public key from our JWKS endpoint.
* Do not cache only 1 key. Caching should be done for the entire JWKS.


# Staging and Production Endpoints

| Endpoint                                                                                                                              | Access Mechanism                | Staging                                           | Production                                    |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------- | --------------------------------------------- |
| [Backchannel Authentication Endpoint](https://stg-id.singpass.gov.sg/docs/step-up-auth-ciba/api#_backchannel_authentication_endpoint) | Public TLS w/ Client Assertions | <https://stg-id.singpass.gov.sg/bc-auth>          | <https://id.singpass.gov.sg/bc-auth>          |
| [Token Endpoint](https://stg-id.singpass.gov.sg/docs/step-up-auth-ciba/api#_token_endpoint)                                           | Public TLS w/ Client Assertions | <https://stg-id.singpass.gov.sg/token>            | <https://id.singpass.gov.sg/token>            |
| [JWKS endpoint](https://stg-id.singpass.gov.sg/docs/step-up-auth-ciba/api#_jwks_endpoint)                                             | Public TLS                      | <https://stg-id.singpass.gov.sg/.well-known/keys> | <https://id.singpass.gov.sg/.well-known/keys> |

{% hint style="danger" %}
RPs must not do "cert pinning" or create any form of dependency to the TLS certificates of the above domains. Singpass reserves the right to rotate its TLS certificates without prior notice to RPs.
{% endhint %}


# Error Response

Singpass APIs are RESTful in design and communicate classes of errors based on the **HTTP status code**. The status code should be used to determine if the error is caused by consumer or provider. Consumers should log the HTTP status code along with the `id` and/or `trace_id` of the error.

Example: Invalid Request Parameters

```http
HTTP/1.1 400 Bad Request
Connection: keep-alive
Cache-Control: no-cache, no-store, must-revalidate
Transfer-Encoding: chunked
Content-Type: application/json
Date: Fri, 14 Feb 2025 01:37:57 GMT
Content-Length: 190

{
  "id" : "bcba4bc3-534e-4891-bfa2-e872b4502d80",
  "error" : "CLIENT_SIDE_ERROR",
  "error_description" : "This is an invalid request.",
  "trace_id" : "67ae9e7585c905b608ca205f42270eff"
}
```

Example: Server Error

```http
HTTP/1.1 500 Internal Server Error
Cache-Control: no-cache, no-store, must-revalidate
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Fri, 14 Feb 2025 01:37:57 GMT
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
  "trace_id" : "67ae9e75bce5bd9bef0c2a4128d71c7f"
}
```

| Path                | Type                             | Description                                                                                                                                                                                                                                                                                               |
| ------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                | `String`                         | The unique identifier for this error/request. Please log this identifier for support and debugging purposes.                                                                                                                                                                                              |
| `trace_id`          | `String InstanceOfAssertFactory` | (Optional) An auxiliary id for request correlation across services. Please also log this identifier for operational support and debugging purposes.                                                                                                                                                       |
| `error`             | `String`                         | Error code representing broad class of error; likely to be one of CLIENT\_SIDE\_ERROR, ARGUMENTS\_NOT\_VALID, SERVER\_SIDE\_ERROR, TOO\_MANY\_REQUESTS. However, specific error codes can be returned for some endpoints, in which case you may find more details in the documentation for that endpoint. |
| `error_description` | `String`                         | Returns human readable general information about the reason for the error. Note that due to security reasons; detailed information is unlikely to be available in this message.                                                                                                                           |


# Legacy Myinfo v3/v4

{% hint style="danger" %}
Onboarding for Myinfo v3/v4 is discontinued. Please use [new Singpass](https://docs.developer.singpass.gov.sg/docs/)
{% endhint %}

Myinfo enables citizens and residents to manage the use of their personal data for simpler online transactions.All Singpass users are automatically provisioned with a Myinfo profile. Users are able to view their personal data and access records of past usage via the [Singpass app](https://app.singpass.gov.sg/).<br>

{% embed url="<https://www.youtube.com/watch?v=NGj3XXU-HgE>" %}

## How Myinfo API can enhance your digital service

**Less form filling, higher data quality**

* Users can share their data by providing consent via Singpass and organisations no longer have to deal with manual data management.

**Data from government sources**

* With data from participating government sources, this allows the provisioning of products instantly, where applicable.


# Data Catalog

Please see link to see latest data catalog for both private sector and public agencies.

{% content-ref url="/spaces/W3T7d7fy7OGYkZf4zVKU/pages/vd0uuoOUB5jVH8E4M53Z" %}
[Data Catalog (Myinfo)](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/understanding-the-data)
{% endcontent-ref %}


# Key Principles

Please see link to see [latest key principles](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo/key-principles) for both private sector and public agencies.[<br>](https://app.gitbook.com/o/oIOKcTCZC2fptOuInlww/s/k67iNluSpweCPqhbIY5t/)


# Myinfo v4

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FTE0gPPvxZel3w6eu16nQ%2Fimage.png?alt=media&amp;token=f2999415-bfd2-4d5f-a164-ffa4ef5fe003" alt=""><figcaption><p>Logical overview of Myinfo v4</p></figcaption></figure>

Integrating with Myinfo requires your application to invoke 3 different APIs as part of the OAuth2.1 authorization code flow:

## **1. Authorize API**

This API triggers the Singpass authentication process, followed by presenting a consent page to the user to obtain explicit consent from the user to allow his/her personal details to be released to your application.

Our system will return a short-lived "authorization code(authcode)" at the end of this process.

{% hint style="info" %}
This API is triggered over the browser via the 302 redirect.
{% endhint %}

***

## **2. Token API**

Your application server invokes this API to obtain an access\_token, which can be used to call the /person API for the actual data. Your application needs to provide a valid authorization code(authcode) from the /authorize API in exchange for the access\_token.

The access\_token will be valid for 30 minutes.

{% hint style="info" %}
This API is a server-to-server call (does not go through the browser)
{% endhint %}

***

## **3. Person API**

This API returns a JSON response with the personal data that was requested. Your application must provide a valid access\_token from the /token API in exchange for the person data.

Once your application receives the person data, you can use this data to populate the online form on your application.

{% hint style="info" %}
This API is a server-to-server call (does not go through the browser)
{% endhint %}

![](https://api.singpass.gov.sg/assets/api-lib/myinfo/img/v4/myinfo-v4-flow.png)


# Difference between v3 and v4

The diagram below highlights the end to end flow of v4 APIs with key changes:\
\
![](https://api.singpass.gov.sg/assets/api-lib/myinfo/img/v4/myinfo-v4-flow.png)

Myinfo v4 APIs bring about improved security posture, standards and features.

For the comprehensive list of changes, refer to our [API Specs Release notes](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html).

| v3                            | v4                                                                                                                          | Justification                                                                                                                        |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| -                             | Proof of Key Code Exchange (PKCE) (Reference : [PKCE](https://api.singpass.gov.sg/library/myinfo/developers/pkce))          | Improve security posture between /authorize and /token by protecting against authcode injection                                      |
| X.509 Certificate public keys | JSON Web Key Store (JWKS) (Reference : [JWKS](https://api.singpass.gov.sg/library/myinfo/developers/jwks))                  | Enable minimal disruption on key rotations                                                                                           |
| PKI Base string signing       | Client Assertions (Reference : [Client Assertions](https://api.singpass.gov.sg/library/myinfo/developers/clientassertion))  | Alignment to international standards                                                                                                 |
| -                             | Demonstration of Proof-of-Possesion (DPoP) (Reference : [DPoP](https://api.singpass.gov.sg/library/myinfo/developers/dpop)) | Improve security posture between /token and /person by proving legitimacy of possession for access token before data can be released |


# Technical Guidelines

## 1. Transaction Log

Digital services which have integrated with Myinfo should track and store user transactions for potential issue management.

The following are some of the suggested minimum fields for tracking:

* UUID, Partial NRIC/FIN or NRIC/FIN (as relevant to usage under PDPA guidelines)
* Fields requested from Myinfo
* Time Stamp
* Transaction ID

In the event of user feedback or contact, these transaction logs may be requested by Myinfo to reconcile and resolve issues raised by the user.

***

## 2. JSON Web Key Store (JWKS)

The relying party is expected to provide public keys to Myinfo in the JWK format. These public keys will be used in the following (non-exhaustive) scenarios:

* **Signature JWK** used to verify the signature of the `client_assertion JWT` presented during `/token` request.
* **Encryption JWK** used to encrypt the retrieved user's data in `/person` request.

The relying party is expected to host the **JWKS** with below specifications:

* is served behind HTTPS on port 443 using a TLS server certificate issued by a standard publicly verifiable CA issuer (no private CAs), with complete cert chain presented by the server
* is publicly accessible (no IP whitelisting, mTLS or other custom HTTP header requirements outside standard HTTP headers such as Content-Type, Accept)
* is able to respond in a timely fashion
* Contains at least 1 `sig` key with `alg ES256`
* Contains at least 1 `enc` key with `alg ECDH-ES+A256KW`

The Relying party is expected to follow below key rotation and caching policies

* Retrieval of **Myinfo JWKS** should be cached for at least `one hour` and not retrieved for every JWT validation.
* For varying reasons, keys used for signing can and will be **rotated/changed with no defined schedule**, and at the full discretion of Myinfo. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different kid value. The new kid value will be reflected in all the new JWTs signed by Myinfo. In such cases, cached copies of Myinfo public keys must be refreshed by re-invoking the JWKS endpoint.
* **All Key pairs** are recommended to be rotated every `2 years` with the old key pairs removed once rotation is sucessful.
* Keying materials e.g shared secrets, seeds shall be destroyed immediately or as soon as possible when no longer requried.

***

## 3. TLS & Cipher Suites

**IMPORTANT:** In line with contemporary industry best practices, Myinfo supports TLS 1.2.

The list of supported strong cipher suites include:

* TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256
* TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

**Recommendation on Myinfo Certificate pinning**\
\
RPs must not do "cert pinning" or create any form of dependency to the TLS certificates to Myinfo domains. **Myinfo reserves the right to rotate its TLS certificates without prior notice to RPs.**\
\
Should your application architecture require cert pinning, we recommend that your application trust / pin against the [root certificates](https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/amazonrootcas.zip) instead.

***

## 4. Callback URLs

For security reasons:

* Different callback URLs should be used for staging and production environments
* Fully Qualified Domain Name (FQDN) of staging and production environments should be used (i.e. instead of IP address)
* Callback URLs should not contain Hash (#) or Wildcard (\*) characters

***

## 5. Mobile App integration

* Myinfo offers integration via browser redirections. Native application integration is not supported.
* Integration should be done via in-app browser (not WebViews) or external browser.
* For services integrating on Android, setDomStorageEnable should be enabled.
* Camera permissions for your app must be enabled to support cases where additional security verification with Singpass Face Verification is required.


# Technical Concepts


# OAuth 2.1 Concepts

MyInfo APIs use [OAuth2.1](https://oauth.net/2.1/) - Authorization code flow to perform authentication & authorization; it allows mobile and web clients to obtain tokens securely.

The code flow comprises 2 main parts:

1. Authorization flow that runs in the browser
2. Token flow that is a server-to-server call

***

## 1. Authorization Flow

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FqGSFvfW10qoD9SuBAmRS%2Fimage.png?alt=media&amp;token=14eb42ae-4664-444b-9858-00e914b8bcfe" alt=""><figcaption></figcaption></figure>

1. Browser redirects to the /authorize endpoint of the AuthZ server.
2. The AuthZ server redirects to the Singpass, the AuthN server.
3. The User authenticates and redirects back to the AuthZ server.
4. The AuthZ server redirects to the consent page for user consent.&#x20;
5. The User consents.
6. The AuthZ server redirects back to the client application callback URL with a one-time token called Authorization Code(authcode)

## 2. Token Flow

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FokMF84Zq5czeOEfF1I05%2Fimage.png?alt=media&amp;token=3d24a0fc-a7ab-49b0-a13d-c5134b95566c" alt=""><figcaption></figcaption></figure>

1. The client application makes a post request to the /token API endpoint with the Authorization code (authcode) and client\_assertion.
2. The AuthZ Server validates the authcode and client\_assertion before issuing the access\_token.

<br>


# Proof of Key Code Exchange (PKCE)

Proof Key for Code Exchange(PKCE) is an extension to the Authorization Code flow to prevent Cross Site Request Forgery(CSRF) and Authorization code injection attacks. (Refer to <https://datatracker.ietf.org/doc/html/rfc7636>)\
\
![](https://api.singpass.gov.sg/assets/api-lib/myinfo/img/v4/pkce.png)

1. User access to the client application.
2. Client application creates a cryptographically random string as a secret key (code\_verifier) that only it knows and creates a base64url encoded hash of the secret key(code\_challenge).
3. Client application returns the code\_challenge and creates a frontend session to the user's browser.
4. Browser calls /authorize API with the code\_challenge.
5. The AuthZ server returns the authcode.
6. Client application calls /token API with the code\_verifier and authcode.
7. The AuthZ server will ensure that the code\_verifier has the same hash as the code\_challenge before issuing the access\_token.

**i) Create code\_verifier**

***

Create a code\_verifier, which is the cryptographically random string that will eventually be sent to Token API to request for access\_token.Copy to clipboard

```
// Dependency: Node.js crypto module (https://nodejs.org/api/crypto.html#crypto_crypto)
 
function base64URLEncode(str) {
    return str.toString('base64')
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
}
 
// The client generates a random string of bytes and saved into a persistent session store
let codeVerifier = base64URLEncode(crypto.randomBytes(32));
```

**i) Create code\_challenge**

***

Using the code\_verifier, generate a code\_challenge that will be sent in the /authorize API. Copy to clipboard

```
// Dependency: Node.js crypto module (https://nodejs.org/api/crypto.html#crypto_crypto)
 
function base64URLEncode(str) {
    return str.toString('base64')
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
}
 
// The client hashes these bytes and encodes them for use in a url
let codeChallenge = base64URLEncode(crypto.createHash('sha256').update(codeVerifier).digest());
```

code\_challenge should be generated from the raw bytes of the code\_verifier and not the hex encoded string.\
\
Example: 'helloworld' code\_verifier should produce 'k2oYXKqiZrucvpgengXLeM1zKwsygOuURBK7b4-PB68' as code\_challenge


# JSON Web Token (JWT)

## 1.JSON Web Token (JWT)

JSON Web Tokens consist of three parts separated by dots (.), which are:

* Header
* Payload
* Signature

Therefore, a JWT typically looks like the following: \`xxxxx.yyyyy.zzzzz\`

The header and the payload are Base64Url encoded. The signature is created using these two, a secret and the hashing algorithm being used (as specified in the header: ES256).

To parse the JWT, you can use one of the libraries listed in the [JWT Libraries ](https://jwt.io/libraries)for Token Signing/Verification section of  [JWT.io ](https://jwt.io/).

## 2.JSON Web Signature (JWS)

The decrypted payload is signed in [JWS (JSON Web Signature)](https://www.rfc-editor.org/rfc/rfc7515) format, similar to the access\_token.

* The signature algorithm used is ES256.

You may download our Public JWKS from Myinfo JWKS URI for verification, after application is created during onboarding on the application details page upon login.

Copy to clipboard

```
module.exports.verifyJWS = async (compactJWS, jwksUrl) => {
  var jwks = await getJwks(jwksUrl);
   
  try {
    let keyStore = await jose.JWK.asKeyStore(jwks);
   
    let result = await jose.JWS.createVerify(keyStore).verify(compactJWS);
    let payload = JSON.parse(Buffer.from(result.payload).toString());
   
    return payload;
  } catch (error) {
    console.error("Error with verifying JWS:", error);
    throw constant.ERROR_VERIFY_JWS;
  }
};
```

The code example above verify the JWS and return the JSON object, which is the person's data.

## 3.JSON Web Encryption (JWE)

* The encryption is done using your application's public key you provided during onboarding. So the payload's decryption should use your corresponding private key.
* Current encryption algorithms used:
  * **ECDH-ES+A256KW** (for content key wrapping)
  * **AES256GCM** (for content key wrapping)

### 3.1 What is the JWE (JSON Web Encryption) Compact Serialization format?

The format consists of five parts separated by dots (.), which are:

| PART                  | DESCRIPTION                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Header                | <p>Contains the encryption algorithms used to produce the</p><ol><li>cipher text(encrypted data)</li><li>encrypted key (symmetric key encrypted with application's RSA public key)</li><li><p></p><ol><li></li></ol></li></ol> |
| Encrypted Key         | The encrypted symmetric key that was used to encrypt the data.                                                                                                                                                                 |
| Initialization Vector | Secure random value used together with the symmetric key to encrypt the data.                                                                                                                                                  |
| Ciphertext            | The encrypted data.                                                                                                                                                                                                            |
| Tag                   | Value used to ensure integrity of the encrypted data and header.                                                                                                                                                               |

Therefore, a JWE typically looks like the following: aaaaa.bbbbb.ccccc.ddddd.eeeee

### 3.2 How can I decrypt the JWE?

You will need to use a library that performs JWE decryption to decrypt the Ciphertext. Such libraries are readily available on the internet.

For example, in our sample application (using Node.js), we use the jose.jwe.decrypt method from jose library. If the decryption fails, the library will throw an error the application needs to handle.

### 3.3 How does JWE library decrypt the JWE in detail?

Firstly, your JWE library will decrypt the Encrypted Key inside the JWE using your application's corresponding Encryption private key. Once it's decrypted, your library can retrieve the symmetric key that is used to encrypt the Ciphertext in JWE. Next, the JWE library will decrypt the Ciphertext using that symmetric key together with the Initialization Vector, Tag and the encryption algorithm in the ASCII-encoded Header.

***

With reference to myinfo-connector/lib/securityHelper.js sample application connector code:

Copy to clipboard

```
module.exports.decryptJWEWithKey = async (compactJWE, encryptionPrivateKey) => {
  try {
    let keystore = jose.JWK.createKeyStore();
    let jweParts = compactJWE.split("."); // header.encryptedKey.iv.ciphertext.tag
    if (jweParts.length != 5) {
      throw constant.ERROR_INVALID_DATA_OR_SIGNATURE;
    }
     
    //Session encryption private key should correspond to the session encryption public key passed in to client assertion
    let key = await keystore.add(encryptionPrivateKey, "pem");
     
    let data = {
      "type": "compact",
      "protected": jweParts[0],
      "encrypted_key": jweParts[1],
      "iv": jweParts[2],
      "ciphertext": jweParts[3],
      "tag": jweParts[4],
      "header": JSON.parse(jose.util.base64url.decode(jweParts[0]).toString())
    };
     
    let result = await jose.JWE.createDecrypt(key).decrypt(data);
     
    return result.payload.toString();
  } catch (error) {
    throw constant.ERROR_DECRYPT_JWE;
  }
};
```

The code example above decrypts the JWE and returns the payload signed in JWS;


# Client Assertions

A client assertion is a JWT directly produced by a client application using a cryptographic key and presented as proof of the client's identity. (Refer to <https://datatracker.ietf.org/doc/html/rfc7521>)

Client Assertions provide a strong method of authenticating clients before returning an access\_token for them to access the data.

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2F8DDy98VX6BGQ5QmJg9S4%2Fimage.png?alt=media&amp;token=805380bc-0e5d-4bba-aa47-360efd4a9689" alt=""><figcaption></figcaption></figure>

1. Client application invoke the Token API with a JWT client\_assertion.
2. AuthZ server will retrieve the client's trusted public key (JWK) from the client's onboarded JWKS URI. (As the JWKS endpoint only exposes public information, it does not need securing)
3. AuthZ server will verify the signature of the client\_assertion by extracting the matching public key from the client's JWKS with reference to the kid field in the client\_assertion JWT header.
4. AuthZ server returns the JWT access\_token.
5. Client application will retrieve AuthZ's trusted public key (JWK) from AuthZ's JWKS URI.
6. Client application will verify the signature of the access\_token by extracting the matching public key from AuthZ's JWKS with reference to the kid field in the access\_token JWT header.

{% hint style="info" %}
JSON Web Key (JWK) is a JSON object that represents a cryptographic public key that can be used to validate the signature of a signed JSON Web Token (JWT).

JSON Web Key Set (JWKS) is composed of 1 or more JSON Web Keys (JWK) in an array format.&#x20;
{% endhint %}

***

## **Generate Client Assertion**

An example JWT client assertion is shown below.

```
{
    "typ": "JWT",
    "alg": "ES256",
    "kid": "x0zDLIC9yNRIXu3gW8nTQDOMNe7sKMAjQnZj3AWTW2U"
}.
{
    "sub": "PROD2-MYINFO-SELF-TEST",
    "jti": "jNDZuyLw66gkTjmCNMawzrTJNlhS8wdjpU0DHTzo",
    "aud": "https://api.myinfo.gov.sg/com/v4/token",
    "iss": "PROD2-MYINFO-SELF-TEST",
    "iat": 1662365106,
    "exp": 1662365406,
    "cnf":{
        "jkt": "G_q8Qv9-xv_9xJo-esolTnvxVSobMER7O0LKGPBlTqY"
    }
}.
[signature]
```

The claims (Refer to <https://www.rfc-editor.org/rfc/rfc7519#section-4.1>) expected in the signed assertion are:

| PARAMETER | DESCRIPTION                                                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| sub       | Subject - client\_id issued by Myinfo upon onboarding                                                                                          |
| jti       | JWT ID - random unique identifier                                                                                                              |
| aud       | Audience - URL that client application is calling                                                                                              |
| iss       | Issuer - client\_id issued by Myinfo upon onboarding                                                                                           |
| iat       | Issued At - current timestamp                                                                                                                  |
| cnf.jkt   | JWK Thumbprint - base64url encoding of the JWK SHA-256 Thumbprint of the client's ephemeral public signing key used to sign the DPoP Proof JWT |

**Sample Code:**

```
// jktThumbprint: base64url encoding of the JWK SHA-256 Thumbprint of the client's ephemeral public signing key used to sign the DPoP Proof JWT
     
    async function generateClientAssertion (url, clientId, privateSigningKey, jktThumbprint) => {
      let now = Math.floor((Date.now() / 1000));
     
      let payload = {
        'sub': clientId,
        'jti': generateRandomString(40),
        'aud': url,
        'iss': clientId,
        'iat': now,
        'exp': now + 300,
        'cnf' : {
          'jkt': jktThumbprint
        }
      };
      let jwsKey = await jose.JWK.asKey(privateSigningKey, 'pem');
     
      let jwtToken = await jose.JWS.createSign({ 'format': 'compact', 'fields': { 'typ': 'JWT' } }, jwsKey).update(JSON.stringify(payload)).final();
      return jwtToken;
    };
```

The client\_assertion is produced by generating the JSON payload and signing it with a private key. The signing and headers are produced by a JWT security library which uses a private key in JWK format.&#x20;


# JSON Web Key Store (JWKS)

The relying party is expected to provide public keys to Myinfo in the JWK format. These public keys will be used in the following (non-exhaustive) scenarios:

* **Signature JWK** used to verify the signature of the client\_assertion JWT presented during /token request.
* **Encryption JWK** used to encrypt the retrieved user's data in /person request.

The relying party is expected to host the **JWKS** with below specifications:

* is served behind HTTPS on port 443 using a TLS server certificate issued by a standard publicly verifiable CA issuer (no private CAs), with complete cert chain presented by the server
* is publicly accessible (no IP whitelisting, mTLS or other custom HTTP header requirements outside standard HTTP headers such as Content-Type, Accept)
* is able to respond in a timely fashion
* Contains at least 1 `sig` key with `alg ES256`
* Contains at least 1 `enc` key with `alg ECDH-ES+A256KW`

For Staging and Production environments, please ensure

* You have a separate JWKS endpoint for each environment
* Different keypairs configured in the JWKS endpoints for each environment

## Generation of JSON Web Key Store

**JWKS Endpoint Sample Code**\
Sample Code to generate a Private/Public Key Pair

```
const jose = require('node-jose');
const crypto = require('crypto');
async function generateKey(){
  let key = crypto.generateKeyPairSync('ec', {
    namedCurve: 'prime256v1',
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem',
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem',
    },
  });
  let cryptoKey = await jose.JWK.asKey(key.privateKey, 'pem');
  return cryptoKey;
}
```

Sample Code to generate Signing and Encryption keys and create JWKS from public keys.

```
const jose = require('node-jose');
async function generateJwks() {
  //Creating Signing Key
  let signingKey = await generateKey();
  let publicSigningKeyJSON = signingKey.toJSON();
 
  //Creating Encryption Key
  let encryptionKey = await generateKey();
  let publicEncryptionKeyJSON = encryptionKey.toJSON();
 
    let jwks = {
      keys: [{...publicSigningKeyJSON,
              ...{use: 'sig'},
              ...{crv: 'P-256'},
              ...{alg: 'ES256'},
    },
    {...publicEncryptionKeyJSON,
              ...{use: 'enc'},
              ...{crv: 'P-256'},
              ...{alg: 'ECDH-ES+A256KW'},
    }]};
 
    console.log(JSON.stringify(jwks));
}
```

{% hint style="info" %}
For production use, the private key must be generated separately in your production environment and stored directly. The Private Key should not leave your production Environment
{% endhint %}

{% hint style="info" %}
Generating the JWK in this manner will set a default kid(Thumbprint of JWK). You may set your own value for kid, but ensure that upon signing with Private key, the correct corresponding kid is reflected in JWT header
{% endhint %}

{% hint style="info" %}
Different keys are required to be created for Staging and Production
{% endhint %}

## JWKS for signing

The signing JWK will be used to verify the client\_assertion JWT provided during /token request, thereby authenticating the client.

Clients are allowed to provide multiple signature keys in the JWKS hosted on the JWKS url provided during onboarding on DPP.

The signature JWK should have the following attributes:

* Must have key use of value 'sig'
* Must be an EC key, with curves: P-256 (NIST curves, aka secp256r1)
* Must have an alg of value 'ES256'

**Example EC signing key**

```
{
    "kty": "EC",
    "use": "sig",
    "alg": ES256
    "kid": "sig-2021-01-15T12:09:06Z",
    "crv": "P-256",
    "x": "Tjm2thouQXSUJSrKDyMfVGe6ZQRWqCr0UgeSbNKiNi8",
    "y": "8BuGGu519a5xczbArHq1_iVJjGGBSlV5m_FGBJmiFtE"
}
```

## Signing key rotation

Relying parties can rotate their signing keys in a self-driven manner. To do this with zero downtime, the Relying party must

* support use of **JWKS URLs** and be onboarded as such
* ensure their replacement signing key has a different key ID (`kid`) to the original key
* ensure their replacement signing key matches the other cryptographic key requirements

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Prep          | Relying party generates a new signing key pair (K2) supported for signing.                                                           |
| T0            | Relying party adds public key K2 to its JWKS endpoint (and leaves K1 on the endpoint)                                                |
| T0 - T+1 hour | Myinfo’s cache will expire, and re-retrieves the relying party’s published keys from their JWKS endpoint which now includes K2       |
| > T+1 hour    | Relying party changes their system to start signing client assertions using the new signing key K2                                   |
| Clean Up      | Post-validation, relying party can remove key K1 from their JWKS endpoint when they are comfortable their new signing key is working |

***

## JWKS for encryption

The encryption JWK will be used to encrypt ID user's requested data from the `/person` API.

The encryption JWK must have the following attributes:

* Must have key use of value 'enc'
* The key ID will be specified in the returned JWE header so that clients can pick the right key for decryption
* Must have key type (kty) of either EC
* Must have alg type of either ECDH-ES+A256KW

**Example EC encryption key**

```
{
    "kty": "EC",
    "use": "enc",
    "kid": "enc-2021-01-15T12:09:06Z",
    "crv": "P-256",
    "x": "xom6kD54yfXRPvMFVYFlVjUKzmNhz7wf0DP_2h9kXtY",
    "y": "lrh8C9c8-SBJTm1FcfqLkj2AnHtaxpnB1qsN6PiFFJE",
    "alg": "ECDH-ES+A128KW"
}
```

In the event of multiple encryption keys found. Myinfo will use the first compatible key. Relying party is expected to be able to choose the correct private key for decryption based on kid.

***

## Encryption key rotation

Relying parties can rotate their encryption keys in a self-driven manner. To do this with zero downtime the Relying party must

* support use of JWKS URLs and be onboarded as such
* have the ability to decrypt tokens produced with either one of two different encryption keys based on either
  * selecting the correct decryption key by its key ID (kid)
  * trial-and-error decryption against multiple keys in a collection
* ensure their replacement key matches the other cryptographic key requirements noted above

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                                     |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new encryption key pair (K2) supported for decryption. The existing key pair (K1) is still available for decryption of ID tokens |
| T0            | Relying party removes public key K1 and adds public key K2 on its JWKS endpoint                                                                            |
| T0 - T+1 hour | NDI’s caches will expire at any (indeterminate) time within this period, and start encrypting tokens with new encryption key K2.                           |
| T0 - T+1 hour | Relying party may be receiving tokens encrypted with either K1 or K2 keys throughout this period; and must be able to decrypt either.                      |
| > T+1 hour    | Relying party can remove support for decrypting with the previous K1 key                                                                                   |

***

## Caching and key rotation policy

* Retrieval of Myinfo JWKS should be cached for at least one hour and not retrieved for every JWT validation.
* For varying reasons, keys used for signing can and will be rotated/changed with no defined schedule, and at the full discretion of Myinfo. When a key rotation happens, the new key will be available from the JWKS endpoint and will have a different kid value. The new kid value will be reflected in all the new JWTs signed by Myinfo. In such cases, cached copies of Myinfo public keys must be refreshed by re-invoking the JWKS endpoint.
* All Key pairs are recommended to be rotated every 2 years with the old key pairs removed once rotation is successful.
* Keying materials e.g shared secrets, seeds shall be destroyed immediately or as soon as possible when no longer requried.


# Demonstration of Proof-of-Possession (DPoP)

## Introduction

The Demonstration of Proof-of-Possession(DPoP) is a mechanism to tie an access\_token to the client who gets it. The client will have to provide a proof of possession before the access\_token can be used.

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FJe69vANdS0wMDXE1YU5P%2Fimage.png?alt=media&amp;token=120021f9-9a33-4619-b877-84373d2998b2" alt=""><figcaption><p>DPoP Mechanism</p></figcaption></figure>

**1. Client application generates an ephemeral (One time) keypair on each API request.**

{% hint style="info" %}
Please ensure a new ephemeral keypair is generated on each request to ensure DPoP Proof is always unique per transaction.
{% endhint %}

* Ephemeral public key (JWK)
* Ephemeral private key

With the following information:&#x20;

* alg: ES256
* use: sig

***

**2. Client application generates the DPoP Proof JWT(for /token API)**

* Embed the DPoP Proof JWTephemeral public key (JWK) into the header of the DPoP Proof JWT DPoP Proof JWT
* Sign the DPoP Proof JWT using the DPoP Proof JWT ephemeral private key

***

**3. Client application appends ephemeral public key (JWK) thumbprint into the payload of the client\_assertion (cnf.jkt)**

Refer to Generate [Client Assertion](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v4/technical-concepts/client-assertions)

{% hint style="info" %}
This step ensures that the identical client application generates the DPoP Proof (for Token API) and client\_assertion.
{% endhint %}

***

**4. Client application calls the /token API to request for an access\_token** with the following information:

* DPoP Proof (for Token API)
* client\_assertion
* authcode

***

**5. AuthZ server validates and embeds the ephemeral public key (JWK) thumbprint of the DPoP Proof JWT (for /token API) into the access\_token (cnf.jkt).**&#x20;

{% hint style="info" %}
This step ensures that the access\_token can only be used by the client application.
{% endhint %}

***

**6. AuthZ server returns access\_token to the client application with token\_type as DPoP.**&#x20;

***

**7. Client application generates another DPoP Proof JWT (for /person API):**

{% hint style="info" %}
This step ensures that the access\_token can only be used by the client application.
{% endhint %}

***

**8. Client application calls the /person API to request for the person data (Resource)** with the following information:

* DPoP Proof (for Person API)
* access\_token

***

**9. Resource server validates the payload (ath) and ensures the ephemeral public key (JWK) thumbprint of the DPoP Proof JWT (for /person API) matches the access\_token hash and cnf.jkt.**&#x20;

{% hint style="info" %}
This step ensures that the access\_token belongs to the client application that generates the DPoP Proof (Person API).&#x20;
{% endhint %}

***

**10. Resource server response with the person data.**&#x20;

***

## **Generate Ephemeral keys**

**Sample Code:**

```
async function generateEphemeralKeys() {
  let options = {
    namedCurve: "P-256",
    publicKeyEncoding: {
      type: "spki",
      format: "pem",
    },
    privateKeyEncoding: {
      type: "sec1",
      format: "pem",
    },
  };
     
  let ephemeralKeyPair = crypto.generateKeyPairSync("ec", options);
 
  return ephemeralKeyPair;
}


```

***

## Generate DPoP Proof JWT

The claims (Refer to <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-dpop#name-dpop-proof-jwt-syntax>) expected in the DPoP Proof JWT are:&#x20;

| PARAMETER | DESCRIPTION                                                                                                                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| typ       | Type - Type (Header), value "dpop+jwt"                                                                                                                                                                                  |
| alg       | Algorithm (Header) - digital signature algorithm identifier as per RFC7518 (Refer to <https://datatracker.ietf.org/doc/html/rfc7518>). MUST NOT be none or an identifier for a symmetric algorithm (MAC), value "ES256" |
| jwk       | JSON Web Key (Header) - public key chosen by the client. MUST NOT contain the private key.                                                                                                                              |
| jti       | JWT ID (Payload) - unique identifier                                                                                                                                                                                    |
| htu       | HTTP URL (Payload) - HTTP URI used for the request, without query (?) and fragment parts (#)                                                                                                                            |
| htm       | HTTP Method (Payload) - HTTP method for the request to which the JWT is attached                                                                                                                                        |
| iat       | Issued At (Payload) - current timestamp                                                                                                                                                                                 |
| exp       | Expiry (Payload) - expiry timestamp                                                                                                                                                                                     |
| ath       | Access token hash (Payload) - The base64url encoded SHA-256 hash of the ASCII encoding of the associated access token's value (Required only for /person call after DPoP-bound access token is issued)                  |
|           |                                                                                                                                                                                                                         |

**DPoP Proof Sample**

**Token API**

```
{
  "typ": "dpop+jwt",
  "jwk": {
    "kty": "EC",
    "kid": "M2OJVTdfiUw9C1HQkO1vTijLXGOypcFuT5wd4-5WdzE",
    "crv": "P-256",
    "x": "n92tLt2RNoBgB3jbOkq61wl_33USS08tS-GR7de0Mf0",
    "y": "3riG1jcEY8BLZdR8fseAkXA-RoIov_x9C_bG3JXVUq4",
    "use": "sig",
    "alg": "ES256"
  },
  "alg": "ES256"
}.
{
  "htu": "https://sit.api.myinfo.gov.sg/com/v4/token",
  "htm": "POST",
  "jti": "bWDY6aTCnAGKWtCUjYLVIVmoEmB4XarepsBD85GC",
  "iat": 1662714998,
  "exp": 1662715118
}.
[signature]
```

**Person API**

```
{
  "typ": "dpop+jwt",
  "jwk": {
    "kty": "EC",
    "kid": "M2OJVTdfiUw9C1HQkO1vTijLXGOypcFuT5wd4-5WdzE",
    "crv": "P-256",
    "x": "n92tLt2RNoBgB3jbOkq61wl_33USS08tS-GR7de0Mf0",
    "y": "3riG1jcEY8BLZdR8fseAkXA-RoIov_x9C_bG3JXVUq4",
    "use": "sig",
    "alg": "ES256"
  },
  "alg": "ES256"
}.
{
  "htu": "https://sit.api.myinfo.gov.sg/com/v4/person/915267f0-5939-0230-78e7-b8cdbaab8518",
  "htm": "GET",
  "jti": "XFj7vBWCOlpI2Qyuxi4R7l2BTwFWDwZu1lWDT47p",
  "iat": 1662715005,
  "exp": 1662715125,
  "ath": "Eh9xM2CDQyrI3OMLJJJDhtmQeakdYYTDckNtklRQOVw"
}.
[signature]
```

**Sample Code:**

```
// ath: Base64urlencoded Hash of the access_token
 
async function generateDpop(url, ath, method, ephemeralKeyPair) {
  let now = Math.floor(Date.now() / 1000);
  let payload = {
    htu: url,
    htm: method,
    jti: generateRandomString(40),
    iat: now,
    exp: now + 120,
  };
     
  if (ath) {
    payload.ath = ath;
  }
 
  let privateKey = await jose.JWK.asKey(ephemeralKeyPair.privateKey, "pem");
  let jwk = (await jose.JWK.asKey(ephemeralKeyPair.publicKey, "pem")).toJSON(true);
  jwk.use = "sig";
  jwk.alg = "ES256";
  let DPoP = await jose.JWS.createSign(
    { format: "compact", fields: { typ: "dpop+jwt", jwk: jwk } },
    { key: privateKey, reference: false }
  )
    .update(JSON.stringify(payload))
    .final();
  return DPoP;
}
```


# API Specifications

Please see [API Specification v4.0](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html) for in depth specification

{% openapi src="/files/PvA5SHuiVEDCCxqZTRuD" path="/com/v4/person-sample/{uinfin}/" method="get" %}
[myinfov4swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2Fs62gr9GeEdFwky5Tei56%2Fmyinfov4swagger.json?alt=media\&token=d79dee93-d223-41c9-86d8-50ad8a47d4b5)
{% endopenapi %}

{% openapi src="/files/PvA5SHuiVEDCCxqZTRuD" path="/com/v4/authorize" method="get" %}
[myinfov4swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2Fs62gr9GeEdFwky5Tei56%2Fmyinfov4swagger.json?alt=media\&token=d79dee93-d223-41c9-86d8-50ad8a47d4b5)
{% endopenapi %}

{% openapi src="/files/PvA5SHuiVEDCCxqZTRuD" path="/com/v4/token" method="post" %}
[myinfov4swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2Fs62gr9GeEdFwky5Tei56%2Fmyinfov4swagger.json?alt=media\&token=d79dee93-d223-41c9-86d8-50ad8a47d4b5)
{% endopenapi %}

{% openapi src="/files/PvA5SHuiVEDCCxqZTRuD" path="/com/v4/person/{sub}" method="get" %}
[myinfov4swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2Fs62gr9GeEdFwky5Tei56%2Fmyinfov4swagger.json?alt=media\&token=d79dee93-d223-41c9-86d8-50ad8a47d4b5)
{% endopenapi %}


# Tutorials


# Tutorial 1: Myinfo Person sample Data

This tutorial will call a basic API to get sample Person data in JSON response. You can then use this JSON object to pre-fill your online form in your application.

## 1. Request

Open another browser window and type in the following URL:

```
https://sandbox.api.myinfo.gov.sg/com/v4/person-sample/S9812381D
```

This will call our sandbox API using HTTPS GET.

`S9812381D` is the *UINFIN* (NRIC or FIN) parameter which refers to the ID of the person you wish to get the data of. For this sample API, the following *UINFIN* are supported:

* `S9812381D`
* `S9812382B`
* `S9812385G`
* `S9812387C`
* `S9912363Z`
* `S9912366D`
* `S9912369I`
* `S9912370B`
* `S9912372I`
* `S9912374E`
* `S6005053H`
* `S6005055D`
* `S9812379B`
* `F1612347K`
* `G1612348Q`
* `G1612349N`
* `G1612350T`
* `G1612352N`
* `G1612353L`

{% hint style="info" %}
This API will take in the actual UINFIN as the sub for easier reference, however in the actual implementation UUID of the user will be used instead.
{% endhint %}

Please refer to our [API specifications](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html) for this tutorial.

***

## 2. Response

You should see a JSON object which looks like this after you access the Person Sample API.

**Sample JSON for Person data**

```
{
  "uinfin": {
    "lastupdated": "2019-03-26",
    "source": "1",
    "classification": "C",
    "value": "S9812381D"
  },
  "name": {
    "value": "TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinname": {
    "value": "CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "aliasname": {
    "value": "TRICIA TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinaliasname": {
    "value": "TRICIA CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marriedname": {
    "value": "",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "sex": {
    "code": "F",
    "desc": "Female",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "race": {
    "code": "CN",
    "desc": "CHINESE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "secondaryrace": {
    "code": "EU",
    "desc": "EURASIAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dialect": {
    "code": "SG",
    "desc": "SWISS GERMAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "nationality": {
    "code": "SG",
    "desc": "SINGAPORE CITIZEN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dob": {
    "value": "1958-05-17",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "birthcountry": {
    "code": "SG",
    "desc": "SINGAPORE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "residentialstatus": {
    "code": "C",
    "desc": "Citizen",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportnumber": {
    "value": "E35463874W",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportexpirydate": {
    "value": "2020-01-01",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "regadd": {
    "type": "SG",
    "block": {
      "value": "548"
    },
    "building": {
      "value": ""
    },
    "floor": {
      "value": "09"
    },
    "unit": {
      "value": "128"
    },
    "street": {
      "value": "BEDOK NORTH AVENUE 1"
    },
    "postal": {
      "value": "460548"
    },
    "country": {
      "code": "SG",
      "desc": "SINGAPORE"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  ...
}
```

Try using the JSON object in your own application to prefill your forms!

***

## Summary

You've successfully called a basic Person API and gotten a sample JSON response from Myinfo.


# Tutorial 2: End-to-end Integration with Myinfo v4 APIs

This tutorial will call the APIs from your server-based (or running from localhost) application.\
\
Myinfo uses [OAuth 2.1](https://oauth.net/2.1/) for our Authentication and Authorisation flow.\
\
For a brief overview of the end to end flow, please refer to our [Overview](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v4)

***

## 1. Download & Setup Sample Client Application<br>

### **1.1 Install Node.js and NPM**

In order for the demo application to run, you will need to Install Node.js and NPM. Follow the instructions given by the links below depending on your OS.

* [Install Node.js and NPM for Windows](http://blog.teamtreehouse.com/install-node-js-npm-windows)
* [Install Node.js and NPM for Linux](http://blog.teamtreehouse.com/install-node-js-npm-linux)
* [Install Node.js and NPM for Mac](http://blog.teamtreehouse.com/install-node-js-npm-mac)

### **1.2 Download the sample client application**

Please download the sample client application from our [Github](https://github.com/singpass/myinfo-demo-app-v4).<br>

### **1.3 Run NPM install**

Run the following command in the folder where you unzipped the application:

```
npm install
```

### **1.4 Start the Application**

Execute the following command to start the application:

```
npm start
```

### **1.5 Access the Application on Your Browser**

You should be able to access the sample application via the following URL:

```
http://localhost:3001
```

***

## 2. Authorize API

Click on the "**Retrieve Myinfo**" button on the sample application.<br>

This calls the /authorize API below (with some additional parameters):

| PARAMETER               | DESCRIPTION                                                                                                                                                                                                                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id              | unique ID for your application. For our sample application, this is STG2-MYINFO-SELF-TEST                                                                                                                                                                                                                 |
| scope                   | space separated list of attributes requested. Possible attributes are listed in the Person object definition in the API specifications.                                                                                                                                                                   |
| purpose\_id             | purpose\_id should have a corresponding pre-registered purpose(s) description as part of the setup. Purpose description refers to what the user will see in the consent page                                                                                                                              |
| code\_challenge         | Value resulting from performing Base64 encoding of a SHA256 hash of code\_verifier (cryptographic random value generate on server side.) Refer to the section on Proof Key for Code Exchange (PKCE) for more information (Reference : [PKCE](https://api.singpass.gov.sg/library/myinfo/developers/pkce)) |
| code\_challenge\_method | Hashing method used in producing code\_challenge. Only supports 'S256'                                                                                                                                                                                                                                    |
| redirect\_uri           | your callback URL for Myinfo to return with the authorisation code. For our sample application the callback url is <http://localhost:3001/callback>                                                                                                                                                       |
| response\_type          | Response type for authorisation code flow - must be "code".                                                                                                                                                                                                                                               |

### **2.1 Code Example for Authorize API**

With reference to views/html/index.html in the [sample application](https://github.com/singpass/myinfo-demo-app-v4) code:

The index.html is the frontend(client side) code.

```
function callAuthorizeApi() {
//Call backend server to generate code challenge 
$.ajax({
    url: "/generateCodeChallenge",
    data: {},
    type: "POST",
    success: function (code_challenge) {
        //Redirect to authorize url after generating code challenge
        var authorizeUrl = authApiUrl + "?client_id=" + clientId +
        "&scope=" + scope +
        "&purpose_id=" + purpose_id +
        "&code_challenge=" + code_challenge +
        "&code_challenge_method=" + method + 
       "&response_type=code" + 
        "&redirect_uri=" + redirectUrl;
     
        window.location = authorizeUrl;
        },
        error: function (result) {
            alert("ERROR:" + JSON.stringify(result.responseJSON.error));
        }
    });
}
```

This code example above triggers the /authorize API.

### **2.2 Login with MockPass**  Select the test ID and login using MockPass:

NRIC: 60050408A

You may also use test personas found in the [Personas](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas).

The `/authorize` API endpoint triggers the MockPass login and shows the consent page after successful login.

{% hint style="info" %}
Mockpass is a mock Singpass/Corppass login page for testing in development consistently
{% endhint %}

### **2.3 Consent Page**

Once you have successfully logged into MockPass, a consent page similar to the one below will be shown:

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FyuB0HC1aGJhAXVaVe5rP%2Fimage.png?alt=media&amp;token=3318543c-835b-4765-918a-62acfc0b3f11" alt=""><figcaption><p>Consent Screen</p></figcaption></figure>

### **2.4 Retrieve Authorization Code**<br>

If you have followed the steps above correctly, our system should return you an authorization code by invoking your callback URL.

You should now see something like this in your browser URL dialog:

```
http://localhost:3001/callback?code=e2369168-52da-421a-b70f-03f64e779c4b
```

Notice that the query string parameter value of code above is the **authorization code(authcode)**. We will use this **authorization code(authcode)** in the next `/token` API call.

In the example above, the **authorization code(authcode)** is e2369168-52da-421a-b70f-03f64e779c4b.

The `/token` API and `/person` API calls should be invoked automatically by the sample app once you have finished the consent page.

We will look at the code for these 2 APIs in the following sections.

***

## 3. Token API

Now that you have the `authcode`, you can invoke the `/token` API to get the `access_token`.

{% hint style="info" %}
The Token API must be called from a server-side component. It cannot be called from the browser or mobile native client application due to security reasons (there is no secure place to store your private key).
{% endhint %}

### 3.1 Request

**Request Parameters:**

* Method: POST
* Content-Type: application/x-www-form-urlencoded
* Agent: HTTP client
* Response Type: json

**i) Headers:**

| PARAMETER | DESCRIPTION                                                                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DPoP      | DPoP Proof (JWT) containing the client's ephemeral public signing key that can be used to prove legit possession of the access\_token issued. (Reference: DPoP flow) |

Sample header of the Token API request:

```
POST https://test.api.myinfo.gov.sg/com/v4/token HTTP 1.1
Accept: application/json
Content-Type: application/x-www-form-urlencoded
DPoP: eyJ0eXAiOiJkcG9wK2p3dCIsImp3ayI6eyJrdHkiOiJFQyIsImtpZCI6Ik0yT0pWVGRmaVV3OUMxSFFrTzF2VGlqTFhHT3lwY0Z1VDV3ZDQtNVdkekUiLCJjcnYiOiJQLTI1NiIsIngiOiJuOTJ0THQyUk5vQmdCM2piT2txNjF3bF8zM1VTUzA4dFMtR1I3ZGUwTWYwIiwieSI6IjNyaUcxamNFWThCTFpkUjhmc2VBa1hBLVJvSW92X3g5Q19iRzNKWFZVcTQiLCJ1c2UiOiJzaWciLCJhbGciOiJFUzI1NiJ9LCJhbGciOiJFUzI1NiJ9.eyJodHUiOiJodHRwczovL3NpdC5hcGkubXlpbmZvLmdvdi5zZy9jb20vdjQvdG9rZW4iLCJodG0iOiJQT1NUIiwianRpIjoiYldEWTZhVENuQUdLV3RDVWpZTFZJVm1vRW1CNFhhcmVwc0JEODVHQyIsImlhdCI6MTY2MjcxNDk5OCwiZXhwIjoxNjYyNzE1MTE4fQ.yOsoD-q7DPlgI_cnRVmjXcBraSxD5riCVmc8kaEoxGstTipFdTZIvnMs6EYs8oSFUYv4OVWcYm5MKLrJNLdtew
```

| PARAMETER               | DESCRIPTION                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                    | The authcode given by the Authorize API. (Reference: [Authorize](https://api.singpass.gov.sg/library/myinfo/developers/tutorial2#authorize))                                                                          |
| grant\_type             | <p>Default: "authorization\_code"<br><br>Grant type for getting token (default "authorization\_code")</p>                                                                                                             |
| client\_id              | Unique ID for your application.                                                                                                                                                                                       |
| redirect\_uri           | Application's callback URL.                                                                                                                                                                                           |
| client\_assertion       | The assertion being used to authenticate the client. (Reference: [Client Assertion](https://api.singpass.gov.sg/library/myinfo/developers/clientassertion))                                                           |
| client\_assertion\_type | <p>Default: "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"<br><br>The format of the assertion, which is defined to be 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'</p>                          |
| code\_verifier          | Cryptographic random string generated and kept secret on server-side, it's corresponding to code\_challenge sent in the Authorize API (Reference: [PKCE](https://api.singpass.gov.sg/library/myinfo/developers/pkce)) |

Sample body of the /token API request in application/x-www-form-urlencoded:

Copy to clipboard

```
body : 'code=KhtDB67e2DrPgB3wpLjUsDfppHsBB42A9Crsx2b0
&grant_type=authorization_code
&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fcallback
&client_id=STG2-MYINFO-SELF-TEST
&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer
&client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6ImFRUHlaNzJOTTA0M0U0S0Vpb2FIV3ppeHQwb3dWOTlnQzlrUkszODhXb1EifQ.eyJzdWIiOiJTVEcyLU1ZSU5GTy1TRUxGLVRFU1QiLCJqdGkiOiJtZzBNcFl0dkcyQTRUOWFRZkxON0o3OEY3dVltUmZJVmVyRUhIUFpaIiwiYXVkIjoiaHR0cHM6Ly9zaXQuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3Rva2VuIiwiaXNzIjoiU1RHMi1NWUlORk8tU0VMRi1URVNUIiwiaWF0IjoxNjYyNzE0OTk4LCJleHAiOjE2NjI3MTUyOTgsImNuZiI6eyJqa3QiOiJNMk9KVlRkZmlVdzlDMUhRa08xdlRpakxYR095cGNGdVQ1d2Q0LTVXZHpFIn19.OlluOi2RkwAavibqhGrDL4m6m91IlM_vnfu-4CY0pmkSbUDcKS_NBlggNrTNcc_wnbFBSqMYNo2V4Geh9Ucc6g
&code_verifier=Av6ktmeC1UsjHY677P-zf5Vk2x94W38Zu4pl4qhbeok'
```

The sample application will then send the constructed request to the /token API

**Sample Code:**\
With reference to myinfo-connector/index.js in our sample [sample client application connector](https://github.com/singpass/myinfo-demo-app-v4)

index.js is the backend (server side) code.

```
callTokenAPI = async function (authCode, privateSigningKey, codeVerifier, sessionPopKeyPair) {
     
      let cacheCtl = "no-cache";
    let contentType = "application/x-www-form-urlencoded";
    let method = constant.HTTP_METHOD.POST;
    let clientAssertionType = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer";
    let jktThumbprint = await this.securityHelper.generateJwkThumbprint(sessionPopKeyPair.publicKey)
    let strParams;
    // assemble params for Token API
    strParams = `grant_type=authorization_code` +
        "&code=" + authCode +
        "&redirect_uri=" + CONFIG.REDIRECT_URL +
        "&client_id=" + CONFIG.CLIENT_ID +
        "&code_verifier=" + codeVerifier +
        "&client_assertion_type=" + clientAssertionType +
        "&client_assertion=" + await this.securityHelper.generateClientAssertion(CONFIG.TOKEN_URL, CONFIG.CLIENT_ID, privateSigningKey, jktThumbprint);
     
    let params = querystring.parse(strParams);
    let dPoP= await this.securityHelper.generateDpop(CONFIG.TOKEN_URL, null, null,constant.HTTP_METHOD.POST, sessionPopKeyPair);
     
    // assemble headers for Token API
    let strHeaders = `Content-Type=${contentType}&Cache-Control=${cacheCtl}&DPoP=${dPoP}`;
    let headers = querystring.parse(strHeaders);
     
    // invoke Token API
    let tokenURL = (CONFIG.USE_PROXY && CONFIG.USE_PROXY == "Y") ? CONFIG.PROXY_TOKEN_URL : CONFIG.TOKEN_URL;
    let parsedTokenUrl = urlParser.parse(tokenURL);
    let tokenDomain = parsedTokenUrl.hostname;
    let tokenRequestPath = parsedTokenUrl.path;
     
    let accessToken = await requestHandler.getHttpsResponse(tokenDomain, tokenRequestPath, headers, method, params);
    return accessToken;
 };
```

The code example above creates the request to call the /token API.

```
[HTTP POST] 
https://test.api.myinfo.gov.sg/com/v4/token
```

### 3.2 Response

* Response Type: application/json

| PARAMETER         | DESCRIPTION                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access\_token     | The resulting access token for the code flow                                                                                                                |
| token\_type       | Describes how the token can be used. (e.g. DPoP)                                                                                                            |
| expires\_in       | Expiry of access token (in seconds)                                                                                                                         |
| refresh\_token    | Refresh token that can be used to exchange for another access token. Only available if client is configured to receive refresh token.                       |
| client\_assertion | The assertion being used to authenticate the client. (Reference: [Client Assertion](https://api.singpass.gov.sg/library/myinfo/developers/clientassertion)) |
| scope             | Scopes requested, separated by space                                                                                                                        |

Sample response from Token API in application/json:

Copy to clipboard

```
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IkFGTW5uS1JXVGFCWUVoTmZFQjZpUTVFckMxeXFHVnlaY2hIOEE3bmxfeU0ifQ.eyJzdWIiOiI5MTUyNjdmMC01OTM5LTAyMzAtNzhlNy1iOGNkYmFhYjg1MTgiLCJqdGkiOiJvMkZaVUpmSFZWVjA3aFpLTFZrc2Yxd0RBYnNUUUtWblFXM3RjZDI5Iiwic2NvcGUiOiJ1aW5maW4gbmFtZSBzZXggcmFjZSBuYXRpb25hbGl0eSBkb2IgZW1haWwgbW9iaWxlbm8gcmVnYWRkIGhvdXNpbmd0eXBlIGhkYnR5cGUiLCJleHBpcmVzX2luIjoxODAwLCJhdWQiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3BlcnNvbiIsInJlYWxtIjoibXlpbmZvLWNvbSIsImlzcyI6Imh0dHBzOi8vdGVzdC5hcGkubXlpbmZvLmdvdi5zZy9zZXJ2aWNlYXV0aC9teWluZm8tY29tIiwiY2xpZW50Ijp7ImNsaWVudF9pZCI6IlNURzItTVlJTkZPLVNFTEYtVEVTVCIsImNsaWVudF9uYW1lIjoiTXlJbmZvIFNlbGYgVGVzdCBBcHAgR0NDIiwiZW50aXR5X3VlbiI6IlQxNkdCMDAwMkciLCJlbnRpdHlfbmFtZSI6IkdvdlRlY2gifSwiY25mIjp7ImprdCI6ImhHdHN1S3h3UmFMOE1NeDVqVjVUYUluSWpqOFNLS3N3VEVOOGcxaU9FY1EifSwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ1c2UiOiJlbmMiLCJraWQiOiI3VGt5TWFqV0JYUlo3aVpmZ3lQUGZmMmdMMzloMlh0ZkpEemNzNXRjZXJNIiwieCI6Ik5mSXhKdWRCTzFfWEQ0RG5oa1ZLUG9uSHV4MExHMTJPM0QtWjJOZnN1RUUiLCJ5IjoiMkhHNmV5SmNFRUJWWlVwMVlsRjU3TFdNbEFJbXlTdU41d1FjZUVybW85OCIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0sImlhdCI6MTY2NzIwMTY4OCwibmJmIjoxNjY3MjAxNjg4LCJleHAiOjE2NjcyMDM0ODh9.0CMpP4Whxk11XTMxg1fz6Srw2HkPiY-t2Tydb8ouQVpCwMNe6DW3Mu6KBdOo00ipa7Nlhw375zwmWAIT-8-3CQ",
  "token_type": "DPoP",
  "expires_in": 1799,
  "refresh_token": "bsAJGkONZJJjs0cR11ZQzGHzxLKwDoEwaApy0krW",
  "scope": "uinfin name sex race nationality dob email mobileno regadd housingtype hdbtype"
}
```

Notice the response contains an access\_token, which is in the JWT (JSON Web Token) format. (Reference: [JWT](https://api.singpass.gov.sg/library/myinfo/developers/jwt))

The access\_token can be verified using Myinfo JWK URI and decoded.(Reference: [JWS](https://api.singpass.gov.sg/library/myinfo/developers/jwt))

You should see the decoded access\_token in the onscreen logs that looks like this:

Copy to clipboard

```
{
  "sub": "915267f0-5939-0230-78e7-b8cdbaab8518",
  "jti": "o2FZUJfHVVV07hZKLVksf1wDAbsTQKVnQW3tcd29",
  "scope": "uinfin name sex race nationality dob email mobileno regadd housingtype hdbtype",
  "expires_in": 1800,
  "aud": "https://test.api.myinfo.gov.sg/com/v4/person",
  "realm": "myinfo-com",
  "iss": "https://test.api.myinfo.gov.sg/serviceauth/myinfo-com",
  "client": {
    "client_id": "STG2-MYINFO-SELF-TEST",
    "client_name": "MyInfo Self Test App GCC",
    "entity_uen": "T16GB0002G",
    "entity_name": "GovTech"
  },
  "cnf": { "jkt": "hGtsuKxwRaL8MMx5jV5TaInIjj8SKKswTEN8g1iOEcQ" },
  "epk": {
    "kty": "EC",
    "crv": "P-256",
    "use": "enc",
    "kid": "7TkyMajWBXRZ7iZfgyPPff2gL39h2XtfJDzcs5tcerM",
    "x": "NfIxJudBO1_XD4DnhkVKPonHux0LG12O3D-Z2NfsuEE",
    "y": "2HG6eyJcEEBVZUp1YlF57LWMlAImySuN5wQceErmo98",
    "alg": "ECDH-ES+A256KW"
  },
  "iat": 1667201688,
  "nbf": 1667201688,
  "exp": 1667203488
}
```

This access\_token is a representation of the permissions that was given by the user when he/she clicked on "I Agree" on the consent page.

{% hint style="info" %}
Your application must validate the signature of the JWT to ensure the JWT was not modified in transit - intentionally or unintentionally.&#x20;
{% endhint %}

Notice the sub attribute in the JSON token is the identifier of the person who logged in via MockPass. We will use this identifier for the /person API call next.

***

## 4. Person API

Now that you have the access\_token, you can invoke the /person API to get the Person data.

{% hint style="info" %}
The Person API must be called from a server-side component. It cannot be called from the browser or mobile native client application due to security reasons (there is no secure place to store your private key).
{% endhint %}

This API call is essentially the same as the one in our Tutorial 1, except that you will need to provide a valid access\_token, or else we will reject your API request call.

### 4.1 Request

**Request Parameters:**

* Method: GET
* Agent: HTTP client
* Response Type: json

**i) Header:**

| PARAMETER     | DESCRIPTION                                                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authorization | Include the access\_token (JWT) from /Token API in this header prefixed with 'DPoP'.                                                              |
| DPoP          | Include the generated Demonstration of Proof of Possession token. (Reference: [DPoP](https://api.singpass.gov.sg/library/myinfo/developers/dpop)) |

**ii) Path Parameters:**

<table><thead><tr><th>PARAMETER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>sub</td><td><p>Identifier of user obtained from 'sub' attribute in access_token. </p><pre><code>Example: 915267f0-5939-0230-78e7-b8cdbaab8518     
</code></pre></td></tr></tbody></table>

**iii) Query parameters:**

<table><thead><tr><th>PARAMETER</th><th>DESCRIPTION</th></tr></thead><tbody><tr><td>scope</td><td><p>Space separated list of scopes requested.</p><pre><code>Example: scope=name nationality   
</code></pre></td></tr></tbody></table>

**iii) Sample Code:**

With reference to myinfo-connector/index.js in our sample client application connector code:

Copy to clipboard

```
callPersonAPI = async function (sub, accessToken, sessionPopKeyPair) {
    let urlLink;
     
    urlLink = CONFIG.PERSON_URL + "/" + sub;
    let cacheCtl = "no-cache";
    let method = constant.HTTP_METHOD.GET;
     
    // assemble params for Person API
    let strParams ="scope=" + encodeURIComponent(CONFIG.SCOPE);
     
    // assemble headers for Person API
    let strHeaders = "Cache-Control=" + cacheCtl;
    let headers = querystring.parse(strHeaders);
     
    let decodedToken = await this.securityHelper.verifyJWS(accessToken, CONFIG.AUTHORIZE_JWKS_URL);
    let ath = this.securityHelper.base64URLEncode(this.securityHelper.sha256(accessToken))
    let dpopToken = await this.securityHelper.generateDpopProof(urlLink, method, sessionPopKeyPair, ath);
    headers["dpop"] = dpopToken;
     
    headers["Authorization"] = "DPoP " + accessToken;
     
    logger.info("Authorization Header for MyInfo Person API: ", JSON.stringify(headers));
     
    // invoke person API
    let personURL = (CONFIG.USE_PROXY && CONFIG.USE_PROXY == "Y") ? CONFIG.PROXY_PERSON_URL : CONFIG.PERSON_URL;
    let parsedUrl = urlParser.parse(personURL);
    let domain = parsedUrl.hostname;
    let requestPath = parsedUrl.path + "/" + sub + "?" + strParams;
    //invoking https to do GET call
    let personData = await requestHandler.getHttpsResponse(domain, requestPath, headers, method, null);
  
return personData;
};
```

The code example above creates the request to call the /person API:

Copy to clipboard

```
[HTTP GET] 
https://test.api.myinfo.gov.sg/com/v4/person/915267f0-5939-0230-78e7-b8cdbaab8518?scope=uinfin%20name%20sex%20race%20nationality%20dob%20email%20mobileno%20regadd%20housingtype%20hdbtype
```

<br>

**4.1.1 Providing the Access Token in the Request Header**\
\
**STEP 1**: The access\_token should be provided in the header of your /person API request under "Authorization" with Prefix "DPoP"

Copy to clipboard

```
{
  "Authorization": "DPoP eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IkFGTW5uS1JXVGFCWUVoTmZFQjZpUTVFckMxeXFHVnlaY2hIOEE3bmxfeU0ifQ.eyJzdWIiOiI5MTUyNjdmMC01OTM5LTAyMzAtNzhlNy1iOGNkYmFhYjg1MTgiLCJqdGkiOiJvMkZaVUpmSFZWVjA3aFpLTFZrc2Yxd0RBYnNUUUtWblFXM3RjZDI5Iiwic2NvcGUiOiJ1aW5maW4gbmFtZSBzZXggcmFjZSBuYXRpb25hbGl0eSBkb2IgZW1haWwgbW9iaWxlbm8gcmVnYWRkIGhvdXNpbmd0eXBlIGhkYnR5cGUiLCJleHBpcmVzX2luIjoxODAwLCJhdWQiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3BlcnNvbiIsInJlYWxtIjoibXlpbmZvLWNvbSIsImlzcyI6Imh0dHBzOi8vdGVzdC5hcGkubXlpbmZvLmdvdi5zZy9zZXJ2aWNlYXV0aC9teWluZm8tY29tIiwiY2xpZW50Ijp7ImNsaWVudF9pZCI6IlNURzItTVlJTkZPLVNFTEYtVEVTVCIsImNsaWVudF9uYW1lIjoiTXlJbmZvIFNlbGYgVGVzdCBBcHAgR0NDIiwiZW50aXR5X3VlbiI6IlQxNkdCMDAwMkciLCJlbnRpdHlfbmFtZSI6IkdvdlRlY2gifSwiY25mIjp7ImprdCI6ImhHdHN1S3h3UmFMOE1NeDVqVjVUYUluSWpqOFNLS3N3VEVOOGcxaU9FY1EifSwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ1c2UiOiJlbmMiLCJraWQiOiI3VGt5TWFqV0JYUlo3aVpmZ3lQUGZmMmdMMzloMlh0ZkpEemNzNXRjZXJNIiwieCI6Ik5mSXhKdWRCTzFfWEQ0RG5oa1ZLUG9uSHV4MExHMTJPM0QtWjJOZnN1RUUiLCJ5IjoiMkhHNmV5SmNFRUJWWlVwMVlsRjU3TFdNbEFJbXlTdU41d1FjZUVybW85OCIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0sImlhdCI6MTY2NzIwMTY4OCwibmJmIjoxNjY3MjAxNjg4LCJleHAiOjE2NjcyMDM0ODh9.0CMpP4Whxk11XTMxg1fz6Srw2HkPiY-t2Tydb8ouQVpCwMNe6DW3Mu6KBdOo00ipa7Nlhw375zwmWAIT-8-3CQ"
}
```

**STEP 2** The DPoP proof JWT should be provided in the header of your /person API request under "DPoP"

Copy to clipboard

```
{
  "DPoP": "eyJ0eXAiOiJkcG9wK2p3dCIsImp3ayI6eyJrdHkiOiJFQyIsImtpZCI6ImhHdHN1S3h3UmFMOE1NeDVqVjVUYUluSWpqOFNLS3N3VEVOOGcxaU9FY1EiLCJjcnYiOiJQLTI1NiIsIngiOiJMX0F3SklGeDZWUEk1RklIZFBwSnppLVZFNGdkUlhCU3Zld3ktTmhySFFFIiwieSI6IjF0czFnZENpTWhjUHI1WkJPSjNaSHdBY0YtUkJPVVd6MjJGX296SGRjbk0iLCJ1c2UiOiJzaWciLCJhbGciOiJFUzI1NiJ9LCJhbGciOiJFUzI1NiJ9.eyJodHUiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3BlcnNvbi85MTUyNjdmMC01OTM5LTAyMzAtNzhlNy1iOGNkYmFhYjg1MTgiLCJodG0iOiJHRVQiLCJqdGkiOiJxc21vU21BVzF6WmtCTHNBUEZUWU8xNFQ1Ukl3eWxHQXFueHdCb3ViIiwiaWF0IjoxNjY3MjAxNjg5LCJleHAiOjE2NjcyMDE4MDksImF0aCI6InNGdjVQYnhGbXJKQ3BFY1pQYzA0aXNfWTdfOXJUMkk3Z2ZMVlNtMHI4djAifQ.MoMtWxT7igolVcGPY7qe15kyi5DxAz1XaJKlvip3b4H0E7RzwL38UE9u6nv3afMgGxQkOhWHU8tZigxlfk3lg"
}
```

**STEP 3** Combine both "Authorization" and "DPoP" into the header of your /person API request, and you should see something like this in the onscreen logs:

Copy to clipboard

```
{
  "Cache-Control": "no-cache",
   
  "Authorization": "DPoP eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IkFGTW5uS1JXVGFCWUVoTmZFQjZpUTVFckMxeXFHVnlaY2hIOEE3bmxfeU0ifQ.eyJzdWIiOiI5MTUyNjdmMC01OTM5LTAyMzAtNzhlNy1iOGNkYmFhYjg1MTgiLCJqdGkiOiJvMkZaVUpmSFZWVjA3aFpLTFZrc2Yxd0RBYnNUUUtWblFXM3RjZDI5Iiwic2NvcGUiOiJ1aW5maW4gbmFtZSBzZXggcmFjZSBuYXRpb25hbGl0eSBkb2IgZW1haWwgbW9iaWxlbm8gcmVnYWRkIGhvdXNpbmd0eXBlIGhkYnR5cGUiLCJleHBpcmVzX2luIjoxODAwLCJhdWQiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3BlcnNvbiIsInJlYWxtIjoibXlpbmZvLWNvbSIsImlzcyI6Imh0dHBzOi8vdGVzdC5hcGkubXlpbmZvLmdvdi5zZy9zZXJ2aWNlYXV0aC9teWluZm8tY29tIiwiY2xpZW50Ijp7ImNsaWVudF9pZCI6IlNURzItTVlJTkZPLVNFTEYtVEVTVCIsImNsaWVudF9uYW1lIjoiTXlJbmZvIFNlbGYgVGVzdCBBcHAgR0NDIiwiZW50aXR5X3VlbiI6IlQxNkdCMDAwMkciLCJlbnRpdHlfbmFtZSI6IkdvdlRlY2gifSwiY25mIjp7ImprdCI6ImhHdHN1S3h3UmFMOE1NeDVqVjVUYUluSWpqOFNLS3N3VEVOOGcxaU9FY1EifSwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ1c2UiOiJlbmMiLCJraWQiOiI3VGt5TWFqV0JYUlo3aVpmZ3lQUGZmMmdMMzloMlh0ZkpEemNzNXRjZXJNIiwieCI6Ik5mSXhKdWRCTzFfWEQ0RG5oa1ZLUG9uSHV4MExHMTJPM0QtWjJOZnN1RUUiLCJ5IjoiMkhHNmV5SmNFRUJWWlVwMVlsRjU3TFdNbEFJbXlTdU41d1FjZUVybW85OCIsImFsZyI6IkVDREgtRVMrQTI1NktXIn0sImlhdCI6MTY2NzIwMTY4OCwibmJmIjoxNjY3MjAxNjg4LCJleHAiOjE2NjcyMDM0ODh9.0CMpP4Whxk11XTMxg1fz6Srw2HkPiY-t2Tydb8ouQVpCwMNe6DW3Mu6KBdOo00ipa7Nlhw375zwmWAIT-8-3CQ",
   
  "DPoP": "eyJ0eXAiOiJkcG9wK2p3dCIsImp3ayI6eyJrdHkiOiJFQyIsImtpZCI6ImhHdHN1S3h3UmFMOE1NeDVqVjVUYUluSWpqOFNLS3N3VEVOOGcxaU9FY1EiLCJjcnYiOiJQLTI1NiIsIngiOiJMX0F3SklGeDZWUEk1RklIZFBwSnppLVZFNGdkUlhCU3Zld3ktTmhySFFFIiwieSI6IjF0czFnZENpTWhjUHI1WkJPSjNaSHdBY0YtUkJPVVd6MjJGX296SGRjbk0iLCJ1c2UiOiJzaWciLCJhbGciOiJFUzI1NiJ9LCJhbGciOiJFUzI1NiJ9.eyJodHUiOiJodHRwczovL3Rlc3QuYXBpLm15aW5mby5nb3Yuc2cvY29tL3Y0L3BlcnNvbi85MTUyNjdmMC01OTM5LTAyMzAtNzhlNy1iOGNkYmFhYjg1MTgiLCJodG0iOiJHRVQiLCJqdGkiOiJxc21vU21BVzF6WmtCTHNBUEZUWU8xNFQ1Ukl3eWxHQXFueHdCb3ViIiwiaWF0IjoxNjY3MjAxNjg5LCJleHAiOjE2NjcyMDE4MDksImF0aCI6InNGdjVQYnhGbXJKQ3BFY1pQYzA0aXNfWTdfOXJUMkk3Z2ZMVlNtMHI4djAifQ.MoMtWxT7igolVcGPY7qe15kyi5DxAz1XaJKlvip3b4H0E7RzwL38UE9u6nv3afMgGxQkOhWHU8tZigxlfk3lg"
}
```

Once this is ready, you may call our /person API and receive the JWE response of the data, which requires decoding and decrypting in the next step.&#x20;

### 4.2 Response

* Response Type: application/json

Copy to clipboard

```
eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiI3VGt5TWFqV0JYUlo3aVpmZ3lQUGZmMmdMMzloMlh0ZkpEemNzNXRjZXJNIiwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoibUVaMHhpRmQ4SV9nbERTVDRYWHZaUTgwN2E4X1lpN0ZaYkxmdnhZUEtJZyIsInkiOiJoNEEtOV9tYndJeVQ3UlVnVzNBVV9fQjg2TFYyWUhTWFlZN1l6ekEtX2NjIn19.-tkyW9doM-nvfi5iLIX30livPwFb4Ocpj_sH9lf3EBT_665a4obEiQ.YInOs5ZA_wA0kfAA.ESz3K9C-K7BUtifjT-sLlam7sddzAmpfW0QeF5oDrDYOLJXwgwCYbZCwXP7BBkI0TbccTdatQja76Vs2Y-OWsSDS-AOvg46HWUmUkSnzQAREJ_fxPGhDhDLvmBwLl4Y64zVOHDwZFC9dfnJAH8_2ezM03kqatw1gjs5gmipaicdoGZNA3doy33J6W2uAnjl6eunw47ABlu1PKdizumYnISZjPYWxIGLI3BMSfQSo9arvXT9R7sodhmVMb_KlRG9tnbqazvXwjafRs4B9moT7a2pTNts2hVKZ72Oknl-YpED4pkmx7IoV8CUHU0JIrtAnD_fkZlAl1zUSYtJgy7EXJ11T-UktkBWGzXswQQm913YV0ZYiwBkK80exOoGq-40YTDcFnhAqAJQW3N7Ro2nX4Mk4ujBxtxB-j25rtYmIG1-lU0MPepTzFrTLupzrslkPHyfW8a5LystczDLPH7ryCYUAKw1ex87Wbf784mmkd62QfxLjAhvK3fHh0MA_naOBoIzX89o7B2EjAZ015YJvsIKRPb2JM-Y1_Ll5mFmxttMk17ItjDfcxCqQE9dU_4_X3Z8A6LW0HOSMjrIop-9WvmWKCK3DzpgWw_x4H7dlbTPsOKM7cVnP8_LqNMSmmxjskJeBZ4XMOG9G273RvrZbgA8POS0zESTvkrwULTwPFr4fsfDP8t82WWBzsuwuXXNqE_BE-McfoyZJZ-a6iWbMyp8b3CSrLj5neCYHQSGJ14ZJagfOoz8BgTzqJxUoeQdg6K14bdP2Wdwu32q207al7riw35tFU45WFy8lUuIKURsznadUeyG1GzBJ6Rl7zjVmFmtGReawCbGrFLZDxkHl6520YbDVHqnjHbBX4vnneoISdx3YhSHdd08rHNSOPPOrbpv22bWsLCr-6PKZzzM9XG4J4oloDxwMZgwJ-fmExlCwRml9aywlEArbs0UqLdjC9mtngNb4Sw1kNhUleVzXRD3qkKZj1Zzzei-oHN-LEz9hWVMtAdy-bpuq8eVYt437Td2IQnCMQ-f3hA8FqaASLVlfjrbNm0GwRQpki3s6hA2FlUEXlE3RGyOYB9Z9jyf8AB1WQ9QfWpOPUNKlf8pmqS7f-Ym0EVabTFtTT-QNHXWo5CAQ1RZ7K_sxmiLSiMsE-V6V7DFjq0b7bXPiCFbKAyJW21gC_t_G8Shg7nzXtxKY2YEOCFMOjn-RsnQAWYlJZ9sCpiL3PoueLdK2ouAq9KebqpP-syM8jlwTh6ZrL8k_InYCSZAWvCRdqf85hu4qoKxTFd7biVpeJQ1fQb9sLGHihSMx3_kOOsS-OUctuVy_nElcuFaVy4vGk6bjDetED8egwwQZn3oRtbrQeye0filIYw_hcJyXzwNzGKUox7C8aIV6-Mi4x0fJTQPPJrJyEU4fSJC9auGOi75CWPQOf-Kd8GOpr8vLQ8FULaPB3S1zVfhXN7q08Qcp_MolotPPFfBhn7VMM7ai5JG4vhB-oti3gsih4xaIDiYK98Nitqp_OnY34keiEjzxWL8PQJugTyXiGuM6Gft-Xu07OrOzYC-CqtX7QOUhLSSQefP1HhyvuSAocCvgWQ2Q7EydphmlCJAgzlIwXtePcQ-YKqM_bbJ5TZmD_of4T9-Ab-VwNdgcor_Ro1rq3c6zbzTsKxaJ1SeHRSzIfyfz854TbZd4PiJwERYp4dSt-I-sPW21h90CJXCujS--2QzgVeOkSHlUI94dkl54-ahiKd8UlnU_N24_uVsiVYpqkh2Ouce8uy9FRQAL6ZRh5bOC78GWKQEyMvMDWEZl8myrlSiKWm4OFH65hiBZx6uoNIramaMKQNVZOMFLiTUCOoqJc_Xk-LrNzh7FNdfzP9NgbqfPdwKwVeuy4lWLttYOq2UHXVIU_u4aHEjkUuGVO0O2Fz_Ig_pIyTSIQGkhTC7MQjzWfMTuUCPphh4x7bO74VzqprsN35TxxOVvD9iTpDZ-kg5fJ53j2f5G413q8JmCMHhf3rqX7N8bPTHXlkvHoeCMwc7TMyU4ugJOzxQgMqoO78iWHhr4PxriotwB3vvnvzMsg4fVPRzwUWiD_adBhWB_ZZOnoxQHftb9fmcIP6DGyNne11_4VsuIPmifdSDixBVV6AOk39hkQDbBMQctGPat2TXVo8kl3vg_sgqkTDobccEWT5YnQ3XRpQCrD7V9Z5P9u64_rSeFxz1dBLFHe39sytwFtJT-NzhDAN_5UWyNln5uS-R5WtNARjP5b7W50oQntUql1smZiH3o-xqittFs-QoPeH94D5qtLUpK-XF1fWFJrNaL_GhVBkH0S56fYGfceDs-JZ73AePN5lNbFBVLVuA55QMzBHM_Y8k7zcu6cWIRa15z3UdariVcGXsaurFfTYpP0ABmKtJPbBotEEBWb-N7gvdXuH25MLpEXtqjh6GLXcuRMwIUeQ9mcQKFjh2tJF0jf4kEnMsVs9XtK8pO47owp0TAR1iLre80ryuLcbaSoj_Cm4T5IJORuURKftjfQsoC9NMpPLV8dJrBT0hjv2QgZrQmjyZ1lZwZa1cjVy2_o72epuJsdSgf_aSJ1Pq7ucHnr9WnOmvlwU0IWQ.bjsOSR3XIMI6WMNkJ2gCqg
```

The response payload from our /person API (for test and production environments) is first signed, then encrypted:

* Signing is done using the JWS (JSON Web Signature) format
* Encryption is done using the JWE (JSON Web Encryption) Compact Serialization format

Encryption protects the data at rest, while a signed payload means, if necessary, you can pass this signed payload to a 3rd party where they can verify the payload's integrity with our public JWKS.<br>

**4.2.1 Decrypt & Verify the Person Response**\
\
To read the payload, you have to perform the following steps in order:

* **STEP 1**: Decrypt the payload with your application's private key (Reference: [JWE](https://api.singpass.gov.sg/library/myinfo/developer/technical-concepts/jwt))
* **STEP 2**: Validate the decrypted payload signature with Myinfo public key (JWKS URI) (Reference: [JWS](https://api.singpass.gov.sg/library/myinfo/developer/technical-concepts/jwt))

After the above steps, your application can extract the payload in JSON format.

After which, you should see the response as below in the logs.&#x20;

Copy to clipboard

```
{
  "uinfin": {
    "lastupdated": "2022-10-27",
    "source": "1",
    "classification": "C",
    "value": "S6005048A"
  },
  "name": {
    "lastupdated": "2022-10-27",
    "source": "1",
    "classification": "C",
    "value": "ANDY LAU"
  },
  "sex": {
    "lastupdated": "2022-10-27",
    "code": "M",
    "source": "1",
    "classification": "C",
    "desc": "MALE"
  },
  "race": {
    "lastupdated": "2022-10-27",
    "code": "CN",
    "source": "1",
    "classification": "C",
    "desc": "CHINESE"
  },
  "nationality": {
    "lastupdated": "2022-10-27",
    "code": "SG",
    "source": "1",
    "classification": "C",
    "desc": "SINGAPORE CITIZEN"
  },
  "dob": {
    "lastupdated": "2022-10-27",
    "source": "1",
    "classification": "C",
    "value": "1988-10-06"
  },
  "email": { 
    "lastupdated": "2022-10-27",
    "source": "4", 
    "classification": "C", 
    "value": "" 
  },
  "mobileno": {
    "lastupdated": "2022-10-27",
    "source": "4",
    "classification": "C",
    "areacode": { "value": "" },
    "prefix": { "value": "" },
    "nbr": { "value": "" }
  },
  "regadd": {
    "country": { "code": "SG", "desc": "SINGAPORE" },
    "unit": { "value": "10" },
    "street": { "value": "ANCHORVALE DRIVE" },
    "lastupdated": "2022-10-27",
    "block": { "value": "319" },
    "source": "1",
    "postal": { "value": "542319" },
    "classification": "C",
    "floor": { "value": "38" },
    "type": "SG",
    "building": { "value": "" }
  },
  "housingtype": {
    "lastupdated": "2022-10-27",
    "code": "",
    "source": "1",
    "classification": "C",
    "desc": ""
  },
  "hdbtype": {
    "lastupdated": "2022-10-27",
    "code": "115",
    "source": "1",
    "classification": "C",
    "desc": "5-ROOM FLAT (HDB)"
  }
}
```

Once you have decrypted the JWE and verified the JWS, you will get the Person JSON data format and use this data to pre-fill your application form.

***

## Summary

You've successfully used the OAuth2.1 process to get the Person data from the Myinfo test environment. You are now ready to use the same method to integrate your application with Myinfo Production APIs.

{% hint style="info" %}
For Staging and Production APIs, please ensure you have different keypairs and different JWKS endpoints configured for each environment. Your business user/partner should submit these as part of the onboarding process.
{% endhint %}


# Resources


# Myinfo Connectors

Partners can refer to the following connectors to help your integration with Myinfo V4.

As onboarding for Myinfo v3/v4 is discontinued., we are no longer providing updates for these connectors.

| Language | Github Link                                              | Requirements      |
| -------- | -------------------------------------------------------- | ----------------- |
| NodeJS   | <https://github.com/singpass/myinfo-connector-v4-nodejs> |                   |
| Java     | <https://github.com/singpass/myinfo-connector-v4-java>   | Java 1.8 or later |


# Error Codes

During implementation, you may encounter various errors with Myinfo API. This can be caused by various reasons such as implementation issues, wrong input or environmental differences.&#x20;

All Myinfo APIs will return a standard HTTP error code together with an error message. The error code/message may change from time to time but it can be used for debugging.&#x20;

Troubleshooting and debugging of the APIs can be done in the following steps.&#x20;

1. Identification of which API is not working and an error is being returned from Myinfo Servers (e.g /authorize, /token, /person) Errors cound also occur due to
   * Connectivity errors (ensure there is no firewall blocking)
   * Incorrect urls and path parameters
2. Once an error is returned from Myinfo API, note down the error message and status code and utilise below table to debug
3. If issue persists or unable to resolve the issue, please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/)

***

## Authorize API

|            |               |                                                                                                                                                                                                                   |                                                                                                                                                                |
| ---------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Error Code | Error Message | Reason                                                                                                                                                                                                            | Remediation                                                                                                                                                    |
| 302        |               | <p>Possible to have the following error codes in the 'error' attribute.</p><ul><li>invalid\_scope : Invalid scope was requested in authorize URL</li><li>access\_denied: When user did not give consent</li></ul> |                                                                                                                                                                |
| 400        |               | Invalid parameters sent in authorize URL                                                                                                                                                                          | Verify querystring parameters are correct as per specifications(<https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#operation/getauthorize>) |
| 404        |               | Invalid client\_id sent in authorize URL                                                                                                                                                                          | Verify if client\_id used has been set to live in DPP and correct client\_id was passed in url                                                                 |
| 440        |               | You are not logged in, or your previous session has expired.                                                                                                                                                      | Verify session is still valid, expiry of 2mins and also verify that browser is passing session cookie during redirect                                          |
| 500        |               | Unexpected error.                                                                                                                                                                                                 |                                                                                                                                                                |

***

## Token API

|                                                                                                                                                                                                                                                                                                                                                                                |                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Error Code                                                                                                                                                                                                                                                                                                                                                                     | Error Message                                     | Reason                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Remediation                                                                                                                    |
| 400                                                                                                                                                                                                                                                                                                                                                                            | No body found for POST request                    | Body was not sent in request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Verify body was sent in request                                                                                                |
| <ul><li>Invalid client\_assertion</li><li>Missing jti in client\_assertion</li><li>Missing sub in client\_assertion</li><li>Invalid sub in client\_assertion</li><li>Missing aud in client\_assertion</li><li>Missing iat in client\_assertion</li><li>Missing exp in client\_assertion</li><li>Invalid exp in client\_assertion</li><li>Duplicate client\_assertion</li></ul> | Format of client\_assertion is incorrect          | <p>Verify client\_assertion format are correct as per specifications(<a href="https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Client-Assertion"><https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Client-Assertion></a>)<br><br>Utilize client\_assertion <a href="https://api.singpass.gov.sg/library/myinfo/developers/client-assertion-verifier">Generator/Verifier</a><br><br>Ensure client\_assertion is signature is correct (Need to be signed with private key corresponding to sign key configured in JWKS) <br><br>Ensure client\_assertion is used only once per transactiont</p> |                                                                                                                                |
| Invalid client\_assertion\_type                                                                                                                                                                                                                                                                                                                                                | Invalid client\_assertion\_type value passed in   | Verify value is "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                |
| Error Retrieving JWKS                                                                                                                                                                                                                                                                                                                                                          | Error retrieving JWKS from Myinfo Servers         | Ensure correct JWKS endpoint is configured onto DPP and is a public URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                |
| <ul><li>Invalid JWKS</li><li>Missing valid sig key in JWKS</li><li>Missing valid enc key in JWKS</li></ul>                                                                                                                                                                                                                                                                     | JWKS format is incorrect                          | <p>Ensure JWKS is returned as a JSON object with this format (<a href="https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Enhancements-in-v4"><https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Enhancements-in-v4></a>) <br><br>Ensure JWKS has at least 1 sign key with alg = 'ES256' and use = 'sig<br><br>Ensure JWKS has at least 1 encryption key with alg = 'ECDH-ES +A256KW' and use = 'enc'<br><br>Utilize <a href="https://api.singpass.gov.sg/library/myinfo/developers/jwks-verifier">JWKS verifier</a></p>                                                                         |                                                                                                                                |
| Missing DPoP Proof                                                                                                                                                                                                                                                                                                                                                             | DPoP Proof JWT is missing in headers              | Ensure DPoP Proof JWT is passed in correctly in HTTP headers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                |
| Missing  {param} from headers                                                                                                                                                                                                                                                                                                                                                  | Missing mandatory param in the HTTP header        | Verify specified mandatory param is passed in the HTTP header as per specifications (<https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#operation/gettoken>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                |
| Missing  {param} from body                                                                                                                                                                                                                                                                                                                                                     | Missing mandatory param in the HTTP body          | Verify specified mandatory param is passed in the HTTP header as per specifications (<https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#operation/gettoken>)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                |
| 401                                                                                                                                                                                                                                                                                                                                                                            | Unauthorized.                                     | App does not have access to this API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Ensure App is configured correctly and is live on DPP                                                                          |
| <ul><li>Invalid DPoP Proof</li><li>Missing jkt in DPoP Proof</li><li>Invalid jkt in DPoP Proof</li><li>Missing htm in DPoP Proof</li><li>Invalid htm in DPoP Proof</li><li>Missing htu in DPoP Proof</li><li>Invalid htu in DPoP Proof</li></ul>                                                                                                                               | Invalid DPoP Proof JWT format                     | <p>Verify DPoP Token format is correct as per specifications(<a href="https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Demonstration-of-Proof-of-Possesion-(DPoP)"><https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Demonstration-of-Proof-of-Possesion-(DPoP)></a><br><br>Utilize <a href="https://api.singpass.gov.sg/library/myinfo/developers/dpop-verifier">DPoP verifier</a><br><br>Ensure DPoP is signature is correct (Need to be signed with private key corresponding to public key embedded in JWT header) </p>                                                                   |                                                                                                                                |
| Invalid JWS Verification                                                                                                                                                                                                                                                                                                                                                       | Signature of DPoP or client\_assertion is invalid | <ul><li>Verify private key used to sign client\_assertion matches the sig key in JWKS</li><li>Verify kid in client\_assertion header matches the corresponding kid in JWKS</li><li>Verify JWK in DPoP Proof header is the correct public key to verify the private key</li></ul><p><br><br>Utilize <a href="https://api.singpass.gov.sg/library/myinfo/developers/dpop-verifier">DPoP verifier</a><br><br>Ensure DPoP is signature is correct (Need to be signed with private key corresponding to public key embedded in JWT header) </p>                                                                                                                              |                                                                                                                                |
| 404                                                                                                                                                                                                                                                                                                                                                                            | Not found.                                        | Invalid client\_id passed to API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Verify App is configured correctly on DPP and correct client\_id(ensure correct id is used in the correct environment) is used |
| 500                                                                                                                                                                                                                                                                                                                                                                            | Internal server error.                            | Unexpected error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                |

***

## Person API

|                                                                        |                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Error Code                                                             | Error Message                                                                                                                                                                                                                                                                                                        | Reason                                                                                                                                                                                | Remediation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 400                                                                    | Invalid Encyption key                                                                                                                                                                                                                                                                                                | Encryption key is of an Invalid format                                                                                                                                                | Ensure JWKS has at least 1 encryption key with alg = 'ECDH-ES +A256KW' and use = 'enc'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Missing DPoP Proof                                                     | DPoP Proof JWT is missing in headers                                                                                                                                                                                                                                                                                 | Ensure DPoP Token is passed in correctly in HTTP headers                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Duplicated DPoP-bound access\_token                                    | access\_token has already been used                                                                                                                                                                                                                                                                                  | access\_token is a one time use, ensure a new access\_token is retrieved for every API call                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Missing {param} from query parameters                                  | Missing mandatory param in the query parameters                                                                                                                                                                                                                                                                      | Verify specified mandatory param is passed in the query parameters as per specifications (<https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#operation/getperson>) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Missing {param} from headers                                           | Missing mandatory param in the HTTP headers                                                                                                                                                                                                                                                                          | Verify specified mandatory param is passed in the query parameters as per specifications (<https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#operation/getperson>) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 401                                                                    | <ul><li>Invalid DPoP Proof</li><li>Missing ath in DPoP Proof</li><li>Invalid ath in DPoP Proof</li><li>Missing jkt in DPoP Proof</li><li>Invalid jkt in DPoP Proof</li><li>Missing htm in DPoP Proof</li><li>Invalid htm in DPoP Proof</li><li>Missing htu in DPoP Proof</li><li>Invalid htu in DPoP Proof</li></ul> | Invalid DPoP Proof JWT format                                                                                                                                                         | <p>Verify DPoP Token format is correct as per specifications(<a href="https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Demonstration-of-Proof-of-Possesion-(DPoP)"><https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.0.html#section/Security/Demonstration-of-Proof-of-Possesion-(DPoP)></a><br><br>Utilize <a href="https://api.singpass.gov.sg/library/myinfo/developers/dpop-verifier">DPoP verifier</a><br><br>Ensure DPoP is signature is correct (Need to be signed with private key corresponding to public key embedded in JWT header) <br><br>Ensure DPoP is signed with the same private key used to create DPoP in /token call.</p> |
| 403                                                                    | DPoP-bound access\_token aud doesn't match with requested url                                                                                                                                                                                                                                                        | access\_token aud does not match resource being called                                                                                                                                | Verify correct access\_token matching service being called is used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DPoP-bound access\_token realm doesn't match with requested realm      | access\_token realm does not match resource being called                                                                                                                                                                                                                                                             | Verify correct access\_token matching service being called is used                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DPoP-bound access\_token subject doesn't match with requested sub      | access\_token sub does not match uuid being requested in API                                                                                                                                                                                                                                                         | Verify the same uuid is requested as provided in access\_token                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DPoP-bound access\_token scope doesn't match with requested attributes | access\_token scope does not match scope being requested in API                                                                                                                                                                                                                                                      | Verify the same scope is requested as provided in access\_token                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DPoP-bound access\_token invalid                                       | access\_token is of an invalid format                                                                                                                                                                                                                                                                                | Verify the access\_token passed in API request is correct and from /token response                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 404                                                                    |                                                                                                                                                                                                                                                                                                                      | Requested sub's data may not be available                                                                                                                                             | Verify the access\_token passed in API request is correct and from /token response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 500                                                                    | Internal server error.                                                                                                                                                                                                                                                                                               | Unexpected error.                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

<br>


# FAQ

## Q1. I am currently using Myinfo v3. When is the deadline to upgrade to Myinfo v4?

Rps on Myinfov3/v4 will need to migrate to Myinfo v5 by 30 Sept 2025.

***

## Q2. I encountered an error while developing my digital service integrating with Myinfo APIs, who can I contact?

For troubleshooting, you may refer to the [error codes page](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v4/resources/error-codes) with the possible causes.

Please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/)if you encounter error with the implementation.

***

## Q3. My Enterprise Architecture design requires whitelisting of Myinfo APIs IP address. What is the IP address that I should whitelist?

Myinfo APIs does not support IP whitelisting as our API Gateway is using dynamic IPs. Please whitelist the following Fully Qualified Domain Names (FQDN) instead:

* test.api.myinfo.gov.sg
* api.myinfo.gov.sg

***

## Q4. How frequent does Myinfo APIs get updated? How do I get notified when there is a new version of Myinfo APIs? Can I continue to use the older API version even if a newer version is released?

The Government plans to make Myinfo more useful for digital transactions by progressively including other frequently-used profile data.

When a new version of APIs is released, there will be a transition period for digital services to migrate to the latest version. The earlier API version is usually deprecated 6 months after the new version is released.

Please ensure that your support emails are registered in your app to receive important announcement such as Myinfo new version or new data items release.

***

## Q5. Does Myinfo APIs support native mobile application?

Myinfo APIs currently only support web-based integration.

***

## Q6. Is there any requirement for the JWKS? Can we use the same url endpoint for our staging and production environments?Please ensure that JWKS URL :

* Is served behind HTTPS on port 443 using a TLS server certificate issued by a standard publicly verifiable CA issuer (no private CAs), with complete cert chain presented by the server
* Is publicly accessible (no IP whitelisting, mTLS or other custom HTTP header requirements outside standard HTTP headers such as Content-Type, Accept)
* Is able to respond in a timely fashion
* Contains at least 1 sig key with alg ES256
* Contains at least 1 enc key with alg ECDH-ES+A256KW

Due to security reasons, we recommend that you have a different JWKS URL for both staging and production environment

***

## Q7. How can I rotate my Signing Keys?

Relying parties can rotate their signing keys in a self-driven manner. To do this with zero downtime the Relying party must

* support use of JWKS URLs and be onboarded as such
* ensure their replacement signing key has a different key ID (kid) to the original key
* ensure their replacement signing key matches the other cryptographic key requirements

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Prep          | Relying party generates a new signing key pair (K2) supported for signing.                                                           |
| T0            | Relying party adds public key K2 to its JWKS endpoint (and leaves K1 on the endpoint)                                                |
| T0 - T+1 hour | Myinfo’s cache will expire, and re-retrieves the relying party’s published keys from their JWKS endpoint which now includes K2       |
| > T+1 hour    | Relying party changes their system to start signing client assertions using the new signing key K2                                   |
| Clean Up      | Post-validation, relying party can remove key K1 from their JWKS endpoint when they are comfortable their new signing key is working |

***

## Q8: How can I rotate my Encryption Keys?

Relying parties can rotate their encryption keys in a self-driven manner. To do this with zero downtime the Relying party must

* support use of JWKS URLs and be onboarded as such
* have the ability to decrypt tokens produced with either one of two different encryption keys based on either
  * selecting the correct decryption key by its key ID (kid)
  * trial-and-error decryption against multiple keys in a collection
* ensure their replacement key matches the other cryptographic key requirements noted above

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                                     |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new encryption key pair (K2) supported for decryption. The existing key pair (K1) is still available for decryption of ID tokens |
| T0            | Relying party removes public key K1 and adds public key K2 on its JWKS endpoint                                                                            |
| T0 - T+1 hour | NDI’s caches will expire at any (indeterminate) time within this period, and start encrypting tokens with new encryption key K2.                           |
| T0 - T+1 hour | Relying party may be receiving tokens encrypted with either K1 or K2 keys throughout this period; and must be able to decrypt either.                      |
| > T+1 hour    | Relying party can remove support for decrypting with the previous K1 key                                                                                   |

***

## Q9. I am trying to decrypt the JWE response string returned from Myinfo Person API. However, I am getting the following error message:

```
*A256M is not valid algorithm*
```

The library that you are using to decrypt the response string might not support A256GCM algorithm. Please use a library that supports the algorithm.

***

## Q10. My architecture design requires trusting of Myinfo web SSL certificate. Where can I retrieve the certificate?

We recommend that your application trust / pin against the [root certificates](https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/amazonrootcas.zip) instead, as the web SSL certificates will be renewed from time to time.

***

## Q11. What are the requirements for callback URLs in the app configurations submission?

Please note the following requirements for callback URLs submission:

* Use different callback URLs in staging and production environments.
* Use static callback URLs (i.e. dynamic callback URLs are not supported)
* Use Fully Qualified Domain Names (FQDN) for both the staging and production callback URLs (i.e. static IP address or port numbers in callback URLs are not supported)
* Multiple callback URLs may be submitted for each environment.
* Use the default pre-configured <http://localhost:3001/callback> as staging callback URL for localhost testing. We do not support other localhost port and http configurations.

***

## Q12. There is no 'state' parameter in /authorize. How can I identify the specific request?

You are required to maintain a session with the user's frontend browser. This can also be used to tie the correct code\_verifier to code\_challenge ([PKCE](https://api.singpass.gov.sg/library/myinfo/developers/pkce))

***

## Q13. How may I test that my app is able to support cases where additional security verification with Singpass Face Verification is required?

To ensure that SFV works for your Myinfo user journeys, you may verify that camera permissions are enabled through the following methods:

1. Staging: Test additional Singpass Face Verification through the link provided on the Mockpass page
2. Production: Test that SFV works for the Myinfo user journey on different modalities (e.g. mobile/computer browser, native mobile app). You can test SFV through the following steps:\
   a. Initiate the Myinfo user journey in your linked up service with the above App IDs\
   b. Log in with your Singpass ID and password instead of the QR code\
   c. Select Singpass Face Verification as the 2FA method instead of SMS OTP

***

## Q14. What are the supports available for me to conduct performance testing?

Performance Testing in Production environment is strictly not allowed. Please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/)if you are planning to conduct performance testing in Test environment.

***

## Q15. Who do I contact if I require more details?

If you have any other query, please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/).


# Myinfo v3

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FRZv6EqPB2HaAsJaOfkyY%2Fimage.png?alt=media&amp;token=843751d4-a5bf-43ee-a95d-5d6115e1f34c" alt=""><figcaption><p>Logical overview of Myinfo v3</p></figcaption></figure>

## Understanding OAuth 2.0 flow for Myinfo APIs

Integrating with Myinfo requires your application to invoke 3 different APIs as part of the OAuth2.0 authorisation code flow:

### 1. Authorise

This API triggers the Singpass authentication process, followed by presenting a consent page to the user to obtain explicit consent from the user to allow his/her personal details to be released to your application.

At the end of this process, our system will return to you a short-lived "authorisation code".

{% hint style="info" %}
This API is triggered over the browser via 302 redirect.
{% endhint %}

### 2. Token

This API is invoked by your application server to obtain an "access token", which can be used to call the person API for the actual data. Your application needs to provide a valid "authorisation code" from the authorise API in exchange for the "access token".

The "access token" will be valid for 30 minutes.

{% hint style="info" %}
This API is a server-to-server call (does not go through browser)
{% endhint %}

### 3. Person

This API returns a JSON response with the personal data that was requested. Your application needs to provide a valid "access token" in exchange for the JSON data.\
Once your application receives this JSON data, you can use this data to populate the online form on your application.

{% hint style="info" %}
This API is a server-to-server call (does not go through browser)
{% endhint %}

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FHClkFMhccHgr3nGhIHZV%2Fimage.png?alt=media&amp;token=9fbd5621-efa5-4f46-8a4f-8c8d793d63ee" alt=""><figcaption><p>End-to-end Myinfo sequence diagram</p></figcaption></figure>


# Technical Guidelines

## 1. Transaction Log

Digital services which have integrated with Myinfo should track and store user transactions for potential issue management.

The following are some of the suggested minimum fields for tracking:

* UUID, Partial NRIC/FIN or NRIC/FIN (as relevant to usage under PDPA guidelines)
* Fields requested from Myinfo
* Time Stamp

In the event of user feedback or contact, these transaction logs may be requested by Myinfo to reconcile and resolve issues raised by the user.

***

## 2. X.509 Public Key

To implement RS256 (RSA Signature with SHA-256) Digital Signature for Myinfo APIs in your apps, please use a X.509 Public Key Certificate with RSA key size of 2048 bits or larger from one of the following compatible Certificate Authority (CA):

* Comodo/Sectigo
* digiCert
* GeoTrust
* GlobalSign
* [Netrust](https://www.netrust.net/netrust-singpass-myinfo-certificates)\*
* Thawte
* VeriSign

\*Certificate must be issued by Netrust. Entrust-issued certs are not accepted.

{% hint style="danger" %}
ECC and ECDSA Public Key Certificates are currently NOT supported.
{% endhint %}

***

## 3. TLS & Cipher Suites

**IMPORTANT:** In line with contemporary industry best practices, Myinfo supports TLS 1.2.

The list of supported strong cipher suites include:

* TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256
* TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

***

## 4. Callback URLs

For security reasons:

* Different callback URLs should be used for staging and production environments
* Fully Qualified Domain Name (FQDN) of staging and production environments should be used (i.e. instead of IP address)
* Callback URLs should not contain Hash (#) or Wildcard (\*) characters

***

## 5. Mobile App integration

* Myinfo offers integration via browser redirections. Native application integration is not supported.
* Integration should be done via in-app browser (not WebViews) or external browser.
* For services integrating on Android, setDomStorageEnable should be enabled.
* Camera permissions for your app must be enabled to support cases where additional security verification with Singpass Face Verification is required.


# API Specifications

Please see [API Specification v3.2](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.2.html) for indepth specification

{% openapi src="/files/NvZfEpGj9Yy9a9PrlOAT" path="/com/v3/authorise" method="get" %}
[swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FA5p95JAUNe42YGxRDDNv%2Fswagger.json?alt=media\&token=19a82e6a-a412-4bda-aa85-b2599380b628)
{% endopenapi %}

{% openapi src="/files/NvZfEpGj9Yy9a9PrlOAT" path="/com/v3/token" method="post" %}
[swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FA5p95JAUNe42YGxRDDNv%2Fswagger.json?alt=media\&token=19a82e6a-a412-4bda-aa85-b2599380b628)
{% endopenapi %}

{% openapi src="/files/NvZfEpGj9Yy9a9PrlOAT" path="/com/v3/person/{sub}/" method="get" %}
[swagger.json](https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FA5p95JAUNe42YGxRDDNv%2Fswagger.json?alt=media\&token=19a82e6a-a412-4bda-aa85-b2599380b628)
{% endopenapi %}


# Latest X.509 Public Key Certificate

Our last public key certificate has expired on 07 Nov 2024

Please download the latest Public Key Certificate here

{% file src="/files/H8s7FPPAcBBkzVhQ5WkO" %}

Once you are ready to deploy, follow the following steps (screenshot has been attached below)

1. Login to SDP
2. Edit affected application
3. Select "Renewed certificate"
4. Select Update

<figure><img src="https://1982108655-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fk67iNluSpweCPqhbIY5t%2Fuploads%2FjZdwd2EtKARuARId6CLX%2Fimage.png?alt=media&amp;token=0c35f8a2-423a-4adc-be20-3768f76337ba" alt=""><figcaption><p>Certificate selection on Application Configuration page</p></figcaption></figure>


# Tutorials

{% content-ref url="/pages/r2O4pLuQpLOpIZ6JoNWU" %}
[Tutorial 1: Basic Person API](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v3/tutorials/tutorial-1-basic-person-api)
{% endcontent-ref %}

{% content-ref url="/pages/p8IAGQO9JE28tIO6OEAT" %}
[Tutorial 2: Using OAuth2](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v3/tutorials/tutorial-2-using-oauth2)
{% endcontent-ref %}

{% content-ref url="/pages/6F5YEMpuaYEXiTx6gaow" %}
[Tutorial 3: Implementing PKI Digital Signature](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v3/tutorials/tutorial-3-implementing-pki-digital-signature)
{% endcontent-ref %}


# Tutorial 1: Basic Person API

In this tutorial we will try to call a basic API to get a sample Person JSON response. You can then use this JSON object in your application to pre-fill your online application form.

***

## 1. Invoke the Sandbox Person API

Open another browser window and type in the following URL:

```
https://sandbox.api.myinfo.gov.sg/com/v3/person-sample/S9812381D
```

This will call our sandbox API using HTTPS GET.

`S9812381D` is the *UINFIN* (NRIC or FIN) parameter which refers to the ID of the person you wish to get the data of. For this sample API, the following *UINFIN* are supported:

* S9812381D
* S9812382B
* S9812385G
* S9812387C
* S9912363Z
* S9912366D
* S9912369I
* S9912370B
* S9912372I
* S9912374E
* S6005053H
* S6005055D
* S9812379B
* F1612347K
* G1612348Q
* G1612349N
* G1612350T
* G1612352N
* G1612353L

Please refer to our [API specifications](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.2.html) for this tutorial.

***

## 2. Verify the JSON response

You should get a response JSON file which looks like this:

**Sample JSON for Person data**

```
{
  "uinfin": {
    "lastupdated": "2019-03-26",
    "source": "1",
    "classification": "C",
    "value": "S9812381D"
  },
  "name": {
    "value": "TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinname": {
    "value": "CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "aliasname": {
    "value": "TRICIA TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinaliasname": {
    "value": "TRICIA CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marriedname": {
    "value": "",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "sex": {
    "code": "F",
    "desc": "Female",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "race": {
    "code": "CN",
    "desc": "CHINESE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "secondaryrace": {
    "code": "EU",
    "desc": "EURASIAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dialect": {
    "code": "SG",
    "desc": "SWISS GERMAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "nationality": {
    "code": "SG",
    "desc": "SINGAPORE CITIZEN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dob": {
    "value": "1958-05-17",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "birthcountry": {
    "code": "SG",
    "desc": "SINGAPORE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "residentialstatus": {
    "code": "C",
    "desc": "Citizen",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportnumber": {
    "value": "E35463874W",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportexpirydate": {
    "value": "2020-01-01",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "regadd": {
    "type": "SG",
    "block": {
      "value": "548"
    },
    "building": {
      "value": ""
    },
    "floor": {
      "value": "09"
    },
    "unit": {
      "value": "128"
    },
    "street": {
      "value": "BEDOK NORTH AVENUE 1"
    },
    "postal": {
      "value": "460548"
    },
    "country": {
      "code": "SG",
      "desc": "SINGAPORE"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  ...
}
```

***

## 3. Using the JSON Object

Try using the JSON object in your own application to prefill your forms!

***

## Summary

You've successfully called a basic Person API and gotten a sample JSON response from Myinfo.

Before trying out Tutorial 2, you will need to understand the OAuth Process.


# Tutorial 2: Using OAuth2

{% hint style="info" %}
Note: Make sure that you have completed Tutorial 1 and familiarised yourself with the Person JSON schema, and that you have understood the OAuth Process first.
{% endhint %}

For this tutorial, you will need to call the APIs from your server-based (or running from localhost) application.

Myinfo uses [OAuth2.0](https://oauth.net/2/) for our Authentication and Authorisation flow.

Please refer to our [API specifications](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.2.html) for this tutorial.

***

## 1. Download our Sample Client Application

For the purposes of the tutorial, please download our sample client application from [Github.](https://github.com/singpass/myinfo-demo-app)

### **1.1 Install Node.js and NPM**

In order for the demo application to run, you will need to Install Node.js and NPM. Follow the instructions given by the links below depending on your OS.

* [Install Node.js and NPM for Windows](http://blog.teamtreehouse.com/install-node-js-npm-windows)
* [Install Node.js and NPM for Linux](http://blog.teamtreehouse.com/install-node-js-npm-linux)
* [Install Node.js and NPM for Mac](http://blog.teamtreehouse.com/install-node-js-npm-mac)

### **1.2 Run NPM install**

Run the following command in the folder you unzipped the application:

```
npm install
```

### **1.3 Start the Application**

**For Linux/MacOS**

Execute the following command to start the application:

```
./start.sh
```

**For Windows**\
\
Execute the following command to start the application:

```
.\start.bat
```

**Access the Application on Your Browser**\
\
You should be able to access the sample application via the following URL:

```
http://localhost:3001
```

***

## 2. Trigger MockPass Login and Consent (authorise API)

The authorise endpoint triggers the MockPass login and shows the consent page after successful login.\
Click on the "Retrieve Myinfo" button on the sample application.\
\
This calls the URL below (with some additional parameters):

```
http://sandbox.api.myinfo.gov.sg/com/v3/authorise
```

This calls the URL below (with some additional parameters):

| PARAMETER     | DESCRIPTION                                                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id    | unique ID for your application. For our sample application, this is `STG2-MYINFO-SELF-TEST`                                                                   |
| attributes    | comma separated list of attributes requested. Possible attributes are listed in the Person object definition in the API specifications.                       |
| purpose       | state the purpose of requesting the data. This will be shown to the Person when requesting for his consent                                                    |
| state         | identifier to reconcile query and response. This will be sent back to you via the callback URL. Use a unique system generated number for each and every call. |
| redirect\_uri | your callback URL for Myinfo to return with the authorisation code. For our sample application this is `http://localhost:3001/callback`                       |

Look at the file `views/html/index.html` in the sample application and look for the following lines of code:

The `index.html` file is the frontend (client side) code.

```
function callAuthoriseApi() {
  var authoriseUrl = authApiUrl + "?client_id=" + clientId +
    "&attributes=" + attributes +
    "&purpose=" + purpose +
    "&state=" + state +
    "&redirect_uri=" + redirectUrl;
     
  window.location = authoriseUrl;
}
```

This code triggers the authorise API.<br>

### **2.1 Login with MockPass**

Select this test ID and login using MockPass:

NRIC: `S9812381D`

You may also use test personas found in the Personas Page when testing Tutorial 2.

### **2.2 Consent Page**

Once you have successfully logged into MockPass, a consent page similar to the one below will be shown:

![](https://api.singpass.gov.sg/assets/api-lib/myinfo/img/home-revamp/consent-page-screenshot.png)

### **2.3 Get the Authorisation Code**

If you have followed the steps above correctly, the Consent Platform should return you an authorisation code by invoking your callback URL. You should now see something like this in your browser URL dialog:

```
http://localhost:3001/callback?code=e2369168-52da-421a-b70f-03f64e779c4b&state=123
```

Notice the parameter `code` is the authorisation code that your application will need to invoke the next API (token). In the example above, the authorisation code is `e2369168-52da-421a-b70f-03f64e779c4b`. We will use this authorisation code in the next token API call.

The **token** and **person** API calls will follow automatically once you have finished the consent page.

We will look at the code for these 2 APIs in the following sections.

## 3. Call the Token API (with the authorisation code)

Now that you have the authorisation code, you can invoke the token API to get the access token.

{% hint style="info" %}
Note: This API must be called from a server-side component. It cannot be called from the browser or mobile native client application due to security reasons (there is no secure place to store your private key).
{% endhint %}

Look at the code in the file `routes/index.js` in our sample client application and search for the following:

`index.js` is the backend (server side) code.

```
// function to prepare request for TOKEN API
function createTokenRequest(code) {
  var cacheCtl = "no-cache";
  var contentType = "application/x-www-form-urlencoded";
  var method = "POST";
  var request = null;
   
  // preparing the request with header and parameters
  // assemble params for Token API
  var strParams = "grant_type=authorization_code" +
    "&code=" + code +
    "&redirect_uri=" + _redirectUrl +
    "&client_id=" + _clientId +
    "&client_secret=" + _clientSecret;
  var params = querystring.parse(strParams);
   
   
  // assemble headers for Token API
  var strHeaders = "Content-Type=" + contentType + "&Cache-Control=" + cacheCtl;
  var headers = querystring.parse(strHeaders);
   
  // Sign request and add Authorization Headers
  var authHeaders = generateAuthorizationHeader(
    _tokenApiUrl,
    params,
    method,
    contentType,
    _authLevel,
    _clientId,
    _privateKeyContent,
    _clientSecret
  );
   
  if (!_.isEmpty(authHeaders)) {
    _.set(headers, "Authorization", authHeaders);
  }
   
  var request = restClient.post(_tokenApiUrl);
   
  // Set headers
  if (!_.isUndefined(headers) && !_.isEmpty(headers))
    request.set(headers);
   
  // Set Params
  if (!_.isUndefined(params) && !_.isEmpty(params))
    request.send(params);
   
  return request;
}
```

The code is creating the request to call the following API:

```
https://sandbox.api.myinfo.gov.sg/com/v3/token
```

{% hint style="info" %}
Note: This API is using HTTPS POST.
{% endhint %}

The parameters in the POST body are as follows:

| PARAMETER      | DESCRIPTION                                                                                                                            |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| grant\_type    | grant type for getting token (default "authorization\_code")                                                                           |
| code           | the authcode given by the authorise API.                                                                                               |
| redirect\_uri  | your callback URL for Myinfo to validate. For our sample application this is `http://localhost:3001/callback`                          |
| client\_id     | unique ID for your application. For our sample application, this is `STG2-MYINFO-SELF-TEST`                                            |
| client\_secret | secret key given to your application during onboarding. For our sample application, this is `44d953c796cccebcec9bdc826852857ab412fbe2` |

The sample application will then send the constructed request to the API Gateway, and you should see the following response from the onscreen logs:

```
Response from Token API:{"access_token":"eyJ0eXAiOiJKV1QiLCJ6aXAiOiJOT05FIiwia2lkIj
oiRWtnWkZDeG5taXY2T2JDZ3B4blRIRUkyK3FVPSIsImFsZyI6IlJTMjU2I
n0.eyJzdWIiOiJTOTgxMjM4MUQiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNT
X0d
SQU5UIiwiYXV0aF9sZXZlbCI6MCwiYXVkaXRUcmFja2luZ0lkIjoiYzNjOT
U1MjUtNzEwYS00ZjU3LWFhZTMtMzEzMjUwZDkxOWE3LTEzOTc3NiIsImlzc
yI6Imh0dHBzOi8vY29uc2VudC5jbG91ZC5teWluZm8uZ292LnNnL2NvbnNl
bnQvb2F1dGgyL3JlYWxtcy9yb290L3JlYWxtcy9teWluZm8tY29tIiwidG9
rZW5OYW1lIjoiYWNjZXNzX3Rva2VuIiwidG9rZW5fdHlwZSI6IkJlYXJlci
IsImF1dGhHcmFudElkIjoiZDVzZ3RWZHl1UFNOc0haTHJkYVUyMTAwTV9zI
iwiYXVkIjoibXlpbmZvIiwibmJmIjoxNTUzNTk0OTc4LCJncmFudF90eXBl
IjoiYXV0aG9yaXphdGlvbl9jb2RlIiwic2NvcGUiOlsiZWR1bGV2ZWwiLCJ
tb2JpbGVubyIsImFzc2Vzc2FibGVpbmNvbWUiLCJvd25lcnByaXZhdGUiLC
JuYXRpb25hbGl0eSIsImRvYiIsImNwZmNvbnRyaWJ1dGlvbnMiLCJlbWFpb
CIsInNleCIsImhvdXNpbmd0eXBlIiwiY3BmYmFsYW5jZXMiLCJuYW1lIiwi
cmVnYWRkIiwicmFjZSIsImhkYnR5cGUiLCJtYXJpdGFsIiwiYXNzZXNzeWV
hciJdLCJhdXRoX3RpbWUiOjE1NTM1OTQ3NzIsInJlYWxtIjoiL215aW5mby
1jb20iLCJleHAiOjE1NTM1OTY3NzgsImlhdCI6MTU1MzU5NDk3OCwiZXhwa
XJlc19pbiI6MTgwMCwianRpIjoieGRIN1QwSjI0TmFHS1FpWWVnNjcyREJf
ZGdrIn0.jbdjui3WLe-cwPRDCCR09ya5fK4UUntx31Y87PosGV_FTnKTmiy
_cYOeaVT
pjLmPx4ebo0fLooPHpKH_5_4lFPVaNdQkOGjvScV1fl04DR1UW0uutQubkI
alYW-WgmIDhQz4ZddXyLswUnGc7-eURR47VDzjiMr-ptcn0uSfrI1RNgnc8
kY12slOAE4bGxxmYE_PlBLQuZiCdORD9JKKjEKAptKVyQF7p9o6EAg2TQe4
cpwcDLXYUkwjLcaoEdCXmX16QICFm9RsVFaW_PRl29fY9ErxcN27UrRnj4m
qfbYUuRnN-W2e6DSnMfkZwMRKOlmPgD7fflfh5dnuNwGAXQ",
"scope":"edulevel mobileno assessableincome ownerprivate 
nationality dob cpfcontributions email sex housingtype 
cpfbalances name regadd race hdbtype marital assessyear",
"token_type":"Bearer","expires_in":1799}
```

Notice the response contains an "access\_token", which is in the JWT\_ \_ (JSON Web Token) format.

### **3.1 What is the JSON Web Token structure?**

JSON Web Tokens consist of three parts separated by dots (.), which are:

* Header
* Payload
* Signature

Therefore, a JWT typically looks like the following: `xxxxx.yyyyy.zzzzz`

The header and the payload are Base64Url encoded. The signature is created using these two, a secret and the hashing algorithm being used (as specified in the header: HMAC, SHA256 or RSA).

### **3.2 How can I parse the JWT?**

In order to parse the JWT you can use one of the libraries listed in the Libraries for Token Signing/Verification section of `JWT.io.`\_ \_

For example, in our sample application, which is implemented with Node.js, we use the `node-jsonwebtoken` library, and we call the `jwt.verify()` method. If the parsing fails then the library will return a JsonWebTokenError error with the message jwt malformed.

{% hint style="info" %}
Note: Many web frameworks (such as ASP.NET Core for example) have JWT middleware that handle the token validation. Most of the times this will be a better route to take, rather that resorting to use a third-party library, as the middleware typically integrates well with the framework's overall authentication mechanisms.
{% endhint %}

Look at the code in the file `lib/security/security.js` and search for the following code snippet:

```
// Verify & Decode JWS or JWT
security.verifyJWS = function verifyJWS(jws, publicCert) {
  // verify token
  // ignore notbefore check because it gives errors sometimes if the call is too fast.
  var decoded = jwt.verify(jws, publicCert, { algorithms: ['RS256'], ignoreNotBefore: true });
  return decoded;
}
```

This calls the library to parse the JWT and return the decoded JSON object, which is the **access token.**

You should see the decoded access token in the onscreen logs that looks like this:

```
Decoded Access Token:
{"sub":"9E9B2260-47B8-455B-89B5-C48F4DB98322","cts":"OAUTH2_STATELESS_GRANT","auth_level":0,"auditTrackingId":"c3c95525-710a-4f57-aae3-C48F4DB98322","iss":"https://consent.cloud.myinfo.gov.sg/consent/oauth2/realms/root/realms/myinfo-com","tokenName":"access_token","token_type":"Bearer","authGrantId":"d5sgtVdyuPSNsHZLrdaU2100M_s","aud":"myinfo","nbf":1553594978,"grant_type":"authorization_code","scope":["edulevel","mobileno","assessableincome","ownerprivate","nationality","dob","cpfcontributions","email","sex","housingtype","cpfbalances","name","regadd","race","hdbtype","marital","assessyear"],"auth_time":1553594772,"realm":"/myinfo-com","exp":1553596778,"iat":1553594978,"expires_in":1800,"jti":"xdH7T0J24NaGKQiYeg672DB_dgk"}
```

This access token is a representation of the permissions that was given by the user when he/she clicked on "I Agree" on the consent page.

Note:It is very important for your application to validate the signature of the JWT to ensure the response has not been changed in transit.

Notice the `sub` attribute in the JSON token. That is the **identifier** of the person who logged in via MockPass. We will use this identifier for the Person API call next.

***

## 4. Call the Person API (with the access token)

Now that you have the access token, you can invoke the person API to get the Person data.

Note:This API must be called from a server-side component. It cannot be called from the browser or mobile native client application due to security reasons (there is no secure place to store your private key).

This API call is essentially the same as the one you tried in Tutorial 1, except that here you will need to provide a valid access token or your API call will be rejected.

Look at the code in the file `routes/index.js` in our sample client application and search for the following:

`index.js` is the backend (server side) code.

```
// function to prepare request for PERSON API
function createPersonRequest(sub, validToken) {
  var url = _personApiUrl + "/" + sub + "/";
  var cacheCtl = "no-cache";
  var method = "GET";
  var request = null;
  // assemble params for Person API
  var strParams = "client_id=" + _clientId +
    "&attributes=" + _attributes;
  var params = querystring.parse(strParams);
 
  // assemble headers for Person API
  var strHeaders = "Cache-Control=" + cacheCtl;
  var headers = querystring.parse(strHeaders);
  var authHeaders;
 
  // Sign request and add Authorization Headers
  authHeaders = generateAuthorizationHeader(
    url,
    params,
    method,
    "", // no content type needed for GET
    _authLevel,
    _clientId,
    _privateKeyContent,
    _clientSecret
  );
 
  if (!_.isEmpty(authHeaders)) {
    _.set(headers, "Authorization", authHeaders + ",Bearer " + validToken);
  }
  else {
    // NOTE: include access token in Authorization header as "Bearer " (with space behind)
      _.set(headers, "Authorization", "Bearer " + validToken);
  }
 
  // invoke token API
  var request = restClient.get(url);
 
  // Set headers
  if (!_.isUndefined(headers) && !_.isEmpty(headers))
    request.set(headers);
 
  // Set Params
  if (!_.isUndefined(params) && !_.isEmpty(params))
    request.query(params);
 
  return request;
}
```

The code is creating the request to call the following API:

```
https://sandbox.api.myinfo.gov.sg/com/v3/person/9E9B2260-47B8-455B-89B5-C48F4DB98322/?client_id=STG2-MYINFO-SELF-TEST&attributes=name%2Csex%2Crace%2Cnationality%2Cdob%2Cemail%2Cmobileno%2Cregadd%2Chousingtype%2Chdbtype%2Cmarital%2Cedulevel%2Cassessableincome%2Chanyupinyinname%2Caliasname%2Chanyupinyinaliasname%2Cmarriedname%2Ccpfcontributions%2Ccpfbalances
```

**Note that this API is called using HTTPS `GET`.**

The additional query parameters are as follows:

| PARAMETER  | DESCRIPTION                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| client\_id | unique ID for your application. For our sample application, this is `STG2-MYINFO-SELF-TEST`                                             |
| attributes | comma separated list of attributes requested. Possible attributes are listed in the Person object definition in the API specifications. |

### **4.1 Providing the Access Token in the Request Header**

The access token should be provided in the *header* of your API call under "Bearer".

You should see something like this in the onscreen logs:

```
headers:{"Cache-Control":"no-cache","Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJ6aXAiOiJOT05FIiwia2lkIjoiRWtnWkZDeG5taXY2T2JDZ3B4blRIRUkyK3FVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJTOTgxMjM4MUQiLCJjdHMiOiJPQVVUSDJfU1RBVEVMRVNTX0dSQU5UIiwiYXV0aF9sZXZlbCI6MCwiYXVkaXRUcmFja2luZ0lkIjoiYzNjOTU1MjUtNzEwYS00ZjU3LWFhZTMtMzEzMjUwZDkxOWE3LTEzOTc3NiIsImlzcyI6Imh0dHBzOi8vY29uc2VudC5jbG91ZC5teWluZm8uZ292LnNnL2NvbnNlbnQvb2F1dGgyL3JlYWxtcy9yb290L3JlYWxtcy9teWluZm8tY29tIiwidG9rZW5OYW1lIjoiYWNjZXNzX3Rva2VuIiwidG9rZW5fdHlwZSI6IkJlYXJlciIsImF1dGhHcmFudElkIjoiZDVzZ3RWZHl1UFNOc0haTHJkYVUyMTAwTV9zIiwiYXVkIjoibXlpbmZvIiwibmJmIjoxNTUzNTk0OTc4LCJncmFudF90eXBlIjoiYXV0aG9yaXphdGlvbl9jb2RlIiwic2NvcGUiOlsiZWR1bGV2ZWwiLCJtb2JpbGVubyIsImFzc2Vzc2FibGVpbmNvbWUiLCJvd25lcnByaXZhdGUiLCJuYXRpb25hbGl0eSIsImRvYiIsImNwZmNvbnRyaWJ1dGlvbnMiLCJlbWFpbCIsInNleCIsImhvdXNpbmd0eXBlIiwiY3BmYmFsYW5jZXMiLCJuYW1lIiwicmVnYWRkIiwicmFjZSIsImhkYnR5cGUiLCJtYXJpdGFsIiwiYXNzZXNzeWVhciJdLCJhdXRoX3RpbWUiOjE1NTM1OTQ3NzIsInJlYWxtIjoiL215aW5mby1jb20iLCJleHAiOjE1NTM1OTY3NzgsImlhdCI6MTU1MzU5NDk3OCwiZXhwaXJlc19pbiI6MTgwMCwianRpIjoieGRIN1QwSjI0TmFHS1FpWWVnNjcyREJfZGdrIn0.jbdjui3WLe-cwPRDCCR09ya5fK4UUntx31Y87PosGV_FTnKTmiy_cYOeaVTpjLmPx4ebo0fLooPHpKH_5_4lFPVaNdQkOGjvScV1fl04DR1UW0uutQubkIalYW-WgmIDhQz4ZddXyLswUnGc7-eURR47VDzjiMr-ptcn0uSfrI1RNgnc8kY12slOAE4bGxxmYE_PlBLQuZiCdORD9JKKjEKAptKVyQF7p9o6EAg2TQe4cpwcDLXYUkwjLcaoEdCXmX16QICFm9RsVFaW_PRl29fY9ErxcN27UrRnj4mqfbYUuRnN-W2e6DSnMfkZwMRKOlmPgD7fflfh5dnuNwGAXQ"}
```

Once this is done, you should see the person JSON in the onscreen logs that looks like this:

```
Person Data (Decoded):
{"name":{"lastupdated":"2019-03-26","source":"1","classification":"C","value":"TAN XIAO HUI"},"sex":{"lastupdated":"2019-03-26","code":"F","source":"1","classification":"C","desc":"FEMALE"},"race":{"lastupdated":"2019-03-26","code":"CN","source":"1","classification":"C","desc":"CHINESE"},"nationality":{"lastupdated":"2019-03-26","code":"SG","source":"1","classification":"C","desc":"SINGAPORE CITIZEN"},"dob":{"lastupdated":"2019-03-26","source":"1","classification":"C","value":"1998-06-06"},"email":{"lastupdated":"2019-03-26","source":"2","classification":"C","value":"myinfotesting@gmail.com"},"mobileno":{"lastupdated":"2019-03-26","source":"2","classification":"C","areacode":{"value":"65"},"prefix":{"value":"+"},"nbr":{"value":"97399245"}},"regadd":{"country":{"code":"SG","desc":"SINGAPORE"},"unit":{"value":"128"},"street":{"value":"BEDOK NORTH AVENUE 4"},"lastupdated":"2019-03-26","block":{"value":"102"},"source":"1","postal":{"value":"460102"},"classification":"C","floor":{"value":"09"},"type":"SG","building":{"value":"PEARL GARDEN"}},"housingtype":{"lastupdated":"2019-03-26","code":"","source":"1","classification":"C","desc":""},"hdbtype":{"lastupdated":"2019-03-26","code":"113","source":"1","classification":"C","desc":"3-ROOM FLAT (HDB)"},"marital":{"lastupdated":"2019-03-26","code":"2","source":"1","classification":"C","desc":"MARRIED"},"edulevel":{"lastupdated":"2019-03-26","code":"3","source":"2","classification":"C","desc":"SECONDARY"},"ownerprivate":{"lastupdated":"2019-03-26","source":"1","classification":"C","value":false},"cpfcontributions":{"lastupdated":"2019-03-26","source":"1","history":[{"date":{"value":"2018-02-18"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2018-01"}},{"date":{"value":"2018-03-18"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2018-02"}},{"date":{"value":"2018-04-18"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2018-03"}},{"date":{"value":"2018-05-18"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2018-04"}},{"date":{"value":"2018-05-27"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2018-05"}},{"date":{"value":"2018-07-15"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-01"}},{"date":{"value":"2017-02-01"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-01"}},{"date":{"value":"2017-02-12"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-02"}},{"date":{"value":"2017-02-21"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-02"}},{"date":{"value":"2017-03-01"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-02"}},{"date":{"value":"2017-03-12"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-03"}},{"date":{"value":"2017-03-21"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-03"}},{"date":{"value":"2017-04-01"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-03"}},{"date":{"value":"2017-04-12"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-04"}},{"date":{"value":"2017-04-21"},"employer":{"value":"Crystal Horse Invest Pte Ltd"},"amount":{"value":500},"month":{"value":"2017-04"}}],"classification":"C"},"cpfbalances":{"oa":{"value":1581.48},"ma":{"value":11470.7},"lastupdated":"2019-03-26","source":"1","classification":"C","sa":{"value":21967.09},"ra":{"value":0}},"uinfin": {"lastupdated": "2019-03-26","source": "1","classification": "C","value": "S9812381D"
}}
```

***

## 5. Use the JSON object to Prefill Form

If you have followed the steps above correctly, you should have gotten the Person JSON object. Now you can use this JSON object to prefill the form values in your application.

Look at the code in our sample client application and you will see it is using the response JSON to prefill the values on the application form. Once this is done, the user just needs to submit the form and your application can save the values into your database for subsequent processing.

***

## Summary

You've successfully used the OAuth2 process to get the Person data from Myinfo sandbox environment.


# Tutorial 3: Implementing PKI Digital Signature

{% hint style="info" %}
Note: Make sure that you have completed Tutorial 1 and 2, and that you have understood the OAuth Process first.
{% endhint %}

Now that you have successfully used the OAuth2 process to get Myinfo Person data, the final step is to implement PKI digital signature in your server-to-server calls to Myinfo APIs.

Please refer to our [API specifications](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v3.2.html) for this tutorial.

You may use test personas found in the [Personas Page](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) when testing Tutorial 3.

***

#### Importance of Security

Security is of utmost importance for Myinfo. To enhance security, Myinfo APIs requires your application to implement PKI digital signature when calling our server-to-server APIs, namely, the **token** and **person** APIs.

Using PKI digital signature, we can ensure the following:

* The *caller* (your application) and the *receiver* (Our API Gateway) are both valid and trusted identities; i.e. they are who they say they are.
* The *request* (from your application) and the *response* (from Our API Gateway) has not been changed in transit.

***

#### What is PKI Digital Signature?

Digital signatures are like electronic “fingerprints.” In the form of a coded message, the digital signature securely associates a signer with a document in a recorded transaction. Digital signatures use a standard, accepted format, called Public Key Infrastructure (PKI), to provide the highest levels of security and universal acceptance. They are a specific signature technology implementation of electronic signature (eSignature).

***

#### **Public Key Infrastructure – PKI**

A cryptographic system that uses two keys, a public key known to everyone and a private key, the private key has full control to the key owner, and has to keep in secured environment. A unique element to the public key system is that the public and private keys are related in such a way that only the public key can be used to encrypt messages and only the corresponding private key can be used to decrypt them. Moreover, it is virtually impossible to deduce the private key if you know the public key.

***

#### Generating a Public/Private Keypair

The first step is to generate the public/private keypair for your app, based on your CA cert. Please refer to your CA certificate vendor for instructions on how to do so. Once this is complete, you should have the files similar to the list shown below:

| FILE NAME      | KEY TYPE                | COMMENTS                                                                                                                                                                                  |
| -------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| privatekey.key | private key             | Make sure you save a copy of the private key in a safe place. If you lose this key you will need to generate a new key pair. You will sign your request using the private key.            |
| mycert.cer     | X.509 cert (public key) | Important:Submit this file in the Deploy step of your onboarding process upon approval of your linkup request. The API uses this file for signature verification on your app’s API calls. |

{% hint style="info" %}
Note: Our sample application has a private key installed in it. This is only used for demo purposes. Your application will need its own private key.
{% endhint %}

For implementation on your own application, please make sure that your business user/partner has submitted your public key to Myinfo as part of the onboarding process.

***

## 1. Enable PKI digital signature on our Sample application

### **1.1 Modify configuration**

Modify the configuration in the sample application you downloaded in Tutorial 2.

For Linux/MacOSFor Windows

***

## 2. Trigger MockPass Login and Consent (authorise API)

Now access the sample application via your browser at `http://localhost:3001` and click on the **Retrieve Myinfo** button on the application and go through the MockPass login and on the consent page, click on **I Agree**.

Note:The process for this is exactly the same as in Tutorial 2.

The **token** and **person** API calls will follow automatically once you have finished the consent page.

We will look at the code for these 2 APIs in the following sections.

***

## 3. Call the Token API

Look at the code in the file `routes/index.js` in the sample application.

You should see the following code:

```
// function to prepare request for TOKEN API
function createTokenRequest(code) {
  var cacheCtl = "no-cache";
  var contentType = "application/x-www-form-urlencoded";
  var method = "POST";
  var request = null;
 
  // preparing the request with header and parameters
  // assemble params for Token API
  var strParams = "grant_type=authorization_code" +
    "&code=" + code +
    "&redirect_uri=" + _redirectUrl +
    "&client_id=" + _clientId +
    "&client_secret=" + _clientSecret;
  var params = querystring.parse(strParams);
 
 
  // assemble headers for Token API
  var strHeaders = "Content-Type=" + contentType + "&Cache-Control=" + cacheCtl;
  var headers = querystring.parse(strHeaders);
 
  // Sign request and add Authorization Headers
  var authHeaders = generateAuthorizationHeader(
    _tokenApiUrl,
    params,
    method,
    contentType,
    _authLevel,
    _clientId,
    _privateKeyContent,
    _clientSecret
  );
 
  if (!_.isEmpty(authHeaders)) {
    _.set(headers, "Authorization", authHeaders);
  }
 
  var request = restClient.post(_tokenApiUrl);
 
  // Set headers
  if (!_.isUndefined(headers) && !_.isEmpty(headers))
    request.set(headers);
 
  // Set Params
  if (!_.isUndefined(params) && !_.isEmpty(params))
    request.send(params);
 
  return request;
}
```

You will notice that the code is calling `securityHelper.generateAuthorizationHeader()` before sending out the request. This function is found in `lib/security/security.js` and generates the security headers for calling Our API Gateway. Here's the code for this function:

```
// generates the security headers for calling API gateway
  function generateAuthorizationHeader(url, params, method, strContentType, 
  authType, appId, keyCertContent, passphrase) {
     
    if (authType == "L2") {
      return generateRS256Header(url, params, method, strContentType, appId, 
      keyCertContent, passphrase);
    } else {
      return "";
    }
  };
```

### **3.1 Signing Your Requests**

Let's have a closer look at the `generateAuthorizationHeader()` function in the `lib/security/security.js` file.

To sign your request, a few steps are required:\
A. Constructing the Authorisation Token\
B. Forming the Signature Base String\
C. Signing the Base String to get the Digital Signature\
D. Assembling the Header

You can see the different steps involved in the code below:

```
  // Signing Your Requests
  function generateRS256Header(url, params, method, strContentType, appId, keyCertContent, keyCertPassphrase) {
    var nonceValue = nonce();
    var timestamp = (new Date).getTime();
 
    // A) Construct the Authorisation Token Parameters
    var defaultAuthHeaders = {
      "app_id": appId, // App ID assigned to your application
      "nonce": nonceValue, // secure random number
      "signature_method": "RS256",
      "timestamp": timestamp // Unix epoch time
    };
 
    // B) Forming the Base String
    // Base String is a representation of the entire request (ensures message integrity)
 
    // i) Normalize request parameters
    var baseParams = sortJSON(_.merge(defaultAuthHeaders, params));
 
    var baseParamsStr = qs.stringify(baseParams);
    baseParamsStr = qs.unescape(baseParamsStr); // url safe
 
    // ii) concatenate request elements (HTTP method + url + base string parameters)
    var baseString = method.toUpperCase() + "&" + url + "&" + baseParamsStr;
 
    // C) Signing Base String to get Digital Signature
    var signWith = {
      key: fs.readFileSync(keyCertContent, "utf8")
    }; // Provides private key
 
    // Load pem file containing the x509 cert & private key & sign the base string with it to produce the Digital Signature
    var signature = crypto.createSign("RSA-SHA256")
      .update(baseString)
      .sign(signWith, "base64");
 
    // D) Assembling the Authorization Header
    var strAuthHeader = "PKI_SIGN app_id=\"" + appId + // Defaults to 1st part of incoming request hostname
      "\",timestamp=\"" + timestamp +
      "\",nonce=\"" + nonceValue +
      "\",signature_method=\"RS256\"" +
      ",signature=\"" + signature +
      "\"";
 
    return strAuthHeader;
  };
```

The following sections explain in detail each of the steps and how to do it for your own application.

#### **A. Constructing the Authorisation Token**

In order for the platform to recognize your app, you must construct a token and send it with the request message. This token is sent in the header of your request.

| NAME              | DESCRIPTION                                                                                                                                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| app\_id           | The AppID assigned to your application. For our sample application, this is `STG2-MYINFO-SELF-TEST`                                                                                                                                                                                    |
| nonce             | A random string, uniquely generated for each request. The nonce allows the server to verify that a request has never been made before and helps prevent replay attacks when requests are made over a non-secure-channel. For more information, see Generating a Nonce Value.           |
| signature\_method | <p>A value indicating the signature method.<br>Value = <strong>RS256</strong></p>                                                                                                                                                                                                      |
| signature         | The signature value. For information on how the signature value is calculated, see later sections.                                                                                                                                                                                     |
| timestamp         | The timestamp of the request, expressed as the number of milliseconds since January 1, 1970 00:00:00 GMT. The timestamp must be a positive integer and must be greater than or equal to the timestamp used in previous requests. For more information, see *Generating the Timestamp.* |

#### **A.1 Generating a Nonce Value**

A nonce is a random string that is uniquely generated for each request. The nonce allows the API providers to verify that a request has never been made before. A nonce is sent in the message header for both Shared Secret and PKI security mechanisms. In the Shared Secret mechanism, the same nonce value sent in the message header is also used in creating the Secret Digest.

The way you create the nonce will depend on your development environment. Most programming languages include a method for creating a nonce.

Below is an example of generating a nonce value in Java:

```
  // Generate the nonce value
  Import java.security.SecureRandom:
  Random rand = SecureRandom.getInstance ("SHA1PRNG");
  long nonce = rand.nextLong();
```

#### **A.2 Generating the Timestamp**

The timestamp of the request is sent in the message header. The timestamp must be in Unix epoch time, expressed as the number of milliseconds since January 1, 1970 00:00:00 GMT. The timestamp must be a positive integer and must be greater than or equal to the timestamp used in previous requests. In most implementations, the timestamp is taken from the host server. It's important that the timestamp in the message is accurate; if the timestamp is off, the message might be rejected.

For more information on Unix epoch time, and examples of implementation of the timestamp in different programming languages, see [Epoch Converter](http://www.epochconverter.com/).\_ \_

A Java example of generating the timestamp is shown below.

```
  // Get the timestamp in milliseconds
  long timestamp = System.currentTimeMillis();
```

#### **B. Forming the Signature Base String**

The **basestring** is a string constructed to represent the contents of your request, which is then signed to create the digital signature of your request. This ensures that the contents of your request can be verified to ensure it has not been changed in transit.

**Base String Examples:**\
Below is an example of the Signature Base String that you will see in the onscreen logs of our demo application when calling the **token** API.

```
baseString:
POST&https://test.api.myinfo.gov.sg/com/v3/token&app_id=STG2-MYINFO-SELF-TEST&
client_id=STG2-MYINFO-SELF-TEST&client_secret=44d953c796cccebcec9bdc826852857a
b412fbe2&code=13a2f7db-1665-4c4e-9baa-b8ec464b9aad&grant_type=authorization_co
de&nonce=150589435358500&redirect_uri=http://localhost:3001/callback&signature
_method=RS256&timestamp=1505894353585
```

Likewise, the Base String for the **person** API looks like this:

```
baseString:
GET&https://test.api.myinfo.gov.sg/com/v3/person/9E9B2260-47B8-455B-89B5-C48F4
DB98322/&app_id=STG2-MYINFO-SELF-TEST&attributes=name,sex,race,nationality,dob
,email,mobileno,regadd,housingtype,hdbtype,marital,edulevel,assessableincome,h
anyupinyinname,aliasname,hanyupinyinaliasname,marriedname,cpfcontributions,cpf
balances&client_id=STG2-MYINFO-SELF-TEST&nonce=150589435395700&signature_metho
d=RS256&timestamp=1505894353957
```

The process of constructing the Signature Base String consists of three steps:

<details>

<summary>Step 1: Normalize request parameters</summary>

Collect the request parameters, sort them, and concatenate them into a normalized string. Parameters to include:

* All parameters in the HTTP Authorization header except the *signature* parameters which must be excluded.
* Parameters in the HTTP POST request body (with a content-type of application/x-www-form-urlencoded).
* HTTP GET parameters added to the URLs in the query part.

Normalize the parameters into a single string following the steps below:

* Sort by parameter name, using lexicographical byte value ordering. If two or more parameters share the same name, sort by value. For example:

  ```
    a=1, c=hi%20there, f=25, f=50, f=a, z=p, z=t
  ```
* When parameters are sorted, concatenate them into a single string. For each parameter, separate the name from the corresponding value by an equals (=) character (ASCII code 61), even if the value is empty. Each name-value pair is separated by an ampersand (&) character (ASCII code 38).&#x20;
  * For example: a=1\&c=hi%20there\&f=25\&f=50\&f=a\&z=p\&z=t

</details>

<details>

<summary>Step 2: Construct request URL</summary>

The Signature Base String includes the absolute URL for the request, tying the signature to a specific endpoint. The URL used in the Signature Base String:

* Must include the scheme, authority, and path.
* Must exclude the query and fragment.

URL scheme and authority must be **lowercase** and must include the port number (except port 80 or 443).

{% hint style="info" %}
Note: HTTP default port 80 and HTTPS default port 443 must be excluded.
{% endhint %}

For example, this person GET request:

```
https://test.api.myinfo.gov.sg:443/com/v3/person/
9E9B2260-47B8-455B-89B5-C48F4DB98322/?attributes=name,sex,race,
nationality,dob,email,mobileno,regadd,housingtype,hdbtype,marital,
edulevel,assessableincome,hanyupinyinname,aliasname,
hanyupinyinaliasname,marriedname,cpfcontributions,
cpfbalances&client_id=STG2-MYINFO-SELF-TEST
```

Would be included in the Signature Base String as:

```
https://test.api.myinfo.gov.sg/com/v3/person/9E9B2260-47B8-455B-89B5-C48F4DB98322/
```

</details>

<details>

<summary>Step 3: Concatenate request elements</summary>

The following items must be concatenated in order into a single Signature Base string. Each item is encoded and separated by an ampersand (<mark style="color:red;">`&`</mark>) character (ASCII code 38), even if empty.

* The HTTP request method used to send the request. Value must be uppercase, for example: POST, GET, PUT.
* The request URL.
* The normalized request parameters string. Note that the signature parameter, scheme are excluded.

</details>

#### **C. Signing the Base String to get the Digital Signature**

Once the Signature Base String is constructed, the next step is signing:

1. Use the SHA-2 algorithm to generate the hash of the Signature Base String.
2. Sign the hashed value using the private key of the app.
3. Base64-encode the signature value.

{% hint style="info" %}
Note: Base64 encoding should not include the CRLF (carriage return/line feed) every 72 characters which is part of strict Base64 encoding. Instead, the whole Base64 encoded string should be without line breaks.
{% endhint %}

4. Set the string as the value for the *signature* parameter.

Example code in Java below:

```
String baseString = "Constructed base string";
Signature sig = Signature.getInstance("RSA-SHA256");
sig.initSign(privateKey); // Get private key from keystore
sig.update(baseString.getBytes());
byte[] signedData = sig.sign();
String finalStr = Base64.getEncoder().encodeToString(signedData);
```

Example code in NodeJS below:

```
var signature = crypto.createSign('RSA-SHA256')
.update(baseString)
.sign(signWith, 'base64');
```

#### **D. Assembling the Header**

Now that you have gotten the digital signature, you are ready to assemble the final header for your request. Make sure you include the following parameters in the header:

* app\_id
* nonce
* signature\_method
* signature
* timestamp

**Sample header with authorization parameters**

Below is an example of an Authorization header for the sample application. Make sure you list the parameters in the sequence shown below.

```
Authorization: PKI_SIGN
timestamp="1505900210349",
nonce="150590021034800",
app_id="STG2-MYINFO-SELF-TEST",
signature_method="RS256",
signature="EEm+HEcNQajb5FkVd82zjojk+daYZXxSGPCO
R2GHZeoyjZY1PK+aFMzHfWu7eJZYMa5WaEwWxdOdq5hjNbl
8kHD7bMaOks7FgEPdjE++TNomfv7
SMktDnIvZmPYAxhjb/C9POU2KT6tSlZT/Si/qMgD1cryaPw
SeMoM59UZa1GzY
mqlkveba7rma58uGwb3wZFH0n57UnouR6LYX
DOOLkqi8uMZBuvRUvSJRXETAj2N0hT+4QJiN96Ct6IEQh/w
oZh0o74K5Ol9Pp
DSM08qC7Lj6N/k694J+hbBQVVviGn7/6mDkfbwdMDuoKs4t
7NpqmAnwT+xaQS
IZcexfrAVQYA=="

```

### **3.2 Sending the Request**

Once the header is assembled, you are ready to send out your request. If you have done the steps correctly, Our API Gateway should recognize your request to be valid and send back a valid response, similar to the one you saw in Tutorial 2.

{% hint style="info" %}
Note: Verify that the request URL remains as e.g. <https://api.myinfo.gov.sg/com/v3/\\>\*
{% endhint %}

### **3.3 Validating the Response**

Validate the JWT response sent back to you in the way that we went through in Tutorial 2.

{% hint style="info" %}
Note: It is very important for your application to validate the signature of the JWT to ensure the response has not been changed in transit.
{% endhint %}

***

## 4. Call the Person API

### **4.1 Send Request**

Now that you have the *JWT access token*, you can call the **person** API in the same way as the **token** API.

{% hint style="info" %}
Note: Remember to construct the header and digital signature of your request in the same way as the token API.
{% endhint %}

### **4.2 Decrypt & Verify the Person Response**

The response payload for the **Person** API (for test and production environments) is first signed, then encrypted:

* Signing is done using [**JWS (JSON Web Signature)**](https://tools.ietf.org/html/rfc7515) format
* Encryption is done using [**JWE (JSON Web Encryption) Compact Serialization**](https://tools.ietf.org/html/rfc7516) format

Encryption protects the data at rest while a signed payload means, if necessary, you will be able to pass this signed payload to a 3rd party where they can verify the payload's integrity with our public certificate.

In order to read the payload, you have to perform the following steps in order:

1. Decrypt the payload with your application's private key.
2. Validate the decrypted payload signature with our public key.

After doing the above steps, your application will be able to extract the payload in JSON format.

#### **STEP 1: Decryption**

* Encryption is done using your application's public key that you provided during onboarding. Decryption of the payload should be using the private key of that key-pair.
* Current encryption algorithms used:
  * **RSA-OAEP** (for content key wrapping)
  * **AES256GCM** (for content encrytion)

**What is the JSON Web Encryption Compact Serialization format?**

The format consist of five parts separated by dots (.), which are:

| PART                  | DESCRIPTION                                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Header                | Contains the encryption algorithms used to produce the 1. cipher text (encrypted data) and 2. encrypted key (symmetric key encrypted with application's RSA public key) |
| Encrypted Key         | The encrypted symmetric key that was used to encrypt the data.                                                                                                          |
| Initialization Vector | Secure random value used together with the symmetric key to encrypt the data.                                                                                           |
| Cipher Text           | The encrypted data.                                                                                                                                                     |
| Tag                   | Value used to ensure integrity of the encrypted data and header.                                                                                                        |

Therefore, a JWE typically looks like the following: `aaaaa.bbbbb.ccccc.ddddd.eeeee`

**How can I decrypt the JWE?**

You will need to use a library that performs JWE decryption in order to decrypt the cipher text. Such libraries are readily available on the internet.

For example, in our sample application, which is implemented with Node.js, we use the `jose` library, and we call the `jose.jwe.decrypt` method. If the decryption fails then the library will throw an error which the application needs to handle.

Firstly, the `Encrypted Key` is decrypted using your application's RSA private key with the "alg" algorithm specified in the `Header` to produce the symmetric key. Next, the JWE decryption library is used to decrypt the `Cipher Text` using the symmetric key, `Initialization Vector`, `Tag` and ascii-encoded `Header`, with the "enc" algorithm in the `Header`.

Look at the code in the file `lib/security/security.js` and search for the following code snippet:

```
// Decrypt JWE using private key
security.decryptJWE = function decryptJWE(header, encryptedKey, iv, cipherText, tag, privateKey) {
  console.log("Decrypting JWE".green + " (Format: " + "header".red + "." +
  "encryptedKey".cyan + "." + "iv".green + "." +
  "cipherText".magenta + "." + "tag".yellow + ")");
  console.log(header.red + "." + encryptedKey.cyan + "." + iv.green + "." + cipherText.magenta + "." + tag.yellow);
  return new Promise((resolve, reject) => {
     
    var keystore = jose.JWK.createKeyStore();
     
    console.log((new Buffer(header,"base64")).toString("ascii"));
     
    var data = {
      "type": "compact",
      "ciphertext": cipherText,
      "protected": header,
      "encrypted_key": encryptedKey,
      "tag": tag,
      "iv": iv,
      "header": JSON.parse(jose.util.base64url.decode(header).toString())
    };
    keystore.add(fs.readFileSync(privateKey, "utf8"), "pem")
      .then(function(jweKey) {
        // {result} is a jose.JWK.Key
        jose.JWE.createDecrypt(jweKey)
          .decrypt(data)
          .then(function(result) {
            resolve(JSON.parse(result.payload.toString()));
          })
          .catch(function(error) {
            reject(error);
          });
      });
       
  })
  .catch (error => {
    console.error("Error with decrypting JWE: %s".red, error);
    throw "Error with decrypting JWE";
  })
}
```

This calls the library to decrypt the JWE and return the decrypted JSON object, which is the **signed person's data**.

#### **STEP 2: Verification of Signature**

The decrypted payload is signed according to [**JWS (JSON Web Signature)**](https://tools.ietf.org/html/rfc7515) format, similar to the access token.

* signature algorithm used is `RS256`.

You may download Myinfo X.509 Public Key Certificate used for verification, after application is created during onboarding in the application details page upon login.

**Sample Code in `NodeJS`**

```
      // Sample Code for Verifying & Decoding JWS or JWT
      function verifyJWS(jws, publicCert) {
        // verify payload
        // ignore notbefore check because it gives errors sometimes if the call is too fast.
        try {
          var jwspayload = jwt.verify(jws, fs.readFileSync(publicCert, "utf8"), {
            algorithms: ["RS256"],
            ignoreNotBefore: true
          });
          return jwspayload;
        }
        catch(error) {
          throw("Error with verifying and decoding JWS");
        }
      }
```

***

## 5. Use the JSON object to Prefill Form

Once you have decrypted the JWE and verified the JWS, you will get the Person JSON data format which we saw in Tutorial 1 and 2. Use this data to prefill your application form.

***

## Summary

You've successfully used the OAuth2 process and PKI digital signature to get the Person data from Myinfo sandbox environment.

You are now ready to use the same method to integrate your own application to our Staging and Production APIs

{% hint style="info" %}
Note: For Staging and Production APIs, please ensure you have separate pairs of (private key+public cert) for each environment. Your business user/partner should submit these as part of the onboarding process.
{% endhint %}


# Resources


# Myinfo Connectors

Partners can refer to the following connectors to help your integration with Myinfo V3.

As onboarding for Myinfo v3/v4 is discontinued., we are no longer providing updates for these connectors.

| Language | Github Link                                           | Requirements       |
| -------- | ----------------------------------------------------- | ------------------ |
| NodeJS   | <https://github.com/singpass/myinfo-connector-nodejs> |                    |
| Java     | <https://github.com/singpass/myinfo-connector-java>   | Java 1.7 or later  |
| .NET     | <https://github.com/singpass/myinfo-connector-dotnet> | .NET Framework 4.8 |


# Error Codes

Here are some of the error codes you might encounter:

| Error Code                                                                                                        | API                                                     | Reason                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 302                                                                                                               | Authorise                                               | <p>Possible to have the following error codes in the 'error' attribute.</p><ul><li>500: Unknown or other server side errors</li><li>503: Myinfo under maintenance</li><li>access\_denied: When user did not give consent</li></ul> |
| 400                                                                                                               | Token                                                   | Same authcode in the body is being re-used.                                                                                                                                                                                        |
| Authcode error - missing, invalid, expired, revoked.                                                              |                                                         |                                                                                                                                                                                                                                    |
| 401                                                                                                               | Token                                                   | No security header given                                                                                                                                                                                                           |
| Invalid App ID used. Digital service is not registered with Myinfo                                                |                                                         |                                                                                                                                                                                                                                    |
| The timestamp of server is not synchronised. Check timestamp of server                                            |                                                         |                                                                                                                                                                                                                                    |
| The value of the nonce in the authorisation header was deemed to be repeated. Check that the nonce is not re-used |                                                         |                                                                                                                                                                                                                                    |
| Ensure HTTP 'Authorization' header to be 'PKI\_SIGN'                                                              |                                                         |                                                                                                                                                                                                                                    |
| Person                                                                                                            | No security header given                                |                                                                                                                                                                                                                                    |
| Invalid App ID used. Digital service is not registered with Myinfo                                                |                                                         |                                                                                                                                                                                                                                    |
| The timestamp of server is not synchronised. Check timestamp of server                                            |                                                         |                                                                                                                                                                                                                                    |
| The value of the nonce in the authorisation header was deemed to be repeated. Check that the nonce is not re-used |                                                         |                                                                                                                                                                                                                                    |
| Ensure HTTP 'Authorization' header to be 'PKI\_SIGN'                                                              |                                                         |                                                                                                                                                                                                                                    |
| The requested UIN/FIN does not match the UIN/FIN of the person who logged in                                      |                                                         |                                                                                                                                                                                                                                    |
| Requested attributes do not match the attributes consented by person                                              |                                                         |                                                                                                                                                                                                                                    |
| 403                                                                                                               | Person                                                  | Requested attributes does not match the attributes consented by person. This happens if the list of attributes in your request are different from the attributes specified when calling the token API.                             |
| Incorrect API URL used                                                                                            |                                                         |                                                                                                                                                                                                                                    |
| Digital service is not registered with Myinfo                                                                     |                                                         |                                                                                                                                                                                                                                    |
| Request contains attributes not allowable for the digital service                                                 |                                                         |                                                                                                                                                                                                                                    |
| 404                                                                                                               | Token                                                   | Incorrect API URL used.                                                                                                                                                                                                            |
| Same authcode in the body is being re-used.                                                                       |                                                         |                                                                                                                                                                                                                                    |
| Person                                                                                                            | Incorrect API URL used.                                 |                                                                                                                                                                                                                                    |
| UIN/FIN has a Singpass account, but does not have a Myinfo profile                                                |                                                         |                                                                                                                                                                                                                                    |
| 500                                                                                                               | Token                                                   | Unexpected error. Check response body for actual error.                                                                                                                                                                            |
| Person                                                                                                            | Unexpected error. Check response body for actual error. |                                                                                                                                                                                                                                    |


# FAQ

## Q1. Can I change the callback URL in the sample app, what should I do?

If your digital service has not onboarded with Myinfo, please use <http://localhost:3001/callback> while you are prototyping.

If your digital service has onboarded with Myinfo, please use the callback URLs that have been configured for you.&#x20;

***

## Q2. I encountered an error while developing my digital service integrating with Myinfo APIs, who can I contact?

For troubleshooting, you may refer to the [error codes page](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v3/resources/error-codes) with the possible causes.

Please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/)if you encounter error with the implementation.

***

## Q3. My Enterprise Architecture design requires whitelisting of Myinfo APIs IP address. What is the IP address that I should whitelist?

Myinfo APIs does not support IP whitelisting as our API Gateway is using dynamic IPs. Please whitelist the following Fully Qualified Domain Names (FQDN) instead:

* test.api.myinfo.gov.sg
* api.myinfo.gov.sg

***

## Q4. How frequent does Myinfo APIs get updated? How do I get notified when there is a new version of Myinfo APIs? Can I continue to use the older API version even if a newer version is released?

The Government plans to make Myinfo more useful for digital transactions by progressively including other frequently-used profile data.

When a new version of APIs is released, there will be a transition period for digital services to migrate to the latest version. The earlier API version is usually deprecated 6 months after the new version is released.

Please ensure that your support emails are registered in your app to receive important announcement such as Myinfo new version or new data items release.

***

## Q5. Does Myinfo APIs support native mobile application?

Myinfo APIs currently only support web-based integration.

***

## Q6. Is there any requirement for the X.509 public key? Can we use the same X.509 certificate for our staging and production environments?

Due to security reasons, please use:

* Keys that are from a compatible CA (i.e. self-signed keys are not supported)
* Different keys for staging and production environments

You may use the same X.509 public key for different products/services that integrate with Myinfo, as long as different keys are used for staging and production environments.

***

## Q7: What type of digital certificate should I obtain for integrating with Myinfo?

Integration with Myinfo requires X.509 certificate that can produce RS256 digital signature for the purpose of server to server communication.

***

## Q8: Can I use a Web SSL certificate for integrating with Myinfo?

Web SSL certificate proves the authenticity of a domain. As integration with Myinfo is a server to server, the certificate should be issued to your company and not to a domain.

***

## Q9. I am trying to decrypt the JWE response string returned from Myinfo Person API. However, I am getting the following error message:

```
*A256M is not valid algorithm*
```

The library that you are using to decrypt the response string might not support A256GCM algorithm. Please use a library that supports the algorithm.

***

## Q10. My architecture design requires trusting of Myinfo web SSL certificate. Where can I retrieve the certificate?

We recommend that your application trust / pin against the [root certificates](https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/amazonrootcas.zip) instead, as the web SSL certificates will be renewed from time to time.

***

## Q11. What are the requirements for callback URLs in the app configurations submission?

Please note the following requirements for callback URLs submission:

* Use different callback URLs in staging and production environments.
* Use static callback URLs (i.e. dynamic callback URLs are not supported)
* Use Fully Qualified Domain Names (FQDN) for both the staging and production callback URLs (i.e. static IP address or port numbers in callback URLs are not supported)
* Multiple callback URLs may be submitted for each environment.

***

## Q12. How may I test that my app is able to support cases where additional security verification with Singpass Face Verification is required?

To ensure that SFV works for your Myinfo user journeys, you may verify that camera permissions are enabled through the following methods:

1. Staging: Test additional Singpass Face Verification through the link provided on the Mockpass page
2. Production: Test that SFV works for the Myinfo user journey on different modalities (e.g. mobile/computer browser, native mobile app). You can test SFV through the following steps:\
   a. Initiate the Myinfo user journey in your linked up service with the above App IDs\
   b. Log in with your Singpass ID and password instead of the QR code\
   c. Select Singpass Face Verification as the 2FA method instead of SMS OTP

***

## Q13. What are the supports available for me to conduct performance testing?

Performance Testing in Production environment is strictly not allowed. Please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/)if you are planning to conduct performance testing in Test environment.

***

## Q14. What is the Myinfo v3 certificate change about?

The last Myinfo v3 X.509 Public Key Certificate have expired on 7th Nov 2024.<br>

1. Please [download the new certificate](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-myinfo-v3-v4/technical-specifications/myinfo-v3/latest-x.509-public-key-certificate) and integrate the new certificate with your digital service.
2. After the new certificate is integrated with your digital service, return to App Details page in Singpass Developer Portal and toggle to switch to the new certificate.

\
Please take note that Step 2 is to be performed immediately after Step 1 is completed.

***

## Q15. Who do I contact if I require more details?

If you have any other query, please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/).


# Overview

{% hint style="danger" %}
Verify API is no longer supporting new onboarding. Please consider onboarding to [Singpass](https://docs.developer.singpass.gov.sg/docs/) instead
{% endhint %}

**Verify** enables secure in-person identity verification and data transfer.Verify enables residents to perform secure in-person identity verification and data sharing through scanning QR codes.This service provides businesses a digital alternative for visitor registration and access, customer acquisition at roadshows, or other use cases that require user identification.<br>

## How Verify API can enhance your digital service

* Align with [PDPC's NRIC Advisory Guidelines](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/Advisory-Guidelines-for-NRIC-Numbers---310818.pdf)\
  Businesses can verify users digitally without collecting or retaining physical NRICs, FIN cards and NRIC/FIN numbers. Verify is a recommended alternative means to conduct identity verification. Please refer to PDPC’s Technical Guide [here](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Technical-Guide-to-Advisory-Guidelines-on-NRIC-Numbers---260819.pdf).
* Scan and Go, Less Form Filling\
  Users can share their relevant data quickly by scanning a QR code and providing consent via [Singpass Mobile](https://app.singpass.gov.sg/).

\ <br>


# Key Principles

## 1. Requesting for Data

**Request only what you need**

* Do not over-collect data, where this is not required for business purposes or legal reasons.

**PDPA & Applicable Regulations/Legislation**

* Protect, retain, transfer and dispose of data retrieved according to the rules of the Personal Data Protection Act (PDPA), relevant industry regulations and applicable legislation.
* For collection of National Identification Numbers, refer to the advisory guidelines from PDPC [here.](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/Advisory-Guidelines-for-NRIC-Numbers---310818.pdf)

**Use for lawful purposes**

* Use the data items retrieved for lawful purposes only.

***

## 2. Designing your User Journey

**Display As-Is**

* Data items retrieved from our APIs should be displayed as-is on digital forms (exception of Mobile Number and Email Address) so as to assure users that the correct data items have been retrieved.
* This minimises clarifications on the data retrieved and encourage users to update the relevant Government data source agency if any information is outdated.

**Store only if submitted**

* Data should be purged if form is not successfully submitted.
* If ‘Save-as-draft’ feature is available, unsubmitted data should be purged periodically.

**Provide non-Verify alternative**

* Partners are encouraged to support customers who prefer to use a non-Verify alternative.

**Showing customers the benefits of using Verify**

* Indicate that Verify service is available for your service and clearly state the target users (e.g. for SC/PR and/or Foreigners).
* Present the benefits of using Verify option (e.g. time saving, does not require ID cards or documents).

**Remove collection and retention of physical NRIC or other identification documents.**

* Data from Government sources which are uneditable on your form should be assessed as an alternative to collection and retention of identification documents for verification (e.g. NRIC, Work Pass (EP, PEP, EntrePass, S-Pass), Dependent Pass, Visit Pass (LTVP, LTVP+), selected Work Permit, driver's licence, and passport).

**Display & Technical Requirements**

* Design your application according to our [technical requirements](https://api.singpass.gov.sg/library/verify/developers/implementation-technical-requirements).

***

### 3. Possible Enhancements

**Visitor Registration and Access**

* Use Verify data items to replace collection and retention of physical NRIC or other identification document.

**Customer Acquisition**

* Use Verify QR scanning to speed up customer acquisition in the roadshows or seminars.

**Scenarios where Collection of NRIC Numbers is Not Required by Law**

* Use Verify Partial NRIC/FIN for use cases, such as redemption of free parking or signing up for retail membership and lucky draw.


# Verify  API Data Catalog

## Data Available

Verify leverages Myinfo profile, and provides the following data:

### **Basic Identity Data**

* This refers to data reflected in identification documents such as NRIC, Work Pass (EP, PEP, EntrePass, S-Pass), Dependent Pass, Visit Pass (LTVP, LTVP+), selected Work Permit, Driver’s Licence, and Passport.

### **Additional Data**

* This additional data provides businesses with alternative identifiers such as partial NRIC/FIN or UUID and contact details such as mobile number and email address.

## Data Catalog

<table><thead><tr><th width="109.79296875">id</th><th width="101.328125">name</th><th width="299.17578125">description</th><th>Data Available</th><th>Source</th></tr></thead><tbody><tr><td>uinfin</td><td>NRIC/FIN</td><td>NRIC number or FIN of user. NRIC number is the unique identifier given to every Singapore Citizens (SC) and Permanent Residents (PR), while FIN is the unique identifier for Foreigners.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>partialuinfin</td><td>Partial NRIC/FIN</td><td>Last 3 numerical digits and checksum of the NRIC/FIN number, prefixed with '*****' (e.g. "*****567A" from the full NRIC number of "S1234567A").</td><td>SC,PR,FIN</td><td>-</td></tr><tr><td>name</td><td>Principal Name</td><td>Full name of user printed on NRIC or FIN card. Includes Surname if any.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>aliasname</td><td>Alias Name</td><td>Refers to an alternate/additional name of the user that is legally recognised.</td><td>SC,PR</td><td>ICA</td></tr><tr><td>hanyupinyinname</td><td>Hanyu Pinyin Name</td><td>Refers to the officially romanised Chinese name of the user.</td><td>SC,PR</td><td>ICA</td></tr><tr><td>hanyupinyinaliasname</td><td>Hanyu Pinyin Alias Name</td><td>Refers to the legally-recognised alternate officially romanised Chinese name of the user.</td><td>SC,PR</td><td>ICA</td></tr><tr><td>marriedname</td><td>Married Name</td><td>Refers to the family name or surname adopted by the user upon marriage.</td><td>SC,PR</td><td>ICA</td></tr><tr><td>sex</td><td>Sex</td><td>Gender of the user. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (SexCode) for list of possible values.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>race</td><td>Race</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>secondaryrace</td><td>Secondary Race</td><td><p>Refers to secondary racial category of the Person, if any.</p><p></p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values</p></td><td>SC,PR</td><td>ICA</td></tr><tr><td>dialect</td><td>Dialect</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (DialectCode) for list of possible values</td><td>SC,PR</td><td>ICA</td></tr><tr><td>dob</td><td>Date of Birth</td><td></td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>residentialstatus</td><td>Residential Status</td><td>Indicate if the user is a Citizen, PR or others. Blank value will be returned for FIN holder. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (ResidentialCode) for list of possible values</td><td>SC,PR</td><td>ICA</td></tr><tr><td>nationality</td><td>Nationality/Citizenship</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (NationalityCitizenshipCode) for list of possible values</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>birthcountry</td><td>Country/Place of Birth</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (CountryPlaceCode) for list of possible values</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td>passportnumber</td><td>Passport Number</td><td></td><td>SC</td><td>ICA</td></tr><tr><td>passportexpirydate</td><td>Passport Expiry Date</td><td></td><td>SC</td><td>ICA</td></tr><tr><td>passtype</td><td>Pass Type</td><td><p>This refers to the pass type of a FIN holder.</p><p></p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (PassTypeCode) for list of possible values.</p><p></p><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td>passstatus</td><td>Pass Status</td><td><p>This refers to the pass status of a FIN holder.</p><p></p><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td>passexpirydate</td><td>Pass Expiry Date</td><td><p>This refers to the pass expiry date of a FIN holder.</p><p></p><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td>employmentsector</td><td>Employment Sector</td><td><p>This refers to the employment sector of a FIN holder.</p><p></p><p>Note that this only applies to a FIN holder with a valid pass issued by MOM.</p></td><td>FIN</td><td>MOM</td></tr><tr><td>mobileno</td><td>Mobile Number</td><td>Mobile number must be made editable at digital services even though data source is Singpass.</td><td>SC,PR,FIN</td><td>Singpass</td></tr><tr><td>email</td><td>Email Address</td><td>Email address must be made editable at digital services even though data source is Singpass.</td><td>SC,PR,FIN</td><td>Singpass</td></tr><tr><td>regadd</td><td>Registered Address</td><td><p>For SC/PR - Registered address is the address that is printed on the NRIC card.</p><p></p><p>For FIN - Registered address is applicable for foreigners under the following Pass Types:<br><strong>ICA-issued Passes</strong><br>- Long Term Visit Pass / Long Term Visit Pass +<br>- Student Pass<br>- Immigration Exemption Order<br><br><strong>MOM-issued Passes</strong><br>- S Pass<br>- Employment Pass<br>- Personalised Employment Pass<br>- EntrePass<br>- Dependent Pass</p></td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr></tbody></table>


# Brand Guidelines and Resources

#### Brand Guidelines & Assets

The Singpass brand is more than just a name. It's a set of values, attributes, and design principles that reflects the spirit of our brand. Using it consistently will reinforce our passion and commitment to give all Singapore residents a National Digital Identity that empowers them to live confidently in a Smart Nation.

Please help us protect our brand, and present your work in the most appropriate way, by following these guidelines and only using approved brand assets from this site (any logos or images found elsewhere on the web are not approved for use).

**When to use Singpass brand:**

* Product Page
* Digital Surface
* Kiosks

<br>

{% file src="/files/CkrmsFtkoN2EkdMHBnhp" %}

{% file src="/files/4ZZkzxyZaiSKEdXZ6VoV" %}

{% file src="/files/JcfXMXS3SGPy0ju2PSJ8" %}

Examples

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2F10HaEgZcl9EPQzIJNMGt%2Fimage.png?alt=media&amp;token=aa3f69e3-c145-4c24-ae25-5f929b45e01d" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2F5eXXhoGiz4JuHlTfQ5mt%2Fimage.png?alt=media&amp;token=299fd425-cee0-42b7-94b2-77eeaf47ffe1" alt=""><figcaption></figcaption></figure>

#### Logo and QR Code Usage

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FBGrTxIt6l30xRBSsuoyc%2Fimage.png?alt=media&amp;token=75d90622-0838-4d1a-8410-551cf8109211" alt=""><figcaption><p>Example of the logo placement</p></figcaption></figure>

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FFCROMnacJpFZvHNXo0XB%2Fimage.png?alt=media&amp;token=64c8465e-7712-48df-807c-d821e5b2fa78" alt=""><figcaption><p>Examples of Singpass Logo with Text Placement</p></figcaption></figure>

**Minimum Size**

Minimum sizes of the Singpass logo:

* Digital: 80 pixels wide
* Print: 18mm wide

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FVODyQ3Sg2Derf6tu4e3F%2Fimage.png?alt=media&amp;token=7c18437e-a11a-4f48-98a5-e170c55372cb" alt=""><figcaption><p>Example of 80px/18mm wide, approximate</p></figcaption></figure>

**Usage on Backgrounds**

Whenever possible, it is recommended to use the full colour Singpass logo. It should be used on only either white or light grey background only. The single colour logos should only be used on either Singapore red or black background. For photograph backgrounds, the single colour logo in reverse white should be used.

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FqkGeJxVDVyyDch2yFN2E%2Fimage.png?alt=media&amp;token=52d51c7f-0db5-48cc-a5a9-93525a2a2b26" alt=""><figcaption><p>Example of Singpass logo with background</p></figcaption></figure>

**Singpass Logo Don’ts**

Don't combine the Singpass name or logos, or any portion of any of them, with other logo, company name, mark or generic terms. Don't edit, modify, distort, rotate or re-colour the logo.

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2F2Jmq9uR6tsgZvw9WNWMp%2Fimage.png?alt=media&amp;token=5f58f1af-5949-4478-8a7d-99704d38a968" alt=""><figcaption><p>Examples of Don'ts</p></figcaption></figure>

**Singpass Key Figure Don’ts**

Don't combine the Singpass key figure name or logos, or any portion of any of them, with other logo, company name, mark or generic terms. Don't edit, modify, distort, rotate or re-colour the logo.

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FaCJx72JXOmLdN4l981Ih%2Fimage.png?alt=media&amp;token=5144070c-57dc-48b0-83ea-acf24ea85444" alt=""><figcaption><p>Examples of Don'ts</p></figcaption></figure>

**QR Code Dos**

* Ensure that the QR code is **at least 500px wide.**
* Ensure that the QR code is, **high-quality and sharp** not blur or pixelated.
* Ensure that the **aspect ratio of the template remain unchanged.**
* Ensure that the QR code is a **black filled colour on a white background** for high contrast.

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FHzmfUwAtBWK9dK3VIzJc%2Fimage.png?alt=media&amp;token=57de793f-54d4-4519-b35a-853a4022789b" alt=""><figcaption><p>Examples of Don'ts</p></figcaption></figure>

***

#### Naming Usage

Never modify or abbreviate the name 'Singpass'. The 'S' in Singpass is always capitalised. Keep 'Singpass' as a single word.

***

#### Contact Us

Please submit a request at [partnersupport.singpass.gov.sg](https://partnersupport.singpass.gov.sg/) if you have any questions on the usage of the Singpass logo with Verify service.


# FAQ

## Q1. What should I do when a user’s data in the business conflicts with the user’s data retrieved from Verify APIs?

You should assess which dataset takes precedence, based on business or regulatory requirements, and also factor in the following:

1. Whether the data is retrieved from government sources
2. Time-stamp of the data retrieved, to determine which is more recent

***

## Q2. Can I request for more data items than what I need for my digital service?

No. You should only request for the data items that you need for your digital service. This is aligned with the guidelines of the Personal Data Protection Act, which instructs the collection of personal data in an appropriate manner for the circumstances. Each request will be reviewed prior to approval.

***

## Q3. I would like to linkup multiple digital services with Verify APIs. Do I submit a single request for all my digital services or one request each for each digital service?

A new request must be submitted for digital services with different use cases/user journeys. If in doubt, please submit a request for each digital service.

***

## Q4. I would like to develop my digital service to solely depend on Verify APIs to populate user data. Is this a recommended approach?

As a general guideline, it is useful for digital services to consider the possible user journeys for their target audience. For example, users could fill up a digital form manually if they:

1. Do not wish to use Verify;
2. If the user is a foreigner who does not have Verify; or
3. If the Verify service is temporarily unavailable (e.g. system maintenance).

***

## Q5. How should my digital service handle scenarios where the user finds that the data retrieved from Verify is out-of-date? (e.g. user has not updated ICA about his/her change of registered address)

Businesses may allow users to fill out the form manually with the correct data. In this case, data previously retrieved from Verify should not be saved.

***

## Q6. Are the registered addresses of users restricted to Singapore addresses?

No, the registered address field can contain overseas addresses.

***

## Q7. Is there any guideline to display the QR Code?

Digital services should adhere to the Display Guidelines when displaying the QR Code. Please see Verify [Display Guidelines](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-verify/brand-guidelines-and-resources).

***

## Q8. I have some issues uploading my X.509 public key with my iOS device. How can I upload my X.509 public key?

It is recommended to upload your X.509 public key using compatible browsers (e.g. Safari, Chrome, Firefox) on your desktop.

***

## Q9. Can foreigners use Verify to transact with digital services?

Foreigners who have a valid Singpass account, will have a Myinfo profile, and can use Verify service

***

## Q10. Who do I contact if I require more details?

If you have any other query, please submit a request at [partnersupport.singpass.gov.sg ](https://partnersupport.singpass.gov.sg/).


# Verify API

{% hint style="info" %}
[For Verify API Specifications v2](https://public.cloud.myinfo.gov.sg/sg-verify/v2/sgverify2-oauth-specs.html)
{% endhint %}

{% hint style="info" %}
[For Verify Webhook Specifications v1](https://public.cloud.myinfo.gov.sg/sg-verify/sgverify-webhook-specs.html)
{% endhint %}

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FqAEhHlg1cnckGrTYM034%2Fimage.png?alt=media&amp;token=658a453f-9be6-4146-9f2a-8c90f6b40c9e" alt=""><figcaption><p>Logical Architecture Overview</p></figcaption></figure>

The diagram shows how a user consents to sharing of his personal information to your application via Verify:

1\. The user scans a Verify QR code pertaining to your application e.g. at a kiosk with Singpass Mobile

2\. The user authenticates himself on Singpass Mobile, and provides consent to share requested personal information with your application.

3\. Singpass mobile relays an authorisation code to your application's via registered callback URL.

4\. Your application then make a series of calls to Verify in order to obtain the user's data.

5\. User verifies his particulars displayed by your application before continuing the transaction.

***

## Understanding OAuth2.0 flow for Verify APIs

Verify is built on the OAuth 2.0 framework which is the web standard for obtaining user's authorisation in order to access user-owned resources. The flow involves invocation of 3 APIs: authorise, token and person (resource API).

### 1. Authorise

This API is embedded in the QR code that your application needs to generate (Learn more at [Verify QR Code](https://api.singpass.gov.sg/library/verify/developers/generateqrcode)). Upon scanning the QR code using Singpass Mobile, it will trigger the /authorise API. After authentication on SPM, a consent page is displayed requesting the user's explicit consent to allow his/her personal details to be released.

At the end of this process, Verify will return a short-lived "authorisation code" to your application's callback URL.

{% hint style="info" %}
Note: Your application will need to provide a callback URL (API) in order to receive the "authorisation code".
{% endhint %}

### 2. Token

This API is invoked by your application to obtain an "access token", which can be used to call the person API for the actual data. A valid "authorisation code" from the authorise API will be required in order to exchange for the "access token".

The "access token" will be valid for 30 minutes.

{% hint style="info" %}
Note:This API is a server-to-server call (does not go through browser)
{% endhint %}

### 3. Person

This API returns a JSON response with the personal data that was requested. Your application needs to provide a valid "access token" in order to exchange for the JSON data.

Once your application receives this JSON data, it should then display the user's information for verification.

{% hint style="info" %}
Note:This API is a server-to-server call (does not go through browser)
{% endhint %}

The diagram below shows the sequence diagram for all 3 APIs:<br>

<figure><img src="https://2818768107-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FrwG6ATZg7k01ReAAuMFx%2Fuploads%2FUE0KEOTWGXfLBOA7PmiN%2Fimage.png?alt=media&amp;token=de8b04da-b6d6-499e-ac0d-60921b7c8663" alt=""><figcaption></figcaption></figure>


# Technical Requirements

## 1. Transaction Log

Digital services which have integrated with Verify should track and store user transactions for potential issue management.

The following are some of the suggested minimum fields for tracking:

* State/ Transaction No. from the Verify request body
* Fields requested from Verify
* Time Stamp

In the event of user feedback or contact, these transaction logs may be requested by us to reconcile and resolve issues raised by the user.

***

## 2. X.509 Public Key

To implement RS256 (RSA Signature with SHA-256) Digital Signature for Verify APIs in your apps, please use a X.509 Public Key Certificate with RSA key size of 2048 bits or larger from one of the following compatible Certificate Authority (CA):

* Comodo/Sectigo
* digiCert
* GeoTrust
* GlobalSign
* [Netrust](https://www.netrust.net/netrust-singpass-myinfo-certificates/)\*
* Thawte
* VeriSign

\*Certificate must be issued by Netrust. Entrust-issued certs are not accepted.

{% hint style="warning" %}
ECC and ECDSA Public Key Certificates are currently NOT supported.
{% endhint %}

***

## 3. TLS & Cipher Suites

{% hint style="info" %}
**IMPORTANT:** In line with contemporary industry best practices, Verify supports TLS 1.2 and above.
{% endhint %}

The list of supported strong cipher suites include:

* TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256
* TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384
* TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

***

## 4. Webhook URLs (applicable to version 1 only)

For security reasons:

* Different Webhook URLs should be used for staging and production environments
* Fully Qualified Domain Name (FQDN) of staging and production environments should be used (i.e. instead of IP address)
* Webhook URLs should not contain Hash (#) or Wildcard (\*) characters


# Testing with Test Personas

Please refer to [test personas](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) for testing purpose


# Error Code

| Error Code                                                                                                        | API                                                     | Reason                                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| 400                                                                                                               | Token                                                   | Same authcode in the body is being re-used.             |
| Authcode error - missing, invalid, expired, revoked.                                                              |                                                         |                                                         |
| 401                                                                                                               | Token                                                   | No security header given                                |
| Invalid App ID used. Digital service is not registered with Verify                                                |                                                         |                                                         |
| The timestamp of server is not synchronised. Check timestamp of server.                                           |                                                         |                                                         |
| The value of the nonce in the authorisation header was deemed to be repeated. Check that the nonce is not re-used |                                                         |                                                         |
| Ensure HTTP 'Authorization' header to be 'PKI\_SIGN'                                                              |                                                         |                                                         |
| Person                                                                                                            | No security header given (HTTP 'Authorization' header)  |                                                         |
| Invalid App ID used. Digital service is not registered with Verify                                                |                                                         |                                                         |
| The timestamp of server is not synchronised. Check timestamp of server.                                           |                                                         |                                                         |
| The value of the nonce in the authorisation header was deemed to be repeated. Check that the nonce is not re-used |                                                         |                                                         |
| Ensure HTTP 'Authorization' header to be 'PKI\_SIGN'                                                              |                                                         |                                                         |
| The requested UIN/FIN does not match the UIN/FIN of the person who logged in                                      |                                                         |                                                         |
| Requested attributes do not match the attributes consented by person                                              |                                                         |                                                         |
| 403                                                                                                               | Token                                                   | Incorrect API URL used.                                 |
| Person                                                                                                            | Incorrect API URL used.                                 |                                                         |
| Digital service is not registered with Verify.                                                                    |                                                         |                                                         |
| Request contains attributes not allowable for the digital service.                                                |                                                         |                                                         |
| 404                                                                                                               | Person                                                  | Missing Myinfo profile.                                 |
| 500                                                                                                               | Token                                                   | Unexpected error. Check response body for actual error. |
| Person                                                                                                            | Unexpected error. Check response body for actual error. |                                                         |


# Verify QR Code

Verify process starts from the user scanning a QR code that is specific to your application. This section explains the different types of QR codes supported, the URL formats, as well as how they can be generated.

## 1. Choosing type of QR code

Verify supports 2 types of QR code: *"static"* and *"dynamic"*.

### **1.1 Static QR**

Static QR codes are normally used for time-bound/one-off events. They can be printed on paper and distributed, and scanned multiple times. Being static in nature, the QR codes will not work after the stipulated validity.

### **1.2 Dynamic QR**

Dynamic QR codes are normally used on digital devices such as tablet or kiosk. The QR codes should not be printed out, and should be displayed on the digital devices. Characteristics of dynamic QR codes are:

* generated on the fly
* short-lived e.g. valid for only 5 minutes after generation
* one-time used i.e. invalidated once scanned.

You can choose to generate either QR codes depending on your application needs.

***

## 2. Generate Verify QR Code

### **2.1 URL format**

The following is the format of the URL that will be used to produce Verify Dynamic QR code:

```http
https://app.singpass.gov.sg/sgverify?callback=https%3A%2F%2Ftest.yourcallbackurl%2Fcallback&client_id=STG2-SGVERIFY-SELF-TEST&nonce=4110833&qr_type=dynamic&signature_method=RS256&state=kiosk001&timestamp_expiry=1602324610000&timestamp_start=1570702210000&v=2&signature=h8jdRRpS5ArE0pdWDXHv04JiELnEvR54ulO7O0x//mewoZDQW+cfnSPdwC2kZZzLkMYtd2HjeTLBqTG5HKjbDiH3C5YkB9lS81mVgV3oj6E7LjzPZQgypNHzp1F3sBrj/4MNjJbL119VA15RJ0HlR1sOeF05yR7rFkDAZfRth37UFAFYoVDFzU4MwLYZt7W0eNRESXWVWLK94qqJg/ubR/xNKXqI93Tdw032DxapCIM3jLwQhk327f6a21ZpnSOKWXxWl1FUv4WcOxHXLvs8B/C43kJpn8TpGMHUyk5cRB/kFxljltH1Yq4n5ROhXFhjQUmk+nTMVsg31MKl6NKQnA==
```

The URL contains parameters that denotes the type of QR, validity, application ID etc, summarised in the table below. Ensure that the parameters are given in the sequence shown below:

| PARAMETER                                         | DESCRIPTION                                                                                                                                                                                                                                                                               |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>callback<br><code>required</code></p>          | <p>string<br><em>Example: "https%3A%2F%2Ftest.yourcallbackurl%2Fcallback"</em><br><br>Your application's registered callback URL (URL encoded) for Verify to return authorisation code to.</p>                                                                                            |
| <p>client\_id<br><code>required</code></p>        | <p>string<br><em>Example: "STG2-SGVERIFY-SELF-TEST"</em><br><br>Unique ID for your application.</p>                                                                                                                                                                                       |
| nonce                                             | <p>string<br><em>Example: 4110833</em><br><br>Unique-random text to prevent replay attack.<br><br>Note: Mandatory only if qr\_type is dynamic</p>                                                                                                                                         |
| <p>qr\_type<br><code>required</code></p>          | <p>string<br><em>Enum: "static" "dynamic"</em><br><br>Type of QR</p>                                                                                                                                                                                                                      |
| <p>signature\_method<br><code>required</code></p> | <p>string<br><em>Default: "RS256"</em><br><br>Signature algorithm used to produce the digital signature.</p>                                                                                                                                                                              |
| <p>state<br><code>required</code></p>             | <p>string<br><em>Example: "kiosk001"</em><br><br>Identifier that represents the user's session/transaction with the client for reconciling query and response. The same value will be sent back via the callback URL. Use a unique system generated number for each user/transaction.</p> |
| <p>timestamp\_expiry<br><code>required</code></p> | <p>string<br><em>Example: "1602324610000"</em><br><br>QR code expiry timestamp (UNIX epoch time in milliseconds)</p>                                                                                                                                                                      |
| <p>timestamp\_start<br><code>required</code></p>  | <p>string<br><em>Example: "1570702210000"</em><br><br>QR code start timestamp (UNIX epoch time in milliseconds)</p>                                                                                                                                                                       |
| <p>v<br><code>required</code></p>                 | <p>string<br><em>Default: 2</em><br><br>Version of Verify API.</p>                                                                                                                                                                                                                        |
| <p>signature<br><code>required</code></p>         | <p>string<br><em>Example: "MEyCBY/XSBBB..."</em><br><br>Binary of the generated signature encoded in Base64 URL-safe format. This digital signature will be used to ensure non-repudiation of the request.</p>                                                                            |

### **2.2 Construct URL**

The process of constructing the URL consists of three steps:

#### Step 1: Form the Verify URL with the query parameters

Form the base URL, excluding the digital signature.

```
// function to derive Verify url with the query parameters 
function formURL(qrType, callbackURL, clientId, state, nonce, signatureMethod, timestampExpiry, timestampStart, version) {
 
    let nonceString = nonce ? "&nonce=" + nonce : '';
    let baseUrl = "https://app.singpass.gov.sg/sgverify";
    let sgverifyURl = baseUrl +
        "?callback=" + encodeURIComponent(callbackURL) +
        "&client_id=" + clientId +
        nonceString +
        "&qr_type=" + qrType +
        "&signature_method=" + signatureMethod +
        "&state=" + state +
        "&timestamp_expiry=" + timestampExpiry + // Saturday, 10 October 2020 10:10:10
        "&timestamp_start=" + timestampStart + // Thursday, 10 October 2019 10:10:10
        "&v=" + version;
 
    /* Display all the params */
    console.log('--- Verify URL Params ---:'.green);
    console.log(' - baseUrl: ' + baseUrl);
    console.log(' - callback: ' + callbackURL);
    console.log(' (1) callback(URL Encoded): ' + encodeURIComponent(callbackURL));
    console.log(' (2) client_id: ' + clientId);
    console.log(' (3) nonce: ' + nonce);
    console.log(' (4) qr_type: ' + qrType);
    console.log(' (5) signature_method: ' + signatureMethod);
    console.log(' (6) state: ' + state);
    console.log(' (7) timestamp_expiry: ' + timestampExpiry);
    console.log(' (8) timestamp_start: ' + timestampStart);
    console.log(' (9) v: ' + version);
 
    /* Display the URL */
    console.log('--- Verify URL ---:'.green);
    console.log(sgverifyURl);
 
    return sgverifyURl;
 
}

```

#### Step 2: Sign the Verify URL on Step(1) with your private key

Digitally sign the URL constructed in Step 1 using your application's private key with cryptographic algorithm e.g. "RSA-SHA256".

```
function signURL(sgverifyURl, keytoSign) {
    var signedSgVerifyURl = crypto.createSign('RSA-SHA256')
        .update(sgverifyURl)
        .sign(keytoSign, 'base64');
 
    /* Signature */
    console.log('--- Signature of Verify URL ---:'.green);
    console.log(signedSgVerifyURl);
 
    return signedSgVerifyURl;
}
```

#### Step 3: Add the signature into the URL

Append the digital signature as a parameter to the URL constructed in Step 1.

```
function assemblingUrlWithSignature(sgverifyURl, signedSgVerifyURl) {
 
    var sgverifyURlwithSignature = sgverifyURl +
        "&signature=" + signedSgVerifyURl;
    return sgverifyURlwithSignature;
}
```

The final URL will look like the one above, echoed below:

```http
https://app.singpass.gov.sg/sgverify?callback=https%3A%2F%2Ftest.yourcallbackurl%2Fcallback&client_id=STG2-SGVERIFY-SELF-TEST&nonce=4110833&qr_type=dynamic&signature_method=RS256&state=kiosk001&timestamp_expiry=1602324610000&timestamp_start=1570702210000&v=2&signature=h8jdRRpS5ArE0pdWDXHv04JiELnEvR54ulO7O0x//mewoZDQW+cfnSPdwC2kZZzLkMYtd2HjeTLBqTG5HKjbDiH3C5YkB9lS81mVgV3oj6E7LjzPZQgypNHzp1F3sBrj/4MNjJbL119VA15RJ0HlR1sOeF05yR7rFkDAZfRth37UFAFYoVDFzU4MwLYZt7W0eNRESXWVWLK94qqJg/ubR/xNKXqI93Tdw032DxapCIM3jLwQhk327f6a21ZpnSOKWXxWl1FUv4WcOxHXLvs8B/C43kJpn8TpGMHUyk5cRB/kFxljltH1Yq4n5ROhXFhjQUmk+nTMVsg31MKl6NKQnA==
```

### **2.3 Generate QR Code**

Once you have the URL, you can use online tools to generate static QR codes, for example:

* <https://www.qr-code-generator.com/>
* <https://www.qrcode-monkey.com/>

For dynamic QR codes, you will need to use platform specific libraries to generate the QR code image on the fly.

***

## 3. Displaying Verify QR code

Please ensure that the QR codes generated is in-line with our [display guideline.](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-verify/brand-guidelines-and-resources)


# Tutorial 1: Sample Application


# Tutorial 2: PKI Digital Signature


# Technical Concepts

This section provides information about important technical concepts that will be helpful for your integration with Singpass.


# JSON Web Key Sets (JWKS)

## Overview

A JSON Web Key Set (JWKS) is a set of keys that contain a list of cryptographic keys that can be used either for signature verification or for encryption. Each key in the JWKS is stored in the JSON Web Key format, as specified in [RFC 7517](https://datatracker.ietf.org/doc/html/rfc7517).

In order to integrate with Singpass, you are required to [register](#registration-of-jwks) your JWKS with us. The same JWKS can be reused across multiple Singpass integrations.

Conversely, we also broadcast our JWKS at <https://id.singpass.gov.sg/.well-known/keys>. These are our public keys used for signing, and you should use them to verify the signature in both the ID token and the Userinfo response.

<details>

<summary>Example JWKS</summary>

```json
{
  "keys": [
    {
      "kty": "EC",
      "alg": "ES256",
      "use": "sig",
      "kid": "ydGFKJbIoqzSJyMpUiprLpaQz7RxV8C_HLiCW-l0q1k",
      "crv": "P-256",
      "x": "vx_9JwRUaXaj8nE21-mgtjrx2JPkOM_iawIIbIV2huc",
      "y": "ZvqP1ErOvOmMvaaWVA2WzB6eroYsz4I1PML1AiEIvsQ"
    },
    {
      "kty": "EC",
      "alg": "ECDH-ES+A256KW",
      "use": "enc",
      "kid": "R-G-GcB8vBaBCdQENkLD5k8MJnLQG4a1TR1Fx94CUvM",
      "crv": "P-256",
      "x": "fr9yjpnKygf6ZwR0L9kVIGES-B4CqQUo8_X_PyF725s",
      "y": "5iaXtCMTRXZzA-RwAHji0KUi_5XrrzeIGDuOoDNdPxo"
    }
  ]
}
```

</details>

## Purpose of JWKS

The keys that you provide in your JWKS will be used for the following:

* Verification of your [client assertions](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/technical-concepts/generation-of-client-assertion) (they are signed by one of your private keys). This is done during both the [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request) and [Token Exchange](broken://pages/oCGrLTZClE3OaHssLwYF)
* Encryption of the [ID Token](broken://pages/wotZhaPr8MmU8dBWEZY1)
* Encryption of the [Userinfo response](broken://pages/NFTOlGDvNbPvMcG841Xk#response)

## Registration of JWKS

When registering your JWKS with us, you have two options:

1. Directly register the JWKS with us as a JSON object in your app configuration
2. Host the JWKS on a publicly accessible URL, and register that URL with us in your app configuration.

## Requirements for JWKS

### General

1. Your JWKS must have at least one encryption key and one signing key.
2. All of the keys in your JWKS must **not** expose your private key. Specifically, it must **not** contain the `d` property, which represents the private key. Exposure of this property is a critical security vulnerability.
3. All of the keys in the JWKS must:
   1. Have unique key IDs in the `kid` field. Additionally, any new keys should not reuse previously-used key IDs.
   2. Contain a `kty` of `EC`
   3. Contain one of the following `crv` values:
      1. `P-256`
      2. `P-384`
      3. `P-521`
4. If your JWKS is hosted at a URL:
   1. The URL **must** be publicly accessible at all times
   2. It should respond as fast as possible, as the user experience of your users will be affected if your JWKS endpoint takes a long time to respond. In the worst case, it must respond within 3 seconds; otherwise, your users will fail to authenticate with us.

### Signing Keys

1. Must have a `use` value of `sig`

### Encryption Keys

1. Must have a `use` value of `enc`
2. Must contain one of the following `alg` values:
   1. `ECDH-ES+A128KW`
   2. `ECDH-ES+A192KW`
   3. `ECDH-ES+A256KW`

## Key Rotation

You should rotate your keys at least once a year. You will be able to rotate your keys without downtime. The process for rotating encryption keys and signing keys is slightly different, and will be outlined below.

### Signing Keys

1. Generate your new signing key pair, and add the public signing key to your JWKS **without** removing the old public signing key. The newly added key must have a different `kid` from any of the existing keys.
2. Wait for 1 hour. This ensures that our cache has expired and that we will have fetched your new keys, which we can then use to verify requests that you sign using your new key.
3. Start signing your requests using your new private key.
4. Remove the old public signing key from your JWKS.

### Encryption Keys

1. Generate your new encryption key.
2. Update your application such that it can perform decryption using either the old or the new key, depending on the `kid` value in the JWE header.
3. Replace the old key in your JWKS with the new key. The new key should have a different `kid` from the old one.
4. Wait for one hour. This ensures that our cache has expired, and that we will only perform encryption using your new key.
5. Remove the old encryption key from your JWKS.

You may use the Singpass Troubleshooting Tool below to validate whether your Encryption and Signing keys are correctly configured: <https://developer.singpass.gov.sg/troubleshooting-tool>


# Generation Of Client Assertion

{% hint style="info" %}
If you are using a [certified OIDC Relying Party library](https://openid.net/developers/certified-openid-connect-implementations/), the generation of client assertion will be handled by the library, as long as you specify that the `private_key_jwt` method is used for authentication.
{% endhint %}

## Overview

When your backend calls our APIs, you will need to generate a client assertion to authenticate yourself. The generation of this client assertion should be done using the `private_key_jwt` mechanism specified in the [OIDC specifications](https://openid.net/specs/openid-connect-core-1_0-final.html#ClientAuthentication). This mechanism involves you building a client assertion by signing a JWT using one of your signing keys defined in your [JWKS](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/technical-concepts/json-web-key-sets-jwks).

Client assertions need to be sent in the [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request) and the [Token Request](broken://pages/oCGrLTZClE3OaHssLwYF).

## Generation of JWT

To reduce complexity, we recommend that you use a JWT library to perform the JWT encoding and signing on your behalf, instead of implementing this on your own. You may refer to [this list](https://www.jwt.io/libraries?support=sign\&algorithm=es256) to look for a suitable library for your programming language. To learn more about JWTs and their structure, you may read [this article](https://www.jwt.io/introduction).

The JWT must have the structure outlined below.

### JWT Header

The JWT header should contain the following parameters:

<table><thead><tr><th width="122.17578125">Parameter</th><th>Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>alg</code></td><td>The signature algorithm that you are using to sign this JWT</td><td><p>One of the following strings:</p><ul><li><code>ES256</code></li><li><code>ES384</code></li><li><code>ES512</code></li></ul></td></tr><tr><td><code>typ</code></td><td>The type of this JWT</td><td>Must be the string <code>JWT</code></td></tr><tr><td><code>kid</code></td><td>The <code>kid</code> of the signing key that you are using to sign this JWT header.<br><br>If this is not provided, we will test against all of the signing keys in your JWKS when attempting to verify the signature.</td><td>String, optional</td></tr></tbody></table>

<details>

<summary>Sample JWT header in JSON form</summary>

```json
{
  "typ": "JWT",
  "alg": "ES256",
  "kid": "my_key_id_01"
}
```

</details>

### JWT Payload

The JWT payload should contain the following claims:

<table><thead><tr><th width="88.7265625">Claim</th><th width="440.61328125">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>sub</code></td><td>The client ID of your registered client, provided by Singpass during app onboarding.</td><td>A 32-character case-sensitive alphanumeric string.</td></tr><tr><td><code>aud</code></td><td>This should be the issuer identifier of our authorization server. You can obtain this value from the <code>issuer</code> field in the OpenID configuration of our authorization server.</td><td>String</td></tr><tr><td><code>iss</code></td><td>The client ID of your registered client, provided by Singpass during app onboarding.</td><td>A 32-character case-sensitive alphanumeric string.</td></tr><tr><td><code>iat</code></td><td>The unix timestamp, in seconds, at which you generated this JWT.</td><td>Number</td></tr><tr><td><code>exp</code></td><td>The unix timestamp, in seconds, on or after which this JWT <strong>must not</strong> be accepted by us for processing.<br><br>Note also that this must be less than or equal to 2 minutes after <code>iat</code>.</td><td>Number</td></tr><tr><td><code>jti</code></td><td>A unique identifier for this token. This identifier must only be used once. You should generate a new <code>jti</code> value for every request</td><td>String</td></tr></tbody></table>

<details>

<summary>Sample JWT Payload in JSON form</summary>

```json
{
  "sub": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "aud": "https://id.singpass.gov.sg/fapi",
  "iss": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "iat": "1756785377",
  "exp": "1756785493",
  "jti": "59e05e3c-9418-4e63-8119-a05157219b74"
}
```

</details>

### Overall JWT (Signed and Encoded)

The JWT should be signed using your private key to form a JSON Web Signature (JWS) in compact serialisation format. This is a format where the three parts of the JWS (the header, the payload, and the signature), are base64url encoded and concatenated together, using a dot (`.`) as the separator.

You must publish the public key corresponding to the private key you used to sign this JWT in your [JWKS](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/technical-concepts/json-web-key-sets-jwks).

<details>

<summary>Sample Signed JWT (in Compact Serialisation Format)</summary>

{% code overflow="wrap" %}

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6Im15X2tleV9pZF8wMSJ9.eyJzdWIiOiJUNXNNNWE1M1lhdzNVUnlERXYyeTkxMjlDYkVsQ04yRiIsImF1ZCI6Imh0dHBzOi8vaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkiLCJpc3MiOiJUNXNNNWE1M1lhdzNVUnlERXYyeTkxMjlDYkVsQ04yRiIsImlhdCI6IjE3NTY3ODUzNzciLCJleHAiOiIxNzU2Nzg1NDkzIiwiY29kZSI6IlhjeXpsU2VYMWhJeUpGbHN0eHNTRl9VZVhDNUR0aVlrRmdKOFZWeDUybWcifQ.fQMHTVNeCsa_mK6pmfjfi0rxERxDtu6eiMFkkpFdQrirc3u9LxP1_-E_7yIalIhmot1NdBQxbA9s_VztlQUhTQ
```

{% endcode %}

</details>

### Validate Your Client Assertion

You can validate your Client Assertion using this online validator tool:

<https://developer.singpass.gov.sg/troubleshooting-tool>

This tool helps you:

* Verify JWT structure and compact format
* Check required header parameters (alg, typ, jwk)
* Validate required payload claims
* Confirm signature validity
* Detect common implementation errors


# Proof Key for Code Exchange (PKCE)

## Overview

Proof Key for Code Exchange (PKCE) is a security mechanism specified in [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636). It ensures that only you, the requester of the authorization code, can use the authorization code during [Token Exchange](broken://pages/oCGrLTZClE3OaHssLwYF).

PKCE works in tandem with [client assertions](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/technical-concepts/generation-of-client-assertion) and [DPoP](broken://pages/HwQNmzFnTtrV92EVaT2k) in order to prevent authorization code interception attacks, which is a type of attack where attackers gain access to the authorization code (e.g. via malware installed on the user's device) and use it to obtain a user's access token.

## How To Implement PKCE

PKCE is used in two parts of the flow: the [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request) and the Token Exchange.

### Authorization Request

PKCE requires you to send two additional parameters in the Pushed Authorization Request: the `code_challenge` and `code_challenge_method`.

You should follow the steps below to understand how to send these parameters.

#### 1. Generate a code verifier

You should generate a **high-entropy random string** between 43-128 characters long, containing only alphanumeric characters, dashes, and underscores. This string **must** be different for every request.

<details>

<summary>Example code verifier</summary>

`6I9tQd5tKn7Uy9ZfwEqd-YC71gSVfzcfVcyXLc34vQo`

</details>

#### 2. Generate a code challenge from the code verifier

The code challenge is generated by hashing the code verifier using the SHA-256 algorithm, then encoding the result using base64url encoding. Take note that base64url encoding is not the same as base64 encoding.

<details>

<summary>Example code challenge</summary>

`hu0mAmPq8n91vRqudsGmriiG7blJDJS0bsDeOmEt17M`

</details>

#### 3. Send the code challenge and code challenge method in the Pushed Authorization Request

When you send the Pushed Authorization Request, you must include the code challenge generated in step 2 as the `code_challenge` parameter, and also send the `code_challenge_method` with the value of `S256`.

#### 4. Store the code verifier in session storage

You must store the code verifier in your backend and associate it with the user's session, as you will need it later during Token Exchange.

### Token Exchange

During token exchange, you must pass the code verifier that you had used to generate the code challenge for this authentication request as the `code_verifier` parameter in the request body. This serves as proof that you were the original generator of the `code_challenge`.

You may use the Singpass Troubleshooting Tool below to generate or validate your PKCE (Proof Key for Code Exchange) parameters: <https://developer.singpass.gov.sg/troubleshooting-tool>

The tool can help you:

* Generate a PKCE `code_verifier`
* Generate the corresponding `code_challenge`
* Validate existing PKCE values
* Verify that the correct `S256` transformation method is used


# (Legacy) Pre-FAPI 2.0 Singpass API Specifications

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

The purpose of this guide is to describe the necessary APIs that Relying Parties (RPs) must invoke to facilitate an Open ID Connect (OIDC) authentication for a Singpass user via the Redirect Authentication Flow.

RPs are to implement the following steps:

**Frontend:**

* Step 1a: Redirect to [Authorization endpoint](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/1.-authorization-endpoint).

**Backend:**

* Step 4: Exchange auth code with ID token (involves client authentication) using [Token endpoint](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/2.-token-endpoint).


# Overview of Singpass Flow

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

```mermaid
---
config:
  theme: base
  sequence:
    noteMargin: 20
---
sequenceDiagram
    actor User
    participant yaFE as Your App's<br>Frontend
    participant yaBE as Your App's<br>Backend
    participant Sing as Singpass


    note right of User: The Authentication Request
    User->>yaFE: The user clicks "login with<br>Singpass" on your app's FE.
    yaFE->>yaBE: This calls your app's BE.
    activate yaBE
    yaBE->>yaBE: Your app's BE generates a code_verifier, code_challenge, nonce,<br>& state, then associates it with a session (to be sent to the FE).
    yaBE->>yaBE: Your app's BE constructs an authorization URL with specific<br>query parameters: scope, response_type, client_id, redirect_uri,<br>code_challenge_method, code_challenge, nonce, & state.
    yaBE->>User: Your app's BE sets a session cookie on the user's browser,<br>and redirects the user to the authorization URL.
    deactivate yaBE
    activate yaFE
    User->>Sing: The user is redirected to the authorization URL.<br>On this page, they authenticate with Singpass and give consent<br>to release Myinfo data to your app (if applicable).
    activate Sing
    Sing->>Sing: Singpass does some checks (this is a simplification),<br>then generates an authorization code.
    Sing->>Sing: Singpass constructs a redirect URL (based on<br>the redirect_uri received) with specific<br>query parameters: code (the authorization<br>code) & state (exactly as received).
    Sing->>User: Singpass redirects the user<br>to the redirect URL.


    note right of User: The Token Request
    User->>yaBE: The user is redirected to the redirect URL,<br>with the authorization code, state, and session cookie.
    deactivate yaFE
    activate yaBE
    yaBE->>yaBE: Using the session cookie, your app's BE retrieves the<br>code_verifier, state, & nonce for this session.
    yaBE->>yaBE: Your app's BE verifies that the received state matches<br>the one generated earlier.
    yaBE->>yaBE: Your app's BE generates a client assertion.
    yaBE->>Sing: Your app's BE sends a POST request to Singpass' token endpoint<br>with: scope, grant_type, client_id, redirect_uri,<br>client_assertion_type, client_assertion,<br>code_verifier, & code (the authorization code).
    Sing->>Sing: Singpass does some checks (again, this is a<br>simplification), then generates an Access Token and<br>an ID Token. The ID Token contains the nonce sent in<br>the initial authentication request. If applicable,<br>the ID Token will also be encrypted using your<br>public encryption key.
    Sing->>yaBE: Singpass returns the Access Token and ID Token.
    yaBE->>yaBE: If applicable, your app's BE decrypts the ID Token<br>using your private encryption key.
    yaBE->>yaBE: Your app's BE validates the ID Token:<br>it must be signed with one of Singpass' signing keys,<br>its iss value must match Singpass' Issuer URL,<br>its aud value must match or contain your app's client_id, and<br>its nonce value must match the one generated earlier.
    Note right of yaBE: At this point, your app is able to use the user's ID Token<br>(i.e. the Singpass Login flow ends here).

    note right of User: The UserInfo Request (If Applicable)
    yaBE->>Sing: Your app's BE sends a GET request to Singpass' userinfo endpoint,<br>including the Access Token as a Bearer Token (via the<br>Authorization request header field.
    Sing->>Sing: Singpass does some checks (yet another<br>simplification), then prepares the userinfo response.<br>This comes in the form of a signed and encrypted<br>JWT (i.e. a nested JWT). Note that this JWT is<br>encrypted using your public encryption key.
    Sing->>yaBE: Singpass returns the userinfo response.
    yaBE->>yaBE: Your app's BE decrypts the userinfo response<br>using your private encryption key.
    yaBE->>yaBE: Your app's BE validates the userinfo response:<br>it must be signed with one of Singpass' signing keys,<br>its iss value must match Singpass' Issuer URL,<br>its aud value must match or contain your app's client_id, and<br>its sub value must match the sub claim in the ID token.
    Note right of yaBE: At this point, your app is able to use the user's info<br>(i.e. the Myinfo integration flow ends here).
    deactivate Sing

    deactivate yaBE
```


# 1. Authorization Endpoint

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

> NOTE: This section is only applicable for the Redirect Authentication Flow.

Upon user action (e.g. user clicks on a login button on the RP’s website), the RP should redirect the User Agent (browser) to Singpass's authorization endpoint with the request parameters documented below. See [OpenID connect specs](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint) for more details.

## Sample Request

> NOTE: The actual GET request is made by the browser - RPs only need to construct the URL and redirect the browser to it.

```bash
$ http GET 'https://stg-id.singpass.gov.sg/auth?scope=openid&response_type=code&redirect_uri=https%3A%2F%2Fpartner.gov.sg%2Fredirect&nonce=bb5e1672-a460-4a9b-874e-c38d55ac3922&client_id=T5sM5a53Yaw3URyDEv2y9129CbElCN2F&state=dGVzdCBzdHJpbmcK&code_challenge=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&code_challenge_method=S256'
```

## Sample Response

This will be a 302 response that redirects the browser to the Singpass login page.

## Request Parameters

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scope`                   | <p><strong>Mandatory</strong>. A string value where <code>openid</code> is the minimum scope value.<br><br><strong>For <code>/userinfo</code> flows:</strong> Multiple scope values MAY be used by creating a space-delimited, case-sensitive list of ASCII scope values. For example, <code>openid name uinfin</code>. See <a href="https://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims">OIDC Scope Values specifications</a> for more details.<br><br>The full list of supported scopes for Singpass can be found <a href="broken://pages/P7nYvaLZZKcdyFrsLsqp">here</a>.</p>                                                                                                                   |
| `response_type`           | The authorization processing flow to be used. Supported value is `code` for the Authorization Code Flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `client_id`               | <p>The <code>clientId</code> provided by Singpass during onboarding.</p><p>It is the App ID found at the top of your app configuration page.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `redirect_uri`            | The URL that Singpass will eventually redirect the user to after the user completes the login process using the Singpass App. The value will be validated against the list of redirect URIs that were pre-registered with Singpass during onboarding.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `nonce`                   | <p>A session-based, unique, and non-guessable value that the RP should generate per auth session. This parameter should ideally be generated and set by the RP’s backend and passed to the frontend. As part of threat modelling, NDI is requesting for the nonce parameter so as to mitigate MITM replay attacks against the ASP Service’s Token Endpoint and its resulting ID Token. This parameter serves the same purpose as <a href="https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest">OIDC 1.0’s nonce parameter</a>.</p><p>Maximum of 255 characters. We recommend that you use a hex-encoded random number such as <code>java.security.SecureRandom</code> or <code>UUIDv4</code>.</p> |
| `state`                   | <p>A session-based, unique, and non-guessable value that the RP should generate per auth session. This parameter should ideally be generated and set by the RP’s backend and passed to the frontend. As part of threat modelling, NDI is requesting for the state parameter so as to mitigate replay attacks against the RP’s redirection endpoint (<code>redirectUri</code>). This parameter serves the same purpose as <a href="https://tools.ietf.org/html/rfc6749#section-4.1.1">OAuth 2.0’s <code>state</code> parameter</a>.</p><p>Maximum of 255 characters. Must match <code>regexp</code> pattern of <code>\[A-Za-z0-9/+\_-=.]+,</code>.</p>                                                           |
| `code_challenge`          | <p>The hash of a code verifier generated using the hash method specified in <code>code</code><em><code>challenge\_method</code>. This is to enable Proof Key for Code Exchange (PKCE). This is an extension to the authorization code flow to prevent CSRF and authorization code injection attacks. Refer</em> <a href="https://www.rfc-editor.org/rfc/rfc7636"><em>here</em></a> <em>for more details about PKCE.</em></p><p><em>Must match <code>regexp</code> pattern of <code>\[a-zA-Z0-9</code></em><code>-]{43} (Mandatory)</code>.</p>                                                                                                                                                                  |
| `code_challenge_method`   | <p>The method used to generate the <code>code\_challenge</code> from the code verifier.</p><p>Only <code>S256</code> is supported. (Mandatory)</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `redirect_uri_https_type` | (Required if the `redirect_uri` uses is an [app-claimed HTTPS URL](https://datatracker.ietf.org/doc/html/rfc8252#section-7.2)) Supported values are `app_claimed_https` and `standard_https` (default). This value is ignored if the `redirect_uri` has a custom scheme.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `app_launch_url`          | (Optional) Intended for iOS mobile apps which use QR authentication via redirect auth. This adds the possibility for the user to be redirected back to the provided App Link after they successfully authorize themselves on the Singpass App. The value passed here should be the App Link registered with Apple’s App Store. The provided value will be validated according to the list of app launch URLs which the RP has pre-registered with NDI.                                                                                                                                                                                                                                                          |
| `esrvc`                   | <p>(Special case internal use only)<br>eService ID value for multi-tenant RPs / Singpass OIDC bridge. The value will be validated against registered eServices or registered RP’s <code>client\_external\_id</code>.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `acr_values`              | <p>(Special case internal use only)<br>Authentication Context Class Reference passed by the Singpass Portal kickoff endpoint. Will be forwarded to Singpass OIDC authorization endpoint if provided.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

Refer to this table to determine whether to include the `app_launch_url` param:

| Authenticating From                       | app\_launch\_url Param |
| ----------------------------------------- | ---------------------- |
| Relying Party website                     | Do not include         |
| Relying Party website on a mobile browser | Do not include         |
| Relying Party mobile app                  | Can include            |

## Error Response

Singpass generally follows OIDC error response specifications. For more information, please refer to [Authorization Error Response specifications](https://tools.ietf.org/html/rfc6749#section-4.1.2.1).


# Redirection on success

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Once the user has authenticated successfully, Singpass will redirect the browser to the RP’s registered `redirectUri` along with the `code` and `state` parameters or an interstitial page for users have launched authentication from the RP’s native app.

The interstitial page is required to solicit a user interaction for launching from certain in-app browsers. Singpass will redirect to the interstitial page if the `redirectUri` is custom-schemed or app-claimed HTTPS. To specify that the `redirectUri` is an app-claimed HTTPS, the RP must include the query parameter `redirect_uri_https_type=app_claimed_https` at [Authorization endpoint](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/1.-authorization-endpoint).

Example redirect location: **`https://partner.gov.sg/redirect?code=XcyzlSeX1hIyJFlstxsSF_UeXC5DtiYkFgJ8VVx52mg&state=NGRlZThmNzQtZDU5YS00YTY1LWFkODItYmE4NDA4Y2UwY2Uw`**

| Parameter | Description                                                                                                                                                                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code      | A securely generated random number in **base64-url** format. This parameter must be sent to the [Token endpoint](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/2.-token-endpoint) along with others to exchange for the user’s ID token. |
| state     | The same `state` parameter provided to the [Authorization endpoint](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/1.-authorization-endpoint).                             |

Once redirected, the RP should invoke the [Token endpoint](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/2.-token-endpoint) to obtain an ID token and complete the login process.

> Note: The `code` parameter has a lifetime of **2 minutes**. RPs must exchange it for an ID token within this period.


# For Mobile Developers

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

To facilitate your in-app browser implementation, the following table contains technical resources to help assess, test and implement the changes requested.

|                                                                                                                                            | Android                                                                                                              | iOS                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sample codes implementing the recommended Proof Key for Code Exchange ([PKCE](https://www.rfc-editor.org/rfc/rfc8252)) for Singpass logins | [Android-Singpass-in-app-browser-login-demo](https://github.com/singpass/Android-Singpass-in-app-browser-login-demo) | [iOS-Singpass-in-app-browser-login-demo](https://github.com/singpass/iOS-Singpass-in-app-browser-login-demo)                                                                                                                                                                                                                                                                                                                                                    |
| In-app browser documentations                                                                                                              | [Chrome Custom Tabs](https://developer.chrome.com/docs/android/custom-tabs)                                          | <p>\[iOS 9 to iOS 10]<br><a href="https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller">SFSafariViewController</a><br><br>\[iOS 11]<br><a href="https://developer.apple.com/documentation/safariservices/sfauthenticationsession">SFAuthenticationSession</a><br><br>\[iOS 12 and above]<br><a href="https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession">ASWebAuthenticationSession</a></p> |

<br>


# 2. Token Endpoint

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Endpoint to obtain an ID token and access token. The ID token is a signed JWT that contains user information in the `sub` claim, and is signed by Singpass ASP. RPs will be able to verify the ID token’s JWT signature with our [JWKS endpoint](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/.well-known-endpoints/jwks-endpoint). RPs are expected to validate the ID token as per [OpenID connect specs](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).

For the OIDC authentication flow, only the following grant(s) is supported:

* `authorization_code` (see the [Authentication using the Authorization Code Flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) in the OpenID connect specs for more details)

In the below sections, we are going to describe the API contract:

* [Authorization Code Grant](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant)
* [Client JWK Requirements](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/client-jwk-requirements)


# Authorization Code Grant

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

## Client Authentication - Client Assertion JWT

### Assertion JWT Structure

The RP is required to generate an assertion JWT that has the following header and claims, and is signed with the JWK that was provided during onboarding.

#### **JWT Header**

The header **must include `alg` and `typ`**.

The supported `alg` types are:

* `ES256`
* `ES384`
* `ES512`.

This must match the `alg` value in the signing key used to sign the assertion (if the signing JWK specifies `alg` explicitly).

The header should also include `kid` of the signing key to help identify which of the RP’s signing keys was used, though this is not mandatory. If omitted, we will test against all known signing keys when attempting to verify the signature.

*example*

```json
{
  "typ": "JWT",
  "alg": "ES256",
  "kid": "rp_key_01"
}
```

#### **JWT Claims**

| Path   | Type     | Description                                                                                                                                                                                                                                                                                                  |
| ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sub`  | `String` | This should be `client_id` of the registered client.                                                                                                                                                                                                                                                         |
| `aud`  | `String` | The recipient that the JWT is intended for. This must match the `issuer` field in the response of the OpenID discovery endpoint (<https://id.singpass.gov.sg/.well-known/openid-configuration>) e.g. [https://id.singpass.gov.sg](https://id.singpass.gov.sg/).                                              |
| `iss`  | `String` | This should be `client_id` of the registered client.                                                                                                                                                                                                                                                         |
| `iat`  | `Number` | The time at which the JWT was issued. <https://tools.ietf.org/html/rfc7519#section-4.1.6>                                                                                                                                                                                                                    |
| `exp`  | `Number` | The expiration time on or after which the JWT MUST NOT be accepted by Singpass for processing. Additionally, Singpass will not accept tokens with an `exp` longer than 2 minutes since `iat`. <https://tools.ietf.org/html/rfc7519#section-4.1.4>                                                            |
| `jti`  | `String` | A unique identifier for this token. This identifier must only be used once. You should generate a new `jti` value for every request.                                                                                                                                                                         |
| `code` | `String` | (Optional) This should be the auth `code` which is used to exchange for an ID token. It should be identical to the `code` form param sent outside the `client_assertion`. This enables increased security by signing the `code` so that the `client_assertion` can only be used once for a specific request. |

### Request / Response Structure

Curl request

```bash
$ curl 'https://stg-id.singpass.gov.sg/token' -i -X POST \
    -H 'Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1' \
    -d 'grant_type=authorization_code&redirect_uri=http%3A%2F%2Fexample.com&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJraWQiOiJycF9rZXlfMDEiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJnblk2RXJpY2hwYjV0NE5GUlA5UjRMN2FFQzlOMEZRSCIsImF1ZCI6Imh0dHBzOi8vc3RnLWlkLnNpbmdwYXNzLmdvdi5zZyIsImNvZGUiOiJuMGVzYzNOUnplN0xUQ3U3aVl6UzZhNWFjYzNmMG9ncDQiLCJpc3MiOiJodHRwOi8vZXhhbXBsZS5jb20iLCJleHAiOjE3MjczMjIwNjUsImlhdCI6MTcyNzMyMTk0NX0.AAAAAAAAAAAAAAAAAAAAAIvHG8uapa4w10pPn_S_7uyYPXNJWU7389sTLNHXrCKhAAAAAAAAAAAAAAAAAAAAAIxyKbbZfLSkduU6WIPrrPe1kGvmHmzXL4PHpgAJ0g0d&code=n0esc3NRze7LTCu7iYzS6a5acc3f0ogp4&client_id=gnY6Erichpb5t4NFRP9R4L7aEC9N0FQH&code_verifier=mN7szCmmIc6Z2Vg-iaX7f7RDVsKAhY5GG-r7Crq0jxTdxY0xyPKnsAEWtEMdZ3D8QW5rs-C824W3Jwntcw'
```

#### Form parameters

<table><thead><tr><th width="278">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>client_id</code></td><td>The Client Identifier registered. It is the App ID found at the top of your app configuration page.</td></tr><tr><td><code>redirect_uri</code></td><td>The redirect URI being used in this auth session.</td></tr><tr><td><code>grant_type</code></td><td>The type of grant being requested. This must be set to <code>authorization_code</code>.</td></tr><tr><td><code>code</code></td><td>The code issued earlier in the auth session.</td></tr><tr><td><code>scope</code></td><td>(Optional) If no value is provided, it defaults to <code>openid</code>. If provided, then only <code>openid</code> is allowed.</td></tr><tr><td><code>client_assertion_type</code></td><td>This MUST be set to <code>urn:ietf:params:oauth:client-assertion-type:jwt-bearer</code>.</td></tr><tr><td><code>client_assertion</code></td><td>A JWT identifying the client.</td></tr><tr><td><code>code_verifier</code></td><td><p>(Mandatory) This is the session-based, unique, and non-guessable value that the RP had used to generate the <code>code_challenge</code>.</p><p>Must match <code>regexp</code> pattern of <code>[a-zA-Z0-9_\-.~]+</code> minimum length of 43 characters and a maximum length of 128 characters.</p></td></tr></tbody></table>

#### HTTP request

```http
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-1
Host: stg-id.singpass.gov.sg
Content-Length: 788

grant_type=authorization_code&redirect_uri=http%3A%2F%2Fexample.com&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJraWQiOiJycF9rZXlfMDEiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJnblk2RXJpY2hwYjV0NE5GUlA5UjRMN2FFQzlOMEZRSCIsImF1ZCI6Imh0dHBzOi8vc3RnLWlkLnNpbmdwYXNzLmdvdi5zZyIsImNvZGUiOiJuMGVzYzNOUnplN0xUQ3U3aVl6UzZhNWFjYzNmMG9ncDQiLCJpc3MiOiJodHRwOi8vZXhhbXBsZS5jb20iLCJleHAiOjE3MjczMjIwNjUsImlhdCI6MTcyNzMyMTk0NX0.AAAAAAAAAAAAAAAAAAAAAIvHG8uapa4w10pPn_S_7uyYPXNJWU7389sTLNHXrCKhAAAAAAAAAAAAAAAAAAAAAIxyKbbZfLSkduU6WIPrrPe1kGvmHmzXL4PHpgAJ0g0d&code=n0esc3NRze7LTCu7iYzS6a5acc3f0ogp4&client_id=gnY6Erichpb5t4NFRP9R4L7aEC9N0FQH&code_verifier=mN7szCmmIc6Z2Vg-iaX7f7RDVsKAhY5GG-r7Crq0jxTdxY0xyPKnsAEWtEMdZ3D8QW5rs-C824W3Jwntcw
```

#### HTTP response

```http
HTTP/1.1 200 OK
Cache-Control: no-cache, no-store, must-revalidate
x-ndi-response-category: client-assertion-auth-code
X-XSS-Protection: 0
X-Frame-Options: DENY
Date: Thu, 26 Sep 2024 03:39:05 GMT
Connection: keep-alive
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Content-Type-Options: nosniff
Transfer-Encoding: chunked
Content-Type: application/json
Content-Length: 597

{
  "access_token" : "Ul5JqK8vJX8Jfgo7UjpiIigF7DciW7YGnUACLN1/T80=",
  "token_type" : "Bearer",
  "id_token" : "eyJraWQiOiJuZGlfc3RnXzAxIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJhdWQiOiJnblk2RXJpY2hwYjV0NE5GUlA5UjRMN2FFQzlOMEZRSCIsInN1YiI6InM9Uzg4MjkzMTRCLHU9MWMwY2VlMzgtM2E4Zi00ZjhhLTgzYmMtN2EwZTRjNTlkNmE5IiwiYW1yIjpbInB3ZCIsInN3ayJdLCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2ciLCJleHAiOjE3MjczMjI1NDUsImlhdCI6MTcyNzMyMTk0NSwibm9uY2UiOiJMNW5tUWZjZXREREllaW5jb3F2Q3JGeUd2K25Ib2JrdjRYb2NOWVBDWGFRPSJ9.bD1osnkuL-hXCXY9L_LbveANix_tBsjk8872bL04tTPFGMkzMjE85W8fTwQXrPSFnwQtgzmLB2__i0vdGYnfgA"
}
```

#### Request body

```http
grant_type=authorization_code&redirect_uri=http%3A%2F%2Fexample.com&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJraWQiOiJycF9rZXlfMDEiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzM4NCJ9.eyJzdWIiOiJnblk2RXJpY2hwYjV0NE5GUlA5UjRMN2FFQzlOMEZRSCIsImF1ZCI6Imh0dHBzOi8vc3RnLWlkLnNpbmdwYXNzLmdvdi5zZyIsImNvZGUiOiJuMGVzYzNOUnplN0xUQ3U3aVl6UzZhNWFjYzNmMG9ncDQiLCJpc3MiOiJodHRwOi8vZXhhbXBsZS5jb20iLCJleHAiOjE3MjczMjIwNjUsImlhdCI6MTcyNzMyMTk0NX0.AAAAAAAAAAAAAAAAAAAAAIvHG8uapa4w10pPn_S_7uyYPXNJWU7389sTLNHXrCKhAAAAAAAAAAAAAAAAAAAAAIxyKbbZfLSkduU6WIPrrPe1kGvmHmzXL4PHpgAJ0g0d&code=n0esc3NRze7LTCu7iYzS6a5acc3f0ogp4&client_id=gnY6Erichpb5t4NFRP9R4L7aEC9N0FQH&code_verifier=mN7szCmmIc6Z2Vg-iaX7f7RDVsKAhY5GG-r7Crq0jxTdxY0xyPKnsAEWtEMdZ3D8QW5rs-C824W3Jwntcw
```

#### Response body

```json
{
  "access_token": "Ul5JqK8vJX8Jfgo7UjpiIigF7DciW7YGnUACLN1/T80=",
  "token_type": "Bearer",
  "id_token": "eyJraWQiOiJuZGlfc3RnXzAxIiwidHlwIjoiSldUIiwiYWxnIjoiRVMyNTYifQ.eyJhdWQiOiJnblk2RXJpY2hwYjV0NE5GUlA5UjRMN2FFQzlOMEZRSCIsInN1YiI6InM9Uzg4MjkzMTRCLHU9MWMwY2VlMzgtM2E4Zi00ZjhhLTgzYmMtN2EwZTRjNTlkNmE5IiwiYW1yIjpbInB3ZCIsInN3ayJdLCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2ciLCJleHAiOjE3MjczMjI1NDUsImlhdCI6MTcyNzMyMTk0NSwibm9uY2UiOiJMNW5tUWZjZXREREllaW5jb3F2Q3JGeUd2K25Ib2JrdjRYb2NOWVBDWGFRPSJ9.bD1osnkuL-hXCXY9L_LbveANix_tBsjk8872bL04tTPFGMkzMjE85W8fTwQXrPSFnwQtgzmLB2__i0vdGYnfgA"
}
```

#### Response fields

<table><thead><tr><th width="205">Path</th><th width="134">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>access_token</code></td><td><code>String</code></td><td>For Login flows, the access token will be a random string that is not to be used.<br><br>For Myinfo flows, the token will be an encoded JSON Web Token (JWT). This token is to be used to exchange for payload at UserInfo Endpoint.</td></tr><tr><td><code>token_type</code></td><td><code>String</code></td><td>The type of token being requested, Bearer only so far.</td></tr><tr><td><code>id_token</code></td><td><code>String</code></td><td>The ID token with relevant claims in JWT format signed by the ASP. Note that the example response body shows a JWS (3-part structure separated by dots), but the format will differ for a JWS in JWE (5-part structure). Refer <a href="#id-token-structure">here</a> for more details about the ID token structure.</td></tr></tbody></table>

### **Error Response**

Singpass generally follows OIDC error response specifications. For more information, please refer to [Token Error Response specifications](https://tools.ietf.org/html/rfc6749#section-5.2).

## ID Token Structure

The format and structure of the issued ID Token will vary depending on the client’s profile as specified in this table below:

| Client Profile                            | `sub` Claim Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | ID token format                                                                                                |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `direct`                                  | UUID only (eg. `u=32af8b7d-ad1d-4c25-8dc7-0a981b533000`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | JWS                                                                                                            |
| `direct_pii_allowed`                      | <p><strong>Regular NRIC holders</strong>: NRIC and UUID (eg. <code>s=S1234567A,u=32af8b7d-ad1d-4c25-8dc7-0a981b533000</code>)<br></p><p><strong>Singpass Foreign Account (SFA) holders</strong>: Singpass User ID (UID), Foreigner ID (FID), Country-of-Issuance (COI) and UUID (eg. <code>s=Y7613265T,fid=G730Z-H5P96,coi=DE,u=e2af740e-25b4-4b19-b527-494670952cb0</code>)<br></p><p>This class of users were previously known as "Foreign Unique Account" or "Singpass Foreign Unique Account" users. Only designated relying parties are able to have SFA users authenticate & complete token exchange.</p> | <p>JWS in JWE (encrypted with client’s JWK)</p><p>See section below for more details about the JWE format.</p> |
| `bridge` (special case internal use only) | NRIC and UUID (eg. `s=S1234567A,u=32af8b7d-ad1d-4c25-8dc7-0a981b533000`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | JWS                                                                                                            |

### Overview of a JWS in JWE

An encrypted ID token will returned from the `/token` endpoint is a JWS in JWE that is in compact serialization form. It has the following structure:

* JWE Header
* Encrypted Key
* Initialization Vector
* Encrypted Payload (if decrypted, this would be the Base64 encoded form of a [JWS ID Token](#overview-of-jws))
* Authentication Tag

See <https://datatracker.ietf.org/doc/html/rfc7516#section-3.1> for more details.

### JWE Header

The JWE will contain these standard headers. Refer to <https://tools.ietf.org/html/rfc7515#section-4> for more information about each header.

> Note: Relying parties should use the `kid` field in the header to determine which key NDI used for encryption.

*example*

```json
{
  "kid": "client_01",
  "cty": "JWT",
  "enc": "A256CBC-HS512",
  "alg": "ECDH-ES+A256KW"
}
```

### Overview of JWS

The [JWS](https://tools.ietf.org/html/rfc7515) ID token returned from the `/token` endpoint is in compact serialization form. A JWS has the following structure.

* JWS Header
* Payload (containing claims)
* Signature

### JWS Header

The JWS ID token will contain these standard headers. Refer to <https://tools.ietf.org/html/rfc7515#section-4> for more information about each header.

*example*

```json
{
  "kid": "ndi_stg_01",
  "typ": "JWT",
  "alg": "ES256"
}
```

### JWS Claims<br>

The JWS ID token will contain the following claims.

*example*

```json
{
  "aud": "gnY6Erichpb5t4NFRP9R4L7aEC9N0FQH",
  "sub": "s=S8829314B,u=1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9",
  "amr": ["pwd", "swk"],
  "iss": "https://stg-id.singpass.gov.sg",
  "exp": 1727322545,
  "iat": 1727321945,
  "nonce": "L5nmQfcetDDIeincoqvCrFyGv+nHobkv4XocNYPCXaQ="
}
```

*Table 1. Description of Claims*

| Path    | Type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sub`   | `String` | The principal that is the subject of the JWT. Contains a comma-separated, key=value mapping that identifies the user; possibly including multiple alternate IDs representing the user. The keys included vary by the profile of the OIDC client, and the user type, however the minimal format is `u=<UUID>` where UUID represents the user’s globally unique identifier. <https://tools.ietf.org/html/rfc7519#section-4.1.2> |
| `aud`   | `String` | The client\_id of the relying party. <https://tools.ietf.org/html/rfc7519#section-4.1.3>                                                                                                                                                                                                                                                                                                                                      |
| `iss`   | `String` | The principal that issued the JWT. <https://tools.ietf.org/html/rfc7519#section-4.1.1>                                                                                                                                                                                                                                                                                                                                        |
| `iat`   | `Number` | The time at which the JWT was issued. <https://tools.ietf.org/html/rfc7519#section-4.1.6>                                                                                                                                                                                                                                                                                                                                     |
| `exp`   | `Number` | The expiration time on or after which the JWT MUST NOT be accepted for processing. Defaults to 10 minutes since "iat". <https://tools.ietf.org/html/rfc7519#section-4.1.4>                                                                                                                                                                                                                                                    |
| `amr`   | `Array`  | Authentication method references. Example values are `["face"]`, `["fv"]`, `["fv-alt"]`, `["otp"]`, `["pwd","fv"]`, `["pwd","otp-email"]`, `["pwd","sms"]`, `["pwd","swk"]`, `["pwd"]`, `["sso"]`. Note that this list is non-exhaustive, and NDI reserves the right to introduce new values without prior notice to RPs.                                                                                                     |
| `nonce` | `String` | String value used to associate a Client session with an ID Token, and to mitigate replay attacks. The value is passed through unmodified from the Authentication Request to the ID Token. Clients MUST verify that the nonce Claim Value is equal to the value of the nonce parameter sent in the Authentication Request. <https://openid.net/specs/openid-connect-core-1_0.html#IDToken>                                     |
| `acr`   | `String` | (Optional) The Authentication Context Class Reference. The values are context-specific and agreed upon between NDI and relying parties when used.                                                                                                                                                                                                                                                                             |


# Client JWK Requirements

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Clients are expected to provide public keys to Singpass in the [JWK](https://tools.ietf.org/html/rfc7517) format. These public keys will be used in the following (non-exhaustive) scenarios:

* Signature JWK used to verify the signature of the [client assertion JWT](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant#client-authentication-client-assertion-jwt) presented during token request.
* Encryption JWK used to [encrypt an ID token](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant) which contains the user’s PII.

The client must provide the public key(s) during onboarding, and they can do so only via **ONE** of the following forms:

* Provide a JWKS in a JSON format.
* Host the JWKS on a publicly accessible URL. This endpoint must be compatible with Singpass's [service level expectations](#jwks-url-service-level-expectations).

Signing key is always required for both `direct` and `direct_pii_allowed` clients. Encryption key is only required for `direct_pii_allowed` clients. `direct_pii_allowed` clients must ensure that the provided JWKS or the resource returned by the JWKS URL contains both the signing and encryption keys.

> TIP: [mkjwk.org](https://mkjwk.org/) is a useful open-source tool to generate different types of JWK for signing and encryption; compliant with Singpass's broad requirements on structure. While we **DO NOT** suggest this as a secure way to generate your *real* keypair (including private key); this can be a useful tool to understand how JWK works; and how it is represented for signing and encryption purposes; while you are reviewing against our supported algorithms below.

## JWK for signing

The signing JWK will be used to verify the [client assertion JWT](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant#client-authentication-client-assertion-jwt) provided during `/token` request, thereby authenticating the client.

Clients are allowed to provide multiple signature keys in the JWKS / hosted on the JWKS url provided during client creation.

The signature JWK should have the following attributes:

* Must have key `use` of value `sig` per [rfc7517#section-4.2](https://tools.ietf.org/html/rfc7517#section-4.2)
* Must contain a key ID in the standard `kid` field per [rfc7517#section-4.5](https://tools.ietf.org/html/rfc7517#section-4.5)
  * Will be used by Singpass to select the relevant key to verify the client assertion
* Must be an EC key, with curves: `P-256`, `P-384` or `P-521` *(NIST curves, aka `secp256r1`, `secp384r1`, `secp521r1` respectively)*

*Example EC signing key using P-256 and a timestamped key Id*

```json
{
  "kty": "EC",
  "use": "sig",
  "kid": "sig-2021-01-15T12:09:06Z",
  "crv": "P-256",
  "x": "Tjm2thouQXSUJSrKDyMfVGe6ZQRWqCr0UgeSbNKiNi8",
  "y": "8BuGGu519a5xczbArHq1_iVJjGGBSlV5m_FGBJmiFtE"
}
```

### **Key Rotation**

Relying parties can **rotate** their signing keys in a self-driven manner. To do this with **zero downtime** the Relying party must

* support use of **JWKS URLs** and be onboarded as such
* ensure their replacement signing key has a different key ID (`kid`) to the original key
* ensure their replacement signing key matches the other cryptographic key requirements

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                  |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new signing key pair (`K2`) supported for signing.                                                            |
| T0            | Relying party **adds** public key `K2` to its JWKS endpoint (and leaves `K1` on the endpoint).                                          |
| T0 - T+1 hour | Singpass's cache will expire, and re-retrieves the relying party’s published keys from their JWKS endpoint which now includes `K2`.     |
| > T+1 hour    | Relying party changes their system to start signing client assertions using the new signing key `K2`.                                   |
| Clean Up      | Post-validation, relying party can remove key `K1` from their JWKS endpoint when they are comfortable their new signing key is working. |

## **JWK for encryption**

The encryption JWK will be used to [encrypt ID tokens](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant) requested from the `/token` endpoint.

Singpass will select the strongest available, supported encryption key from either a **local JWKS**, or **JWKS URL** to encrypt returned ID tokens for those relying parties who require any PII in the ID token.

The encryption JWK must have the following attributes:

* Must not contain the `d` property
  * The `d` property represents the private key of your key pair, and should never be exposed. Exposure in the JWK is a critical security vulnerability.
  * If you have accidentally included the `d` property in your JWK, remove it immediately and rotate your keys.
* Must have key `use` of value `enc` per [rfc7517#section-4.2](https://tools.ietf.org/html/rfc7517#section-4.2)
* Must contain a key ID in the standard `kid` field per [rfc7517#section-4.5](https://tools.ietf.org/html/rfc7517#section-4.5)
  * The key ID will be specified in the returned JWE header so that clients can pick the right key for decryption
* Must have key type (`kty`) of `EC`
* Must specify the appropriate key encryption `alg` the relying party wants Singpass to use, consistent with the key type/curve (`kty`), and meet the requirements below on allowed `alg`/`curve`/key sizes, consistent with [RFC7518 - JSON Web Algorithm specification](https://tools.ietf.org/html/rfc7518#section-4.1)

| Status                           | **Required** for new Relying Parties                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Key encryption algorithm (`alg`) | <p>ECDH-ES+A128KW<br>ECDH-ES+A192KW<br>ECDH-ES+A256KW</p>                                                                   |
| Curve (`crv`)                    | <p>P-256 <em>(NIST, aka secp256r1)</em><br>P-384 <em>(NIST, aka secp384r1)</em><br>P-521 <em>(NIST, aka secp521r1)</em></p> |

*Example EC encryption key using P-256 and a timestamped key Id; asking us to encrypt the CEK using ECDH-ES+A128KW*

```json
{
  "kty": "EC",
  "use": "enc",
  "kid": "enc-2021-01-15T12:09:06Z",
  "crv": "P-256",
  "x": "xom6kD54yfXRPvMFVYFlVjUKzmNhz7wf0DP_2h9kXtY",
  "y": "lrh8C9c8-SBJTm1FcfqLkj2AnHtaxpnB1qsN6PiFFJE",
  "alg": "ECDH-ES+A128KW"
}
```

### **Key Preference**

If the relying party exposes *multiple supported encryption keys*, Singpass will select the key to use for encrypting tokens based on the following logic:

1. prefer any EC key (`kty`) matching the above requirements
2. prefer EC keys with stronger `crv` (curve) *above* EC keys with weaker curve
3. prefer EC keys with stronger `alg` key wrapping *above* weaker ones
4. otherwise pick the first compatible key we find

### **Key Rotation**

Relying parties can **rotate** their encryption keys in a self-driven manner. To do this with **zero downtime** the Relying party must

* support use of **JWKS URLs** and be onboarded as such
* have the ability to decrypt tokens produced with either **one of two** different encryption keys based on either
  * selecting the correct decryption key by its key ID (`kid`)
  * trial-and-error decryption against multiple keys in a collection
* ensure their replacement key matches the other cryptographic key requirements noted above

To do this with zero downtime, the following procedure should be followed by the Relying Party:

| Time          | Action                                                                                                                                                          |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prep          | Relying party generates a new encryption key pair (`K2`) supported for decryption. The existing key pair (`K1`) is still available for decryption of ID tokens. |
| T0            | Relying party **removes** public key `K1` and **adds** public key `K2` on its JWKS endpoint.                                                                    |
| T0 - T+1 hour | Singpass's caches will expire at any (indeterminate) time within this period, and start encrypting tokens with new encryption key `K2`.                         |
| T0 - T+1 hour | Relying party may be receiving tokens encrypted with either `K1` or `K2` keys throughout this period; and must be able to decrypt either.                       |
| > T+1 hour    | Relying party can remove support for decrypting with the previous `K1` key.                                                                                     |

## JWKS URL Service Level Expectations

Singpass requires that any JWKS is published on an endpoint that

* is served behind HTTPS on port `443` using a TLS server certificate issued by a standard *publicly verifiable CA issuer* (no private CAs), with *complete cert chain* presented by the server;
* is publicly accessible (no IP whitelisting, mTLS or other custom HTTP header requirements outside standard HTTP headers such as `Content-Type`, `Accept`);
* is able to respond in a timely fashion with respect to the below configuration.

| Per try timeout                   | 3s |
| --------------------------------- | -- |
| Max attempts                      | 3  |
| Cache duration for retrieved JWKS | 1h |

> Note: While the above is a technical requirement; the user experience of your users may be affected if we are unable to retrieve your JWKS in a timely fashion upon our cache expiry due to slower token exchanges with your backend. We recommend aiming for this response to be as fast as possible based on an in-memory cache; or simple static asset retrieval.

If Singpass fails to retrieve a valid JWKS from the provided URL after cache expiry, the relying party’s token exchange will fail with an OAuth2/OIDC `invalid_client` error in these circumstances:

* if *client assertions* are used, and we are unable to validate the relying party’s assertion using their signing key
* if *encryption of returned ID tokens* is required, and we are unable to retrieve the relying party’s preferred encryption key


# 3. Userinfo Endpoint

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

The UserInfo endpoint is an OAuth 2.0 [protected resource](http://tools.ietf.org/html/rfc6749#section-7) of the Singpass Authentication server; where client applications can retrieve consented [claims](http://openid.net/specs/openid-connect-core-1_0.html#Claims), or assertions, about the logged-in end-user.

The claims are typically packaged in a JSON object where the `sub` member denotes the subject (end-user) identifier, along with the data items that were tagged to the scopes requested in the `/auth` [request parameters](https://docs.developer.singpass.gov.sg/docs/technical-specifications/singpass-authentication-api/1.-authorization-endpoint#request-parameters) earlier.

> The full list of scopes are under the [Myinfo Data Catalogue](broken://pages/P7nYvaLZZKcdyFrsLsqp).

For the purposes of Userinfo in the context of Singpass, we will be returning an encrypted payload in the form of a signed JSON Web Token (JWS) in a JSON Web Encrypted (JWE) token.


# Requesting Userinfo

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

Clients must present a valid access token (of type `Bearer`) to retrieve the UserInfo claims. This access token is produced from the [token endpoint](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant#http-response). Only those claims that are scoped in the successful authentication request will be made available to the client.

Example request to get the `userinfo` claims:

```http
GET /userinfo HTTP/1.1
Host: id.singpass.gov.sg
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6ImF0K2p3dCIsImtpZCI6ImFsaWFzL3ByZC1zcC1hdXRoLWFwaS1pZC10b2tlbi1zaWduaW5nLWtleS1rbXMtYXN5bW1ldHJpYy1rZXktYWxpYXMifQ.eyJzdWIiOiJzPVM2NTAwMDEwRSx1PWIyMGVhNjRhLTc2OTQtNDQyZi04Njc0LTRjMDVkNmQ5NDdmZiIsImNsaWVudF9pZCI6Ik9RYnNHU0NUNWRzUEhmUWdGbGlieUZud1g0YUpXYWlaIiwic2NvcGUiOiJvcGVuaWQgdWluZmluIG5hbWUgYmlydGhjb3VudHJ5IGRpYWxlY3QgZG9iIGhhbnl1cGlueWlubmFtZSBuYXRpb25hbGl0eSBwYXNzcG9ydGV4cGlyeWRhdGUgcGFzc3BvcnRudW1iZXIgcmFjZSByZXNpZGVudGlhbHN0YXR1cyBzZWNvbmRhcnlyYWNlIHNleCIsImp0aSI6ImF0LWJRTmEtT2FveEdvdXh3TTFiSmtsTU5leFNvSjJLOXJOcGdFS0wyb0ptcEEiLCJpYXQiOjE3Mjg2MjIxMTksImV4cCI6MTcyODYyMzkxOSwiYXVkIjoiaHR0cHM6Ly9pZC5zaW5ncGFzcy5nb3Yuc2cvdXNlcmluZm8iLCJpc3MiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZyJ9.3KjEQKXEhc88e6mRCv6sIe4U-psd1Pe4hLp7hQCN6MQGcHNFHpL8lmJ3B-RAxeunb-HKAxQLfSWnzpu767EQYQ
```

Example response:

```http
HTTP/1.1 200 OK
Content-Type: application/jwt;
eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiJ0ZXN0LXJwLWtleS0wMSIsImVwayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6IjZkWHpIbFBFT2d0c0ZCZlc0THRlNlV3a00taXk2NGJ0dkF2c0R2WTYtd00iLCJ5IjoiZDRTZkdrYnRiZ19lakhPZnJ6Ul9fU2R1b0tCYVluVHVKbU84Uk0zUWFENCJ9fQ.jZi6w7zl9Tbl0t-AucyVCIzoaztu6QAtvQh4eegdBQ5ekTRJBPhChtuaT0WLVRsWd7WFmiZA3R27VVs6ZoYZy2_Oq7-SfNpZ.FhY_KkI5FhrsEz-v77SrwQ.rGdyiIXNvn_pra6AW48V_zIR59C4qDVL0JdJ9lmz9OLmnepy4X2ZpfbvaU54NU6d94g9KjWRYUprqoFLBQJB2c1_87qfCT-phkluJOYX0nyEIHahYvqADmxd7wtu3KguYEz45EPa2mSLgYM6ieUsR0Mw5s9pUjPkl3TomSIeN-4K9ZebeyPbkygxiT7bX74o31ODqXRDED-2kqeTpuqs6Dx92sUV-HNhPDIVnYp7nJurqvh46mF4Zt83OuH3QDOVmQsQQxYUupE95vfRZae9cQx8ZMrGTC-GSXNAqv2Gd6q5V4n9FFBwsOvsn-Gwd6i3gxYKMYr8k4jRQ2ykBYtFWMryeBZQCBhHaZEpcbZFCgLaD5XvXmWjNwA1Qm_gkPBF6Luhm6wYgjURxCwA7FQx4sZkrNL5jZjTfRaW38GiBHnvTXEPdGFVzXwIohVVqCCFr7nrf1uQfq1UXKduZVrtcTLnX7v1-sVEhpFyGFCmDtKAtQSaLvg4IMDK7U943NgB3ddRjJK4PQuBtivexSBgJc_RRIKIBKIQJxI3WYId0-WxmDsMSzgCZ5iJWIfKqUEAbhImtK2vzcqNs8obgEeIfzZPYd9g977l0PgPiJzfoCBQDirxu-ftEOLlepT6YIMnetSbrs3y6bQDjdMBv-SDXHRwFT7qRZefdoUSV9yhsN52_U4P8W7u4l_uUJWZHZyhxgMDg7AluRBSPG2g4ti7I8B_3cYsEY9m4YYYMLlIhhM5cRg4KfJeoRH7UK9unkNeyGRjLLRLwisL3tQN1KsPdVeaAUYOuFKtaz-3U8lW3zprYdeJ0cNERiToczOjmpvv.PUNV3te9SF7OgGY8UFbIzTBJy7iJhBb4RDy9Kj5cuFc
```

{% hint style="success" %}
An access token can be re-used up to its validity period of thirty (30) minutes.
{% endhint %}

### **Error Response**

Singpass generally follows OIDC error response specifications. For more information, please refer to the [Userinfo error response specifications](https://openid.net/specs/openid-connect-core-1_0.html#UserInfoError).

***

**An access token is only valid for 30 minutes**.

Sending a request to the `/userinfo` endpoint beyond its lifetime will result in an `invalid_token` error:

```http
HTTP/1.1 401 Unauthorized
Date: Wed, 09 Oct 2024 10:49:52 GMT
Content-Type: application/json; charset=utf-8

{"id":"afc64481-a01b-44c8-a716-52ef45c9c527","error":"invalid_token","error_description":"An error has occurred.","trace_id":"1-67065fd0-079db77d1f7a760e616f2271"}
```


# Validating the payload

{% hint style="danger" %}
All Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant authentication API](broken://pages/MsIagGMlUBUeCNFCcqI3) by 31 Dec 2026.

The specifications on this page apply to you only if you are maintaining an existing Login / Myinfo (v5) integration. We encourage you to [migrate](broken://pages/TjKrhykp8SG191nbTozq) early to avoid service disruptions.
{% endhint %}

As mentioned in [the introduction](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/3.-userinfo-endpoint), the response returned from the GET `/userinfo` endpoint will be a [JWS within the payload of a JWE token](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/legacy-pre-fapi-2.0-api-specifications/technical-specifications/singpass-authentication-api/2.-token-endpoint/authorization-code-grant#overview-of-a-jws-in-jwe).

For example, the response typically returns the following JWE token:

```
eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiJ0ZXN0LXJwLWtleS0wMSIsImVwayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6Ik1RVTBWRnlfUWFUYktzTmJrVTdMZkFnUjJ2Y1FQYW94UzBXM2RLRm9yOU0iLCJ5IjoibkdRam5PRlZ4emdzRERjMUJqQ3otZi1KeUY4VC14WW0xQVp4NjFtZWVCOCJ9fQ.gDvjBmkLqQ42hbNM2ULPwaskGPBlLvslPAqr0XcN2a-OYqOHXKfwvoUUOuoibTfzg_l8rr-WalvY8FY_a8yfHOaL2GLt6ZWj.O_tgtrTbPRbL_p0Y2rvnCQ.38npNWj1nL1AQxS2A3JrxokxHms6GPYT2OFhaFghI7N0QkR48gPuUvKi-m7wPbESTYA-9O-bSHEX9fUXD4FtlztrhjRTpGmdfppooVMn9_bHcLLyHbHnS3_yW5JaybqHNfD6zXCB1pw24vvHfGmRJ7C86CeBgosuYslMk7y7m_rIT6YhVnotN_kRBOppVW9eC3g0upRxXQJ3O10__pR-QcBb_eXKqwm6tcpeTEqBPl0Dbedk6DDoq6KSRV5LzyFLMutAjInQpKGdWYa7FCgfHL3FWNfcwyPq27s3d14ArZJVkIJsOW_VTI_lrnSBzCcdJpbGj9wPe0e2SfslliZlSxYTTpECyV5AZZgwxz0pMaE85Ob7KzrJjMdbZqZZC53HnZmq6pS8RiUce4950IwvsfF0xDUDaZuMxKnISoPcuUX2jHr8FG0SytO8Pr6m3DyOYbQnSkUFdjCRSHiKRqDxlqM15hSkle3jtd9qf-EzuGeHNqaJCjD7XWeviwJgD70fUZDM8lDvCp5mTfl0pcy7mlGEWjVmfR3MB1ohGwkZLeq3H_KrCyhn_FJ-DRPiE4oIaO8oSsFOhRocND4RDlliOIRK_B1XRmw1YpJFBRpn04N2ytnJrxCJ4cZeTEa4QCYkKaJHPqWkN_qvdgxywkwELLB5Tb1sgdKcq3Kh77uHWl7AfZF9iE1L-kgg4hT5KaJSp4qEYz-nbb4TqmrsnZiPbjnzSFrOGZ778OpDWnXhbb5VcXk9ZjejEdBtoqnIJ_vubEWTw-ZeMI4fCmNuiZ4HnY130VKfnU2f19GSNYaeL7GX7bVQWVS_H01mbll6_GUe.g7la6rSFevvuUrEoqVb41SQB1dk4JuTkrl8zwE0fzG4
```

After decrypting the JWE token, the resultant payload contains a JWS token that looks like this:

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFsaWFzL3N0Zy1zcC1hdXRoLWFwaS1pZC10b2tlbi1zaWduaW5nLWtleS1rbXMtYXN5bW1ldHJpYy1rZXktYWxpYXMifQ.eyJ1aW5maW4iOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiUzkwMDAwMDFCIn0sIm5hbWUiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiU09IIEhBTyBGRU5HIn0sImJpcnRoY291bnRyeSI6eyJsYXN0dXBkYXRlZCI6IjIwMjQtMDktMjYiLCJjb2RlIjoiU0ciLCJzb3VyY2UiOiIxIiwiY2xhc3NpZmljYXRpb24iOiJDIiwiZGVzYyI6IlNJTkdBUE9SRSJ9LCJkaWFsZWN0Ijp7Imxhc3R1cGRhdGVkIjoiMjAyNC0wOS0yNiIsImNvZGUiOiJUQyIsInNvdXJjZSI6IjEiLCJjbGFzc2lmaWNhdGlvbiI6IkMiLCJkZXNjIjoiVEVPQ0hFVyJ9LCJkb2IiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiMTk4OS0wNy0wOSJ9LCJoYW55dXBpbnlpbm5hbWUiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiIn0sIm5hdGlvbmFsaXR5Ijp7Imxhc3R1cGRhdGVkIjoiMjAyNC0wOS0yNiIsImNvZGUiOiJTRyIsInNvdXJjZSI6IjEiLCJjbGFzc2lmaWNhdGlvbiI6IkMiLCJkZXNjIjoiU0lOR0FQT1JFIENJVElaRU4ifSwicGFzc3BvcnRleHBpcnlkYXRlIjp7Imxhc3R1cGRhdGVkIjoiMjAyNC0wOS0yNiIsInNvdXJjZSI6IjEiLCJjbGFzc2lmaWNhdGlvbiI6IkMiLCJ2YWx1ZSI6IjE5MzMtMDgtMDgifSwicGFzc3BvcnRudW1iZXIiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiRTc4OTg1NjFDIn0sInJhY2UiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2IiwiY29kZSI6IkNOIiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsImRlc2MiOiJDSElORVNFIn0sInJlc2lkZW50aWFsc3RhdHVzIjp7Imxhc3R1cGRhdGVkIjoiMjAyNC0wOS0yNiIsImNvZGUiOiJDIiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsImRlc2MiOiJDSVRJWkVOIn0sInNlY29uZGFyeXJhY2UiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2IiwiY29kZSI6IiIsInNvdXJjZSI6IjEiLCJjbGFzc2lmaWNhdGlvbiI6IkMiLCJkZXNjIjoiIn0sInNleCI6eyJsYXN0dXBkYXRlZCI6IjIwMjQtMDktMjYiLCJjb2RlIjoiTSIsInNvdXJjZSI6IjEiLCJjbGFzc2lmaWNhdGlvbiI6IkMiLCJkZXNjIjoiTUFMRSJ9LCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2ciLCJzdWIiOiJzPVM5MDAwMDAxQix1PWQ0NWQ4ZjIxLTYxNzgtNDcxMy1iOTYyLTg2MzVlZDJhOTQ1YSIsImF1ZCI6InRXVDNyZkltbjloQ2V6bExyME0xblJVdlE0MGZDTkw0IiwiaWF0IjoxNzQ2Njc4MDg5fQ.Tmvh5V_BN0fMBgqa2-Z4vG_Ayp_OoeWfyQrWMZjG9y9NBFwyRnjMpwDK_qFzkn_0D7AjOX-np6p3Nk5KFwvKiA
```

Where the payload (if the following scopes: `uinfin` and `name` were requested) is:

```json
{
  "uinfin": {
    "lastupdated": "2024-09-26",
    "source": "1",
    "classification": "C",
    "value": "S9000001B"
  },
  "name": {
    "lastupdated": "2024-09-26",
    "source": "1",
    "classification": "C",
    "value": "SOH HAO FENG"
  },
  // above scopes are returned in the same format as the Myinfo Get Person response
  "iss": "https://stg-id.singpass.gov.sg",
  "sub": "s=S9000001B,u=d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "tWT3rfImn9hCezlLr0M1nRUvQ40fCNL4",
  "iat": 1746678089
}
```

{% hint style="success" %}
Please note that currently the structure of the payload follows the existing [Myinfo Get Person response](https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html#operation/getperson) – along with `iss`, `sub`, `aud`, `iat`. You can expand the toggle below for the full list.
{% endhint %}

<details>

<summary>Myinfo get-person sample response</summary>

```json
{
  "partialuinfin": {
    "value": "*****111D",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "uinfin": {
    "value": "S1111111D",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "name": {
    "value": "TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinname": {
    "value": "CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "aliasname": {
    "value": "TRICIA TAN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hanyupinyinaliasname": {
    "value": "TRICIA CHEN XIAO HUI",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marriedname": {
    "value": "",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "sex": {
    "code": "F",
    "desc": "FEMALE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "race": {
    "code": "CN",
    "desc": "CHINESE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "secondaryrace": {
    "code": "EU",
    "desc": "EURASIAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dialect": {
    "code": "SG",
    "desc": "SWISS GERMAN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "nationality": {
    "code": "SG",
    "desc": "SINGAPORE CITIZEN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "dob": {
    "value": "1958-05-17",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "birthcountry": {
    "code": "SG",
    "desc": "SINGAPORE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "residentialstatus": {
    "code": "C",
    "desc": "CITIZEN",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportnumber": {
    "value": "E35463874W",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passportexpirydate": {
    "value": "2020-01-01",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "regadd": {
    "type": "SG",
    "block": {
      "value": "548"
    },
    "building": {
      "value": ""
    },
    "floor": {
      "value": "09"
    },
    "unit": {
      "value": "128"
    },
    "street": {
      "value": "BEDOK NORTH AVENUE 1"
    },
    "postal": {
      "value": "460548"
    },
    "country": {
      "code": "SG",
      "desc": "SINGAPORE"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "housingtype": {
    "code": "123",
    "desc": "TERRACE HOUSE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hdbtype": {
    "code": "112",
    "desc": "2-ROOM FLAT (HDB)",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "hdbownership": [
    {
      "noofowners": {
        "value": 2
      },
      "address": {
        "type": "SG",
        "block": {
          "value": "548"
        },
        "building": {
          "value": ""
        },
        "floor": {
          "value": "09"
        },
        "unit": {
          "value": "128"
        },
        "street": {
          "value": "BEDOK NORTH AVENUE 1"
        },
        "postal": {
          "value": "460548"
        },
        "country": {
          "code": "SG",
          "desc": "SINGAPORE"
        }
      },
      "hdbtype": {
        "code": "112",
        "desc": "2-ROOM FLAT (HDB)"
      },
      "leasecommencementdate": {
        "value": "2008-06-13"
      },
      "termoflease": {
        "value": 99
      },
      "dateofpurchase": {
        "value": "2008-06-13"
      },
      "dateofownershiptransfer": {
        "value": "2018-06-13"
      },
      "loangranted": {
        "value": 310000.01
      },
      "originalloanrepayment": {
        "value": 25
      },
      "balanceloanrepayment": {
        "years": {
          "value": 2
        },
        "months": {
          "value": 6
        }
      },
      "outstandingloanbalance": {
        "value": 50000.01
      },
      "monthlyloaninstalment": {
        "value": 1000.01
      },
      "outstandinginstalment": {
        "value": 1000.01
      },
      "purchaseprice": {
        "value": 1000.01
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  ],
  "ownerprivate": {
    "value": false,
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "email": {
    "value": "test@gmail.com",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "mobileno": {
    "prefix": {
      "value": "+"
    },
    "areacode": {
      "value": "65"
    },
    "nbr": {
      "value": "66132665"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marital": {
    "code": "2",
    "desc": "MARRIED",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marriagecertno": {
    "value": "123456789012345",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "countryofmarriage": {
    "code": "SG",
    "desc": "SINGAPORE",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "marriagedate": {
    "value": "2007-01-01",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "divorcedate": {
    "value": "",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "childrenbirthrecords": [
    {
      "birthcertno": {
        "value": "S5562882C"
      },
      "name": {
        "value": "Jo Tan Pei Ni"
      },
      "hanyupinyinname": {
        "value": "Cheng Pei Ni"
      },
      "aliasname": {
        "value": ""
      },
      "hanyupinyinaliasname": {
        "value": ""
      },
      "marriedname": {
        "value": ""
      },
      "sex": {
        "code": "F",
        "desc": "FEMALE"
      },
      "race": {
        "code": "CN",
        "desc": "CHINESE"
      },
      "secondaryrace": {
        "code": "",
        "desc": ""
      },
      "dialect": {
        "code": "HK",
        "desc": "HOKKIEN"
      },
      "lifestatus": {
        "code": "D",
        "desc": "DECEASED"
      },
      "dob": {
        "value": "2011-09-10"
      },
      "tob": {
        "value": "0901"
      },
      "vaccinationrequirements": [
        {
          "requirement": {
            "code": "1M3D",
            "desc": "MINIMUM VACCINATION REQUIREMENT FOR PRESCHOOL"
          },
          "fulfilled": {
            "value": true
          }
        }
      ],
      "sgcitizenatbirthind": {
        "value": "Y"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  ],
  "sponsoredchildrenrecords": [
    {
      "nric": {
        "value": "S5562882C"
      },
      "name": {
        "value": "Jo Tan Pei Ni"
      },
      "hanyupinyinname": {
        "value": "Cheng Pei Ni"
      },
      "aliasname": {
        "value": ""
      },
      "hanyupinyinaliasname": {
        "value": ""
      },
      "marriedname": {
        "value": ""
      },
      "sex": {
        "code": "F",
        "desc": "FEMALE"
      },
      "race": {
        "code": "CN",
        "desc": "CHINESE"
      },
      "secondaryrace": {
        "code": "",
        "desc": ""
      },
      "dialect": {
        "code": "HK",
        "desc": "HOKKIEN"
      },
      "dob": {
        "value": "2011-09-10"
      },
      "birthcountry": {
        "code": "SG",
        "desc": "SINGAPORE"
      },
      "lifestatus": {
        "code": "A",
        "desc": "ALIVE"
      },
      "residentialstatus": {
        "code": "C",
        "desc": "Citizen"
      },
      "nationality": {
        "code": "SG",
        "desc": "SINGAPORE CITIZEN"
      },
      "scprgrantdate": {
        "value": "2015-06-13"
      },
      "vaccinationrequirements": [
        {
          "requirement": {
            "code": "1M3D",
            "desc": "MINIMUM VACCINATION REQUIREMENT FOR PRESCHOOL"
          },
          "fulfilled": {
            "value": true
          }
        }
      ],
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  ],
  "occupation": {
    "value": "",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "employment": {
    "value": "ALPHA",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passtype": {
    "code": "RPass",
    "desc": "Work Permit",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passstatus": {
    "value": "Live",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "passexpirydate": {
    "value": "2022-12-31",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "employmentsector": {
    "value": "MANUFACTURING",
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "vehicles": [
    {
      "vehicleno": {
        "value": "SDF1235A"
      },
      "type": {
        "value": "PASSENGER MOTOR CAR"
      },
      "iulabelno": {
        "value": ""
      },
      "make": {
        "value": "TOYOTA"
      },
      "model": {
        "value": "COROLLA ALTIS"
      },
      "chassisno": {
        "value": "ZC11S1735800"
      },
      "engineno": {
        "value": "M13A1837453"
      },
      "motorno": {
        "value": ""
      },
      "yearofmanufacture": {
        "value": "2010"
      },
      "firstregistrationdate": {
        "value": "2010-06-06"
      },
      "originalregistrationdate": {
        "value": "2010-06-06"
      },
      "coecategory": {
        "value": "A - CAR UP TO 1600CC & 97KW (130BHP)"
      },
      "coeexpirydate": {
        "value": "2020-06-05"
      },
      "roadtaxexpirydate": {
        "value": "2020-06-05"
      },
      "quotapremium": {
        "value": 14000.01
      },
      "openmarketvalue": {
        "value": 25000.01
      },
      "co2emission": {
        "value": 146.01
      },
      "status": {
        "code": "1",
        "desc": "LIVE"
      },
      "primarycolour": {
        "value": "BLACK"
      },
      "secondarycolour": {
        "value": "WHITE"
      },
      "attachment1": {
        "value": "DISABLED"
      },
      "attachment2": {
        "value": "WITH SUN ROOF"
      },
      "attachment3": {
        "value": "SIDE CURTAIN"
      },
      "scheme": {
        "value": "REVISED OFF-PEAK CAR"
      },
      "thcemission": {
        "value": 1.011001
      },
      "coemission": {
        "value": 1.100001
      },
      "noxemission": {
        "value": 0.011001
      },
      "pmemission": {
        "value": 0.007
      },
      "enginecapacity": {
        "value": 1600
      },
      "powerrate": {
        "value": 1.41
      },
      "effectiveownership": {
        "value": "2010-08-31T20:12:12+08:00"
      },
      "propellant": {
        "value": "Compressed Natural Gas"
      },
      "maximumunladenweight": {
        "value": 1500
      },
      "maximumladenweight": {
        "value": 1795
      },
      "minimumparfbenefit": {
        "value": 8770.01
      },
      "nooftransfers": {
        "value": 2
      },
      "vpc": {
        "value": "1234567890"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  ],
  "drivinglicence": {
    "comstatus": {
      "code": "Y",
      "desc": "ELIGIBLE"
    },
    "totaldemeritpoints": {
      "value": 0
    },
    "suspension": {
      "startdate": {
        "value": ""
      },
      "enddate": {
        "value": ""
      }
    },
    "disqualification": {
      "startdate": {
        "value": ""
      },
      "enddate": {
        "value": ""
      }
    },
    "revocation": {
      "startdate": {
        "value": ""
      },
      "enddate": {
        "value": ""
      }
    },
    "pdl": {
      "validity": {
        "code": "V",
        "desc": "VALID"
      },
      "expirydate": {
        "value": "2020-06-15"
      },
      "classes": [
        {
          "class": {
            "value": "2A"
          }
        },
        {
          "class": {
            "value": "3A"
          }
        },
        {
          "class": {
            "value": "4P"
          }
        },
        {
          "class": {
            "value": "4AP"
          }
        },
        {
          "class": {
            "value": "5P"
          }
        }
      ]
    },
    "qdl": {
      "validity": {
        "code": "V",
        "desc": "VALID"
      },
      "expirydate": {
        "value": "2020-06-15"
      },
      "classes": [
        {
          "class": {
            "value": "2A"
          },
          "issuedate": {
            "value": "2018-06-06"
          }
        },
        {
          "class": {
            "value": "3A"
          },
          "issuedate": {
            "value": "2018-06-06"
          }
        },
        {
          "class": {
            "value": "4P"
          },
          "issuedate": {
            "value": "2018-06-06"
          }
        },
        {
          "class": {
            "value": "4AP"
          },
          "issuedate": {
            "value": "2018-06-06"
          }
        },
        {
          "class": {
            "value": "5P"
          },
          "issuedate": {
            "value": "2018-06-06"
          }
        }
      ]
    },
    "photocardserialno": {
      "value": "115616"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "academicqualifications": {
    "transcripts": [
      {
        "name": {
          "value": "SINGAPORE-CAMBRIDGE GENERAL CERTIFICATE OF EDUCATION ORDINARY LEVEL"
        },
        "yearattained": {
          "value": "2018"
        },
        "results": [
          {
            "subject": {
              "value": "English Language"
            },
            "level": {
              "value": "Ordinary"
            },
            "grade": {
              "value": "A"
            },
            "subsubject": {
              "value": "SPECIAL PAPER"
            },
            "subgrade": {
              "value": "One"
            }
          }
        ],
        "explanatorynotes": {
          "value": "string"
        }
      }
    ],
    "certificates": [
      {
        "name": {
          "value": "nus.opencert"
        },
        "content": {
          "value": "string"
        },
        "opencertificate": {
          "id": {
            "value": 100000000343840
          },
          "primary": {
            "value": true
          }
        },
        "opencertificateindicator": {
          "value": true
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "ltavocationallicences": {
    "tdvl": {
      "licencename": {
        "value": "TAXI DRIVER'S VOCATIONAL LICENCE (TDVL)"
      },
      "vocationallicencenumber": {
        "value": "E00000001"
      },
      "expirydate": {
        "value": "2025-03-30"
      },
      "status": {
        "code": "ACT",
        "desc": "ACTIVE"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "pdvl": {
      "licencename": {
        "value": "PRIVATE HIRE CAR DRIVER'S VOCATIONAL LICENCE (PDVL)"
      },
      "vocationallicencenumber": {
        "value": "E00000001"
      },
      "expirydate": {
        "value": "2025-03-30"
      },
      "status": {
        "code": "ACT",
        "desc": "ACTIVE"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "bdvl": {
      "licencename": {
        "value": "BUS DRIVER'S VOCATIONAL LICENCE (BDVL)"
      },
      "vocationallicencenumber": {
        "value": "E00000001"
      },
      "expirydate": {
        "value": "2025-03-30"
      },
      "status": {
        "code": "ACT",
        "desc": "ACTIVE"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "bavl": {
      "licencename": {
        "value": "BUS ATTENDANT VOCATIONAL LICENCE (BAVL)"
      },
      "vocationallicencenumber": {
        "value": "E00000001"
      },
      "expirydate": {
        "value": "2025-03-30"
      },
      "status": {
        "code": "ACT",
        "desc": "ACTIVE"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "odvl": {
      "licencename": {
        "value": "OMNIBUS DRIVER'S VOCATIONAL LICENCE"
      },
      "vocationallicencenumber": {
        "value": "E00000001"
      },
      "expirydate": {
        "value": "2025-03-30"
      },
      "status": {
        "code": "ACT",
        "desc": "ACTIVE"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  },
  "chas": {
    "cardtype": {
      "code": "C",
      "desc": "Green"
    },
    "indicator": {
      "code": "C",
      "desc": "Green"
    },
    "expirydate": {
      "value": "2020-06-15"
    },
    "issuedate": {
      "value": "2020-06-15"
    },
    "lastupdated": "2019-03-26",
    "name": {
      "value": "TAN XIAO HUI"
    },
    "classification": "C",
    "source": "1"
  },
  "merdekagen": {
    "eligibility": {
      "value": true
    },
    "quantum": {
      "value": 100
    },
    "message": {
      "code": "2",
      "desc": "You are eligible for the Merdeka Generation Package. For further enquiries, please contact 1800-2222-888."
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "pioneergen": {
    "eligibility": {
      "value": true
    },
    "quantum": {
      "value": 100
    },
    "message": {
      "code": "2",
      "desc": "You are eligible for the Pioneer Generation Package. For further enquiries, please contact 1800-2222-888."
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "noa-basic": {
    "amount": {
      "value": 100000.01
    },
    "yearofassessment": {
      "value": "2018"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "noa": {
    "amount": {
      "value": 100000.01
    },
    "yearofassessment": {
      "value": "2018"
    },
    "employment": {
      "value": 100000.01
    },
    "trade": {
      "value": 0
    },
    "rent": {
      "value": 0
    },
    "interest": {
      "value": 0
    },
    "taxclearance": {
      "value": "N"
    },
    "category": {
      "value": "ORIGINAL"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "noahistory-basic": {
    "noas": [
      {
        "amount": {
          "value": 100000.01
        },
        "yearofassessment": {
          "value": "2018"
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "noahistory": {
    "noas": [
      {
        "amount": {
          "value": 100000.01
        },
        "yearofassessment": {
          "value": "2018"
        },
        "employment": {
          "value": 100000.01
        },
        "trade": {
          "value": 0
        },
        "rent": {
          "value": 0
        },
        "interest": {
          "value": 0
        },
        "taxclearance": {
          "value": "N"
        },
        "category": {
          "value": "ORIGINAL"
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfcontributions": {
    "history": [
      {
        "date": {
          "value": "2016-12-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2016-11"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2016-12-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2016-12-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-01-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-01-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-01-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-02-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-02-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-02-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-03-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-03-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-03-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-04-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-04-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-04-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-05-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-05-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-05-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-06-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-06-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-06-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-07-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-07-12"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-07-21"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-08-01"
        },
        "amount": {
          "value": 500
        },
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "date": {
          "value": "2017-08-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-08-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-09-01"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-09-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-09-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-10-01"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-10-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-10-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-11-01"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-11-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-11-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-12-01"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-12-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2017-12-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2018-01-01"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2018-01-12"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2018-01"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "date": {
          "value": "2018-01-21"
        },
        "amount": {
          "value": 750
        },
        "month": {
          "value": "2018-01"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfemployers": {
    "history": [
      {
        "month": {
          "value": "2016-11"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2016-12"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-01"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-02"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-03"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-04"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-05"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-06"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-07"
        },
        "employer": {
          "value": "Crystal Horse Invest Pte Ltd"
        }
      },
      {
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-08"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-09"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-10"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-11"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2017-12"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2018-01"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      },
      {
        "month": {
          "value": "2018-01"
        },
        "employer": {
          "value": "Delta Marine Consultants PL"
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfbalances": {
    "ma": {
      "value": 11470.71,
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "oa": {
      "value": 1581.48,
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "sa": {
      "value": 21967.09,
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "ra": {
      "value": 0.01,
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  },
  "cpfhousingwithdrawal": {
    "withdrawaldetails": [
      {
        "address": {
          "type": "SG",
          "block": {
            "value": "548"
          },
          "building": {
            "value": ""
          },
          "floor": {
            "value": "09"
          },
          "unit": {
            "value": "128"
          },
          "street": {
            "value": "BEDOK NORTH AVENUE 1"
          },
          "postal": {
            "value": "460548"
          },
          "country": {
            "code": "SG",
            "desc": "SINGAPORE"
          }
        },
        "accruedinterestamt": {
          "value": 1581.48
        },
        "monthlyinstalmentamt": {
          "value": 1196.09
        },
        "principalwithdrawalamt": {
          "value": 2897.01
        },
        "totalamountofcpfallowedforproperty": {
          "value": 10000.01
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfhomeprotectionscheme": {
    "coverage": {
      "value": true
    },
    "premium": {
      "value": 100.01
    },
    "shareofcover": {
      "value": 20
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfdependantprotectionscheme": {
    "coverage": {
      "value": true
    },
    "insurercode": {
      "value": "9GEL"
    },
    "sumassuredamount": {
      "value": 70000
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfinvestmentscheme": {
    "sdsnetshareholdingqty": {
      "value": 1360,
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "account": {
      "agentbankcode": {
        "value": "OCBC"
      },
      "invbankacctno": {
        "value": "098-26644-4"
      },
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    },
    "saqparticipationstatus": {
      "code": "X",
      "desc": "Participated",
      "classification": "C",
      "source": "1",
      "lastupdated": "2019-03-26"
    }
  },
  "cpfmedishieldlife": {
    "medishieldlifecoverage": {
      "hascovertag": {
        "value": true
      },
      "payername": {
        "value": "string"
      },
      "netpremiumpayable": {
        "value": 1000
      },
      "policyrenewaldate": {
        "value": "2019-07-02"
      }
    },
    "integratedshieldplancoverage": {
      "hascovertag": {
        "value": true
      },
      "payername": {
        "value": "string"
      },
      "insurercode": {
        "value": "string"
      }
    },
    "medishieldlifedependants": [
      {
        "dependantname": {
          "value": "string"
        },
        "netpremiumpayable": {
          "value": 1000
        },
        "policyrenewaldate": {
          "value": "2019-07-02"
        }
      }
    ],
    "integratedshieldplandependants": [
      {
        "dependantname": {
          "value": "string"
        },
        "insurercode": {
          "value": "string"
        }
      }
    ],
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfrstucurrentyeartaxrelief": {
    "totaltaxreliefself": {
      "value": 1000
    },
    "remainingtaxreliefself": {
      "value": 1000
    },
    "totaltaxrelieflovedones": {
      "value": 1000
    },
    "remainingtaxrelieflovedones": {
      "value": 1000
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfrstuselftopupamount": {
    "selftopupusingcash": {
      "value": 1000
    },
    "selftopupusingcpf": {
      "value": 1000
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpflife": {
    "cpflifecoverage": {
      "value": true
    },
    "cpflifeplan": {
      "value": "Standard Plan"
    },
    "cpflifemonthlypayout": {
      "value": 1000
    },
    "cpflifepaymentcommencement": {
      "value": true
    },
    "cpflifepaymentdate": {
      "value": "2019-09-02"
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  },
  "cpfmonthlypayouts": {
    "monthlypayout": {
      "value": 1000
    },
    "paymentcommencement": {
      "value": true
    },
    "classification": "C",
    "source": "1",
    "lastupdated": "2019-03-26"
  }
}
```

</details>




---

[Next Page](https://docs.developer.singpass.gov.sg/docs/llms-full.txt/2)

