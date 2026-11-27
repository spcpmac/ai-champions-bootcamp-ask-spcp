> This is part 1 of 3 of the full documentation (pages 1–100 of 205).
> The content is paginated: fetch every part to see all of it.
> Next part: https://docs.developer.singpass.gov.sg/docs/llms-full.txt/1
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

# Singpass APIs Documentation

👋 Your one-stop guide to integrating Singpass Login and Singpass Myinfo

### 🚀 What You Can Do Here

#### For Business Users

* Learn about our Singpass product offerings:
  * [Singpass Login](https://docs.developer.singpass.gov.sg/docs/products/singpass-login)
  * [Myinfo](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo)
  * [Myinfo Business](https://docs.corppass.gov.sg/products/myinfo-business)
  * [Sign with Singpass](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass)
* Understand the [onboarding process](https://docs.developer.singpass.gov.sg/docs/getting-started/quick-start) and required [pre-requisites](https://docs.developer.singpass.gov.sg/docs/getting-started/pre-requisites-for-onboarding)
* Learn how to [navigate and use the Singpass Developer Portal (SDP)](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide)

#### For Developers

* Access our [integration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide) for Singpass Login and Myinfo (v5)
* Use [common test profiles](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) to test Myinfo (v5) integrations
* Understand the [fundamentals of OIDC](https://docs.developer.singpass.gov.sg/docs/introduction/overview-of-singpass) and authentication flows

### 🔥 Latest Updates

#### 📢 Finalised FAPI 2.0 Documentation Is Now Available

All FAPI 2.0 specifications, technical concepts, and migration guides are now published.

#### ⚠️ Mandatory Deadline: **31 December 2026**

All Singpass APIs must be fully compliant with FAPI 2.0 by 31 Dec 2026.

Start reviewing the updated documents and plan your migration early.


# Quick Start

Get started with Singpass APIs onboarding

### Getting started

Before you can begin integrating with Singpass Login or Myinfo, you’ll need access to the [Singpass Developer Portal](https://developer.singpass.gov.sg).

👉 [How to get access to developer.singpass.gov.sg](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/getting-access/obtaining-access-to-the-singpass-developer-portal-sdp)

### Create a Staging App

Once you have access to SDP, your first step is to create a **Staging application.**

The Staging environment lets you configure your app, test your flows, and validate your setup safely before going live.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8113a94be7686d3e128b3f02d287e6e1f821ffad%2Fscreen-1763522210887.gif?alt=media" alt=""><figcaption></figcaption></figure>

> *Create your first Singpass application in under a few minutes using the app setup wizard.*

You’ll choose whether you want to integrate:

* [Singpass Login](https://docs.developer.singpass.gov.sg/docs/products/singpass-login) – for authentication
* [Myinfo](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo) – for verified personal data retrieval
* [Sign with Singpass](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass) - for digital signing

👉 Learn about the various products and their requirements

👉 [How to create a Staging app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app)

### Set up your test environment

Now that your app is created, you can begin testing.

#### Test Singpass Login

Create or use a staging Singpass account to test the login journey.

👉 [How to set up a Staging Singpass account](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-test-account)

👉 [How to download the Singpass Staging app](https://docs.developer.singpass.gov.sg/docs/testing/testing-with-singpass-app)

#### Test Singpass Myinfo

Use our ready made test personas to simulate Myinfo responses.

👉 [Myinfo Common Test Profiles](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas)

### Begin your integration

With your Staging test accounts ready, you can start building your Singpass Integration:

👉 [Integration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide)

👉 [Demo app](https://docs.developer.singpass.gov.sg/docs/getting-started/demo-app-and-sample-codes)

### Review Services agreement and pricing plan

Before moving to Production, make sure you understand the:

* Responsibilities under the Singpass Services Agreement
* Pricing Plan

👉 [Where to review the Services Agreement & Pricing](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/service-agreement/view-singpass-service-agreement)

### Prepare for Production:

Before creating your Production app, ensure you have completed the following:

1. Agree to the Singpass Services Agreement
2. Update your billing contact details in SDP
3. Prepare your user journey
   * Login → follow branding guidelines
   * Myinfo → follow data principles & scope justification

👉 [User Journey Guidelines](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey)

### Create your Production app

Once all prerequisites are met:

1. Create your Production app in SDP
2. Configure your Production redirect URIs, JWKS endpoints, Scopes
3. Start testing using your Production credentials

> ⏳ Note: Production App approval may take up to 2 weeks. Please plan your rollout timeline accordingly.

👉 [How to Create a Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app)


# Pre-requisites for onboarding

Please ensure your organisation and use case meet the requirements below before submitting your onboarding request.

***

### 1. Organisation Requirements

* Your organisation must be a Singapore-registered entity (government or private sector).
* If you operate in a regulated industry, you must provide your relevant licences or permits<br>

👉 What you need to do:

* Prepare your ACRA registration details (or equivalent).
* Prepare your regulatory licence/permit, if applicable.

***

### 2. Use Case Requirements

* Only request data that is directly needed for your service.
* All data scopes must be justified based on your use case.
* Users must be able to see the exact Myinfo data retrieved and who it is shared with.
* Users must have full control at every step of the consent process.

👉 What you need to do:

* Prepare your [user journey](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey) and list the exact data needed.
* Prepare a short justification for each scope you intend to request.
* Ensure your UI displays all retrieved data clearly back to the user.

***

### 3. User Choice Requirements

* Singpass cannot be the only form-filling or authentication option.
* You must provide a manual or alternative method for users who prefer not to use Singpass APIs

👉 What you need to do:

* Include at least one non-Singpass option (e.g., manual entry, document upload, alternative login).


# User Device & Software Requirement

If you are enabling users to access your digital service on non-personal devices (e.g. kiosks or shared terminals), you should ensure that the device meets the following requirements to support Singpass authentication.

### Internet Connectivity

A stable Internet connection is required.

### Supported Browsers

You may find the supported browsers at this [AskGov](https://ask.gov.sg/singpass/questions/clul3am5x003wo12th5witu9z) page.

#### Secure In-App Browsers

Webview embedded browsers are not supported. Please refer to the following help center for additional information.

* [How to identify Webview browser?](https://partnersupport.singpass.gov.sg/hc/en-sg/articles/39909135503129--8-Nov-2024-Discontinuation-of-WebView-Support-for-Singpass-in-Mobile-Apps)
* What should I do?
  * [For iOS](https://github.com/singpass/iOS-Singpass-in-app-browser-login-demo?tab=readme-ov-file#migrating-away-from-webview-for-ios-mobile-app-singpass-logins)
  * [For Android](https://github.com/singpass/Android-Singpass-in-app-browser-login-demo?tab=readme-ov-file#migrating-away-from-webview-for-android-mobile-app-singpass-logins)

### Camera Requirement

The device that your user is using to access your digital service must have a working front camera, as Singpass Face Verification (SFV) may be triggered for higher-risk transactions carrying a greater chance of fraud or account takeover. Find out more [here](https://ask.gov.sg/singpass/questions/cmbjbxmnv01rs4ds4cbi6izvj).


# User Journey

User Journey Submission

When creating an application in the **Production environment**, you are required to submit a **User Journey** showing how your digital service will integrate with Singpass APIs.

Step 1: Download the relevant User Journey template

Please download and complete the User Journey template that is relevant to your use case:

#### Use Case Options:

1. **Myinfo API** - Use this API to retrieve user information for **form filling** or **registration** purposes.

{% file src="/files/zQ92KpQaEamUqcQ9ApLl" %}

2. **Login API** - Use this API as a secure alternative login method to your existing authentication or verification flow.

{% file src="/files/6LHGGISQ5QIdRB8FENtN" %}

3. **Myinfo Business** - Retrieve business-related information. Please use the user journey [here](https://docs.corppass.gov.sg/products/myinfo-business/getting-started/user-journey).
4. **Login with Mandatory Face Verification API** - Enhance Singpass Login with an additional face verification step. This is restricted to approved high-risk use cases, such as digital token setup for banking applications. Please refer to the [SFV eligibility guidelines](https://docs.developer.singpass.gov.sg/docs/products/singpass-face-verification) before applying.

{% file src="/files/9O5N1MnsUyfH7LTFwRVC" %}

Once you’ve completed the User Journey, please submit it via the [portal](https://developer.singpass.gov.sg). Your submission will then be routed for approval.


# App Logo

{% hint style="info" %}
This feature is available for **Login, Myinfo (v5), Myinfo Biz (v3) and Sign with Singpass** apps.
{% endhint %}

Your organisation's logo will be displayed in various places like the Login screen and Singpass app. This helps users identify your organisation when they are transacting with you.

### App logo requirement

When uploading your logo, ensure that they meet the following requirements:

* **File format**: PNG (transparent background)
* **Dimension**: 256px by 256px to 512px by 512px
* **File size**: Up to 200KB
* **Aspect Ratio**: Square (1:1 ratio)
* **No padding**: The logo should fill the entire canvas with no surrounding whitespace. Padding is applied automatically and does not need to be included in your upload.

### Example of logo

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1f5ad361226deb39a3873ec6cbe2484b2da01fd0%2FDocs_%20App%20Logo.png?alt=media" alt=""><figcaption></figcaption></figure>

Note:

* For Singpass app: Logo changes will only be reflected once users update to the latest app version.
* For partners with existing shortcuts in Singpass app: Logo changes or uploaded via SDP will not be reflected on the shortcuts.

### Logo preview during app creation

When creating a new app, a preview of your logo is shown in the first step of the new app wizard. The preview updates as you upload or change your logo.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8fe9254c92eeb4efaba46de2d103ee394f56bd66%2FDOC-045-logo-preview-login-screen.png?alt=media" alt="Logo preview — Login screen tab in new app wizard"><figcaption><p>Login screen preview</p></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-18da70ecd8494a7940bb3eca36a333b816ba4eb1%2FDOC-045-logo-preview-singpass-app.png?alt=media" alt="Logo preview — Singpass app tab in new app wizard"><figcaption><p>Singpass app preview</p></figcaption></figure>

{% hint style="info" %}
**Note:** The preview uses a sample logo. Upload your own logo file to see how it will appear on Singpass screens.
{% endhint %}

### Logo pending approval in change requests

When you submit a logo change for a production app, the new logo is not applied immediately — it enters a pending state while the change request is under review. During this review period:

* The current live logo continues to be shown to end users until the change request is approved.

Once the change request is approved, the new logo replaces the current one.


# Singpass Button Design Specification

{% hint style="info" %}
**These guidelines take effect on 1 September 2026. All Singpass button implementations must comply with the specifications on this page from that date.**
{% endhint %}

This guide covers how to display the Singpass button correctly. It includes the approved button labels, visual style and accessibility considerations.

Following these guidelines helps prevents common implementation issues, and ensure a clear user experience with what users already know and trust.

**Download Singpass assets (approved Singpass button labels and logo):**

{% file src="/files/nNbcYMBIHLLpQmFmMmP9" %}

***

### Approved button labels

The button label communicates what will happen when users click the button.

**These are the** **only approved labels for the Singpass button**. Choose the one that best reflects the user's action in your flow, and do not create your own variations.

**Download Singpass button:**

{% file src="/files/04kdRPf70v4m0pFIeLD1" %}

<table data-search="false"><thead><tr><th width="212.2265625">Use case type</th><th>Use when</th><th>Button</th></tr></thead><tbody><tr><td>Log In</td><td>Users are logging in to your service<br><br>Example: Logging into a portal to access a service</td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-fe9ee73e7348cc8b909b6bf721a09fa8109c928c%2Flog_in_with_singpass_full_white_with_outline.svg?alt=media&amp;token=ad2d0859-f63e-40fc-9524-fc3e77b7e353" alt=""></td></tr><tr><td>Registration and Sign up</td><td><p>Users are signing up or registering for your service</p><p>Example: Creating a new banking, telco, or service account</p></td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1d508cddedb6f1a7fada5a7b089c5dd7a9c92a8c%2Fregister_with_singpass_white_with_outline.svg?alt=media" alt=""><br><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-e8fecaaf8ae1907143eae0df481711856d3c2c9c%2Fsignup_with_singpass_white_with_outline.svg?alt=media" alt=""></td></tr><tr><td>Application</td><td><p>Users are applying for a product or service</p><p><br>Examples: Applying for a credit card, loan, or grants</p></td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-99269c7dfab95a7be5bdd46737f07e17283ef80b%2Fapply_with_singpass_white_with_outline.svg?alt=media" alt=""></td></tr><tr><td>Identity verification</td><td><p>The primary purpose is to confirm the user’s identity</p><p>Examples:</p><ul><li>Verifying identity before accessing sensitive features</li><li>Performing KYC checks before allowing further actions</li></ul></td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-88df5aa76aed010e3b4bd576f284f1b25d2d8a9d%2Fverify_with_singpass_white_with_outline.svg?alt=media" alt=""></td></tr><tr><td>Retrieval or update of information</td><td><p>Users are asked to fill in their details</p><p>Examples:</p><ul><li>Pre-filling details in a form</li><li>Refreshing previously saved information</li></ul></td><td><p><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-0079f0720fe41467f3d5e57e74a5b55a6595cb6a%2Fupdate_with_singpass_white_with_outline.svg?alt=media" alt=""><br></p><p><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1d508cddedb6f1a7fada5a7b089c5dd7a9c92a8c%2Fregister_with_singpass_white_with_outline.svg?alt=media" alt="" data-size="original"></p></td></tr><tr><td>Document signing</td><td>Users are signing a document using Singpass<br><br>Example: Users signing insurance policy</td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-053350bf0ee11e00f0efbbc513b5a334d96ae9c3%2Fsign_with_singpass_full_white_with_outline.svg?alt=media" alt=""></td></tr><tr><td>Others</td><td><p>Singpass is used as a step within a larger flow. The action is to proceed, not to apply or verify</p><p>Examples:</p><ul><li>Booking an appointment</li><li>Moving to the next step before details are shown</li></ul></td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d4c114cab9f774cc076cf344050fd195221b4f53%2Fcontinue_with_singpass_white_with_outline.svg?alt=media" alt=""></td></tr></tbody></table>

***

### Button colour and state

**Do** use colour to indicate emphasis and ensure the Singpass button is clearly visible in your interface.

**Do** use one of the following variants that provides sufficient contrast with the background and reflects the importance of the action.

* White with outline (Default)
* White (for dark mode)
* Black
* Red

**Don't** use colours outside the approved variants, including gradients or modified brand colours.

#### **White with outline (Default)**

Use when a lower visual emphasis is needed or when pairing with other primary actions.

<table><thead><tr><th width="166.5703125">Button state</th><th width="201.4375">Button background colour [hex code]</th><th width="210.86328125">Border colour [hex code]</th><th>Font colour [hex code]</th></tr></thead><tbody><tr><td><strong>Default</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-98673e0ab68eb8a43a607ccbbff97b8a76ebfa5d%2Fimage.png?alt=media" alt=""></td><td>White: <code>#FFFFFF</code></td><td>Grey: <code>#AAABAD</code></td><td>Black: <code>#141414</code></td></tr><tr><td><strong>Hover</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-cbb19f6ab7779896f63560b5c872a6e11b5e3378%2Fimage.png?alt=media" alt=""></td><td>Light grey: <code>#F5F5F7</code></td><td>Grey: <code>#AAABAD</code></td><td>Black: <code>#141414</code></td></tr><tr><td><strong>Disabled</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-99e3f51f7f55aa3b7cbf6821226a2a0e169ca28c%2Fimage.png?alt=media" alt=""></td><td>Grey: <code>#FFFFFF</code></td><td>Grey: <code>#AAABAD</code></td><td>Grey: <code>#AAABAD</code></td></tr></tbody></table>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-6da642e20132a851ac4d9f382ee5897d5d2df94d%2Fimage.png?alt=media" alt=""><figcaption><p>Button guidelines for white with outline</p></figcaption></figure>

#### **White (for dark mode)**

Use this variant when your interface has a dark background. The white button is the only approved variant for dark surfaces, do not use the other variants on dark backgrounds as they are designed for light interfaces.

<table><thead><tr><th width="240.2109375">Button state</th><th>Button background colour [hex code]</th><th>Font colour [hex code]</th></tr></thead><tbody><tr><td><strong>Default</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b0b3255c0ebfb3d674d044559f99d6531c03ff46%2Fimage.png?alt=media" alt=""></td><td>White: <code>#FFFFFF</code></td><td>Black: <code>#141414</code></td></tr><tr><td><strong>Hover</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-187668a1796183222f188538c199ad8a1f7002bd%2Fimage.png?alt=media" alt=""></td><td>Light grey: <code>#F5F5F7</code></td><td>Black: <code>#141414</code></td></tr><tr><td><strong>Disabled</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d2039b3f4988befb7e36c4a4f884828843f7713f%2Fimage.png?alt=media" alt=""></td><td>Grey: <code>#E8E9EB</code></td><td>Light grey: <code>#AAABAD</code></td></tr></tbody></table>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-56dd1cc464fe3813db0dd5396f4819e52cf26df2%2Fimage.png?alt=media" alt=""><figcaption><p>Guidelines for white Singpass button (for dark mode)</p></figcaption></figure>

#### **Black**

Use for primary actions on light backgrounds.

<table><thead><tr><th width="221.69140625">Button state</th><th>Button background colour [hex code]</th><th>Font colour [hex code]</th><th>Singpass logo</th></tr></thead><tbody><tr><td><strong>Default</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ef3da47588f2b959fb8582058c80e8cd44141525%2Fimage.png?alt=media" alt="" data-size="original"></td><td>Black: <code>#141414</code></td><td>White: <code>#FFFFFF</code></td><td>Use white Singpass logo</td></tr><tr><td><strong>Hover</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1a8c0dd4d2aa2a3f41ec41abfb9c4382e7d9ebff%2Fimage.png?alt=media" alt=""></td><td>Dark grey: <code>#3B3C3D</code></td><td>White: <code>#FFFFFF</code></td><td>Use white Singpass logo</td></tr><tr><td><strong>Disabled</strong><br><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d2039b3f4988befb7e36c4a4f884828843f7713f%2Fimage.png?alt=media" alt=""></td><td>Grey: <code>#E8E9EB</code></td><td>Light grey: <code>#AAABAD</code></td><td>Use white Singpass logo</td></tr></tbody></table>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-07f0a71db0722d564a8e541fc459f1597b27b460%2Fimage.png?alt=media" alt=""><figcaption><p>Guidelines for black Singpass button</p></figcaption></figure>

#### **Red**

Use to reinforce Singpass branding.

<table><thead><tr><th width="171.61328125">Button state</th><th>Button background colour [hex code]</th><th>Font colour [hex code]</th><th>Singpass logo</th></tr></thead><tbody><tr><td><strong>Default</strong></td><td>Red: <code>#D93841</code></td><td>White: <code>#FFFFFF</code></td><td>Use white Singpass logo</td></tr><tr><td><strong>Hover</strong></td><td>Dark red: <code>#B0262D</code></td><td>White: <code>#FFFFFF</code></td><td>Use white Singpass logo</td></tr><tr><td><strong>Disabled</strong></td><td>Grey: <code>#E8E9EB</code></td><td>White: <code>#FFFFFF</code></td><td>Use white Singpass logo</td></tr></tbody></table>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-afac8932c2ffdfd994862889299441c4269d691d%2Fimage.png?alt=media" alt=""><figcaption><p>Placement guidelines for red Singpass button</p></figcaption></figure>

***

### Button Font and Logo

#### **Button font**

By default, use Poppins Bold at 16px. If you prefer to use your brand typeface, choose a sans-serif font to better match the Singpass logo.

Download Poppins Bold on [Google fonts](https://fonts.google.com/specimen/Poppins).

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b6966689ffc00b071de0051b7602c969acb3f455%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Singpass logo

For **“Singpass”**, use the official Singpass logo within the button.\
This helps users quickly recognise and trust the action. Avoid replacing it with plain text or recreating it in another typeface.

**Download Singpass logo:**

{% file src="/files/wbjRm7pspGQPVMewvQ3t" %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-7b329e0a0da32afbb593216e49ead251276ec6b3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Singpass logo size**

The Singpass logo must have a minimum height of 14px. Do not scale it smaller than this as it will become illegible on smaller screens.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d2819eaea71e744fb84d68575588ccb27d014dd0%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

* Match the x-height of the label as close as possible to ensure visual balance and proportion.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4a5ede9844dfca53bbc0a9c361b3a2b8b0923fa9%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Button size

Keep the internal padding consistent so the logo and label always have breathing room. The button should never feel cramped.\
\
**Minimum height:**

* Desktop: 40px
* Mobile: 44px — applies to native apps and mobile browsers

**Minimum internal padding:**

* Horizontal: 16px on each side
* Space between label and Singpass logo: 4px

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-38a9e42f0b7a2cbc07bf825e75e4627b145c6173%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Placing the Singpass Button with Other Buttons

Make sure it feels like it belongs — same height, same width, consistent spacing. Here's what works and what to avoid.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-fa380c6eed214112ececccd8557c5c323b2a406c%2Fimage.png?alt=media" alt=""><figcaption><p>Same height as your other buttons. Minimum 40px on desktop, 44px on mobile.</p></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-9d9f663373006df8fd810e4a459fde022da4b110%2Fimage.png?alt=media" alt=""><figcaption><p>Same width as the other buttons in your layout.</p></figcaption></figure>

#### **Color**

Use a colour variant that does not clash or blend with nearby buttons.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-892a0f3126739a041fff11625c1a275cd9700fb5%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Spacing**

Give the Singpass button room to breathe. Maintain a **minimum of 16px** between the button and any surrounding elements such as buttons, form fields, or body text.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-024108634656b1252eb3315f46a9c7e61b6061b7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Border radius

You can adjust the corner radius of the Singpass button to match your own. Whether your buttons are fully rounded, subtly curved, or square-cornered, the Singpass button should follow the same style, so it fits naturally into your UI rather than standing out as a third-party element.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-41f27b0dcb6ba97dfeb22d2edbd8add2a64a1999%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-f12d1d4fe607922f64da799278d125b590de0bcd%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Accessibility: Aria labels for screen readers

For screen readers, ensure the Singpass logo is announced correctly.

Provide an accessible label so it is read as **“Sing-pass”**, instead of being spelled out letter by letter ‘S-i-n-g-p-a-s-s’.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1a8428612c8847e6917045dff1aaa43e7c20817e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-592923bd9db251d61b606755dc3672ff4bf452cc%2FSingpass%20types.png?alt=media" alt=""><figcaption></figcaption></figure>


# Singpass Brand Guidelines

If you are a Singpass partner referencing our brand in your marketing materials, these guidelines explain how to do so correctly.

Singapore residents use Singpass every day to access essential services — spanning government, financial transactions, and healthcare. This is made possible by thousands of partners across the public and private sectors who have integrated Singpass into their platforms.

Presenting our brands accurately strengthens awareness, recognition, and trust with the users we both serve.

#### **Download Singpass logo asset:**

{% file src="/files/GLm5lUdskiz5u4xn3HYH" %}

{% file src="/files/b0cCVS8jCtdbdNYhZ0gn" %}

***

### How to show the Singpass brand

#### Singpass logo

Always present Singpass’ role accurately, both in the content and visual. The Singpass logo is available in three variants to ensure it remains clear and legible across different backgrounds and contexts.

<table><thead><tr><th width="200.484375">Type</th><th>Use when</th><th>Variant</th></tr></thead><tbody><tr><td><p><strong>Full colour (Primary)</strong></p><p>The default logo.</p></td><td>Use this whenever possible on light or neutral backgrounds.</td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-afbf2cd10650dbb1ec3dac01ffd7ca78e16f7bae%2FSingpass_logo_fullcolour.png?alt=media" alt="" data-size="original"></td></tr><tr><td><strong>White (secondary)</strong></td><td>For use on dark backgrounds where the full colour logo would not be legible.</td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-577bf56bec69e6f79d1b55de584fc1ef88f64fa8%2FSingpass_logo_white.png?alt=media" alt="" data-size="original"></td></tr><tr><td><strong>Black (secondary)</strong></td><td>For use on high-contrast backgrounds, where neither the full colour nor white logo would stand out clearly.</td><td><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-51467ab1b89f2a18cf13f3e77031004ca13078e3%2Fblacklogo.png?alt=media" alt="" data-size="original"></td></tr></tbody></table>

<i class="fa-thumbs-down" style="color:red;">:thumbs-down:</i> <mark style="color:red;">**DON'T**</mark>

* DON'T modify the Singpass logo — no stretching, skewing, or colour changes.
* DON'T place the Singpass logo on backgrounds that reduce legibility. Use white or black backgrounds where possible.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8b84e88c35d23739c53791d362c9502207a8c464%2FSingpass_logo_dont.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **Logo placement**

For collaborative brand partnerships, the Singpass logo will come first, followed by respective brand partner logo(s).

* Both logos should be similarly proportioned. We recommend that you first start by matching the height or width of partner logo(s) to the Singpass logo.
* Both logos should be scaled to the same optical size for visual balance.
* Clear space should be used between the logos, denoted by the x-height of the ‘i’.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c3d43cce1f0ac7e4d03b73f8ccaff17322262b60%2Flogin%20placement.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-12a297c03228a041e160ac9f5a6944a1cad645fd%2FLogo%20text%20placement.png?alt=media" alt=""><figcaption></figcaption></figure>

**Minimum size**

Minimum sizes of the Singpass logo:

* Digital: **80 pixels wide**
* Print: **18mm wide**

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b40c343fcb9842fd4b46337e04192d0e6a9872dd%2Fsingpass%20logo.png?alt=media" alt=""><figcaption></figcaption></figure>

#### Singpass buttons

We provide standardised Singpass buttons for use across your websites, mobile applications, and connected platforms. Please refer to the button guidelines [here](#singpass-buttons).

***

### How to talk about the Singpass brand

Ensure you reflect how your service or product integrates with ours in a way that is truthful and precise.

{% hint style="success" icon="thumbs-up" %}

#### <mark style="color:green;">DO</mark>

* DO use the Singpass name only as a proper noun — e.g. "Log in with Singpass" or "Sign up with Singpass".
* DO only describe capabilities your integration actually uses.
  * e.g. If you use Singpass for login only, do not reference use of personal data.
    {% endhint %}

{% hint style="danger" icon="thumbs-down" %}

#### <mark style="color:red;">**DON'T**</mark>

* DON'T alter or combine the Singpass name. This includes:
  * Variations: "SingPass", "SINGPASS"
  * Abbreviations: "SP"
  * Compound names: "MyApp Singpass Login"
* DON'T use the Singpass name to imply a relationship beyond your actual integration. This includes:
  * Phrases like "Powered by Singpass", "Secured by Singpass"
  * Using Singpass to describe your own features, e.g. "a secure Singpass verification link"
* DON'T use the Singpass logo or make statements that imply endorsement from or overstate the involvement of Singpass.
  {% endhint %}

***

### Approval for Brand Usage

All use of Singpass brand elements and product visuals requires prior approval. Submit your proposed content before publishing or distributing any materials.

When submitting, include:

* Draft artwork or mockups showing how the Singpass brand will appear
* The intended placement and context (e.g. website, mobile app, printed collateral)
* Your planned publication or launch date

<a href="https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new" class="button secondary">Submit your request here</a>

Allow at least 2 working weeks for approval. Submit early if your materials are time-sensitive.

<br>


# Demo App & Sample Code

There are various OIDC libraries that make integrating your apps with Singpass effortless. You may find code samples in different languages [here in our Github](https://github.com/singpass/demo-app).

#### **For Mobile Developers**

| Description                                            | Android                                                                  | IOS                                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Sample codes implementing FAPI 2.0 for Singpass logins | <https://github.com/singpass/Android-Singpass-in-app-browser-login-demo> | <https://github.com/singpass/iOS-Singpass-in-app-browser-login-demo> |


# Singpass Login

## What is Singpass Login API?

The Singpass Login API enables residents' easy access to government and private sector digital services. Using the Singpass app, residents can securely log in to digital services without passwords.

This service provides businesses with an accessible and established authentication gateway for all their digital services.

### Use Case: Sign in with your Singpass App

Singpass Login lets users access your service without creating or remembering passwords. Instead, they authenticate through the Singpass app using biometrics, passcode, or SMS OTP. This provides a faster, more secure, and password free login experience.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-63e793cfa8e6a9b06bd48d0c370a44745c37a565%2FScreen%20Recording%202025-11-20%20at%203.48.11%20PM.gif?alt=media" alt=""><figcaption><p>Use Singpass as an alternative login method to provide your users with a seamless and secure login experience.</p></figcaption></figure>

#### How Login can enhance your digital service

1. **Tap on an established and secure authentication gateway for all your digital services**\
   Businesses can easily launch an authentication gateway with the instructions provided.<br>
2. **Get access to 4 million Singpass users**\
   Ready pool of users familiar with authentication gateway and Singpass app.<br>


# Key Principles

***

**Use Login as an authentication service**

* Option 1: NRIC/FIN and UUID
* Option 2: UUID only

**UUID**

* Instead of NRIC/FIN, digital services of businesses can use the Universally Unique Identifier (UUID) to uniquely identify a person

**Provide non-Singpass alternative**

* Provide support to customers who prefer to use a non-Singpass alternative

**PDPA & Applicable Regulations/Legislation**

* Protect, retain and transfer data retrieved according to the rules of the Personal Data Protection Act (PDPA), relevant industry regulations and applicable legislation
* For collection of National Identification Numbers, refer to the advisory guidelines from PDPC [here](https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Advisory-Guidelines/Advisory-Guidelines-for-NRIC-Numbers---310818.pdf)

**Use for lawful purposes**

* Use of user credentials for lawful purposes only


# FAQ

Frequently Asked Questions about Singpass Login

#### Q1. What are the identifiers returned to us after the authentication process? NRIC/FIN numbers or User’s Universally Unique Identifier (UUID).

Please assess which identifier is appropriate for your use case taking into account applicable laws, regulations, guidelines, and industry circulars or notices. This includes the Advisory Guidelines on the Personal Data Protection Act for NRIC and Other National Identifiers (see [here](https://www.pdpc.gov.sg/guidelines-and-consultation/2020/02/advisory-guidelines-on-the-personal-data-protection-act-for-nric-and-other-national-identification-numbers)).

***

#### Q2. What is a UUID?

A Universally Unique Identifier (UUID) is a 128 bits-long identifier to uniquely identify a Singpass user.

***

#### Q3. Can I allow my users to log in with their Singpass usernames and passwords if they do not have the Singpass app?

No, as part of national scam-prevention efforts, new Singpass Login/Myinfo apps will only support QR Login. Password/SMS OTP login will no longer be offered.

Password/OTP logins on mobile browsers are much easier for scammers to exploit, especially when a device is infected or remotely controlled. QR Login is far more secure because the user must verify the login within the Singpass app, which has stronger protections.

Your end users/customers who prefer not to use QR login can still rely on the alternative login or form-filling options provided by your e-service.

***

#### Q4. Can foreigners use Login to transact with digital services?

Foreigners must be at least 15 years old and are either Permanent Residents (PRs) or Foreign Identification Number (FIN) holders with a valid Singpass account to use Login.

***

#### Q5. What are the charges/fees for using Login API?

Singpass Login API adopts a pay-per-transaction tiered pricing structure. You may log into the Singpass API Portal to view details of the price plan.

***

#### Q6. I am a financial institution. Is utilisation of Singpass API services subject to MAS’ expectations under the Guidelines on Outsourcing?

The Monetary Authority of Singapore (MAS) has issued a circular guidance to all financial institutions in June 2020 (see [here](https://www.mas.gov.sg/-/media/mas/regulations-and-financial-stability/regulations-guidance-and-licensing/insurance/regulations-guidance-and-licensing/circulars/circular---id-26_20.pdf)). For outsourcing arrangements involving services which are wholly provided by the Government Technology Agency (GovTech) or agents appointed by GovTech, they will not be subject to the MAS Guidelines on Outsourcing. Please refer to the list of services [here](https://docs.developer.singpass.gov.sg/docs/products/singpass-login).

***

#### Q7: Who do I contact if I require more details?

If you have any other query, please submit a request at [partnersupport.singpass.gov.sg](https://partnersupport.singpass.gov.sg/).

***


# Singpass Myinfo

Myinfo enables citizens and residents to manage the use of their personal data for simpler online transactions. All Singpass users are automatically provisioned with a Myinfo profile. Users are able to view their personal data and access records of past usage via the Singpass app.

***

**How Myinfo API can enhance your digital service**

1. **Less form filling, higher data quality**\
   Users can share their data by providing consent via Singpass and organisations no longer have to deal with manual data management.<br>
2. **Data from government sources**\
   With data from participating government sources, this allows the provisioning of products instantly, where applicable.


# Key Principles

Partners are to comply with Myinfo key principles for your integration and submission of documents.

**Requesting for Data**

1. **Request only what you need**

* Do not over-collect data, where this is not required for business purposes or legal reasons.
* Each request must support only a single purpose.

2. **PDPA & Applicable Regulations/Legislation**

* Protect, retain, transfer and dispose of data retrieved according to the rules of the Personal Data Protection Act (PDPA), relevant industry regulations and applicable legislation.
* Use data in a manner consistent with the purpose of user’s consent.

3. **Use for lawful purposes**

* Use the data items retrieved for lawful purposes only.

***

**Designing your User Journey (UJ)**

1. **Display As-Is**

* Data items retrieved from our APIs should be displayed as-is on digital forms, so as to assure users that the correct data items have been retrieved.
* This minimises clarifications on the data retrieved and encourage users to update the relevant Government data source agency if any information is outdated.

2. **Store only if submitted**

* Data should be purged if form is not successfully submitted.
* If ‘Save-as-draft’ feature is available, unsubmitted data should be purged periodically.

3. **Provide non-Myinfo alternative**

* Partners are encouraged to support customers who prefer to use a non-Myinfo alternative.

4. **Showing customers the benefits of using Myinfo**

* Indicate that Myinfo service is available for your application and clearly state the target users (e.g. for SC/PR and/or Foreigners).
* Present the benefits of using Myinfo option (e.g. time saving, less document uploads or instant provisioning).

5. **Reduce supporting document upload**

* Data from Government sources which are un-editable on your form should be assessed for suitability as an alternative to collecting documents for verification (e.g. NRIC, CPF Contribution History, Notice of Assessment).

***

#### **Using Myinfo Personal Data**

1. **Display all retrieved personal data**

* All Myinfo Personal data retrieved shall be displayed as-is on your digital forms.
* Government-originated data on digital service forms should be un-editable, to preserve data integrity for verification.
* User-provided data should remain editable.


# Data Display Guidelines

This is for CPF Account Balance, Principal Name and NOA (Detailed)

The following provides a set of display guidelines for businesses with digital services consuming CPF, Principal Name and Notice of Assessment (Detailed) data to adhere to, in order to present the respective data in an accurate and consistent manner.

#### CPF Account Balances

***

There are 4 types of CPF accounts and their respective balances are available via Myinfo:

* Ordinary Account (OA)
* Special Account (SA)
* Medisave Account (MA)
* Retirement Account (RA)

CPF data are retrieved real-time (as at the point of retrieval). Organizations whose digital services are obtaining CPF balances via Myinfo, will need to take note of the following points when designing the display of CPF balances in their digital services.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-eb1c42fbcef6fdafee481af6fdb095cc7f10f141%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Example 1: CPF member has OA, SA and MA only

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-6a9742826586151beceae2dbb436f88187abdf69%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Example 2: CPF member with OA, SA, MA and RA

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-9450cf1f20240d2874499f6dfbed388374a23197%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

#### Employment Related CPF Contribution History

Organisations whose digital services are consuming employment related CPF Contribution History via Myinfo, will need to take note of the following points when designing the display of CPF contributions in their digital services. CPF data are retrieved real-time (as at the point of retrieval).

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-58fdd0f6ce4f4feca18a22c5fa51fff7f151acf7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Please take note that:

* The contribution entries are to be sorted by "Paid on" followed by "For Month", in ascending values.
* Myinfo service covers commonly required CPF contribution, i.e. employment related contributions. Non-employment related contribution (e.g. government top-up, self-employed contributions) are not available in Myinfo.

Example 1: CPF member has OA, SA and MA only

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-e29ffea121595c3c651c94fa63048e0af086a4e7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

***

#### Principal Name

Businesses that are capturing customer's name in multiple fields (e.g. First, Middle and Last Name) must take note of the following points:

* Principal Name field must still be displayed in non-editable mode.
* Multiple name fields (e.g. First, Middle, and Last Name) will be displayed in editable mode.
* It is in businesses interest that the final submitted multiple name fields does not substantially differ with the Principal Name.

***

#### Notice of Assessment (Detailed)

Businesses with digital services consuming Notice of Assessment (Detailed, Last Year) or Notice of Assessment (Detailed, Last 2 Years) must take note of the following points:

* All detailed fields in the Notice of Assessment should be displayed.
* Year of Assessment, Type and Tax Clearance (if applicable), Assessable Income and Income Breakdown must be displayed clearly.
* When Tax Clearance = Y, the word 'Clearance' must be displayed after the Type field.

Businesses must adhere to the guideline in order to present the respective Notice of Assessment data in an accurate and consistent manner to Tax Payer.

Examples of Notice of Assessment (Detailed, Last 2 Years) display:

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-651560794fe3e1e9966ba650552be34c44f71e3b%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>


# Scheduled Downtimes

Due to the scheduled downtimes of Myinfo upstream systems, financial data from CPF Board and IRAS, and FIN user data from MOM are unavailable via Myinfo, Myinfo business, Verify and SGFinDex API at the following times:

* **CPFB**
  * On the Wednesday right after the 3rd Sunday of the month, from 0000hrs - 0400hrs
  * Every 1st Sunday of the month from 0000hrs to 0800hrs
  * Every 4th Sunday of the month from 0000hrs to 0500hrs (with effect from April 2026)
  * If the 1<sup>st</sup> or the 2<sup>nd</sup> day of the month falls on the 1<sup>st</sup> Sunday, the maintenance will be on the 2<sup>nd</sup> and 4<sup>th</sup> Sunday instead.
* **IRAS**
  * Every Wednesday, 0200hrs to 0600hrs
  * Every Sunday, 0200hrs to 0830hrs
* **MOM**
  * Every 4th Sunday of the month from 0000hrs to 0600hrs

***

### What to Expect During Downtime

During these maintenance periods, users will encounter an error response when attempting to retrieve the affected data. No data will be returned.

The specific error response that partners will receive will differ depending on their client version.

The error response for Myinfo v3/v4 clients is:

```
{
"statusCode": 500,
"message": "Internal server error - 540"
}
```

For Myinfo v5 clients, you will receive an error of status code 502, with the following response body:

```
{
"id":"872527df-1c6b-4d65-be27-b2b9642a8c92",
"error":"upstream_dependency_error",
"error_description":"An error has occurred.",
"trace_id":"1-68c39359-03322d4443ca5f0c353c7beb"
}
```

Partners are expected to handle the above error responses in their internal systems and display a corresponding user-friendly error message to their end-users. This ensures a smooth user experience even during downtimes.

Please note that Myinfo, Myinfo Business, and Verify APIs will remain available for all other data items not affected by the maintenance.

Similarly, SGFinDex services will be unable to retrieve government-related data (from CPF and IRAS) during these times. However, SGFinDex will still be available for non-government data from financial institutions.


# FAQ

Frequently Asked Questions about Myinfo

#### Q1. What are the benefits of upgrading to the new version of Myinfo?

The new version of Myinfo API improves the security posture of the API and data shared. It aligns to current industry and RFC standards, and improves operations flows for partners to minimise service disruption during key rotation.

***

#### Q2. I am currently using Myinfo v3. When is the deadline to upgrade to Myinfo v4?

It is no longer mandatory for partners to migrate to Myinfo v4. All new onboardings will be to the new Myinfo.

1. Partners on Myinfo v3/v4 will have till end Sep 2026 to migrate to Myinfo v5.
2. Partners are expected to ensure that their apps are compliant with FAPI 2.0 by 31 December 2026.

***

#### Q3. What should I do when a user’s data in the business conflicts with the user’s data retrieved from Myinfo?

You should assess which dataset takes precedence, based on business or regulatory requirements and also factor in the following:

1. Whether the data retrieved from government sources;
2. Time-stamp of the data retrieved, to determine which is more recent.

***

#### Q4. Can I request for more data items than what I need for my digital service?

No. You should only request for the data items that you need for your digital service. This is aligned with the guidelines of the Personal Data Protection Act, which instructs the collection of personal data in an appropriate manner for the circumstances. Each request will be reviewed prior to approval.

***

#### Q5. I would like to linkup multiple digital services with Myinfo. Do I submit a single request for all my digital services or one request for each digital service?

A new request must be submitted for digital services with different use cases/user journeys. If in doubt, please submit a request for every digital service.

***

#### Q6. My digital service saves user data in the transaction session or cookie. If the user closes the browser and comes back to the digital service again, can I populate the digital form using data saved in the session or cookie?

No. To prevent stale data from being mistaken as a Myinfo data, every user profile retrieved by a digital service must fetch new data from Myinfo.

***

#### Q7. I would like to design my digital service to depend solely on Myinfo to fill up a form. Is this a recommended approach?

Digital services should allow users to manually fill up forms to access digital services to accommodate the following scenarios:

1. User does not wish to use Myinfo;
2. If the user is a foreigner who does not have Myinfo or if the user does not have a Singpass account; or
3. If the Myinfo service is temporarily unavailable (e.g. system maintenance).

***

#### Q8. Can my digital service retrieve user data for backend processing without displaying it on a digital form?

No, all data retrieved from Myinfo have to be displayed on the digital form for verification by the user, prior to form submission.

***

#### Q9. How should my digital service handle scenarios where the user finds that the verified data retrieved from Myinfo is out-of-date? (e.g. user has not updated ICA about his/her change of registered address)

Businesses may allow users to fill out the form manually with the correct data. In this case, data previously retrieved from Myinfo should not be saved.

***

#### Q10. Are the registered addresses of users restricted to Singapore addresses?

No, the registered address field can contain overseas addresses.

***

#### Q11. My digital service requires only the last three months of the user’s CPF contribution history. Can my digital service only show the last three months of CPF contribution history?

The retrieval of CPF contribution history will return the last 15 months of the user’s CPF contribution. All 15 months of the contribution should be displayed on your digital service form.

***

#### Q12. Is there any guideline to display CPF contribution history data?

Digital services should adhere to the CPF Display Guidelines when retrieving and displaying CPF data: Click [here](https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines) to refer to the CPF display guidelines.

***

#### Q13. I have some issues uploading my X.509 public key with my iOS device. How can I upload my X.509 public key?

It is recommended to upload your X.509 public key using compatible browsers (e.g. Safari, Chrome, Firefox) on your desktop.

***

#### Q14. I have been given a CorpPass account by my CorpPass administrator. However, I am unable to login to the portal using the CorpPass account.

Please check with your Corppass administrator to ensure your Corppass account is given permission to access 'Singpass Developer Portal'.

***

#### Q15. What is the estimated turnaround time after I have submitted an app request?

We will respond to you in two weeks upon submission of your app request.

***

#### Q16. What is the estimated turnaround time after I have submitted my app configurations?

Upon successful submission, your app configurations will take effect within 5 to 10 minutes.

***

#### Q17. We are a solution company looking to build a product/platform integrated with Myinfo for our client. How do we go about doing so?

Please submit a joint link-up request through your client. You may refer to our portal for the on-boarding process.

***

#### Q18. Can the consent page be customised to allow users to select fields that they wish to retrieve from Myinfo?

To optimise the user experience for customers, users need to consent to share all data items relevant to a transaction. This allows a more seamless and secure user journey that minimises form-filling and document submission.

If users are uncomfortable with sharing any data items, they may opt to fill the form manually.

***

#### Q19. Can foreigners use Myinfo to transact with digital services?

Foreigners who have a valid Singpass account will have a Myinfo profile, and they can use the service.

***

#### Q20. Can I add additional data item(s) to my app after it has been submitted?

You may add additional data item(s) to your app after the original request has been approved.

Please click on the 'Edit' button and under 'Scopes Selection' choose your additional data item(s) for your app.

A revised user journey should be submitted to reflect the additional data item(s), and the justification updated.

***

#### Q21. What are the charges/fees for using Myinfo API?

Charges for using Myinfo API started from Apr 2022. Please log in with Singpass to view pricing table.

***

#### Q22. I am a financial institution. Is utilisation of NDI services subject to MAS’ expectations under the Guidelines on Outsourcing?

The Monetary Authority of Singapore (MAS) has issued a guidance to all financial institutions in June 2020. For outsourcing arrangements involving services which are wholly provided by the Government Technology Agency (GovTech) or agents appointed by GovTech, they will not be subject to the MAS Guidelines on Outsourcing. Please refer to the list of services [here](https://docs.developer.singpass.gov.sg/docs/products/singpass-login).

***

#### Q23. Who do I contact if I require more details?

If you have any other query, please submit a request at [partnersupport.singpass.gov.sg](https://partnersupport.singpass.gov.sg/).


# Singpass Face Verification

### **What is SFV?**

Singpass Face Verification (SFV) adds face verification as a third authentication factor after standard Singpass two-factor authentication (QR code or passkey).

SFV provides Authentication Assurance Level 3 (AAL3), offering greater assurance that the person authenticating is the legitimate Singpass account holder.

**SFV is not a standalone product** and must be integrated with Singpass Login.

### **Who can use SFV?**

SFV is reserved for high risk use cases requiring stronger authentication assurance than standard Singpass Login (AAL2).

#### **Financial Institutions (FIs)**

SFV onboarding is currently available only to **selected FIs with MAS-approved use cases**.

Eligible FIs must obtain approval from the Monetary Authority of Singapore (MAS) before requesting SFV onboarding through [Singpass Partner Support](https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new).

#### **Non-Financial Institutions (Non-FIs)**

**New SFV onboarding for non-FIs is currently paused.**

New SFV onboarding for non-FIs is currently paused while SFV undergoes a technical and service review, expected to continue into H1 2027.

Interested organisations may register their interest through the [SFV Interest Form](https://go.gov.sg/sfv-interest).

### **Supported use cases**

SFV is intended for high risk activities requiring stronger authentication assurance.

| **Use case**                   | **Example**                                                 |
| ------------------------------ | ----------------------------------------------------------- |
| **Digital token setup**        | Registering a banking soft token on a new device            |
| **High value transactions**    | Authorising large fund transfers                            |
| **Sensitive account recovery** | Resetting authentication credentials for high risk accounts |

{% hint style="warning" %}
SFV is **not intended for general purpose login, low risk transactions or replacing in-person identity verification**.

Meeting these use case descriptions does not automatically qualify an organisation for SFV onboarding.
{% endhint %}

### How to request SFV onboarding

This process applies only to eligible FIs with MAS-approved use cases.

1. Obtain MAS approval for your proposed SFV use case.
2. Review the [SFV Integration guide.](https://docs.developer.singpass.gov.sg/docs/products/singpass-face-verification/sfv-integration-guide)
3. Submit an onboarding request through [Singpass Partner Support](https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new)⁠.

Include the following information in your request:

* Organisation name and UEN
* Description of the SFV use case and justification for AAL3
* Confirmation of MAS approval
* Singpass Login Client ID (if available)
* Estimated SFV transaction volume

Once approved, refer to the [SFV Integration guide](https://docs.developer.singpass.gov.sg/docs/products/singpass-face-verification/sfv-integration-guide) for integration and testing instructions.


# SFV Integration Guide

## Integration Guide

Singpass Face Verification (SFV) adds face verification as a third authentication factor on top of standard Singpass two-factor authentication (2FA), providing Authentication Assurance Level 3 (AAL3).

**SFV is not a standalone product.** To integrate SFV, you must first create a Singpass Login application and obtain approval for SFV enablement.

This guide explains how to configure SFV and verify AAL3 authentication.

### Before you begin

Complete the following steps before integrating SFV.

{% stepper %}
{% step %}

### Check your eligibility

Review the [SFV Eligibility](https://docs.developer.singpass.gov.sg/docs/products/singpass-face-verification) requirements to confirm that your organisation and use case qualify for SFV.
{% endstep %}

{% step %}

### Create a Singpass Login application

Create a Singpass Login application in the staging environment through the [Singpass Developer Portal](https://developer.singpass.gov.sg)⁠.

If you already have a Singpass Login application, you may use your existing application.
{% endstep %}

{% step %}

### Request SFV enablement

Submit an onboarding request through [Singpass Partner Support](https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new)⁠.

Include:

* Organisation name
* Singpass Login staging client id
* SFV use case description
* Confirmation of MAS approval, where applicable

Singpass will review your request and enable SFV for your application if approved.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
**SFV enablement is mandatory.**

Only applications approved and whitelisted for SFV can request AAL3 authentication

Requests from applications that are not whitelisted will return an error.

**SFV must be enabled separately for staging and production applications**
{% endhint %}

### How SFV works

SFV uses the existing Singpass Login flow. No separate face verification API integration is required.

Once SFV is enabled for your application:

1. **Request AAL3:** Include `acr_values=urn:singpass:authentication:loa:3` in your Pushed Authorization Request (PAR).
2. **Complete authentication**: Users complete standard Singpass login, followed by face verification in their browser.
3. **Return to your service:** Upon successful authentication, users are redirected to your registered callback URL.

{% hint style="info" %}
**Face verification takes place in the user’s browser, not within the Singpass app.**

After completing Singpass authentication, users return to their browser to complete face verification before being redirected to your digital service.
{% endhint %}

### Technical configuration

#### 1. Request AAL3 authentication

To trigger SFV, include the following `acr_values` parameter in your Pushed Authorization Request (PAR):

```
acr_values=urn:singpass:authentication:loa:3
```

#### Sample PAR request

The following example shows a PAR request for AAL3 authentication in the staging environment.

```http
POST /fapi/par HTTP/1.1
Host: stg-id.singpass.gov.sg
Content-Type: application/x-www-form-urlencoded
DPoP: <dpop-proof>

response_type=code
&client_id=<client_id>
&redirect_uri=<registered_redirect_uri>
&scope=openid%20user.identity%20name%20mobileno%20email
&state=<state>
&nonce=<nonce>
&code_challenge=<code_challenge>
&code_challenge_method=S256
&authentication_context_type=APP_AUTHENTICATION_DEFAULT
&acr_values=urn:singpass:authentication:loa:3
&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
&client_assertion=<client_assertion>
```

{% hint style="warning" %}
**SFV enablement required**\
Your Singpass Login application must be whitelisted for SFV before requesting AAL3. Requests from applications that are not whitelisted will return an error.
{% endhint %}

For the complete PAR requirements, refer to [Authorization Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request).

#### 2. Handle authentication redirection

After completing Singpass Login, users return to their browser to complete face verification.

Upon successful authentication, Singpass redirects users to your registered `redirect_uri` with an authorisation code.

Your application should handle this redirect according to the standard Singpass Login integration requirements.

**Native mobile applications**

For native mobile applications, ensure that users can return to the browser authentication session after completing Singpass 2FA.

Use the appropriate system browser authentication components rather than embedded WebViews.

Refer to the official integration examples:

* [iOS In-App Browser Login Demo](https://github.com/singpass/iOS-Singpass-in-app-browser-login-demo)⁠
* [Android In-App Browser Login Demo](https://github.com/singpass/Android-Singpass-in-app-browser-login-demo)⁠

Refer to [Handling the Redirect](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/2.-handling-the-redirect)⁠ for details.

### Testing SFV in Staging

To test SFV, you must create a Singpass staging test account and register a facial photograph for that account.

{% stepper %}
{% step %}

#### Create a staging test account

Create a staging test account through the [Singpass Developer Portal](https://developer.singpass.gov.sg)⁠.

Follow the [Create Staging Test Account Guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-test-account)⁠.
{% endstep %}

{% step %}

### Register your photograph

Register a facial photograph for your staging test account through the [SFV Photo Tagging Form](https://go.gov.sg/phototagging)⁠.

Ensure your photograph complies with ICA’s photograph requirements.

{% hint style="warning" %}
**Photo registration is required for SFV testing.**\
\
If your staging test account does not have a registered photograph, SFV will not be triggered for that account
{% endhint %}
{% endstep %}

{% step %}

### Test SFV authentication

Using your photo-tagged staging account:

1. Initiate Singpass Login with `acr_values=urn:singpass:authentication:loa:3`.
2. Complete standard Singpass 2FA.
3. Return to the browser and complete face verification.
4. Confirm that authentication completes and the user is redirected to your digital service.
   {% endstep %}
   {% endstepper %}

### Handling incomplete authentication

Your application should provide clear instructions for users who cannot complete SFV or abandon the authentication process.

#### What your application should handle

| Successful authentication                | Redirect users to the appropriate page in your digital service.                  |
| ---------------------------------------- | -------------------------------------------------------------------------------- |
| Singpass authentication or service error | Display an appropriate error message and provide a retry option.                 |
| User closes the browser                  | Allow users to restart authentication                                            |
| User cannot complete SFV                 | Provide clear instructions or alternative verification methods, where permitted. |

{% hint style="info" %}
SFV failure outcomes are not disclosed to partners.

Singpass does not return a separate error indicating that face verification was unsuccessful.

Partners cannot determine whether an incomplete authentication was caused specifically by failed face verification.

Users may also abandon the authentication flow without an error callback.
{% endhint %}

Ensure that your [SFV User Journey](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey) includes appropriate screens for users who cannot complete authentication.

### Next steps

Once you have completed SFV integration and staging testing:

1. **Prepare your User Journey:** Complete the [SFV User Journey ](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey)Template⁠.
2. **Request production approval:** Submit your production application for review and request SFV enablement through [Singpass Partner Support](https://partnersupport.singpass.gov.sg/hc/en-sg/requests/new)⁠.


# Overview of Singpass

Singpass is Singapore's national digital identity authentication provider using the [OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html) protocol. It stores users' identity information and authenticates them for transactions with government agencies and private organizations online.

## How Singpass OIDC Works?

{% hint style="info" %}
**OpenID Provider (OP)** is the party that issues the ID token. In this case, Singpass serves as the OpenID provider.
{% endhint %}

{% hint style="info" %}
**Relying Party (RP)** is the party that requests the ID token from Singpass, which in this context refers to your mobile or web application.
{% endhint %}

[OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html) offers various authentication flows for integrating an OpenID Provider (OP) and a Relying Party (RP). Singpass as the OpenID Provider supports only the **authorization code flow**. This flow is the most widely used OpenID Connect authentication method, ideal for web applications and native applications that employ a client/server architecture. In this more secure and confidential flow, instead of returning the ID and access tokens directly to the Relying Party, an authorization code is provided. The Relying Party can then exchange the code for the necessary tokens to complete the authentication flow. The token will be used for information exchange if user info is required. The relying Party is required to manage the parsing of JWT used in JWT assertion.


# Understanding the basics of OIDC

[OpenID Connect 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (OIDC) is a simple identity layer on top of the OAuth 2.0 protocol. It:

* Allows clients to verify the identity of the end user based on the authentication performed by an Authorization Server
* Allows clients to obtain basic profile information about the end user in an interoperable and REST-like manner
* Allows clients of all types, including Web-based, mobile, and JavaScript clients, to request and receive information about authenticated sessions and end-users

## OIDC Actors

There are several actors involved in the Open ID Connect protocol. The following sections will detail each actor involved in the communication.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-cd8ed7eac1d70dd18168d68496f8cf5dd4e06e1d%2Factors.png?alt=media" alt=""><figcaption><p>OIDC Actors Flowchart</p></figcaption></figure>

<details>

<summary><strong>OIDC Provider (OP)</strong></summary>

Singpass is an OpenID provider and it is the “vouch for” party in an identity federation. That is, it gives assurances of the identity of the user to the other party. The OpenID provider is responsible for:

* Managing users and their identities
* Issuing tokens
* Handling user administration
* Authenticating the user
* Vouching for the user's identity with the relying party
* Revoking user’s authenticated sessions and tokens

</details>

<details>

<summary><strong>Client or Relying Party (RP)</strong></summary>

The business entity will implement the relying party (also client or consumer) which will be the “validating party” in a transaction. The relying party or client is responsible for:

* Controlling access to services
* Validating the various tokens issued by OpenID Provider
* Validating the asserted identity information from the OpenID provider (typically by way of verifying a digital signature)
* Providing access based on asserted identity
* Managing only locally relevant user attributes, not an entire user profile
* Each client must be registered with an OpenID provider.

The clients registered with Singpass OP must be confidential clients, which means every client must be registered with Singpass OP with their `Client ID` and `JWT Assertion`.

</details>

<details>

<summary><strong>User Agent</strong></summary>

The user agent is a web browser or mobile browser or mobile application via which the user (resource owner) will initiate the communication with the OpenID Provider and Relying Party:

* Serves static or dynamic pages
* Handles redirections
* May store cookies, user, and session information
* Should not be used to store confidential data like user identity or tokens

</details>

<details>

<summary><strong>Resource Owner</strong></summary>

The resource owner could be an end-user or an entity capable of granting access to protected resources. In most cases, it would be the user accessing agency applications.

</details>

<details>

<summary><strong>Resource Server</strong></summary>

The resource server will be hosted on the agencies' perimeter. It is the server that is hosting the applications protected by the relying party. Agencies' relying party will communicate with Singpass OP before granting access to protected resources hosted on the resource server.

</details>

Here are some additional resources for learning more about OAuth 2.0 and OIDC:

{% embed url="<https://youtu.be/996OiexHze0?si=Q4ZCygOFo_Y59RGD>" %}


# Changelog

{% hint style="info" %}
New Login and Myinfo apps must follow Singpass' [FAPI 2.0-compliant API specification](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide).

This changelog applies if you are upgrading a Login or Myinfo (v5) integration set up before February 2026. See the [Login and Myinfo (v5) migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/login-myinfo-v5-apps).

For a legacy Myinfo (v3/v4) app, see the [Myinfo migration guides](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides).

**Existing partners:** Non-FAPI integrations remained available during the parallel-run period. App registrations after 10 February 2026 require FAPI compliance.

**Legacy documentation retired on 14 July 2026:** If your integration uses the pre-FAPI API, follow the [Login and Myinfo (v5) migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/login-myinfo-v5-apps) to adopt the FAPI 2.0 Security Profile.
{% endhint %}

## The FAPI 2.0 Security Profile

The FAPI 2.0 Security Profile builds on top of the existing OIDC specifications. Singpass is already OIDC-compliant, which means that you will not need to update your entire existing integration—you will only need to update some parts of the integration.

The following diagram provides an overview of the parts of the Singpass flow that are changing. The changed parts are highlighted in red. For ease of comparison, the same diagram for the prior authentication API flow is no longer available as the legacy API documentation has been retired.

You may also view an interactive version of this diagram in [this page](https://tinyurl.com/singpass-fapi2-changelog).

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-023d3646466ece2005f97ddd55f0a469f0c2cb73%2Fmermaid-diagram-2025-09-03-101046.png?alt=media" alt=""><figcaption></figcaption></figure>

## Pushed Authorization Requests

*Relevant steps in sequence diagram: steps 4-7*

Previously, you would have performed the authorization request by redirecting users to an authorization URL containing all the authorization request parameters (such as `redirect_uri`, `client_id`, `scopes` ) in its query parameters.

We will now instead require pushed authorization requests (as specified in [RFC 9126](https://datatracker.ietf.org/doc/html/rfc9126)) to be performed during the authentication flow. This was done for improved security, as using pushed authorization requests will prevent tampering of the authorization request parameters in the authorization URL.

Switching to pushed authorization requests requires you to make two changes:

1. Before redirecting the user to the authorization URL, you must first make a POST request to the `pushed_authorization_request_endpoint` (which is published in the authorization server metadata) with a request body containing all the authorization request parameters. This is represented by steps 4-5 in the sequence diagram.
2. When you redirect the user to the authorization URL, the query parameters of the URL should only contain `request_uri` (returned from the pushed authorization request) and your `client_id`.

## New Parameters for Authorization Requests

*Relevant step in sequence diagram: step 4*

We now support some new parameters for authorization requests. These parameters are:

* `acr_values`
* `authentication_context_type`
* `authentication_context_message`

These new parameters, which you will pass in the pushed authorization request, will provide you greater control over what your users will experience during the authentication process. Full details of these parameters can be found in [this page](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request#singpass-specific-parameters).

{% hint style="warning" %}
Myinfo (v3/v4) apps have authorization requests that differ from Login and Myinfo (v5) apps, so you will need to make more changes if you are currently integrating with a Myinfo (v3/v4) app.
{% endhint %}

## Demonstrating Proof-of-Possession (DPoP)

*Relevant steps in sequence diagram: steps 5, 17, and 22*

You may also read [this blog post](https://auth0.com/blog/what-are-oauth-push-authorization-requests-par/) to understand more about pushed authorization requests.

A DPoP proof (as specified in [RFC 9449](https://datatracker.ietf.org/doc/html/rfc9449)) is now required for the following requests:

* The pushed authorization request
* The token request
* The userinfo request

This was introduced in order to ensure that both the authorization code and the access token (issued on steps 10-13 and 19 respectively in the sequence diagram) can only be used by you and not by any other party.

You may read more about DPoP in our guide [here](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop).

{% hint style="warning" %}
If you are currently integrating with a Myinfo (v4) app, you will only need to add DPoP for the pushed authorization request.
{% endhint %}

## ID Token Encryption and Format

*Relevant steps in sequence diagram: steps 20-21*

The ID token will now always be encrypted using JSON Web Encryption (JWE), regardless of the client profile of your app. Previously, the ID token was only encrypted if you had requested for NRIC to be returned in the ID token. Note that this will now require you to add an encryption key into your JWKS, if you do not already have one.

Additionally, the format of the claims returned in the ID token is also different. A summary of the changes are:

* The `sub` claim will now only contain the UUID of the user. Previously, it contained key-value pairs containing different values depending on your app's client profile and the type of user, but we have now simplified the claim to just always be the UUID.
* If you require NRIC (for SC/PR), FIN (for pass holders) or the foreign ID (for SFA users) to be returned in the ID token, you may request for the new `user.identity` scope. If the scope is requested, then this information will be returned in the new `sub_attributes` claim in the ID token.
* Note also that `sub_attributes` in the new ID token will only be returned if any of the following scopes (`user.identity` , `name` , `mobileno` and/or `email` ) is/are requested as part of the `scopes` in the authorization request.

Here are some examples to illustrate the difference:

<details>

<summary>ID token differences</summary>

Note: for brevity, the examples here do not contain the whole ID token - they only contain the parts that have changed.

<table><thead><tr><th width="171.453125">User type</th><th>Old ID token</th><th>New ID token</th></tr></thead><tbody><tr><td>Singapore Citizen / PR</td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "sub": "s=S8829314B,u=1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9"
}
</code></pre></td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "sub": "1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9",
  "sub_type": "user",
  "sub_attributes": {
    "account_type": "standard",
    "identity_number": "S8829314B",
    "identity_coi": "SG"
  }
}
</code></pre></td></tr><tr><td>FIN holders</td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json"><strong>{
</strong>  "sub": "s=G4542206U,u=1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9"
}
</code></pre></td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "sub": "1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9",
  "sub_type": "user",
  "sub_attributes": {
    "account_type": "standard",
    "identity_number": "G4542206U",
    "identity_coi": "SG"
  }
}
</code></pre></td></tr><tr><td>Singpass Foreign Account</td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "sub": "s=Y7613265T,fid=G730Z-H5P96,coi=DE,u=e2af740e-25b4-4b19-b527-494670952cb0"
}
</code></pre></td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "sub": "e2af740e-25b4-4b19-b527-494670952cb0",
  "sub_type": "user",
  "sub_attributes": {
    "account_type": "foreign",
    "identity_number": "G730Z-H5P96",
    "identity_coi": "DE"
  }
}
</code></pre></td></tr></tbody></table>

</details>

For full details on the new format, you may refer to [ID token specs](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token).

## Userinfo Response Format

*Relevant step in sequence diagram: step 26*

The userinfo response will have a slightly different format. The format of the data itself remains unchanged - the only difference is that the data is now nested inside a `person_info` field.

The userinfo response will remain encrypted using JWE - no changes will be made on how it is encrypted.

Here's an example to illustrate the difference:

<details>

<summary>Userinfo payload difference</summary>

<table><thead><tr><th>Old response</th><th>New response</th></tr></thead><tbody><tr><td><pre class="language-json"><code class="lang-json">{
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
  "iss": "https://stg-id.singpass.gov.sg",
  "sub": "s=S9000001B,u=d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "tWT3rfImn9hCezlLr0M1nRUvQ40fCNL4",
  "iat": 1746678089
}
</code></pre></td><td><pre class="language-json"><code class="lang-json">{
  "person_info": {
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
  }
  "iss": "https://stg-id.singpass.gov.sg",
  "sub": "d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "tWT3rfImn9hCezlLr0M1nRUvQ40fCNL4",
  "iat": 1746678089
}
</code></pre></td></tr></tbody></table>

</details>

{% hint style="warning" %}
Myinfo (v3/v4) integrations will also need to start using the userinfo endpoint instead of the Myinfo Get Person API.
{% endhint %}

## Enforcement of Proof of Key Code Exchange (PKCE)

We will be enforcing PKCE (specified in [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)) for all integrations with the new authentication API. This is a requirement for FAPI 2.0 compliance, and will help to protect you against misuse of the authorization code. Read more about PKCE in our guide [here](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce).

## Removal Of Support For Custom Scheme URLs

Previously, custom scheme URLs (i.e. URLs that do not use the `https://` scheme) were allowed to be registered as redirect URLs and app launch URLs. This was done to support redirection to mobile apps.

We will be dropping support for the usage of such URLs with the new specifications. If you are currently using custom scheme URLs for mobile app redirection, you are required to instead use App-claimed https URLs ([Universal Links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content) for iOS, and [App Links](https://developer.android.com/training/app-links) for Android) for this purpose instead. This is being done to ensure that redirects from Singpass cannot be intercepted by malicious applications.

### Authentication Error Responses

Currently, we generally do not redirect back to your redirect URL when an error occurs. This will change with the new authentication API. We will now be redirecting back to your redirect URL in more scenarios with an Authentication Error Response, which is specified in [section 3.1.2.6 of the OpenID specifications](https://openid.net/specs/openid-connect-core-1_0.html#AuthError).

With this change, you will get more information about what are the errors that users face while authenticating with Singpass, and can handle the error flows appropriately. However, this also means that you must ensure that you have proper error handling in place for these errors.

View our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/2.-handling-the-redirect#failed-authentication) to see the full list of errors that could be sent to you during the redirect.

## Changes In \`amr\` Claim Values

The `amr` claim values returned in the ID token have been updated. You can ignore this section if you have not been reading the `amr` claim values.

Note that if you have previously been reading the `amr` claim values to determine the level of assurance of the authentication transaction, we recommend that you read the new `acr` claim value instead, which directly provides the level of assurance without requiring you to map the `amr` values to a level of assurance. By using the `acr` claim instead of the `amr` claim, you would not need to update your implementation should we introduce new form factors.

Specifically, the following changes have been made:

### Change in naming

Some of the `amr` values have had their names changed for clarity. Specifically, these three claims have changed:

| Previous value | New value  |
| -------------- | ---------- |
| `sms`          | `otp-sms`  |
| `fv`           | `face`     |
| `fv-alt`       | `face-alt` |

### Provision of all form factors when face verification is used

Previously, when face verification was used **as a third factor** during the authentication, the `amr` claim would only be `["fv"]`, even though multiple form factors were used in the authentication.

With the FAPI2.0 implementation, the `amr` claim would now always contain all form factors used in order to provide more clarity. For example:

| Form factors used                             | Previous amr    | New amr                                                                                                                              |
| --------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Username/password, SMS OTP, face verification | `["fv"]`        | `["pwd", "otp-sms", "face"]`                                                                                                         |
| QR, face verification                         | `["fv"]`        | `["swk", "face"]`                                                                                                                    |
| Username/password, face verification          | `["pwd", "fv"]` | <p><code>\["pwd", "face"]</code><br>(note: no change in number of elements, since face verification was used as a second factor)</p> |


# Integration Guide

This section will walk you through how to set up your Singpass Login or Myinfo (v5) integration.

As Singpass' authentication API is fully compliant with **OIDC** and the **FAPI 2.0 Security Profile**, we suggest that you use any one of these [OpenID-certified relying party libraries](https://openid.net/developers/certified-openid-connect-implementations/) to streamline your integration. Kindly refer to our [demo app](https://github.com/singpass/demo-app) for an example of how such libraries may be used.

Whether you choose to use an off-the-shelf client library, or use your own custom integration, you may refer to the subsequent pages to learn more about the Singpass authentication API.


# 1. The Authorization Request

The first step in the Singpass authentication flow is the authorization request. This involves kicking off a Login or Myinfo (v5) transaction by redirecting users to Singpass' login page, while also providing some information about what this transaction is for (e.g. the data you wish to retrieve).

Singpass requires the use of Pushed Authorization Requests (PAR) ([RFC 9126](https://datatracker.ietf.org/doc/html/rfc9126)), so this step actually consists of the following sub-steps:

1. First, send a POST request to our **`pushed_authorization_request_endpoint`** (as defined in our [OpenID configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery)). If successful, you will receive a response containing a `request_uri`.
2. Next, using that `request_uri` and our **`authorization_endpoint`** (also defined in our [OpenID configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery)), construct an authorization URL.
3. Finally, redirect the user to that authorization URL.

More details about these sub-steps are provided below.

## 1. Sending the pushed authorization request

The pushed authorization request is a HTTP POST request that is sent to the pushed authorization request endpoint.

Your request should contain a request body in the `application/x-www-form-urlencoded` format. The request body supports a lot of parameters, which can be divided into several groups: parameters specified by basic OIDC, parameters for PKCE, parameters for DPoP, and Singpass-specific parameters.

### Basic OIDC Parameters

These are parameters that are specified as part of the original OIDC specifications. More information about them can be viewed in the [official specifications](https://openid.net/specs/openid-connect-core-1_0.html).

<table><thead><tr><th width="200.8359375">Parameter</th><th width="327.26953125">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>response_type</code></td><td>The authorization processing flow to be used.</td><td>Only the value <code>code</code> is supported, as mandated by FAPI2.0 specifications.</td></tr><tr><td><code>scope</code></td><td><p>A space-delimited string, representing a list of scopes that you are requesting.</p><p><br>The scopes that you request will determine the data that is returned in the ID token and in the userinfo endpoint.</p></td><td><p>A space-delimited string representing a list of scopes. For Myinfo apps, See our <a href="https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog">Data Catalog</a> for the allowed values.</p><p>For Login apps, there are some basic scopes that are allowed. The scopes are <code>user.identity</code> , <code>name</code>, <code>email</code>, and <code>mobileno</code> . See <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token">Parsing the ID token</a> for more details.</p><p>The <code>openid</code> scope <strong>must</strong> be specified, as per the OIDC specifications.</p></td></tr><tr><td><code>state</code></td><td><p>A session-based, unique, and non-guessable value that you should generate per auth session. This is used to mitigate Cross-Site Request Forgery (CSRF) attacks.</p><p>This parameter should be uniquely generated for each request and set by your backend. The generated value should be persisted in the backend and associated with your user's session, as it will be needed later.<br><br>This string must be generated in a cryptographically secure way, and should ideally be at least 30 characters long. We recommend using a version 4 UUID for this purpose.</p></td><td>Optional. A string with a maximum length of 255 characters. It must match the regular expression pattern <code>[A-Za-z0-9/+_-=.]+</code>.</td></tr><tr><td><code>nonce</code></td><td><p>A session-based, unique, and non-guessable value that you should generate per auth session. This is used to mitigate replay attacks.</p><p>Just like the <code>state</code> parameter, this parameter should be uniquely generated for each request and set by your backend. The generated value should be persisted in the backend and associated with your user's session, as it will be needed later.<br><br>This string must be generated in a cryptographically secure way, and should ideally be at least 30 characters long. We recommend using a version 4 UUID for this purpose.</p></td><td><p>Optional. A string with a maximum length of 255 characters.</p><p>We recommend using a randomly-generated version 4 UUID for this purpose.<br></p></td></tr><tr><td><code>client_id</code></td><td>The client ID of your registered client, provided by Singpass during app onboarding. It is the App ID found at the top of your app configuration page</td><td>A 32-character case-sensitive alphanumeric string.</td></tr><tr><td><code>redirect_uri</code></td><td>The URL that Singpass will eventually redirect the user to after the user completes the login process using the Singpass App. The value will be validated against the list of redirect URLs that were pre-registered with Singpass during onboarding.</td><td>URL</td></tr><tr><td><code>acr_values</code></td><td><p>A string indicating your preference on the level of assurance required for this authentication. Multiple values, in descending order of preference, may be provided as a space-delimited string.<br><br>Should multiple valid values be provided, we will use the first available level of assurance for the authentication.<br><br>This parameter is applicable only to specific high risk use cases. It should only be used when a higher assurance level is genuinely required, and such use will need to be whitelisted by us.</p><p><br>If you believe your use case may qualify, please submit a request at <a href="https://partnersupport.singpass.gov.sg/">https://partnersupport.singpass.gov.sg</a> for our review.</p></td><td><p>Optional. The possible values are:</p><ul><li><p>urn:singpass:authentication:loa:1</p><ul><li>This refers to an assurance level of 1, meaning that only password authentication is required. This value can only be used in the staging environment for testing, and only if it is registered for your app. It cannot be used in production.</li></ul></li><li><p>urn:singpass:authentication:loa:2</p><ul><li>This refers to an assurance level of 2, meaning that only 2FA is required.</li></ul></li><li><p>urn:singpass:authentication:loa:3</p><ul><li>This refers to an assurance level of 3, meaning that face verification as a third factor is required. Note that you will incur charges starting from 1 Jan 2026 should you opt for an assurance level of 3.</li></ul></li></ul></td></tr><tr><td><code>client_assertion_type</code></td><td>The type of client assertion.</td><td>Must be the string <code>urn:ietf:params:oauth:client-assertion-type:jwt-bearer</code>, as mandated by OIDC specifications.</td></tr><tr><td><code>client_assertion</code></td><td>Your client assertion, which is used for authentication. Refer to <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion">Generation of Client Assertion for instructions</a> on how this should be generated.</td><td>A string containing the signed JWT.</td></tr></tbody></table>

### PKCE Parameters

These are parameters used for Proof of Key Code Exchange (PKCE), which is an additional security measure put in place to protect the authorization code against misuse by malicious actors.

Read our [guide on PKCE](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce) to understand what these parameters are for and how to generate the `code_challenge`.

| Parameter               | Description                                                                | Data Type                                                                                |
| ----------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `code_challenge`        | The base64url encoded SHA256 hash of a randomly generated `code_verifier`. | A base64url-encoded string.(note: base64url encoding is not the same as base64 encoding) |
| `code_challenge_method` | The method used to generate the `code_challenge` from the `code_verifier`  | Only the value `S256` is supported, as mandated by FAPI 2.0 specifications               |

### DPoP Parameters

These are parameters used to perform authorization code binding to your DPoP key, which is a further security measure to protect the authorization code against misuse by malicious actors.

| Parameter  | Description                                                                                                                                                    | Data Type |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `dpop_jkt` | The JWK Thumbprint of your proof-of-possession public key. The JWK thumbprint should be computed using the SHA256 hash algorithm, and encoded using base64url. | String    |

Note that `dpop_jkt` is only required if your request does not contain the DPoP header (which contains the DPoP Proof JWT).

For simplicity, we recommend sending the [DPoP header](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) in the request rather than using the `dpop_jkt` request parameter, as you will also need to implement DPoP header generation in later steps.

### Singpass-Specific Parameters

These are parameters which are not part of any standard, but are instead specific to Singpass.

<table><thead><tr><th width="279.65234375">Parameter</th><th>Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>authentication_context_type</code></td><td>A value selected from a predefined list describing the type of transaction that your user is performing the authentication for. This will be used for anti-fraud purposes.</td><td><p><strong>Mandatory and only allowed for Login apps</strong>,</p><p>The list of possible values is provided <a href="#possible-authentication_context_type-values">below</a>.</p></td></tr><tr><td><code>authentication_context_message</code></td><td>A string value providing context on what users are performing authentication for. This will be displayed to users when they are performing authentication. For guidance on writing authentication messages, refer <a href="https://partnersupport.singpass.gov.sg/hc/en-sg/articles/54859616559769-What-is-Authentication-Context-Message">here</a>. All messages are subject to audit and compliance monitoring.</td><td><p>String, with a maximum length of 100 characters.</p><p>Accepts all printable ASCII characters except <code>&#x3C;</code>, <code>></code>, <code>\</code>, and <code>`</code> (backtick).</p><p>Optional, and <strong>allowed only for Login apps.</strong></p></td></tr><tr><td><code>redirect_uri_https_type</code></td><td>This value describes the type of redirect that you intend to perform. You should specify this as <code>app_claimed_https</code> if you are performing a redirection to a mobile app via an App-claimed https URL.</td><td><p>Either <code>app_claimed_https</code> or <code>standard_https</code>.</p><p>This field is optional; it defaults to <code>standard_https</code> if not provided.</p></td></tr><tr><td><code>app_launch_url</code></td><td>This value is only required if your authentication journey starts and ends for an iOS mobile app. This should be an iOS App Link which will bring the user back to your application after they complete authentication on the Singpass app.</td><td>Optional. <em>only applicable for iOS mobile app integration</em></td></tr></tbody></table>

<details>

<summary>Sample request (Myinfo)</summary>

{% code %}

```http
POST /fapi/par HTTP/1.1
Host: stg-id.singpass.gov.sg
Accept-Charset: ISO-8859-1
DPoP: eyJhbGciOiJFUzI1NiIsImp3ayI6eyJhbGciOiJFUzI1NiIsImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ1c2UiOiJzaWciLCJ4IjoiV2REWGw2SDVjb1g4WjByTDk3UjduMG9KYWpKUXhrRmhXTTVNRzdTZlhnQSIsInkiOiJZeThhcFZRdkVxVDM0ZzhKSDVYUzRIcFBXbTBOMURCaFVMcU5lT3FtTUdJIn0sInR5cCI6ImRwb3Arand0In0.eyJleHAiOjE3NzA3MjE2ODIsImh0bSI6IlBPU1QiLCJodHUiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2cvZmFwaS9wYXIiLCJpYXQiOjE3NzA3MjE1NjIsImp0aSI6ImRjMjYzNDVmLTYzNDEtNGJkYi1hMmVjLTUwZWE4YzRhOGNmMCJ9.QFCtwt8D1VSVEmBuFhHFec7Ii_f981nlIB2s-P-jbHdJR7F22p5r8RC7-lWOExn3vNBmFSP_KGUgo_XIcfhTMw
Content-Type: application/x-www-form-urlencoded
Content-Length: 1037

response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fcallback&client_id=dNGEOSUjyJjTqytbxsspyJAyQIj3tyha&scope=openid%20name%20nationality%20noa&state=5bfda4b1-f67b-4f3c-bbbc-6ca81461fb5a&nonce=5e652418-2373-47f7-8003-43f062244046&code_challenge=52TX5w33iX1u5XEZRmq5IGhZwlajZVVyvdO5ZTqIH6o&code_challenge_method=S256&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJFUzI1NiIsImtpZCI6InNpZy0yMDI0IiwidHlwIjoiSldUIn0.eyJhdWQiOiJodHRwczovL3NpbmdwYXNzLmdvdi5zZyIsImV4cCI6MTc3MDcyMTY4MiwiaWF0IjoxNzcwNzIxNTYyLCJpc3MiOiJkTkdFT1NVanlKalRxeXRieHNzcHlKQXlRSWozdHloYSIsImp0aSI6IjhiMGJkY2E1LTgxNWEtNDI5OC1hZTJlLThjNGQ3NDU0NjM0ZSIsInN1YiI6ImROR0VPU1VqeUpqVHF5dGJ4c3NweUpBeVFJajN0eWhhIn0.qLAv2f6twnoIRR1VOMs5w3daRStOrznH7guJT-yIfRTtK0RB_iFSpgJAOQ4sSKMl7k5pSyIlNWpqMhZTKSeFIA
```

</details>

<details>

<summary>Sample request (Login)</summary>

```http
POST /fapi/par HTTP/1.1
Host: stg-id.singpass.gov.sg
Accept-Charset: ISO-8859-1
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiRTRhOHp0NTZuMnF3WmE3R1ZPdVV4SHMtUHNQWVIzYnVCNGhtcURyTnV3OCIsInkiOiJWQ3ktckFmN3dMOC1PeWlhdS1kS0dJdmN5THpTMHJULTFlQkxyTGVNM09NIn19.eyJqdGkiOiJmMTM3MzgyYS02MjUwLTQxMjUtYjc5NC0yY2Y2OGRlZTljMzAiLCJodG0iOiJQT1NUIiwiaHR1IjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkvcGFyIiwiaWF0IjoxNzcwODA1ODM5LCJleHAiOjE3NzA4MDU5NTl9.DNeFnNXvmxGr5ZZW9o6mfVoG9uCRbgXxRgyhXWlED0xpkV1uSmNTVSA4QA_VVUNjLEgufNXzRqg7vqeyUyQ6nw
Content-Type: application/x-www-form-urlencoded
Content-Length: 965

response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fcallback&client_id=asC7y1wuFmqwCXys6S5EnaILNcy4yJDx&scope=email%20mobileno%20name%20openid%20user.identity&state=b24a1eae-e01b-4856-affd-3098b9fe0fe8&nonce=e9d4d941-99c4-4db1-90d2-1d77906e3a65&code_challenge=52TX5w33iX1u5XEZRmq5IGhZwlajZVVyvdO5ZTqIH6o&code_challenge_method=S256&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhc0M3eTF3dUZtcXdDWHlzNlM1RW5hSUxOY3k0eUpEeCIsInN1YiI6ImFzQzd5MXd1Rm1xd0NYeXM2UzVFbmFJTE5jeTR5SkR4IiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkiLCJpYXQiOjE3NzA4MDU4MzksImV4cCI6MTc3MDgwNTk1OSwianRpIjoiYWZlODg1ZjQtY2FjMC00YmQwLThkMGItMWE3MDkxNzFiMzI1In0.7W_mjPhS6DbvEd32obSany8bqOcrVaS_AvhojjqSHGX6P9OjJUxIdPsjpifO_E8tE3Px-F5egFy2-7nXLLdIFg&authentication_context_type=APP_AUTHENTICATION_DEFAULT&authentication_context_message=Complete%20the%20set%20up%20of%20your%20mobile%20banking%20token
```

</details>

{% hint style="info" %}
The samples above use the **staging** endpoint (`stg-id.singpass.gov.sg`). For production, replace the host with `id.singpass.gov.sg`.
{% endhint %}

#### Possible authentication\_context\_type values

You should select an appropriate `authentication_context_type` value depending on your use case. The possible values for each type of use case are shown below.

<details>

<summary>CPF transactions</summary>

| Event                          | Enum Value                            |
| ------------------------------ | ------------------------------------- |
| Change Payment Mode            | CPF\_CHANGE\_PAYMENT\_MODE            |
| Change daily withdrawal limits | CPF\_CHANGE\_DAILY\_WITHDRAWAL\_LIMIT |
| Profile Update                 | CPF\_PROFILE\_UPDATE                  |
| Link to Bank account           | CPF\_LINK\_BANK\_ACCOUNT              |
| Funds transfer                 | CPF\_FUNDS\_TRANSFER                  |

</details>

<details>

<summary>Banking</summary>

| Event                                          | Enum Value                                      |
| ---------------------------------------------- | ----------------------------------------------- |
| CASA opening                                   | BANK\_CASA\_OPENING                             |
| CASA Initial usage                             | BANK\_CASA\_INITIAL\_USAGE                      |
| Debit/Credit Card application                  | BANK\_CARD\_APPLICATION                         |
| Debit/Credit Card initial usage                | BANK\_CARD\_INITIAL\_USAGE                      |
| Loan Application                               | BANK\_LOAN\_APPLICATION                         |
| Successful addition of local recipient         | BANK\_ADD\_LOCAL\_RECIPIENT                     |
| Successful addition of overseas recipient      | BANK\_ADD\_OVERSEAS\_RECIPIENT                  |
| Increase transfer limit                        | BANK\_INCREASE\_TRANSFER\_LIMIT                 |
| Report Fraud or suspicious activity            | BANK\_REPORT\_FRAUD\_SUSPICIOUS\_ACTIVITY       |
| Funds transfer                                 | BANK\_FUNDS\_TRANSFER\_LOCAL                    |
| Remit money overseas                           | BANK\_REMIT\_MONEY\_OVERSEAS                    |
| Report lost cards                              | BANK\_REPORT\_LOST\_CARD                        |
| Change of notification method                  | BANK\_CHANGE\_NOTIFICATION\_METHOD              |
| Increase credit card limit                     | BANK\_INCREASE\_CREDIT\_CARD\_LIMIT             |
| Cash advance                                   | BANK\_REQUEST\_CASH\_ADVANCE                    |
| Increased inflow and outflow of funds transfer | BANK\_INCREASE\_INFLOW\_OUTFLOW                 |
| Activation of a dormant account                | BANK\_ACTIVATE\_DORMANT\_ACCOUNT                |
| Login using a new device                       | BANK\_LOGIN\_NEW\_DEVICE                        |
| Login from an unfamiliar IP                    | BANK\_LOGIN\_UNFAMILIAR\_IP                     |
| User Information Update                        | BANK\_UPDATE\_USER\_INFORMATION                 |
| New device registration                        | BANK\_NEW\_DEVICE\_REGISTRATION                 |
| Unlock money lock                              | BANK\_UNLOCK\_MONEY\_LOCK                       |
| Google Pay / Apple Pay card onboarding         | BANK\_GOOGLE\_PAY\_APPLE\_PAY\_CARD\_ONBOARDING |

</details>

<details>

<summary>Other Financial Institutions</summary>

| Event                     | Enum Value                      |
| ------------------------- | ------------------------------- |
| Account Opening           | FI\_ACCOUNT\_OPENING            |
| Link Bank account         | FI\_LINK\_BANK\_ACCOUNT         |
| Increase transfer limit   | FI\_INCREASE\_TRANSFER\_LIMIT   |
| Increase withdrawal limit | FI\_INCREASE\_WITHDRAWAL\_LIMIT |
| Initiate Deposit          | FI\_INITIATE\_DEPOSIT           |

</details>

<details>

<summary>Telcos</summary>

| Event                         | Enum Value                          |
| ----------------------------- | ----------------------------------- |
| SIM card application          | TELCO\_SIM\_CARD\_APPLICATION       |
| Activation of SIM card        | TELCO\_SIM\_CARD\_ACTIVATION        |
| Change of account details     | TELCO\_CHANGE\_ACCOUNT\_DETAILS     |
| Activate Roaming              | TELCO\_ACTIVATE\_ROAMING            |
| Change of notification method | TELCO\_CHANGE\_NOTIFICATION\_METHOD |

</details>

<details>

<summary>Others</summary>

| Event                  | Enum Value                              |
| ---------------------- | --------------------------------------- |
| General authentication | APP\_AUTHENTICATION\_DEFAULT            |
| Making a payment       | APP\_PAYMENT\_DEFAULT                   |
| Password Change        | APP\_ACCOUNT\_PASSWORD\_CHANGE\_DEFAULT |
| Password Reset         | APP\_ACCOUNT\_PASSWORD\_RESET\_DEFAULT  |
| Account Details Change | APP\_ACCOUNT\_DETAILS\_CHANGE\_DEFAULT  |
| App onboarding         | APP\_ONBOARDING\_DEFAULT                |

</details>

### Response

#### Successful Response

If the request was successful, you will receive a response in JSON format which contains the following parameters:

| Parameter     | Description                                                                                                 | Data type                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `request_uri` | This is a reference to the payload that you have sent in this request. This will be needed in the next step | String                                      |
| `expires_in`  | This is a number, in seconds, representing the lifetime of the `request_uri`                                | Number. We set this value to be 60 seconds. |

<details>

<summary>Sample successful response body</summary>

```json
{
  "request_uri": "urn:ietf:params:oauth:request_uri:Tku8lLFs7d_UPZznhREj0",
  "expires_in": 60
}
```

</details>

#### Error Response

If there was a problem with the request, you will receive a response in JSON format which will instead contain these parameters:

<table><thead><tr><th width="164.765625">Parameter</th><th width="404.29296875">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>error</code></td><td>An error code identifying the type of error that has occurred.</td><td>This will be an enum value. The possible values are detailed <a href="#possible-error-values">below</a>.</td></tr><tr><td><code>error_description</code></td><td>A human-readable text description of the error.</td><td>String. This is optional.</td></tr><tr><td><code>error_uri</code></td><td>URI of a web page that includes additional information about the error</td><td>URL. This is optional.</td></tr><tr><td><code>state</code></td><td>This will be the same state parameter passed in the authorization request.</td><td>A string with a maximum length of 255 characters. It must match the regular expression pattern <code>[A-Za-z0-9/+_-=.]+</code></td></tr></tbody></table>

<details>

<summary>Sample error response body</summary>

```json
{
  "error": "invalid_request",
  "error_description": "The request is missing a required parameter, includes an unsupported value, or is malformed.",
  "state": "e32b9f28-5d34-4c0f-8b0e-6b670566c97f"
}
```

</details>

#### Possible error values

The table below lists the possible values of `error` that we may return:

<table><thead><tr><th width="237.33203125">error</th><th>What this error indicates</th></tr></thead><tbody><tr><td><code>invalid_request</code></td><td>The request had missing or invalid parameters. You should ensure that all the parameters follow the specifications listed above. This error will also be returned if you did not send either the <code>DPoP</code> header or the <code>dpop_jkt</code> parameter.</td></tr><tr><td><code>invalid_client</code></td><td><p>This error may occur if your client assertion could not be verified. This is most commonly caused by a malformed JWKS, or an incorrectly generated client assertion.</p><p>Refer to our guides on <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion">client assertions</a> and <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks">JWKS</a>, and make sure that your implementation follows both of these guides.<br><br>This can also be caused by an invalid <code>client_id</code> being passed. Check that your <code>client_id</code> is correct, and that your app is currently active.</p></td></tr><tr><td><code>invalid_scope</code></td><td>The <code>scope</code> parameter that you have provided is invalid. This is typically caused if you did not include the <code>openid</code> scope, or if you are requesting for a scope which your app is not allowed to request.<br><br>If requesting for a new scope, you will need to <a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app">edit your app</a> and add the new scope into the list of your app's allowed scopes.</td></tr><tr><td><code>invalid_dpop_proof</code></td><td>The <code>DPoP</code> header which you have provided is invalid, expired, or malformed. Read our <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop">DPoP guide</a> and ensure that your implementation follows the instructions in the guide.</td></tr><tr><td><code>server_error</code></td><td>The server encountered an unexpected error. You should check <code>error_description</code> to understand what was the cause of the error. You may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods.</td></tr><tr><td><code>upstream_dependency_error</code></td><td><p>This error can potentially be caused by your JWKS endpoint not being reachable. Read our guide on <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks#requirements-for-jwks">JWKS</a> and ensure that you follow the requirements. In particular, your JWKS endpoint must be publicly accessible and should respond in a timely manner.</p><p>If the cause was not your JWKS endpoint, you may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods.</p></td></tr><tr><td><code>temporarily_unavailable</code></td><td>The server is temporarily unavailable to handle the request. You may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods, or to guide them to try again some time later.</td></tr></tbody></table>

## 2. Redirecting the user to the authorization URL

After you complete the pushed authorization request, the next step is to redirect the user to open the authorization URL in their browser.

The base URL for the authorization URL can be located as the `authorization_endpoint` field in our authorization server's [OpenID Configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery). You will only need to attach two query parameters to the authorization endpoint to form the authorization URL:

| Parameter     | Description                                                                                                                                                                                                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`   | <p>The client ID of your registered client, provided by Singpass during app onboarding. It is the App ID found at the top of your app configuration page.<br></p><p>This must be the same client ID that you passed in the request body of the pushed authorization request.</p> |
| `request_uri` | The `request_uri` returned by the pushed authorization request.                                                                                                                                                                                                                  |

Once you have redirected the user to the authorization URL, the next step would be to wait for the user to complete authentication. Once they complete authentication, they will be redirected back to the `redirect_uri` that you specified. View the next page to understand how to handle the redirect.

{% hint style="warning" %}
**Configure your session timeout to accommodate the authentication period.** After redirecting the user to Singpass, your application should maintain their login session while authentication is in progress. Users have up to 10 minutes to complete the authentication flow before being redirected back to your `redirect_uri`, so your application's session timeout should be configured to accommodate this.

If your application also supports Corppass, additional time may be required for the user to complete UEN selection after authentication.
{% endhint %}

<details>

<summary>Sample authorization URL</summary>

```url
https://id.singpass.gov.sg/fapi/auth?client_id=T5sM5a53Yaw3URyDEv2y9129CbElCN2F&request_uri=urn:ietf:params:oauth:request_uri:Tku8lLFs7d_UPZznhREj0
```

</details>


# 2. Handling the Redirect

Once the user has completed authentication on Singpass, we will redirect the user to the `redirect_uri` that you have specified in your authorization request.

Depending on whether the authentication was successful or not, the query parameters attached to the URL will be different.

## Failed Authentication

If the user failed to authenticate, or if an error occurred, we may return an Authentication Error Response, as specified in [section 3.1.2.6 of the OIDC specifications](https://openid.net/specs/openid-connect-core-1_0.html#AuthError). The URL will contain the following query parameters:

<table><thead><tr><th width="164.765625">Parameter</th><th width="458.14453125">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>error</code></td><td>An error code identifying the type of error that has occurred.</td><td>This will be an enum value. The possible values are detailed <a href="#possible-error-values">below</a>.</td></tr><tr><td><code>error_description</code></td><td>A human-readable text description of the error.</td><td>String. This is optional.</td></tr><tr><td><code>error_uri</code></td><td>URI of a web page that includes additional information about the error</td><td>URL. This is optional.</td></tr><tr><td><code>state</code></td><td>This will be the same state parameter passed in the authorization request.</td><td>A string with a maximum length of 255 characters. It must match the regular <kbd>expression</kbd> pattern <code>[A-Za-z0-9/+_-=.]+</code></td></tr><tr><td><code>iss</code></td><td>The issuer identifier of the Singpass authorization server (See the <code>issuer</code> field in the <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery">OpenID Discovery Endpoint</a>). Both success and failure response redirects will contain this parameter. For security, it is recommended that clients verify this value against the expected Singpass issuer before acting on the response.</td><td>URL</td></tr></tbody></table>

<details>

<summary>Sample URL for Authentication Error Response</summary>

{% code overflow="wrap" %}

```
https://partner.gov.sg/redirect?error=invalid_request_uri&error_description=The%20request_uri%20provided%20is%20invalid&state=e32b9f28-5d34-4c0f-8b0e-6b670566c97f&iss=https%3A%2F%2Fid.singpass.gov.sg/fapi
```

{% endcode %}

</details>

If you receive an Authentication Error Response, you should display an error page to your users. You may also display different content on your error pages depending on the `error` parameter. However, you should not display `error` or `error_description` verbatim on your web page in order to prevent [content spoofing](https://owasp.org/www-community/attacks/Content_Spoofing) attacks.

#### Possible error values

The table below lists the possible values of the `error` query parameter that we may return.

<table><thead><tr><th width="218.87109375">error</th><th>What this error indicates</th></tr></thead><tbody><tr><td><code>server_error</code></td><td>The server has encountered an unexpected error. You should guide the user to perform a retry.</td></tr><tr><td><code>temporarily_unavailable</code></td><td>The server is temporarily unavailable to handle the request. You should guide users to alternative authentication methods, or to guide them to try again some time later.</td></tr></tbody></table>

## Successful Authentication

As per the OIDC specification, when the authentication is successful, the URL that the user is redirected to will contain three additional query parameters:

<table><thead><tr><th width="121.1015625">Parameter</th><th width="458.14453125">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>code</code></td><td>The authorization code. This will be used in a later step to obtain the user's ID token and access token.</td><td>A base64url-encoded string.</td></tr><tr><td><code>state</code></td><td>This will be the same state parameter passed in the authorization request.</td><td>A string with a maximum length of 255 characters. It must match the regular expression pattern <code>[A-Za-z0-9/+_-=.]+</code></td></tr><tr><td><code>iss</code></td><td>The issuer identifier of the Singpass authorization server (See the <code>issuer</code> field in the <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery">OpenID Discovery Endpoint</a>). Both success and failure response redirects will contain this parameter. For security, it is recommended that clients verify this value against the expected Singpass issuer before acting on the response.</td><td>URL</td></tr></tbody></table>

<details>

<summary>Sample URL for successful authentication</summary>

{% code overflow="wrap" %}

```
https://partner.gov.sg/redirect?code=XcyzlSeX1hIyJFlstxsSF_UeXC5DtiYkFgJ8VVx52mg&state=e32b9f28-5d34-4c0f-8b0e-6b670566c97f&iss=https%3A%2F%2Fid.singpass.gov.sg/fapi
```

{% endcode %}

</details>

Upon redirect, your application's backend should check the `state` parameter provided and ensure that it is the same as the `state` which you have sent in the Pushed Authorization Request. This is an important measure to guard against CSRF attacks.

{% hint style="info" %}
If you are using a [certified OIDC Relying Party library](https://openid.net/developers/certified-openid-connect-implementations/), this check will be automatically performed by the library if you have configured it to do so.
{% endhint %}

Once you have completed this check, you may proceed to perform token exchange to obtain the ID token and access token.


# 3. The Token Request

The next step in the Singpass authentication flow is the token request. This involves making a POST request to our **`token_endpoint`** (as defined in our [OpenID configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery)) to exchange an authorization code (obtained from the redirect URL) for an ID token and access token.

## Request Body

You should send the request body in `application/x-www-form-urlencoded` format. The [DPoP header](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) containing the DPoP JWT proof should also be included in your request.

The request body should have the following parameters:

<table><thead><tr><th width="199.28515625">Parameter</th><th>Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>redirect_uri</code></td><td>The <code>redirect_uri</code> which you had used earlier when making the Authorization request.</td><td>URL</td></tr><tr><td><code>grant_type</code></td><td>The grant being requested.</td><td>Must be the string <code>authorization_code</code>, as mandated by OIDC specifications.</td></tr><tr><td><code>code</code></td><td>The authorization code issued by us, obtained via redirection back to your <code>redirect_url</code> in the previous step.</td><td>A base64url-encoded string.</td></tr><tr><td><code>client_assertion_type</code></td><td>The type of client assertion.</td><td>Must be the string <code>urn:ietf:params:oauth:client-assertion-type:jwt-bearer</code>, as mandated by OIDC specifications.</td></tr><tr><td><code>client_assertion</code></td><td>Your client assertion, which is used for authentication. Refer to our <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion">guide</a> for instructions on how this should be generated.</td><td>A string containing the signed JWT.</td></tr><tr><td><code>code_verifier</code></td><td>The code verifier which you have generated when constructing your authorization request. This is used as part of <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce">PKCE</a>.</td><td>String containing only alphanumeric characters, dashes, and underscores, between 43-128 characters long.</td></tr></tbody></table>

<details>

<summary>Sample request</summary>

{% code overflow="wrap" %}

```http
POST /fapi/token HTTP/1.1
Host: stg-id.singpass.gov.sg
Content-Type: application/x-www-form-urlencoded
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7ImNydiI6IlAtMjU2Iiwia3R5IjoiRUMiLCJ4IjoiRTRhOHp0NTZuMnF3WmE3R1ZPdVV4SHMtUHNQWVIzYnVCNGhtcURyTnV3OCIsInkiOiJWQ3ktckFmN3dMOC1PeWlhdS1kS0dJdmN5THpTMHJULTFlQkxyTGVNM09NIn19.eyJqdGkiOiJiZmM5NWRmOS02NDVjLTQ4OTUtOTM5MS03OWFjMGYzMzI0YWEiLCJodG0iOiJQT1NUIiwiaHR1IjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkvdG9rZW4iLCJpYXQiOjE3NzA4MDU5MzMsImV4cCI6MTc3MDgwNjA1M30.ofhxMZLOme4Q5cQXii7bRyucH5A-xFUNJ0vJMlYSHacsV2oHyZJ2SWBsXXpsB4xHkzdwWamNldqoNZ-90-DYoA

grant_type=authorization_code&redirect_uri=http%3A%2F%2Flocalhost%3A3001%2Fcallback&code_verifier=-gMZo7Qjn113fE6Ri_OGnycEV3idiSkvbFcWIaQyQYQ&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer&client_assertion=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhc0M3eTF3dUZtcXdDWHlzNlM1RW5hSUxOY3k0eUpEeCIsInN1YiI6ImFzQzd5MXd1Rm1xd0NYeXM2UzVFbmFJTE5jeTR5SkR4IiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkiLCJpYXQiOjE3NzA3OTEzMTgsImV4cCI6MTc3MDc5MTQzOCwianRpIjoiODJmMzE2MmYtMjMwNS00ZmRkLTk5MjUtZWJiZGY0ZTgzNjIxIn0.OoUXyRpjT3zismetrSerQwAD7zi5NnODnINDRjDnuYovVof1tOoU3B-JtQ7HqpLBypUfb147gWjwUsSA2F54XA&code=4C0sivAY9mUdYL9C3V6tccx38FdX7-4grP_ZRbhgNCI

```

{% endcode %}

</details>

{% hint style="info" %}
The sample above uses the **staging** endpoint (`stg-id.singpass.gov.sg`). For production, replace the host with `id.singpass.gov.sg`.
{% endhint %}

## Response Body

### Successful Response

If the request was successful. we will return a response in `application/json` format which includes the following parameters:

<table><thead><tr><th width="143.640625">Parameter</th><th width="359.60546875">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>access_token</code></td><td><p>This is an encoded JWT that can be used to obtain user information using the UserInfo endpoint.</p><p><br>For Login applications, you should parse the ID token directly instead of using this access token. Refer to the "<a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token">4. Parsing the ID Token</a>" section for guidance.</p><p><br>This access token has a lifetime of 30 minutes.</p></td><td>String</td></tr><tr><td><code>id_token</code></td><td>The encrypted ID token in JWT format, signed by us. More information on how to parse this ID token is available in the next page.</td><td>String</td></tr><tr><td><code>token_type</code></td><td>The type of token being requested.</td><td>This will always be <code>DPoP</code>, as mandated by FAPI 2.0 specifications.</td></tr><tr><td><code>expires_in</code></td><td><p>The lifetime of the access token, in seconds, counted from the time this response was generated.</p><p>This refers to the access token only, not the ID token. The ID token carries its own expiry in its exp claim.</p><p>For example, a value of 1800 means the access token expires in 30 minutes</p></td><td><p>Number.</p><p>This parameter may not be returned in every environment yet. Do not rely on its presence. If it is absent, treat the access token lifetime as 30 minutes, as described for <code>access_token</code> above.</p></td></tr></tbody></table>

<details>

<summary>Sample successful response body</summary>

{% code overflow="wrap" %}

```json
{
    "id_token": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiJlbmMtMjAyNCIsImVwayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6ImdwM2RVdWc5OWYwYTNoN0xxQzRqZllkQkVBbEtvamlTMkVlQmRXbE1idEUiLCJ5IjoiQlBCaFdkMmFEUjhiSWdaZ0RxQUp5VE96R0hRX2s5cjhqMGtiRFJyNkdRZyJ9fQ.9vW4Y2c4K3bTGGdviOKyCmeU-_akIhBxRYcfE8ZVHAWu_PIcO-wOOqjARbp2pE3nMfvDBK0-1spmIA-LKBWO-I2TMe0_Eijg.7vzyv750dzEXuY2kBCVw6g.bQscx4K2J2WQrRxc--xGP2nAcdPw_bxpdUuAUB7KLZouPNIA70E528ttni7DPbC4ek7zv8ZHZfIgMc6SPQr_b8BvPTcq1Zz4_yc3q4ouVPyra41iMZvPhHf3dB3kdDvLoeLx3HTP-Tilxp2OQGCO1pqC8KDAKEnhJK6E-8XUBlSjsyeSlPwFjK7t4mdQ_hCM19M0C2mAB9lg8vWeGs_Hj55lyKvPXdg9fWIFSBaPrsaYaG9urO_EkswkHrkxVz3LfIRsu2irIx-AtM4Hf_PQAKwhbY55vXoYC3H18vFcK61i_5nyP0t2D_XgfONIZVGJaM_FbEW1DSvs1j8EPMgif8uv9Tdf0lgmMHzu75znKkKkz4bZQg_Srmtr8j3Smz7Tg4X4o0rdrNspeNsx-G1dJENjMLCUJdvejAlql7uFa1AVm13uGsaD8wSaDuvQcFSqlCxOqMLQulbBwNCEr-FRFDFn1sqIDzFS6G25bE_mfQ2aumx7VLAHihRYu9xHGBgLJpKFIoGU5OEV-yOGkGNFVtnR3CubVuCKAFyiJ-jZnE33x56a5xy2cApUK3gZkPZf9ovMnpiu7Lb9wFcFsiO2EzAs3xp7LbUaaEH9VhVXxMHP2qKFr9ww71_xQRvZvGoPajO17ErqfNkss3R1l0BzbFAIA-uN4hdOpE2a-LmTnHAgVmeg5u3u6Y3cXUS0Gpi_QG7sTBMbBhtkCKymlg8brZP8MQzkAFKb8OKlxDr-cHB0iytxA7Q9NtK7tBa9pFYYs46bsrU0_XdoUSSxzFBfyicInGVcZd4Es3i07RzxiDSn2Ku72epLGPxteFipYQeebOiONpf3viN6_mDQpSoUOcG72mNxS7pxk8QIC6BoffFVx2Pn8zjf81BHU4S_v_Gs.AyOBe2pNqOeXMTkjlW3WI3X4UUUOot6tDlcYPoF_Z7w",
    "access_token": "eyJhbGciOiJFUzI1NiIsInR5cCI6ImF0K2p3dCIsImtpZCI6ImFsaWFzL3N0Zy1zcC1hdXRoLWFwaS1pZC10b2tlbi1zaWduaW5nLWtleS1rbXMtYXN5bW1ldHJpYy1rZXktYWxpYXMifQ.eyJzdWIiOiIwMjdjNDdjMi02ZGM1LTRiMjItYTgwZi1iYmM1MmM1NzUwNjQiLCJjbGllbnRfaWQiOiJkTkdFT1NVanlKalRxeXRieHNzcHlKQXlRSWozdHloYSIsInNjb3BlIjoib3BlbmlkIHVpbmZpbiBuYW1lIGNoaWxkcmVuYmlydGhyZWNvcmRzLmRvYiBjaGlsZHJlbmJpcnRocmVjb3Jkcy50b2IgZGl2b3JjZWRhdGUgZG9iIGRyaXZpbmdsaWNlbmNlLmRpc3F1YWxpZmljYXRpb24uc3RhcnRkYXRlIGRyaXZpbmdsaWNlbmNlLmRpc3F1YWxpZmljYXRpb24uZW5kZGF0ZSBkcml2aW5nbGljZW5jZS5wZGwuZXhwaXJ5ZGF0ZSBkcml2aW5nbGljZW5jZS5xZGwuZXhwaXJ5ZGF0ZSBkcml2aW5nbGljZW5jZS5yZXZvY2F0aW9uLnN0YXJ0ZGF0ZSBkcml2aW5nbGljZW5jZS5yZXZvY2F0aW9uLmVuZGRhdGUgZHJpdmluZ2xpY2VuY2Uuc3VzcGVuc2lvbi5zdGFydGRhdGUgZHJpdmluZ2xpY2VuY2Uuc3VzcGVuc2lvbi5lbmRkYXRlIGhkYm93bmVyc2hpcC5kYXRlb2Zvd25lcnNoaXB0cmFuc2ZlciBoZGJvd25lcnNoaXAuZGF0ZW9mcHVyY2hhc2UgaGRib3duZXJzaGlwLmxlYXNlY29tbWVuY2VtZW50ZGF0ZSBsdGF2b2NhdGlvbmFsbGljZW5jZXMuYmF2bC5leHBpcnlkYXRlIGx0YXZvY2F0aW9uYWxsaWNlbmNlcy5iZHZsLmV4cGlyeWRhdGUgbHRhdm9jYXRpb25hbGxpY2VuY2VzLm9kdmwuZXhwaXJ5ZGF0ZSBsdGF2b2NhdGlvbmFsbGljZW5jZXMucGR2bC5leHBpcnlkYXRlIGx0YXZvY2F0aW9uYWxsaWNlbmNlcy50ZHZsLmV4cGlyeWRhdGUgbWFycmlhZ2VkYXRlIHBhc3NleHBpcnlkYXRlIHBhc3Nwb3J0ZXhwaXJ5ZGF0ZSBzcG9uc29yZWRjaGlsZHJlbnJlY29yZHMuZG9iIHNwb25zb3JlZGNoaWxkcmVucmVjb3Jkcy5zY3ByZ3JhbnRkYXRlIHZlaGljbGVzLmNvZWV4cGlyeWRhdGUgdmVoaWNsZXMuZmlyc3RyZWdpc3RyYXRpb25kYXRlIHZlaGljbGVzLm9yaWdpbmFscmVnaXN0cmF0aW9uZGF0ZSB2ZWhpY2xlcy5yb2FkdGF4ZXhwaXJ5ZGF0ZSB2ZWhpY2xlcy55ZWFyb2ZtYW51ZmFjdHVyZSBjcGZiYWxhbmNlcy5tYSBjcGZiYWxhbmNlcy5vYSBjcGZiYWxhbmNlcy5yYSBjcGZiYWxhbmNlcy5zYSBjcGZjb250cmlidXRpb25zIGNwZmVtcGxveWVycyIsImp0aSI6ImF0LXZhenRZOU5fYy1HYTBFTkx0ekJVajh2bnVlb2tyazVyTTczRmZ0aHNtZ1kiLCJpYXQiOjE3NzA3MDk1MzIsImV4cCI6MTc3MDcxMTMzMiwiYXVkIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkvdXNlcmluZm8iLCJpc3MiOiJodHRwczovL3N0Zy1pZC5zaW5ncGFzcy5nb3Yuc2cvZmFwaSIsImNuZiI6eyJqa3QiOiJySF84UFJkUnZtWHg5dVNBMjVQTGdZSGJmQ3FMdlNJc1M1Yml3S004RmJvIn19.CVV8zLacj6nigOu-VU13DubRZcIyEvMpyOOF3m4KR8p9Zp_XNcPGRiQCx_Je9wNXFEUHcXZiWvhVfYVE7P5AxA",
    "token_type": "DPoP",
    "expires_in": 1800
}
```

{% endcode %}

</details>

### Error Response

If there was an error with the request, we will instead return a response body in `application/json` format with the following parameters:

<table><thead><tr><th width="164.765625">Parameter</th><th width="404.29296875">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>error</code></td><td>An error code identifying the type of error that has occurred.</td><td>This will be an enum value. The possible values are detailed <a href="#possible-error-values">below</a>.</td></tr><tr><td><code>error_description</code></td><td>A human-readable text description of the error.</td><td>String. This is optional.</td></tr><tr><td><code>error_uri</code></td><td>URI of a web page that includes additional information about the error</td><td>URL. This is optional.</td></tr></tbody></table>

<details>

<summary>Sample error response</summary>

```json
{
  "error": "invalid_request",
  "error_description": "The request is missing a required parameter, includes an unsupported value, or is malformed."
}
```

</details>

#### Possible error values

The table below lists the possible values of `error` that we may return:

<table><thead><tr><th width="251.06640625">error</th><th>What this error indicates</th></tr></thead><tbody><tr><td><code>invalid_request</code></td><td>The request had missing or invalid parameters. You should ensure that all the parameters follow the specifications listed above. This error will also be returned if you did not send the <code>DPoP</code> header in your request.</td></tr><tr><td><code>unsupported_grant_type</code></td><td>This means that you had passed a <code>grant_type</code> value which is not the value <code>authorization_code</code>. You should update your implementation to send <code>grant_type</code> as <code>authorization_code</code>.</td></tr><tr><td><code>invalid_grant</code></td><td><p>This can be caused by any of the following issues:</p><ul><li>The authorization code has expired. You should ensure that token exchange happens within 60 seconds of the authorization code being issued.</li><li>The authorization code has already been used. Each authorization code can only be exchanged once, even if the earlier token request failed. Start a new authorization request to obtain a new authorization code.</li><li>The <code>redirect_uri</code> provided is different from the one which you have sent in the Pushed Authorization Request.</li><li>The <code>code_verifier</code> does not match the <code>code_challenge</code> that you sent in the Pushed Authorization Request. Refer to our <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce">PKCE guide</a>.</li></ul></td></tr><tr><td><code>invalid_client</code></td><td>The <code>client_assertion</code> that you generated was invalid. Read our <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion">guide on client assertions</a> and ensure that your implementation follows the guide. The method to generate the client assertion should be the same as the one used to generate the client assertion for the Pushed Authorization Request.</td></tr><tr><td><code>invalid_dpop_proof</code></td><td>The <code>DPoP</code> header which you have provided is invalid, expired, or malformed. Read our <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop">DPoP guide</a> and ensure that your implementation follows the instructions in the guide.<br><br>This error is also returned if the DPoP key pair used for this token request is different from the one used for the Pushed Authorization Request.</td></tr><tr><td><code>server_error</code></td><td>The server encountered an unexpected error. You should check <code>error_description</code> to understand what was the cause of the error. You may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods.</td></tr><tr><td><code>upstream_dependency_error</code></td><td><p>This error can potentially be caused by your JWKS endpoint not being reachable. Read our guide on <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks#requirements-for-jwks">JWKS</a> and ensure that you follow the requirements. In particular, your JWKS endpoint must be publicly accessible and should respond in a timely manner.</p><p>If the cause was not your JWKS endpoint, you may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods.</p></td></tr><tr><td><code>temporarily_unavailable</code></td><td>The server is temporarily unavailable to handle the request. You may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods, or to guide them to try again some time later.</td></tr></tbody></table>


# 4. Parsing the ID Token

The ID token returned during token exchange is a JSON Web Signature (JWS), which is also encrypted using JSON Web Encryption (JWE). The JWE and JWS components are represented using compact serialization form, as specified in [section 3.1 of RFC 7516](https://datatracker.ietf.org/doc/html/rfc7516#section-3.1).

To reduce complexity, we recommend that you use a JWT parsing library to decrypt the token and to verify the signature, instead of implementing the decryption and signature verification yourself. You may refer to [this list](https://www.jwt.io/libraries?support=verify\&algorithm=es256) to look for a suitable JWT library for your programming language, though you must also ensure that your library of choice supports decryption of JWTs encrypted using JWE.

A sample ID token is shown below:

<details>

<summary>Sample encrypted ID token (this is a JWE)</summary>

{% code overflow="wrap" %}

```
eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiJteS1lbmMta2V5IiwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoidGIza3UwRHNyUTdFdHRkaVplcDVHUGdUOFgxaW5jYmR3M2YwSHB3ZHQ2SSIsInkiOiJEZzRFXzAwaWxGdEliVFhwMGRTcU84YUJTQXJPT3JSVWNOT3hKcFdReFFRIn19.hNnmqs2S9-vYzEXr7-Q9TmrzddUylJx-_n_HLjMWLQgeGECrwnmYPP2P638dQVGnlr_2KhJh6rFrm2wdoofSXv3YQR49zTC9.oEBMccRGsNtmMpbV1Oh6SA.TtYVOpO8cH1FpADKDIf0paepf7U8Rz2I_QYK2zITAk2wtuMuL3A3sUquvAA9a_KSm23F2WQ5vE0lA1qB54m9IYglWmaLT6epUQGw2gpkdQhrQmCuYMll2uvj1G-OV2TZgtLCNZakZY09U5SpSAjS32Sfa3H9iWmzjj8LiMQ_jLKBN-84TJpwiopOHW3b0O4tvEVdIq6bEfzqRjZ9qcqxkeWnyfajOC-NlCeqalXHJ_uRrJmVVRXmMjvMMOi1AEQJgVlyFaxBSvpkZGdXhuRRCv6LR3RK_SKizIDy1IwP0O5P6s4BKPXNaqjMwdoRKJdwB5euOGN3lK2Nh8hnzBO5Mp_lHf5XbbvdQ5oLWYDPRy19m6sSYPUIP4PfEguY7KmgbTjRd1ciptIetsRtQhKtYs6oLFp1hziwfk9AUYhkLN4dphSfamAZQeFct4lG4-Q865NezAupIs1BgTYPEu8q4Bw0-NXm0S0wISOJxmOCVng3h2uH4lqQY_bS7fGu4b8E30_-NWPesfKGc-dtVG3x7S1vEfDqjqnxY6XzzDnJOv-Op4cfjnATX067utxIJF2o9lo_9AG3Cul3xyGk9gx3DwHKImX_ldaJAajosUQQ8XUyuIsRjO_L8fQG2N9bYsKHt9qX2fK8fZGEfKsERw35i9AOifdlWxT5rcDM202zvZl9RGZOLGv3Z9JUfwtgAPKrEn5bXHwP__tefKgo9Ba__UUivtDzNwQE-ZVMoyKWMTKFLrULlfC9PaBO0UbVp4JsTVjcNgEVsLED-Y3rCBjNjehAGVyJxRcKUsngAEUAZJvNjGxaq149-Q6I7X6JOhrofY_8hqc74d4ROrDZ4vun2qVCzmrQmcCakEGpp9Y2wat0I-v7Q05COWWWu4EL_wdtgRnazA0DnH3el8ZUohsqNQ.fh6pMCnKcgo9yodwB5dPKcxdTZftoEmHKkB-KRxZPiI
```

{% endcode %}

</details>

<details>

<summary>Sample decrypted ID token (this is a JWS)</summary>

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFsaWFzL3N0Zy1zcC1hdXRoLWFwaS1pZC10b2tlbi1zaWduaW5nLWtleS1rbXMtYXN5bW1ldHJpYy1rZXktYWxpYXMifQ.eyJpYXQiOjE3Njk3Mzk4MjMsImV4cCI6MTc2OTc0MDQyMywiaXNzIjoiaHR0cHM6Ly9zdGctaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkiLCJzdWIiOiI3YzljNzJlYy01YmUyLTQ5NWEtYTc4ZS02MWU4MDlhMmEyMzYiLCJhdWQiOiJSc3JPeTJpQjBlZFI1M1RKU3VENVVMYWQxcEdtclZaTCIsImFtciI6WyJwd2QiXSwic3ViX2F0dHJpYnV0ZXMiOnsibmFtZSI6Ik5BTUUgT0YgUzU0MTA4MjhBIn0sInN1Yl90eXBlIjoidXNlciIsIm5vbmNlIjoiV2pxVU1NbU9ldllPWG13QzI3bWNBUVdzRkJuM083d3doYlJJdGwyRkprOCIsImFjciI6InVybjpzaW5ncGFzczphdXRoZW50aWNhdGlvbjpsb2E6MSJ9.pI0nhe0BLToMbuZ-9lpQiBNj2sj_ZWJwYFMT83u4yewZupTClPLUeYp08RR_sV2I70H6qpVmydRmoH8R9SipHQ
```

{% endcode %}

</details>

<details>

<summary>Sample decoded ID token payload</summary>

```json
{
  "sub": "7c9c72ec-5be2-495a-a78e-61e809a2a236",
  "aud": "RsrOy2iB0edR53TJSuD5ULad1pGmrVZL",
  "acr": "urn:singpass:authentication:loa:1",
  "sub_type": "user",
  "sub_attributes": { "name": "NAME OF S5410828A" },
  "amr": ["pwd"],
  "iss": "https:\/\/stg-id.singpass.gov.sg\/fapi",
  "exp": 1769740423,
  "iat": 1769739823,
  "nonce": "WjqUMMmOevYOXmwC27mcAQWsFBn3O7wwhbRItl2FJk8"
}
```

</details>

## JWT Claims

The decrypted JWT will have the following claims:

<table><thead><tr><th width="152.11328125">Claim</th><th width="297">Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>sub</code></td><td>The principal that is the subject of the JWT. Contains a globally unique identifier for the user.</td><td>String</td></tr><tr><td><code>sub_type</code></td><td>A property to describe what is the type of the subject of the JWT.</td><td>For Singpass, this is always the string <code>"user"</code></td></tr><tr><td><code>sub_attributes</code></td><td>This contains some information related to the user's identifiers. This is only returned if the <code>user.identity</code> , <code>name</code>, <code>email</code>, or <code>mobileno</code> scope is requested.</td><td>Object containing key-value pairs. See the <a href="#the-sub_attributes-claim">section below</a> for full details.</td></tr><tr><td><code>act</code></td><td>An object describing actor acting on behalf of the <code>sub</code>. This is currently unused, but this may be used in the future for delegation (e.g. a child acting on behalf of their parent, or vice-versa).<br><br>This object will contain a <code>sub</code> claim, which contains the UUID of the actor. If the <code>user.identity</code> , <code>name</code>, <code>email</code>, or <code>mobileno</code> scope is requested, it will also contain the respective data for the actor in the <code>sub_attributes</code> claim.<br><br>If the <code>sub_attributes</code> claim is returned, the format of <code>sub_attributes</code> is described in the <a href="#the-sub_attributes-claim">section below</a>.</td><td>An object containing <code>sub</code> and <code>sub_attributes</code> (if requested).</td></tr><tr><td><code>aud</code></td><td>The client ID of your registered client, provided by Singpass during app onboarding.</td><td>A 32-character case-sensitive alphanumeric string.</td></tr><tr><td><code>iss</code></td><td>The issuer identifier of our authorization server.</td><td>String</td></tr><tr><td><code>iat</code></td><td>The unix timestamp, in seconds, at which we issued this JWT.</td><td>Number</td></tr><tr><td><code>exp</code></td><td>The unix timestamp, in seconds, on or after which this JWT <strong>must not</strong> be accepted for processing.</td><td>Number</td></tr><tr><td><code>amr</code></td><td>An array of authentication method references. This refers to the form factors used by the user to authenticate themselves.<br><br>The array will contain all the form factors used for this authentication. For example, if the user authenticated themselves using their password and SMS OTP, then this array will contain both <code>pwd</code> and <code>otp-sms</code>.</td><td><p>Array of strings. The possible values are:</p><ul><li><code>face</code></li><li><code>pwd</code></li><li><code>otp-sms</code></li><li><code>face-alt</code></li><li><code>swk</code> (software key)</li><li><code>swk-passkey</code></li></ul><p>Note that this list is non-exhaustive, and we reserve the right to introduce new values without prior notice to you.</p></td></tr><tr><td><code>acr</code></td><td>The authentication class reference value used for this transaction. This identifies the level of assurance that this authentication satisfied.</td><td><p>One of the following values:</p><ul><li><p>urn:singpass:authentication:loa:1</p><ul><li>This indicates that only username and password was used for authentication. This will only happen in the staging environment.</li></ul></li><li><p>urn:singpass:authentication:loa:2</p><ul><li>This indicates that 2-factor authentication was used for authentication.</li></ul></li><li><p>urn:singpass:authentication:loa:3</p><ul><li>This indicates that 3-factor authentication, with face verification as a third factor, was used for authentication.</li></ul></li></ul></td></tr><tr><td><code>nonce</code></td><td>This is the same nonce that you used in your authorization request.</td><td>String</td></tr></tbody></table>

<details>

<summary>Sample ID token</summary>

```json
{
  "aud": "gnY6Erichpb5t4NFRP9R4L7aEC9N0FQH",
  "iss": "https://id.singpass.gov.sg/fapi",
  "exp": 1727322545,
  "iat": 1727321945,
  "nonce": "L5nmQfcetDDIeincoqvCrFyGv+nHobkv4XocNYPCXaQ=",
  "sub": "1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9",
  "sub_type": "user",
  "sub_attributes": {
    "account_type": "standard",
    "identity_number": "S1234567G",
    "identity_coi": "SG"
  }
}
```

</details>

## The sub\_attributes Claim

The `sub_attributes` claim is an object that will contain the following properties:

<table><thead><tr><th width="151.4296875">Property</th><th>Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>account_type</code></td><td><p>The Singpass account type for this user.</p><p>For Singpass Foreign Account (SFA) holders, this will be <code>"foreign"</code>.</p><p>For all other Singpass accounts (i.e. those belonging to Singapore Citizens, Permanent Residents, or FIN holders), this will be <code>"standard"</code>.</p></td><td>A string, which is either <code>"foreign"</code> or <code>"standard"</code>. This is only present if the <code>user.identity</code> scope was requested.</td></tr><tr><td><code>identity_number</code></td><td>A string which contains a referenceable identifier for the user.<br><br>For Singapore Citizens and Permanent residents, this will be their NRIC.<br><br>For FIN holders, this will be their FIN.<br><br>For Singpass Foreign Account holders, this will be their foreign ID.</td><td>String. This is only present if the <code>user.identity</code> scope was requested.</td></tr><tr><td><code>identity_coi</code></td><td>The country code for the of issuance of the identity.<br><br>For Singapore Citizens, Permanent Residents, and FIN holders, this will be <code>"SG"</code>.<br><br>For Singpass Foreign Account holders, this will be the country code of the country which issued the user's foreign ID.</td><td>2-letter country code. This is only present if the <code>user.identity</code> scope was requested.</td></tr><tr><td><code>name</code></td><td>The user's principal name</td><td>Non-empty string. This will only be present if the <code>name</code> scope is requested.</td></tr><tr><td><code>email</code></td><td>The user's email address</td><td>String. This will only be present if the <code>email</code> scope is requested, and if the user has an email registered with Singpass.</td></tr><tr><td><code>mobileno</code></td><td>The user's mobile number. This will always be a Singapore mobile number, and it will not include the country code.</td><td>Numeric string. This will only be present if the <code>mobileno</code> scope is requested, and if the user has a mobile number registered with Singpass.<br><br>For Singpass Foreign Account (SFA) users, this will always be absent.</td></tr></tbody></table>

<details>

<summary>Sample sub_attributes for Singapore Citizen, Permanent Resident, or FIN holder</summary>

```json
"sub_attributes": {
  "account_type": "standard",
  "identity_number": "S1234567G",
  "identity_coi": "SG",
  "name": "John Doe",
  "email": "johndoe@gmail.com",
  "mobileno": "91231234",
}
```

</details>

<details>

<summary>Sample sub_attributes for Singpass Foreign Account holder</summary>

```json
"sub_attributes": {
  "account_type": "foreign",
  "identity_number": "K28394589",
  "identity_coi": "TK",
  "name": "Larry Doe",
  "email": "larrydoe@gmail.com",
}
```

</details>

## Verification Checks

{% hint style="info" %}
If you are using a [certified OIDC Relying Party library](https://openid.net/developers/certified-openid-connect-implementations/), these checks will be automatically performed by the library, though you must pass the nonce to the library for it to perform the nonce check.
{% endhint %}

In order to ensure that the ID token is valid, you must perform the following checks:

1. Verify that the `iss` claim matches the issuer identifier of our authorization server, which you can obtain from the `issuer` field in the [OpenID configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery) of our authorization server.
2. Verify that the `aud` claim matches your client ID.
3. Ensure that the current time is before the timestamp in the `exp` claim.
4. Ensure that the `nonce` claim is the same as the nonce that you had sent in the authorization request.

If you are integrating with Singpass Login, then the flow ends here. If you are integrating with Myinfo (v5), then the next and final step would be to retrieve the user's information using the `/userinfo` endpoint.


# 5. The Userinfo Request

{% hint style="info" %}
This step is applicable only to Myinfo (v5) apps.
{% endhint %}

The final step in the Singpass authentication flow is the userinfo request. This involves making a GET request to our `userinfo_endpoint` (as defined in our [OpenID configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery)) to retrieve user information. To do this, you will need an access token (obtained from a successful token request)

The endpoint will only return information based on the scopes that you have requested when making the authorization request.

## Request

Just like the authorization request and token request, you will need to include the [DPoP header](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) when making the `/fapi/userinfo` request. You will also need to include your access token in the `Authorization` header. The access token should be prefixed with `DPoP` , as shown in the sample request below.

No query parameters are required for this request.

{% hint style="warning" %}
The DPoP proof for the userinfo request **must** include the `ath` claim (the base64url-encoded SHA-256 hash of the access token). It must also set `htu` to the full userinfo endpoint URL (`https://id.singpass.gov.sg/fapi/userinfo` for production). The DPoP sample below is illustrative and does not include `ath`.
{% endhint %}

<details>

<summary>Sample request</summary>

{% code overflow="wrap" %}

```http
GET /fapi/userinfo HTTP/1.1
Host: id.singpass.gov.sg
Authorization: DPoP eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJzdWIiOiJ1c2VyLWphbmUtZG9lIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vZGF0YSIsImV4cCI6MTc1NjczMDM4MCwiaWF0IjoxNzI1MTk0MzgwLCJqdGkiOiJ0eC0xMjMtYWJjIiwiY25mIjp7ImprdCI6Ik93SWlGaVl2T0NXRkpiV1hlbUdUZzRtU1NYQkNwZk9NaFhRV21XOTBVSEEifX0.dGhpcy1pcy1hLXBsYWNlaG9sZGVyLXNpZ25hdHVyZS1hcy1pdC1yZXF1aXJlcy1hLXByaXZhdGUta2V5
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiQXNWakh4elZ4MURaNnNKcEpzUnM2ek5YYXFmcFR3UmNfcXV0bWw0aEFJQSIsInkiOiI0SkhwVVZDRE5DaXhOTW9OclIzSElodFRzTWNfMF9NcmdpMzJxR3VoUkQ4In19.eyJqdGkiOiIyZmM3Y2Q4ZC0xN2IzLTRlYTUtYTg4ZC1lZWM0NTY5M2JhZDQiLCJodG0iOiJHRVQiLCJodHUiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy91c2VyaW5mbyIsImlhdCI6MTc1NjcwODI0N30.wBYjFQRzY2o5aG82LjR1X8qT9bZ-jK3c7hI5fE0gP9vR_7sU6tW5xV4yZ3aB2cE1dF0eG9hI8jJ7kL6mN5oP4qR
```

{% endcode %}

</details>

## Response

### Successful Response

The response body of a successful response will contain a JSON Web Signature (JWS), which is also encrypted via JSON Web Encryption (JWE), represented in compact serialization form. This is the same encryption and signature scheme that was used in our ID token encryption, so you can decrypt and verify the response in exactly the same manner.

The decrypted (and decoded) response is a JSON object with the following fields:

<table><thead><tr><th width="157.6640625">Field</th><th>Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>person_info</code></td><td>The personal data of the user. The information returned in this field depends on the scopes that were requested in your authorization request.</td><td>A JSON object that follows the <a href="https://public.cloud.myinfo.gov.sg/myinfo/api/myinfo-kyc-v4.0.html#operation/getperson">Myinfo Get Person response</a>. You can also download the OpenAPI specifications for this property below.</td></tr><tr><td><code>iss</code></td><td>The issuer identifier of our authorization server. This is identical to the <code>iss</code> returned in the ID token.</td><td>String</td></tr><tr><td><code>iat</code></td><td>The unix timestamp at which we issued this JWT.</td><td>Number</td></tr><tr><td><code>sub</code></td><td>The principal that is the subject of the JWT. Contains a globally unique identifier for the user. This is identical to the <code>sub</code> returned in the ID token.</td><td>String</td></tr><tr><td><code>aud</code></td><td>The client ID of your registered client, provided by Singpass during app onboarding.</td><td>A 32-character case-sensitive alphanumeric string.</td></tr></tbody></table>

The specifications for the `person_info` property is also available in [OpenAPI format](#person-information-openapi-specification)

The examples below show how the response would look like if `openid uinfin name` were the requested scopes.

<details>

<summary>Sample encrypted response (this is a JWE)</summary>

<pre data-overflow="wrap"><code><strong>eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiRUNESC1FUytBMjU2S1ciLCJraWQiOiJ0ZXN0LXJwLWtleS0wMSIsImVwayI6eyJrdHkiOiJFQyIsImNydiI6IlAtMjU2IiwieCI6Ik1RVTBWRnlfUWFUYktzTmJrVTdMZkFnUjJ2Y1FQYW94UzBXM2RLRm9yOU0iLCJ5IjoibkdRam5PRlZ4emdzRERjMUJqQ3otZi1KeUY4VC14WW0xQVp4NjFtZWVCOCJ9fQ.gDvjBmkLqQ42hbNM2ULPwaskGPBlLvslPAqr0XcN2a-OYqOHXKfwvoUUOuoibTfzg_l8rr-WalvY8FY_a8yfHOaL2GLt6ZWj.O_tgtrTbPRbL_p0Y2rvnCQ.38npNWj1nL1AQxS2A3JrxokxHms6GPYT2OFhaFghI7N0QkR48gPuUvKi-m7wPbESTYA-9O-bSHEX9fUXD4FtlztrhjRTpGmdfppooVMn9_bHcLLyHbHnS3_yW5JaybqHNfD6zXCB1pw24vvHfGmRJ7C86CeBgosuYslMk7y7m_rIT6YhVnotN_kRBOppVW9eC3g0upRxXQJ3O10__pR-QcBb_eXKqwm6tcpeTEqBPl0Dbedk6DDoq6KSRV5LzyFLMutAjInQpKGdWYa7FCgfHL3FWNfcwyPq27s3d14ArZJVkIJsOW_VTI_lrnSBzCcdJpbGj9wPe0e2SfslliZlSxYTTpECyV5AZZgwxz0pMaE85Ob7KzrJjMdbZqZZC53HnZmq6pS8RiUce4950IwvsfF0xDUDaZuMxKnISoPcuUX2jHr8FG0SytO8Pr6m3DyOYbQnSkUFdjCRSHiKRqDxlqM15hSkle3jtd9qf-EzuGeHNqaJCjD7XWeviwJgD70fUZDM8lDvCp5mTfl0pcy7mlGEWjVmfR3MB1ohGwkZLeq3H_KrCyhn_FJ-DRPiE4oIaO8oSsFOhRocND4RDlliOIRK_B1XRmw1YpJFBRpn04N2ytnJrxCJ4cZeTEa4QCYkKaJHPqWkN_qvdgxywkwELLB5Tb1sgdKcq3Kh77uHWl7AfZF9iE1L-kgg4hT5KaJSp4qEYz-nbb4TqmrsnZiPbjnzSFrOGZ778OpDWnXhbb5VcXk9ZjejEdBtoqnIJ_vubEWTw-ZeMI4fCmNuiZ4HnY130VKfnU2f19GSNYaeL7GX7bVQWVS_H01mbll6_GUe.g7la6rSFevvuUrEoqVb41SQB1dk4JuTkrl8zwE0fzG4
</strong></code></pre>

</details>

<details>

<summary>Sample decrypted response (this is a JWS)</summary>

{% code overflow="wrap" %}

```
eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFsaWFzL3N0Zy1zcC1hdXRoLWFwaS1pZC10b2tlbi1zaWduaW5nLWtleS1rbXMtYXN5bW1ldHJpYy1rZXktYWxpYXMifQ.eyJwZXJzb25faW5mbyI6eyJ1aW5maW4iOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiUzkwMDAwMDFCIn0sIm5hbWUiOnsibGFzdHVwZGF0ZWQiOiIyMDI0LTA5LTI2Iiwic291cmNlIjoiMSIsImNsYXNzaWZpY2F0aW9uIjoiQyIsInZhbHVlIjoiU09IIEhBTyBGRU5HIn19LCJpc3MiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy9mYXBpIiwic3ViIjoiZDQ1ZDhmMjEtNjE3OC00NzEzLWI5NjItODYzNWVkMmE5NDVhIiwiYXVkIjoiVDVzTTVhNTNZYXczVVJ5REV2Mnk5MTI5Q2JFbENOMkYiLCJpYXQiOjE3NDY2NzgwODl9.Tmvh5V_BN0fMBgqa2-Z4vG_Ayp_OoeWfyQrWMZjG9y9NBFwyRnjMpwDK_qFzkn_0D7AjOX-np6p3Nk5KFwvKiA
```

{% endcode %}

</details>

<details>

<summary>Sample decoded response payload</summary>

```json
{
  "person_info": {
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
    }
  },
  // above scopes are returned in the same format as the Myinfo Get Person response
  "iss": "https://id.singpass.gov.sg/fapi",
  "sub": "d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "iat": 1746678089
}
```

</details>

### Person Information OpenAPI Specification

This OpenAPI YAML file provides the full technical specification for Myinfo person data fields and scopes. It helps developers understand what information can be retrieved from Myinfo and how each field is structured.

The specification includes:

* Available Myinfo data scopes and attributes
* Field names and descriptions
* Value types (e.g. string, number, array, object)
* Maximum field lengths and formatting requirements
* Accepted values and validation rules
* Example API responses
* Government verification indicators
* Display and implementation guidance

Developers may refer to this specification to understand:

* What are the value types and maximum lengths for each field
* What information is returned for each Myinfo scope
* How nested objects and arrays are structured
* Which fields are editable or government-verified
* The expected response format for Myinfo APIs

This serves as the technical reference for applications integrating with Myinfo APIs.

{% file src="/files/tRmLbgT0M1yZWXE4OtbS" %}

## The Person object

```json
{"openapi":"3.1.0","info":{"title":"Myinfo v5","version":"2026-09-30"},"components":{"schemas":{"Person":{"title":"Person","type":"object","description":"Person details","properties":{"academicqualifications":{"description":"Academic qualifications achieved.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"certificates":{"description":"Electronic certificates uploaded.","items":{"additionalProperties":false,"properties":{"content":{"properties":{"value":{"type":"string"}},"type":"object","description":"File content of the electronic certificate, Base64 encoded."},"name":{"properties":{"value":{"type":"string"}},"type":"object","description":"File name of the electronic certificate."},"opencertificate":{"properties":{"id":{"properties":{"value":{"type":"string"}},"type":"object"},"primary":{"properties":{"value":{"type":"boolean"}},"type":"object"}},"type":"object","description":"Open Certificate Information.\n\nNote: The test environment for OpenCert is at https://dev.opencerts.io/\nwhile production is at https://opencerts.io/"},"opencertificateindicator":{"properties":{"value":{"type":"boolean"}},"type":"object","description":"Indicate whether this file is open certificate."}},"type":"object"},"type":["array","null"]},"transcripts":{"description":"Transcript of qualification.","items":{"properties":{"explanatorynotes":{"description":"Explanatory Notes. For an example, see https://public.cloud.myinfo.gov.sg/myinfo/spm/seab-explanatory-notes/SEAB_Cert_A.html","properties":{"value":{"type":"string"}},"type":"object"},"name":{"description":"Qualification's Name.","properties":{"value":{"type":"string"}},"type":"object"},"results":{"description":"Array of results for the qualification.","items":{"properties":{"grade":{"description":"Grade attained.","properties":{"value":{"type":"string"}},"type":"object"},"level":{"description":"Level of subject taken.","properties":{"value":{"type":"string"}},"type":"object"},"subgrade":{"description":"Optional grade attained for subSubject.","properties":{"value":{"type":"string"}},"type":"object"},"subject":{"description":"Subject taken.","properties":{"value":{"type":"string"}},"type":"object"},"subsubject":{"description":"Optional Sub Subject taken.","properties":{"value":{"type":"string"}},"type":"object"}},"title":"SSGResult","type":"object"},"type":"array"},"yearattained":{"description":"Year this qualification was attained. See \"date-fullyear\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","properties":{"value":{"pattern":"[0-9]{4}","type":"string"}},"type":"object"}},"type":"object"},"type":["array","null"]}}}]},"aliasname":{"description":"Alias name of the Person","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":66,"type":"string"}}}]},"birthcountry":{"description":"Country/Place of Birth of Person.\n\nRefer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}}}]},"chas":{"description":"Community Health Assist Scheme (CHAS) card details - Card Type, Date of Issue, Date of Expiry","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"cardtype":{"properties":{"code":{"enum":["A","B","C","NA"],"type":"string"},"desc":{"type":"string"}},"type":"object","description":"CHAS Card Type."},"expirydate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"CHAS Expiry Date. Value of data field in YYYY-MM-DD format.\nSee \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"indicator":{"properties":{"code":{"enum":["PGA","PGB","PGC","MGA","MGB","MGC","PG","MG","A","B","C","NA"],"type":"string"},"desc":{"type":"string"}},"type":"object","description":"CHAS Indicator."},"issuedate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"CHAS Issue Date. Value of data field in YYYY-MM-DD format.\nSee \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"name":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Full Name of the Person."}}}]},"childrenbirthrecords":{"description":"This refers to only local registered birth records (based on ICA’s electronic Birth Certificate Records from 1985 onwards).\nThis includes adoption of locally registered child.\nFor child below 21, the child’s Birth Cert No, Name, Sex, Race, Dialect, Date of Birth and Time of Birth will be shown.\nFor child above 21, only the child’s Birth Cert Number will be shown.","items":{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"aliasname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Alias name of child.\n\nPresentation Logic - If there is a value to aliasname (i.e. not empty), then aliasname should be\ndisplayed in a new line below hanyupinyinname, and prefixed with the '@' symbol i.e. '@aliasname'."},"birthcertno":{"properties":{"value":{"maxLength":15,"type":"string"}},"type":"object","description":"Birth certificate number of child."},"dialect":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Dialect of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"dob":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object","description":"Date of Birth of child."},"hanyupinyinaliasname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Han Yu Pin Yin Alias name of child.\n\nPresentation Logic - If there is a value to hanyupinyinaliasname (i.e. not empty), then\nhanyupinyinaliasname should be displayed in a new line below aliasname, and prefixed with\nthe '@' symbol i.e. \"@hanyupinyinaliasname\"."},"hanyupinyinname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Han Yu Pin Yin name of child.\n\nPresentation Logic - If there is a value to hanyupinyinname (i.e. not empty), then hanyupinyinname\nshould be displayed in a new line below name, and formatted with round brackets\ni.e. \"(hanyupinyinname)\"."},"lifestatus":{"properties":{"code":{"enum":["A","D",""],"type":"string"},"desc":{"enum":["ALIVE","DECEASED",""],"type":"string"}},"type":"object","description":"Life Status of child. Possible values:\n\n- A - ALIVE\n- D - DECEASED"},"marriedname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Married name of child.\n\nPresentation Logic - If there is a value to marriedname (i.e. not empty),\nthen marriedname should be displayed in a new line below hanyupinyinaliasname."},"name":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Full Name of child."},"race":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Race of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"secondaryrace":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Secondary Race of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"sex":{"properties":{"code":{"description":"The 1-character code for the sex.\n\n- 'F': FEMALE\n- 'M': MALE\n- 'U': UNKNOWN\n- '': No Data Yet","enum":["F","M","U",""],"maxLength":1,"type":"string"},"desc":{"description":"The full description of the sex.","enum":["FEMALE","MALE","UNKNOWN",""],"type":"string"}},"type":"object","description":"Sex of child."},"sgcitizenatbirthind":{"properties":{"value":{"enum":["Y","N",""],"type":"string"}},"type":"object","description":"Indicates whether the child is a Singapore Citizen at the time of birth. Possible values:\n\n- Y - YES\n- N - NO\n- < BLANK > - Not applicable"},"tob":{"properties":{"value":{"description":"Format: HHMM","maxLength":4,"type":"string"}},"type":"object","description":"Time of Birth of child."},"vaccinationrequirements":{"items":{"additionalProperties":false,"properties":{"fulfilled":{"properties":{"value":{"type":"boolean"}},"type":"object"},"requirement":{"properties":{"code":{"type":"string"},"desc":{"type":"string"}},"type":"object","description":"Vaccination Requirement.\nRefer to the Code reference tables in the Support section for list of possible values."}},"type":"object"},"type":["array","null"]}}}]}},"countryofmarriage":{"description":"Country/Place of the latest marriage.\nNote: This field must be made editable on your digital service form even though\nsource is '1' (Government Verified).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"description":"The 2-character country code.","maxLength":2,"type":"string"},"desc":{"description":"The full name of the country.","maxLength":300,"type":"string"}}}]},"cpfbalances":{"description":"CPF Balances of Person in SGD.","properties":{"ma":{"description":"Amount Balance in CPF-MA.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"format":"double","type":"number","description":"Value of CPF-MA balance."}}}]},"oa":{"description":"Amount Balance in CPF-OA.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"format":"double","type":"number","description":"Value of CPF-OA balance."}}}]},"ra":{"description":"Amount Balance in CPF-RA.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"format":"double","type":"number","description":"Value of CPF-RA balance."}}}]},"sa":{"description":"Amount Balance in CPF-SA.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"format":"double","type":"number","description":"Value of CPF-SA balance."}}}]}},"type":"object"},"cpfcontributions":{"description":"Employer CPF Contributions of Person in SGD. Does not include any non-employer contributions. Maximum past 15 months' of contributions.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"history":{"items":{"properties":{"amount":{"description":"Amount of contribution in SGD.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"date":{"description":"Date of Contribution Paid. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","properties":{"value":{"format":"date","type":"string"}},"type":"object"},"employer":{"description":"Employer who paid the Contribution.","properties":{"value":{"maxLength":100,"type":"string"}},"type":"object"},"month":{"description":"Month for which CPF Contribution was paid. Format: YYYY-MM","properties":{"value":{"maxLength":7,"type":"string"}},"type":"object"}},"title":"ContributionsHistory","type":"object"},"type":"array"}}}]},"cpfemployers":{"description":"Employers who paid CPF Contributions. Maximum up to past 14 months.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"history":{"items":{"properties":{"employer":{"description":"Employer who paid the Contribution.","properties":{"value":{"maxLength":100,"type":"string"}},"type":"object"},"month":{"description":"Month for which CPF Contribution was paid. Format: YYYY-MM","properties":{"value":{"maxLength":7,"pattern":"^\\d{4}-\\d{2}$","type":"string"}},"type":"object"}},"title":"EmployersHistory","type":"object"},"type":"array"}}}]},"cpfhousingwithdrawal":{"description":"CPF Housing Withdrawal information.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"withdrawaldetails":{"items":{"properties":{"accruedinterestamt":{"description":"Accrued interest amount.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"address":{"description":"Registered Address of Person (including FIN holders).\n\nNote:\n- Address can be either a Singapore address (type: 'SG') or non Singapore address (type: 'UNFORMATTED').\n- May be unavailable for some FIN holders.","anyOf":[{"properties":{"block":{"allOf":[{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object"}],"description":"Block/House of Address."},"building":{"allOf":[{"properties":{"value":{"maxLength":65,"type":"string"}},"type":"object"}],"description":"Building of Address."},"country":{"allOf":[{"properties":{"code":{"default":"SG","maxLength":2,"type":"string"},"desc":{"default":"SINGAPORE","type":"string"}},"type":"object"}],"description":"Country/Place of Address. For AddressSG this will always be 'SG'."},"floor":{"allOf":[{"properties":{"value":{"maxLength":3,"type":"string"}},"type":"object"}],"description":"Floor of Address."},"postal":{"allOf":[{"properties":{"value":{"maxLength":6,"type":"string"}},"type":"object"}],"description":"Postal Code of Address."},"street":{"allOf":[{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object"}],"description":"Street of Address."},"type":{"default":"SG","description":"Type of Address (SG or UNFORMATTED for non SG).","enum":["SG"],"type":"string"},"unit":{"allOf":[{"properties":{"value":{"maxLength":5,"type":"string"}},"type":"object"}],"description":"Unit of Address."}},"title":"SG","type":"object"},{"properties":{"line1":{"type":"object","description":"Unregistered Foreign address line 1","properties":{"value":{"type":"string","maxLength":66}}},"line2":{"type":"object","description":"Unregistered Foreign address line 2","properties":{"value":{"type":"string","maxLength":66}}},"type":{"default":"UNFORMATTED","description":"Type of Address (SG or UNFORMATTED for non SG).","enum":["UNFORMATTED"],"type":"string"}},"title":"UNFORMATTED","type":"object"}]},"monthlyinstalmentamt":{"description":"Monthly instalment amount.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"principalwithdrawalamt":{"description":"Principal withdrawal amount.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"totalamountofcpfallowedforproperty":{"description":"Total amount of CPF allowed for the property.","properties":{"value":{"format":"double","type":"number"}},"type":"object"}},"title":"WithdrawalDetails","type":"object"},"type":"array"}}}]},"cpfinvestmentscheme":{"description":"CPF Investment Scheme.","properties":{"account":{"description":"Account Details.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"agentbankcode":{"description":"Agent Bank Code.","properties":{"value":{"type":"string"}},"type":"object"},"invbankacctno":{"description":"Account Number.","properties":{"value":{"type":"string"}},"type":"object"}}}]},"saqparticipationstatus":{"description":"Self-Awareness Questionnaire (SAQ) Participation Status.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"description":"Possible values:\n- 'Y': Participated\n- 'X': Existing CPFIS participant\n- 'N': Did not participate","enum":["Y","X","N"],"type":"string"},"desc":{"type":"string"}}}]},"sdsnetshareholdingqty":{"description":"Number of Discounted Singtel Shares.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"type":"integer"}}}]}},"type":"object"},"dialect":{"description":"Dialect of Person.\n\n  Refer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}}}]},"divorcedate":{"description":"Last Divorce Date of Person.\nNote: This field must be made editable on your digital service form even though\nsource is '1' (Government Verified).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}}}]},"dob":{"description":"Date of Birth of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["value"],"properties":{"value":{"description":"Value of data field. Format can be one of the below (with reference to https://datatracker.ietf.org/doc/html/rfc3339#section-5.6):\n\n- full-date (YYYY-MM-DD)\n- date-fullyear \"-\" date-month (YYYY-MM)\n- date-fullyear (YYYY)","type":"string","format":"date"}}}]},"drivinglicence":{"description":"Driving Licence details of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"comstatus":{"properties":{"code":{"enum":["Y","N",""],"maxLength":1,"type":"string"},"desc":{"enum":["ELIGIBLE","NOT ELIGIBLE",""],"type":"string"}},"type":"object","description":"Status of Certificate of Merit. Possible values:\n\n- 'Y': ELIGIBLE\n- 'N': NOT ELIGIBLE\n- '': No data yet"},"disqualification":{"properties":{"enddate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"End date"},"startdate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Start date"}},"type":"object","description":"Disqualification date"},"pdl":{"properties":{"classes":{"description":"Licence Classes. Includes Issue Date(e.g. 2B, 2018-01-01)","items":{"properties":{"class":{"properties":{"value":{"maxLength":3,"type":"string"}},"type":"object"},"issuedate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object"}},"type":"object"},"type":["array","null"]},"expirydate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Licence Expiry Date"},"validity":{"properties":{"code":{"type":"string"},"desc":{"type":"string"}},"type":"object","description":"Validity of QDL. Possible values:\n\n- 'V': VALID\n- 'E': EXPIRED\n- 'I': INVALID\n- 'N': NOT HOLDING\n- '': No data yet"}},"type":"object","description":"Provisional Driving Licence (PDL)"},"photocardserialno":{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object","description":"Serial Number of the Photo Card"},"qdl":{"properties":{"classes":{"description":"Licence Classes. Includes Issue Date(e.g. 2B, 2018-01-01)","items":{"properties":{"class":{"properties":{"value":{"maxLength":3,"type":"string"}},"type":"object"},"issuedate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object"}},"type":"object"},"type":["array","null"]},"expirydate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Licence Expiry Date"},"validity":{"properties":{"code":{"type":"string"},"desc":{"type":"string"}},"type":"object","description":"Validity of QDL. Possible values:\n\n- 'V': VALID\n- 'E': EXPIRED\n- 'I': INVALID\n- 'N': NOT HOLDING\n- '': No data yet"}},"type":"object","description":"Qualified Driving Licence (QDL)"},"revocation":{"properties":{"enddate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"End date"},"startdate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Start date"}},"type":"object","description":"Revocation date"},"suspension":{"properties":{"enddate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"End date"},"startdate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Start date"}},"type":"object","description":"Suspension date"},"totaldemeritpoints":{"properties":{"value":{"maxLength":2,"type":"integer"}},"type":"object","description":"Total Demerit Points"}}}]},"email":{"description":"Email Address of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":320,"type":"string"}}}]},"employment":{"description":"Name of Employer.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":124,"type":"string"}}}]},"employmentsector":{"description":"Employment Sector of a FIN holder.\n\nNote: Only applies to a foreigner with a valid work pass.\n\nSome examples of possible values are:\n- MANUFACTURING\n- CONSTRUCTION\n- RECLAMATION\n- SERVICE\n- GRI-TECHNOLOGY\n- LANDSCAPING\n- INCINERATOR PLANT\n- MARINE SHIPYSHIPYARD\n- PROCESS\n- HARBOURCRAFT\n- DOMESTIC","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"type":"string"}}}]},"hanyupinyinaliasname":{"description":"Han Yu Pin Yin Alias name of the Person.\n\nPresentation Logic - If there is a value to hanyupinyinaliasname (i.e. not empty),\nthen hanyupinyinaliasname should be displayed in a new line below aliasname,\nand prefixed with the '@' symbol i.e. \"@hanyupinyinaliasname\".","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":66,"type":"string"}}}]},"hanyupinyinname":{"description":"Han Yu Pin Yin name of the Person.\n\nPresentation Logic - If there is a value to hanyupinyinname (i.e. not empty),\nthen hanyupinyinname should be displayed in a new line below name, and\nformatted with round brackets i.e. \"(hanyupinyinname)\"","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":66,"type":"string"}}}]},"hdbownership":{"description":"HDB Ownership details.","items":{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"address":{"description":"Address details (Singapore Format).","properties":{"block":{"allOf":[{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object"}],"description":"Block/House of Address."},"building":{"allOf":[{"properties":{"value":{"maxLength":65,"type":"string"}},"type":"object"}],"description":"Building of Address."},"country":{"allOf":[{"properties":{"code":{"default":"SG","maxLength":2,"type":"string"},"desc":{"default":"SINGAPORE","type":"string"}},"type":"object"}],"description":"Country/Place of Address. For AddressSG this will always be 'SG'."},"floor":{"allOf":[{"properties":{"value":{"maxLength":3,"type":"string"}},"type":"object"}],"description":"Floor of Address."},"postal":{"allOf":[{"properties":{"value":{"maxLength":6,"type":"string"}},"type":"object"}],"description":"Postal Code of Address."},"street":{"allOf":[{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object"}],"description":"Street of Address."},"type":{"default":"SG","description":"Type of Address (SG or UNFORMATTED for non SG).","enum":["SG"],"type":"string"},"unit":{"allOf":[{"properties":{"value":{"maxLength":5,"type":"string"}},"type":"object"}],"description":"Unit of Address."}},"title":"SG","type":"object"},"balanceloanrepayment":{"properties":{"months":{"properties":{"value":{"format":"int64","maximum":99,"type":"integer"}},"type":"object"},"years":{"properties":{"value":{"format":"int64","maximum":99,"type":"integer"}},"type":"object"}},"type":"object"},"dateofownershiptransfer":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object"},"dateofpurchase":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object"},"hdbtype":{"description":"HDB Ownership details.","type":"object","properties":{"code":{"enum":["111","112","113","114","115","116","118"],"type":"string"},"desc":{"enum":["1-ROOM FLAT (HDB)","2-ROOM FLAT (HDB)","3-ROOM FLAT (HDB)","4-ROOM FLAT (HDB)","5-ROOM FLAT (HDB)","EXECUTIVE FLAT (HDB)","STUDIO APARTMENT (HDB)"],"type":"string"}}},"leasecommencementdate":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object"},"loangranted":{"properties":{"value":{"format":"double","type":"number"}},"type":"object"},"monthlyloaninstalment":{"properties":{"value":{"format":"double","type":"number"}},"type":"object"},"noofowners":{"properties":{"value":{"format":"int64","maximum":9,"type":"integer"}},"type":"object"},"originalloanrepayment":{"properties":{"value":{"format":"int64","maximum":99,"type":"integer"}},"type":"object"},"outstandinginstalment":{"properties":{"value":{"format":"double","type":"number"}},"type":"object"},"outstandingloanbalance":{"properties":{"value":{"format":"double","type":"number"}},"type":"object"},"purchaseprice":{"properties":{"value":{"format":"double","type":"number"}},"type":"object"},"termoflease":{"properties":{"value":{"format":"int64","maximum":99,"type":"integer"}},"type":"object"}}}]},"type":["array","null"]},"hdbtype":{"description":"Flat Type of the HDB flat.\nNote 1: that this excludes Rental Flats, Pre-War SIT flat, PSA flat, HUDC flat,\nExecutive Condominium and Shophouse.\nNote 2: If housingtype is available, this value will be blank.\nNote 3: If housingtype & hdbtype are unavailable, make this field user editable.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"enum":["111","112","113","114","115","116","118",""],"type":"string"},"desc":{"enum":["1-ROOM FLAT (HDB)","2-ROOM FLAT (HDB)","3-ROOM FLAT (HDB)","4-ROOM FLAT (HDB)","5-ROOM FLAT (HDB)","EXECUTIVE FLAT (HDB)","STUDIO APARTMENT (HDB)",""],"type":"string"}}}]},"housingtype":{"description":"Housing Type of Person (non-HDB only).\nNote 1: If hdbtype is available, this value will be blank.\nNote 2: If housingtype & hdbtype are unavailable, make this field user editable.\nRefer to hdbtype for detailed HDB type.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"enum":["121","122","123","131","132","139",""],"type":"string"},"desc":{"enum":["DETACHED HOUSE","SEMI-DETACHED HOUSE","TERRACE HOUSE","CONDOMINIUM","EXECUTIVE CONDOMINIUM","APARTMENT",""],"type":"string"}}}]},"ltavocationallicences":{"description":"LTA vocational licence.","properties":{"bavl":{"description":"Bus Attendant's vocational licence.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","title":"LTAVocationalLicence","properties":{"expirydate":{"description":"Expiry date of the LTA Vocational Licence.","properties":{"value":{"format":"date","type":"string"}}},"licencename":{"description":"Licence Name of LTA Vocational Licence.","properties":{"value":{"type":"string"}}},"status":{"description":"Status of the LTA Vocational Licence.","properties":{"code":{"enum":["ACT","ACTIVE"],"type":"string"},"desc":{"type":"string"}}},"vocationallicencenumber":{"description":"Unique Vocational Licence Number for the licence holder.","properties":{"value":{"type":"string"}}}}}]},"bdvl":{"description":"Bus driver's vocational licence.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","title":"LTAVocationalLicence","properties":{"expirydate":{"description":"Expiry date of the LTA Vocational Licence.","properties":{"value":{"format":"date","type":"string"}},"type":"object"},"licencename":{"description":"Licence Name of LTA Vocational Licence.","properties":{"value":{"type":"string"}},"type":"object"},"status":{"description":"Status of the LTA Vocational Licence.","properties":{"code":{"enum":["ACT","ACTIVE"],"type":"string"},"desc":{"type":"string"}},"type":"object"},"vocationallicencenumber":{"description":"Unique Vocational Licence Number for the licence holder.","properties":{"value":{"type":"string"}},"type":"object"}}}]},"odvl":{"description":"Omnibus driver's vocational licence.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","title":"LTAVocationalLicence","properties":{"expirydate":{"description":"Expiry date of the LTA Vocational Licence.","properties":{"value":{"format":"date","type":"string"}},"type":"object"},"licencename":{"description":"Licence Name of LTA Vocational Licence.","properties":{"value":{"type":"string"}},"type":"object"},"status":{"description":"Status of the LTA Vocational Licence.","properties":{"code":{"enum":["ACT","ACTIVE"],"type":"string"},"desc":{"type":"string"}},"type":"object"},"vocationallicencenumber":{"description":"Unique Vocational Licence Number for the licence holder.","properties":{"value":{"type":"string"}},"type":"object"}}}]},"pdvl":{"description":"Private Hire Car driver's vocational licence.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","title":"LTAVocationalLicence","properties":{"expirydate":{"description":"Expiry date of the LTA Vocational Licence.","properties":{"value":{"format":"date","type":"string"}},"type":"object"},"licencename":{"description":"Licence Name of LTA Vocational Licence.","properties":{"value":{"type":"string"}},"type":"object"},"status":{"description":"Status of the LTA Vocational Licence.","properties":{"code":{"enum":["ACT","ACTIVE"],"type":"string"},"desc":{"type":"string"}},"type":"object"},"vocationallicencenumber":{"description":"Unique Vocational Licence Number for the licence holder.","properties":{"value":{"type":"string"}},"type":"object"}}}]},"tdvl":{"description":"Taxi driver's vocational licence.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","title":"LTAVocationalLicence","properties":{"expirydate":{"description":"Expiry date of the LTA Vocational Licence.","properties":{"value":{"format":"date","type":"string"}},"type":"object"},"licencename":{"description":"Licence Name of LTA Vocational Licence.","properties":{"value":{"type":"string"}},"type":"object"},"status":{"description":"Status of the LTA Vocational Licence.","properties":{"code":{"enum":["ACT","ACTIVE"],"type":"string"},"desc":{"type":"string"}},"type":"object"},"vocationallicencenumber":{"description":"Unique Vocational Licence Number for the licence holder.","properties":{"value":{"type":"string"}},"type":"object"}}}]}},"type":"object"},"marital":{"description":"Marital Status of Person.\nNote: This field must be made editable on your digital service form even though source\nis '1' (Government Verified).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"description":"The code for the marital status.\n\n- '1': SINGLE\n- '2': MARRIED\n- '3': WIDOWED\n- '5': DIVORCED\n- '': No data yet","enum":["1","2","3","5",""],"type":"string"},"desc":{"description":"The full description of the marital status.","enum":["SINGLE","MARRIED","WIDOWED","DIVORCED",""],"type":"string"}}}]},"marriagecertno":{"description":"Certificate number of the latest marriage.\nNote: This field must be made editable on your digital service form even though\nsource is '1' (Government Verified).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field.","maxLength":50,"type":"string"}}}]},"marriagedate":{"description":"Latest Marriage Date of Person.\nNote: This field must be made editable on your digital service form even\nthough source is '1' (Government Verified).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}}}]},"marriedname":{"description":"Married name of the Person.\n\nPresentation Logic - If there is a value to marriedname (i.e. not empty),\nthen marriedname should be displayed in a new line below hanyupinyinaliasname.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":66,"type":"string"}}}]},"merdekagen":{"description":"Merdekagen details.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"eligibility":{"description":"Eligibility.","properties":{"value":{"type":"boolean"}},"type":"object"}}}]},"mobileno":{"description":"Mobile Number of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"areacode":{"properties":{"value":{"default":"65","description":"Area Code of Phone Number. Default to '65'.","maxLength":3,"type":"string"}},"type":"object"},"nbr":{"properties":{"value":{"description":"Phone Number.","maxLength":12,"type":"string"}},"type":"object"},"prefix":{"properties":{"value":{"default":"+","description":"Prefix of Phone Number. Defaults to '+'.","maxLength":1,"type":"string"}},"type":"object"}}}]},"name":{"description":"Full Name of the Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["value"],"properties":{"value":{"minLength":1,"maxLength":66,"type":"string"}}}]},"nationality":{"description":"Nationality/Citizenship of Person.\n\n  Refer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["code","desc"],"properties":{"code":{"pattern":"^[A-Z]{2}$","type":"string"},"desc":{"maxLength":300,"type":"string"}}}]},"noa":{"description":"Detailed breakdown of the latest Notice of Assessment (NOA) within the past three years.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"amount":{"description":"Total Assessable Income from the latest NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"category":{"description":"Type of 'Notice of Assessment' (NOA).","properties":{"value":{"enum":["ADDITIONAL","AMENDED","ORIGINAL","REPAYMENT"],"type":"string"}},"type":"object"},"employment":{"description":"Assessable Income from employment for the latest NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"interest":{"description":"Assessable Income from interest for the latest NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"rent":{"description":"Assessable Income from rent for the latest NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"taxclearance":{"description":"Tax Clearance indicator.","properties":{"value":{"enum":["Y","N"],"maxLength":1,"type":"string"}},"type":"object"},"trade":{"description":"Assessable Income from trade for the latest NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"yearofassessment":{"description":"The year of assessment (YYYY) for the latest NOA.","properties":{"value":{"maxLength":4,"pattern":"[0-9]{4}","type":"string"}},"type":"object"}}}]},"noa-basic":{"description":"Summary of latest Notice of Assessment within the past three years.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"amount":{"description":"The assessable income amount from the latest Notice of Assessment.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"yearofassessment":{"description":"The year of assessment (YYYY) for the latest Notice of Assessment.","properties":{"value":{"maxLength":4,"pattern":"[0-9]{4}","type":"string"}},"type":"object"}}}]},"noahistory":{"description":"Detailed breakdown of latest 2 Notice of Assessments within the past three years.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"noas":{"items":{"properties":{"amount":{"description":"Total Assessable Income for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"category":{"description":"Type of 'Notice of Assessment' (NOA) for this historical NOA.","properties":{"value":{"enum":["ADDITIONAL","AMENDED","ORIGINAL","REPAYMENT"],"type":"string"}},"type":"object"},"employment":{"description":"Assessable Income from employment for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"interest":{"description":"Assessable Income from interest for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"rent":{"description":"Assessable Income from rent for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"taxclearance":{"description":"Tax Clearance indicator for this historical NOA.","properties":{"value":{"enum":["Y","N"],"maxLength":1,"type":"string"}},"type":"object"},"trade":{"description":"Assessable Income from trade for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"yearofassessment":{"description":"The year of assessment (YYYY) for this historical NOA.","properties":{"value":{"maxLength":4,"pattern":"[0-9]{4}","type":"string"}},"type":"object"}},"title":"NOA","type":"object"},"type":"array"}}}]},"noahistory-basic":{"description":"Summary of latest 2 Notice of Assessments within the past three years.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"noas":{"items":{"properties":{"amount":{"description":"Assessable Income for this historical NOA.","properties":{"value":{"format":"double","type":"number"}},"type":"object"},"yearofassessment":{"description":"The year of assessment (YYYY) for this historical NOA.","properties":{"value":{"maxLength":4,"pattern":"[0-9]{4}","type":"string"}},"type":"object"}},"title":"NOABasic","type":"object"},"type":"array"}}}]},"occupation":{"description":"Occupation of Person.\nFor SC/PR holders, blank will be returned.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Free text.","maxLength":100,"type":"string"}}}]},"ownerprivate":{"description":"Ownership of Private Property Status of Person (based on IRAS information).\nCan be true, false, or null (if data is not available).","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field.","type":"boolean"}}}]},"partialuinfin":{"description":"Masked Singapore issued identification number of the Person.\nOnly the last 3 digit and ending alphabet will be in clear.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":9,"type":"string"}}}]},"passexpirydate":{"description":"Pass expiry of a foreigner.\nNote: Only applies to a foreigner with a valid pass.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}}}]},"passportexpirydate":{"description":"Passport Expiry Date of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}}}]},"passportnumber":{"description":"Passport Number of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"maxLength":25,"type":"string"}}}]},"passstatus":{"description":"Pass status of a FIN holder.\nNote: Only applies to a foreigner with a valid pass.\nNote: Currently this field is set as empty string for SG/PR and meta source set to '3'","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"value":{"description":"Value of data field.","enum":["Live","Approved",""],"type":"string"}}}]},"passtype":{"description":"Pass type of a FIN holder.\nNote: Only applies to a foreigner with a valid pass.\nRefer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"description":"Value of data field.","type":"string"},"desc":{"type":"string"}}}]},"pioneergen":{"description":"Pioneergen details.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"eligibility":{"description":"Eligibility.","properties":{"value":{"type":"boolean"}},"type":"object"}}}]},"race":{"description":"Race of Person.\n\n  Refer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["code","desc"],"properties":{"code":{"pattern":"^[A-Z]{2}$","type":"string"},"desc":{"maxLength":300,"type":"string"}}}]},"regadd":{"description":"Registered Address of Person (including FIN holders).\n\nNote:\n- Address can be either a Singapore address (type: 'SG'), non Singapore address (type: 'UNFORMATTED') or empty type address ('')\n- May be unavailable for some FIN holders.","anyOf":[{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"block":{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object","description":"Block/House of Address."},"building":{"properties":{"value":{"maxLength":65,"type":"string"}},"type":"object","description":"Building of Address."},"country":{"properties":{"code":{"default":"SG","maxLength":2,"type":"string"},"desc":{"default":"SINGAPORE","type":"string"}},"type":"object","description":"Country/Place of Address. For AddressSG this will always be 'SG'."},"floor":{"properties":{"value":{"maxLength":3,"type":"string"}},"type":"object","description":"Floor of Address."},"postal":{"properties":{"value":{"maxLength":6,"type":"string"}},"type":"object","description":"Postal Code of Address."},"street":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Street of Address."},"type":{"default":"SG","description":"Type of Address (SG or UNFORMATTED for non SG).","enum":["SG"],"type":"string"},"unit":{"properties":{"value":{"maxLength":5,"type":"string"}},"type":"object","description":"Unit of Address."}},"title":"SG"}]},{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"line1":{"type":"object","description":"Unregistered Foreign address line 1","properties":{"value":{"type":"string","maxLength":66}}},"line2":{"type":"object","description":"Unregistered Foreign address line 2","properties":{"value":{"type":"string","maxLength":66}}},"type":{"default":"UNFORMATTED","description":"Type of Address (SG or UNFORMATTED for non SG).","enum":["UNFORMATTED"],"type":"string"}},"title":"UNFORMATTED"}]}]},"residentialstatus":{"description":"Residential Status of Person. Applicable to Singapore Citizens and Permanent Residents.\nNote: This data item is not applicable for FIN holders i.e. source will be '3'.\nIn such cases, the code and desc properties will be blank or empty string ('').\n\nPossible values:\n- A - ALIEN\n- C - CITIZEN\n- P - PR\n- U - UNKNOWN\n- N - NOT APPLICABLE\n- < BLANK > - (for FIN holders only)","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"enum":["A","C","P","U","N",""],"maxLength":1,"pattern":"^[A-Za-z]{0,1}$","type":"string"},"desc":{"enum":["ALIEN","CITIZEN","PR","UNKNOWN","NOT APPLICABLE",""],"maxLength":300,"type":"string"}}}]},"secondaryrace":{"description":"Secondary Race of Person.\n\n  Refer to the Code reference tables in the Support section for list of possible values.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}}}]},"sex":{"description":"Sex of Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["code","desc"],"properties":{"code":{"description":"The 1-character code for the sex.\n\n- 'F': FEMALE\n- 'M': MALE\n- 'U': UNKNOWN","enum":["F","M","U"],"maxLength":1,"type":"string"},"desc":{"description":"The full description of the sex.","enum":["FEMALE","MALE","UNKNOWN"],"type":"string"}}}]},"sponsoredchildrenrecords":{"description":"Details of children sponsored to be SC/PR/LTVP.\n\nFor child below 21, the child's NRIC/FIN, Name, Sex, Race, Secondary Race, Dialect,\nDate of Birth, Country/Place of Birth, Residential Status and SC/PR/LTVP grant date will be shown.\n\nFor child above 21, only the child's last known NRIC/FIN will be shown.","items":{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"aliasname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Alias name of child."},"birthcountry":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Country/Place of Birth of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"dialect":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Dialect of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"dob":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object","description":"Date of Birth of child."},"hanyupinyinaliasname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Han Yu Pin Yin Alias name of child."},"hanyupinyinname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Han Yu Pin Yin name of child."},"lifestatus":{"properties":{"code":{"enum":["A","D",""],"type":"string"},"desc":{"enum":["ALIVE","DECEASED",""],"type":"string"}},"type":"object","description":"Life Status of child."},"marriedname":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Married name of child."},"name":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Full Name of child."},"nationality":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Nationality/Citizenship of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"nric":{"properties":{"value":{"type":"string"}},"type":"object","description":"NRIC/FIN of child."},"race":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Race of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"scprgrantdate":{"properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date","type":"string"}},"type":"object","description":"Date granted Singapore Citizenship, Permanent Resident or Long-term Visit Pass."},"secondaryrace":{"properties":{"code":{"maxLength":2,"pattern":"^(?:[A-Za-z]{2})?$","type":"string"},"desc":{"maxLength":300,"type":"string"}},"type":"object","description":"Secondary Race of child.\nRefer to the Code reference tables in the Support section for list of possible values."},"sex":{"properties":{"code":{"description":"The 1-character code for the sex.\n\n- 'F': FEMALE\n- 'M': MALE\n- 'U': UNKNOWN\n- '': No data yet","enum":["F","M","U",""],"maxLength":1,"type":"string"},"desc":{"description":"The full description of the sex.","enum":["FEMALE","MALE","UNKNOWN",""],"type":"string"}},"type":"object","description":"Sex of child."},"vaccinationrequirements":{"items":{"properties":{"fulfilled":{"properties":{"value":{"type":"boolean"}},"type":"object"},"requirement":{"properties":{"code":{"type":"string"},"desc":{"type":"string"}},"type":"object","description":"Vaccination Requirement.\nRefer to the Code reference tables in the Support section for list of possible values."}},"type":"object"},"type":"array"}}}]},"type":["array","null"]},"uinfin":{"description":"Singapore issued identification number of the Person.","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","required":["value"],"properties":{"value":{"pattern":"\\b[STFGM]\\d{7}[A-Z]\\b","type":"string"}}}]},"vehicles":{"description":"Vehicle information of the Person.","items":{"allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"attachment1":{"properties":{"value":{"maxLength":50,"type":"string"}},"type":"object","description":"Vehicle Attachment 1 (e.g. DISABLED)."},"attachment2":{"properties":{"value":{"maxLength":50,"type":"string"}},"type":"object","description":"Vehicle Attachment 2 (e.g. WITH SUN ROOF)."},"attachment3":{"properties":{"value":{"maxLength":50,"type":"string"}},"type":"object","description":"Vehicle Attachment 3 (e.g. SIDE CURTAIN)."},"chassisno":{"properties":{"value":{"maxLength":25,"type":"string"}},"type":"object","description":"Vehicle Chassis Number."},"co2emission":{"properties":{"value":{"format":"double","maximum":999999999,"type":"number"}},"type":"object","description":"CO2 emission rate."},"coecategory":{"properties":{"value":{"maxLength":40,"type":"string"}},"type":"object","description":"Vehicle Certificate of Entitlement (COE) bid category."},"coeexpirydate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Vehicle Certificate of Entitlement (COE) expiry date.\nSee \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"coemission":{"properties":{"value":{"format":"double","maximum":999999999,"type":"number"}},"type":"object","description":"Carbon Monoxide emission rate."},"effectiveownership":{"properties":{"value":{"format":"date-time","maxLength":25,"type":"string"}},"type":"object","description":"Effective Date/Time of Ownership.\nSee \"date-time\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","format":"date-time"},"enginecapacity":{"properties":{"value":{"format":"int64","maximum":99999999,"type":"integer"}},"type":"object","description":"Engine Capacity in cubic centimeter (cc)."},"engineno":{"properties":{"value":{"maxLength":25,"type":"string"}},"type":"object","description":"Vehicle Engine Number."},"firstregistrationdate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Date when vehicle is registered with LTA.\nSee \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"iulabelno":{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object","description":"In-Vehicle Unit (IU) number of the device fitted in Singapore-registered vehicles for\nElectronic Road Pricing (ERP) gantries and Electronic Parking System (EPS) car parks."},"make":{"properties":{"value":{"maxLength":44,"type":"string"}},"type":"object","description":"Vehicle Make such as 'TOYOTA', 'HONDA', 'AUDI'."},"maximumladenweight":{"properties":{"value":{"format":"int64","maximum":999999999999,"type":"integer"}},"type":"object","description":"Maximum Laden Weight in kilograms (kg)."},"maximumunladenweight":{"properties":{"value":{"format":"int64","maximum":999999999,"type":"integer"}},"type":"object","description":"Maximum Unladen Weight in kilograms (kg)."},"minimumparfbenefit":{"properties":{"value":{"format":"double","maximum":999999999999,"type":"number"}},"type":"object","description":"Minimum PARF Benefit in Singapore dollars (SGD)."},"model":{"properties":{"value":{"maxLength":40,"type":"string"}},"type":"object","description":"Vehicle Model such as 'COROLLA ALTIS CLASSIC 1.6 CVT', 'HRV 1.5 DX CVT'."},"motorno":{"properties":{"value":{"maxLength":25,"type":"string"}},"type":"object","description":"Vehicle Motor Number."},"nooftransfers":{"properties":{"value":{"format":"int64","maximum":99999,"type":"integer"}},"type":"object","description":"Number of Transfer."},"noxemission":{"properties":{"value":{"format":"double","maximum":999999999,"type":"number"}},"type":"object","description":"Nitrogen Oxide (NOx) emission rate."},"openmarketvalue":{"properties":{"value":{"format":"double","maximum":99999999999,"type":"number"}},"type":"object","description":"Open Market Value is the value of manufacturer invoice price, freight and\ninsurance in Singapore dollars (SGD)."},"originalregistrationdate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"Date when vehicle is first registered in the country of origin.\nSee \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"pmemission":{"properties":{"value":{"format":"double","maximum":999999999,"type":"number"}},"type":"object","description":"Particulates (PM - Atmospheric Particulate Matter) emission rate."},"powerrate":{"properties":{"value":{"format":"double","maximum":99999999,"type":"number"}},"type":"object","description":"Power Rate.\nApplicable to Electric and Hybrid vehicles powered by electric motors. Unit is Kilowatt."},"primarycolour":{"properties":{"value":{"maxLength":30,"type":"string"}},"type":"object","description":"Vehicle Primary Colour (e.g. BLACK)."},"propellant":{"properties":{"value":{"maxLength":40,"type":"string"}},"type":"object","description":"Propellant (e.g. Compressed Natural Gas, Diesel, Diesel-CNG, Diesel-Electric,\nDiesel-Electric (Plug-In), Electric, Gas, Liquefied Petroleum Gas (LPG),\nPetrol, Petrol-CNG, Petrol-Electric, Petrol-Electric (Plug-In), Petrol-LPG."},"quotapremium":{"properties":{"value":{"format":"double","maximum":999999999.99,"type":"number"}},"type":"object","description":"Actual Quota Premium (QP) amount payable for the COE upon registration, conversion or COE\nrevalidation in Singapore dollars (SGD). For renewal of COE, the value will contain\nactual PQP paid."},"roadtaxexpirydate":{"properties":{"value":{"format":"date","maxLength":10,"type":"string"}},"type":"object","description":"See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6"},"scheme":{"properties":{"value":{"maxLength":66,"type":"string"}},"type":"object","description":"Vehicle Scheme (e.g. REVISED OFF-PEAK CAR)."},"secondarycolour":{"properties":{"value":{"maxLength":30,"type":"string"}},"type":"object","description":"Vehicle Secondary Colour (e.g. WHITE)."},"status":{"properties":{"code":{"enum":["1","2"],"maxLength":1,"type":"string"},"desc":{"enum":["LIVE","DE-REGISTERED"],"maxLength":300,"type":"string"}},"type":"object","description":"Status of the Vehicle."},"thcemission":{"properties":{"value":{"format":"double","maximum":999999999,"type":"number"}},"type":"object","description":"Total Hydro Carbon (THC) emission rate."},"type":{"properties":{"value":{"maxLength":55,"type":"string"}},"type":"object","description":"Type of Vehicles such as 'MOTOR CAR', 'STATION /WAGON/JEEP/LAND ROVER'."},"vehicleno":{"properties":{"value":{"maxLength":20,"type":"string"}},"type":"object","description":"Vehicle Registration Number displayed on the vehicle number plates."},"vpc":{"properties":{"value":{"maxLength":10,"type":"string"}},"type":"object","description":"Vehicle Parking Certificate. Applicable for Heavy Vehicles."},"yearofmanufacture":{"properties":{"value":{"maxLength":4,"type":"string"}},"type":"object","description":"Manufacturing year."}}}]},"type":["array","null"]},"healthcare_professions":{"type":"object","description":"Healthcare professional profiles, organised by practice domain.","additionalProperties":false,"properties":{"medical":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- SMC - Singapore Medical Council","enum":["SMC"]},"desc":{"type":"string","enum":["Singapore Medical Council"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- DOCTOR - Doctor\n- SPE_REG - Specialist Registration\n- FAM_PHY_REG - Family Physician Registration","enum":["DOCTOR","SPE_REG","FAM_PHY_REG"]},"desc":{"type":"string","enum":["Doctor","Specialist Registration","Family Physician Registration"]}}}}}]}}}}]},"dental":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- SDC - Singapore Dental Council","enum":["SDC"]},"desc":{"type":"string","enum":["Singapore Dental Council"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- DENTIST - Dentist\n- DEN_SPE_REG - Dental Specialist Registration\n- DH_DT - Dental Hygienist / Dental Therapist\n- DT - Dental Therapist\n- DH - Dental Hygienist","enum":["DENTIST","DEN_SPE_REG","DH_DT","DT","DH"]},"desc":{"type":"string","enum":["Dentist","Dental Specialist Registration","Dental Hygienist / Dental Therapist","Dental Therapist","Dental Hygienist"]}}}}}]}}}}]},"nursing":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- SNB - Singapore Nursing Board","enum":["SNB"]},"desc":{"type":"string","enum":["Singapore Nursing Board"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- REG_NURSE - Registered Nurse\n- ENROLLED_NURSE - Enrolled Nurse\n- REG_NURSE_PSC - Registered Nurse (Psychiatric)\n- REG_MIDWIFE - Registered Midwife\n- APN - Advanced Practice Nurse\n- ENROLLED_NURSE_PSC - Enrolled Nurse (Psychiatric)","enum":["REG_NURSE","ENROLLED_NURSE","REG_NURSE_PSC","REG_MIDWIFE","APN","ENROLLED_NURSE_PSC"]},"desc":{"type":"string","enum":["Registered Nurse","Enrolled Nurse","Registered Nurse (Psychiatric)","Registered Midwife","Advanced Practice Nurse","Enrolled Nurse (Psychiatric)"]}}}}}]}}}}]},"pharmacy":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- SPC - Singapore Pharmacy Council","enum":["SPC"]},"desc":{"type":"string","enum":["Singapore Pharmacy Council"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- PHA - Pharmacist\n- PHA_SPE_REG - Pharmacy Specialist Registration","enum":["PHA","PHA_SPE_REG"]},"desc":{"type":"string","enum":["Pharmacist","Pharmacy Specialist Registration"]}}}}}]}}}}]},"allied_health":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- AHPC - Allied Health Professions Council","enum":["AHPC"]},"desc":{"type":"string","enum":["Allied Health Professions Council"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- PHY - Physiotherapist\n- DIAG_RAD - Diagnostic Radiographer\n- OT_ET - Occupational Therapist\n- SPEECH_THERAPIST - Speech-Language Therapist\n- RAD_THA - Radiation Therapist","enum":["PHY","DIAG_RAD","OT_ET","SPEECH_THERAPIST","RAD_THA"]},"desc":{"type":"string","enum":["Physiotherapist","Diagnostic Radiographer","Occupational Therapist","Speech-Language Therapist","Radiation Therapist"]}}}}}]}}}}]},"optometry_opticianry":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- OOB - Optometrists & Opticians Board","enum":["OOB"]},"desc":{"type":"string","enum":["Optometrists & Opticians Board"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- OPTOMETRIST - Optometrist\n- OPTICIAN_RD - Optician (Refraction and Dispensing)\n- OPTICIAN_D - Optician (Dispensing only)\n- CLP - Optician (Contact Lens Practitioner)","enum":["OPTOMETRIST","OPTICIAN_RD","OPTICIAN_D","CLP"]},"desc":{"type":"string","enum":["Optometrist","Optician (Refraction and Dispensing)","Optician (Dispensing only)","Optician (Contact Lens Practitioner)"]}}}}}]}}}}]},"traditional_chinese_medicine":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionProfile"},{"type":"object","properties":{"practitioner_chinese_name":{"description":"Practitioner's name in Chinese characters. Exposed for TCM only.","type":"object","properties":{"value":{"type":"string"}}},"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- TCM - Traditional Chinese Medicine Practitioners Board","enum":["TCM"]},"desc":{"type":"string","enum":["Traditional Chinese Medicine Practitioners Board"]}}},"registrations":{"type":"array","items":{"allOf":[{"$ref":"#/components/schemas/HealthcareProfessionRegistration"},{"type":"object","properties":{"register_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- TCM_PHY - TCM Physician\n- ACUP - Acupuncturist","enum":["TCM_PHY","ACUP"]},"desc":{"type":"string","enum":["TCM Physician","Acupuncturist"]}}}}}]}}}}]}}},"public_officer_employments":{"description":"Public officer employment records of Person.","items":{"title":"PublicOfficerEmployment","type":"object","allOf":[{"$ref":"#/components/schemas/Meta"},{"type":"object","properties":{"title":{"description":"Job title of the public officer.","properties":{"value":{"type":"string"}},"type":"object"},"type":{"description":"Employment type (e.g. Permanent, Contract).","properties":{"value":{"type":"string"}},"type":"object","required":["value"]},"email":{"description":"Work email of the public officer.","properties":{"value":{"type":"string"}},"type":"object"},"agency":{"description":"Government agency of the public officer.","required":["code","desc"],"properties":{"code":{"type":"string","enum":["ACRA","AGC","AGD","AGO","BCA","BOA","CAAS","CAB","CCCS","CDA","CEA","CNB","CPIB","CSA","CSC","DOS","ECDA","EDB","ELD","EMA","ESG","GOVTECH","GRA","HDB","HPB","HSA","HTA","HTX","IAC","ICA","IMDA","IPOS","IRAS","ISEAS","ISTANA","ITE","JTC","JUDICIARY","LASA","LTA","MAS","MCCY","MDDI","METI","MFA","MHA","MHA-HAD","MINDEF","MINLAW","MND","MOE","MOF","MOH","MOH-SDC","MOHPBB","MOM","MOT","MP","MPA","MSE","MSF","MTI","MTI-SDC","MUIS","NAC","NCSS","NEA","NHB","NLB","NP","NPARKS","NRF","NSCS","NYC","NYP","PA","PARL","PEB","PMO","PMO-CG","PMO-SG","PSC","PSD","PTC","PUB","RP","SC","SCB","SCDF","SEAB","SFA","SLA","SLF","SNB","SP","SPB","SPC","SPF","SPS","SSC","SSG","STB","TCMPB","TOTE BOARD","TP","URA","VITAL","WSG","YRSG"],"description":"Possible values:\n* ACRA - ACCOUNTING AND CORPORATE REGULATORY AUTHORITY\n* AGC - ATTORNEY-GENERAL'S CHAMBERS\n* AGD - ACCOUNTANT-GENERAL'S DEPARTMENT\n* AGO - AUDITOR-GENERAL'S OFFICE\n* BCA - BUILDING AND CONSTRUCTION AUTHORITY\n* BOA - BOARD OF ARCHITECTS\n* CAAS - CIVIL AVIATION AUTHORITY OF SINGAPORE\n* CAB - THE CABINET\n* CCCS - COMPETITION AND CONSUMER COMMISSION OF SINGAPORE\n* CDA - COMMUNICABLE DISEASES AGENCY\n* CEA - COUNCIL FOR ESTATE AGENCIES\n* CNB - CENTRAL NARCOTICS BUREAU\n* CPIB - CORRUPT PRACTICES INVESTIGATION BUREAU\n* CSA - CYBER SECURITY AGENCY OF SINGAPORE\n* CSC - CIVIL SERVICE COLLEGE\n* DOS - DEPARTMENT OF STATISTICS\n* ECDA - EARLY CHILDHOOD AND DEVELOPMENT AGENCY\n* EDB - ECONOMIC DEVELOPMENT BOARD\n* ELD - ELECTIONS DEPARTMENT\n* EMA - ENERGY MARKET AUTHORITY\n* ESG - ENTERPRISE SINGAPORE\n* GOVTECH - GOVERNMENT TECHNOLOGY AGENCY\n* GRA - GAMBLING REGULATORY AUTHORITY\n* HDB - HOUSING & DEVELOPMENT BOARD\n* HPB - HEALTH PROMOTION BOARD\n* HSA - HEALTH SCIENCES AUTHORITY\n* HTA - HOME TEAM ACADEMY\n* HTX - HOME TEAM SCIENCE AND TECHNOLOGY AGENCY\n* IAC - INDUSTRIAL ARBITRATION COURT\n* ICA - IMMIGRATION & CHECKPOINTS AUTHORITY\n* IMDA - INFOCOMM MEDIA DEVELOPMENT AUTHORITY\n* IPOS - INTELLECTUAL PROPERTY OFFICE OF SINGAPORE\n* IRAS - INLAND REVENUE AUTHORITY OF SINGAPORE\n* ISEAS - ISEAS YUSOF ISHAK INSTITUTE\n* ISTANA - ISTANA\n* ITE - INSTITUTE OF TECHNICAL EDUCATION\n* JTC - JTC CORPORATION\n* JUDICIARY - JUDICIARY\n* LASA - LEGAL ASSISTANTS AND SECRETARIAT ASSISTANTS\n* LTA - LAND TRANSPORT AUTHORITY\n* MAS - MONETARY AUTHORITY OF SINGAPORE\n* MCCY - MINISTRY OF CULTURE, COMMUNITY AND YOUTH\n* MDDI - MINISTRY OF DIGITAL DEVELOPMENT AND INFORMATION\n* METI - MINISTRY OF ENERGY, TRADE AND INDUSTRY\n* MFA - MINISTRY OF FOREIGN AFFAIRS\n* MHA - MINISTRY OF HOME AFFAIRS\n* MHA-HAD - MHA-HAD\n* MINDEF - MINISTRY OF DEFENCE\n* MINLAW - MINISTRY OF LAW\n* MND - MINISTRY OF NATIONAL DEVELOPMENT\n* MOE - MINISTRY OF EDUCATION\n* MOF - MINISTRY OF FINANCE\n* MOH - MINISTRY OF HEALTH\n* MOH-SDC - SINGAPORE DENTAL COUNCIL\n* MOHPBB - MOH PROFESSIONAL BOARDS AND BODIES\n* MOM - MINISTRY OF MANPOWER\n* MOT - MINISTRY OF TRANSPORT\n* MP - MEMBERS OF PARLIAMENT\n* MPA - MARITIME AND PORT AUTHORITY OF SINGAPORE\n* MSE - MINISTRY OF SUSTAINABILITY AND THE ENVIRONMENT\n* MSF - MINISTRY OF SOCIAL AND FAMILY DEVELOPMENT\n* MTI - MINISTRY OF TRADE AND INDUSTRY\n* MTI-SDC - SENTOSA DEVELOPMENT CORPORATION\n* MUIS - MUIS MAJLIS UGAMA ISLAM SINGAPURA\n* NAC - NATIONAL ARTS COUNCIL\n* NCSS - NATIONAL COUNCIL OF SOCIAL SERVICE\n* NEA - NATIONAL ENVIRONMENT AGENCY\n* NHB - NATIONAL HERITAGE BOARD\n* NLB - NATIONAL LIBRARY BOARD\n* NP - NGEE ANN POLYTECHNIC\n* NPARKS - NATIONAL PARKS BOARD\n* NRF - NATIONAL RESEARCH FOUNDATION\n* NSCS - NATIONAL SECURITY COORDINATION SECRETARIAT\n* NYC - NATIONAL YOUTH COUNCIL SINGAPORE\n* NYP - NANYANG POLYTECHNIC\n* PA - PEOPLE'S ASSOCIATION\n* PARL - PARLIAMENT OF SINGAPORE\n* PEB - PROFESSIONAL ENGINEERS BOARD, SINGAPORE\n* PMO - PRIME MINISTER'S OFFICE\n* PMO-CG - PRIME MINISTER'S OFFICE - COMMUNICATIONS GROUP\n* PMO-SG - PRIME MINISTER'S OFFICE - STRATEGY GROUP\n* PSC - PUBLIC SERVICE COMMISSION\n* PSD - PUBLIC SERVICE DIVISION\n* PTC - PUBLIC TRANSPORT COUNCIL\n* PUB - PUB SINGAPORE'S NATIONAL WATER AGENCY\n* RP - REPUBLIC POLYTECHNIC\n* SC - SINGAPORE CUSTOMS\n* SCB - SCIENCE CENTRE BOARD\n* SCDF - SINGAPORE CIVIL DEFENCE FORCE\n* SEAB - SINGAPORE EXAMINATIONS AND ASSESSMENT BOARD\n* SFA - SINGAPORE FOOD AGENCY\n* SLA - SINGAPORE LAND AUTHORITY\n* SLF - SINGAPORE LABOUR FOUNDATION\n* SNB - SINGAPORE NURSING BOARD\n* SP - SINGAPORE POLYTECHNIC\n* SPB - SECRETARIAT OF HEALTHCARE PROFESSIONAL BOARDS\n* SPC - SINGAPORE PHARMACY COUNCIL\n* SPF - SINGAPORE POLICE FORCE\n* SPS - SINGAPORE PRISON SERVICE\n* SSC - SINGAPORE SPORTS COUNCIL\n* SSG - SKILLSFUTURE SINGAPORE AGENCY\n* STB - SINGAPORE TOURISM BOARD\n* TCMPB - TRADITIONAL CHINESE MEDICINE PRACTITIONERS BOARD\n* TOTE BOARD - TOTE BOARD\n* TP - TEMASEK POLYTECHNIC\n* URA - URBAN REDEVELOPMENT AUTHORITY\n* VITAL - VITAL\n* WSG - WORKFORCE SINGAPORE\n* YRSG - YELLOW RIBBON SINGAPORE"},"desc":{"type":"string","enum":["ACCOUNTING AND CORPORATE REGULATORY AUTHORITY","ATTORNEY-GENERAL'S CHAMBERS","ACCOUNTANT-GENERAL'S DEPARTMENT","AUDITOR-GENERAL'S OFFICE","BUILDING AND CONSTRUCTION AUTHORITY","BOARD OF ARCHITECTS","CIVIL AVIATION AUTHORITY OF SINGAPORE","THE CABINET","COMPETITION AND CONSUMER COMMISSION OF SINGAPORE","COMMUNICABLE DISEASES AGENCY","COUNCIL FOR ESTATE AGENCIES","CENTRAL NARCOTICS BUREAU","CORRUPT PRACTICES INVESTIGATION BUREAU","CYBER SECURITY AGENCY OF SINGAPORE","CIVIL SERVICE COLLEGE","DEPARTMENT OF STATISTICS","EARLY CHILDHOOD AND DEVELOPMENT AGENCY","ECONOMIC DEVELOPMENT BOARD","ELECTIONS DEPARTMENT","ENERGY MARKET AUTHORITY","ENTERPRISE SINGAPORE","GOVERNMENT TECHNOLOGY AGENCY","GAMBLING REGULATORY AUTHORITY","HOUSING & DEVELOPMENT BOARD","HEALTH PROMOTION BOARD","HEALTH SCIENCES AUTHORITY","HOME TEAM ACADEMY","HOME TEAM SCIENCE AND TECHNOLOGY AGENCY","INDUSTRIAL ARBITRATION COURT","IMMIGRATION & CHECKPOINTS AUTHORITY","INFOCOMM MEDIA DEVELOPMENT AUTHORITY","INTELLECTUAL PROPERTY OFFICE OF SINGAPORE","INLAND REVENUE AUTHORITY OF SINGAPORE","ISEAS YUSOF ISHAK INSTITUTE","ISTANA","INSTITUTE OF TECHNICAL EDUCATION","JTC CORPORATION","JUDICIARY","LEGAL ASSISTANTS AND SECRETARIAT ASSISTANTS","LAND TRANSPORT AUTHORITY","MONETARY AUTHORITY OF SINGAPORE","MINISTRY OF CULTURE, COMMUNITY AND YOUTH","MINISTRY OF DIGITAL DEVELOPMENT AND INFORMATION","MINISTRY OF ENERGY, TRADE AND INDUSTRY","MINISTRY OF FOREIGN AFFAIRS","MINISTRY OF HOME AFFAIRS","MHA-HAD","MINISTRY OF DEFENCE","MINISTRY OF LAW","MINISTRY OF NATIONAL DEVELOPMENT","MINISTRY OF EDUCATION","MINISTRY OF FINANCE","MINISTRY OF HEALTH","SINGAPORE DENTAL COUNCIL","MOH PROFESSIONAL BOARDS AND BODIES","MINISTRY OF MANPOWER","MINISTRY OF TRANSPORT","MEMBERS OF PARLIAMENT","MARITIME AND PORT AUTHORITY OF SINGAPORE","MINISTRY OF SUSTAINABILITY AND THE ENVIRONMENT","MINISTRY OF SOCIAL AND FAMILY DEVELOPMENT","MINISTRY OF TRADE AND INDUSTRY","SENTOSA DEVELOPMENT CORPORATION","MUIS MAJLIS UGAMA ISLAM SINGAPURA","NATIONAL ARTS COUNCIL","NATIONAL COUNCIL OF SOCIAL SERVICE","NATIONAL ENVIRONMENT AGENCY","NATIONAL HERITAGE BOARD","NATIONAL LIBRARY BOARD","NGEE ANN POLYTECHNIC","NATIONAL PARKS BOARD","NATIONAL RESEARCH FOUNDATION","NATIONAL SECURITY COORDINATION SECRETARIAT","NATIONAL YOUTH COUNCIL SINGAPORE","NANYANG POLYTECHNIC","PEOPLE'S ASSOCIATION","PARLIAMENT OF SINGAPORE","PROFESSIONAL ENGINEERS BOARD, SINGAPORE","PRIME MINISTER'S OFFICE","PRIME MINISTER'S OFFICE - COMMUNICATIONS GROUP","PRIME MINISTER'S OFFICE - STRATEGY GROUP","PUBLIC SERVICE COMMISSION","PUBLIC SERVICE DIVISION","PUBLIC TRANSPORT COUNCIL","PUB SINGAPORE'S NATIONAL WATER AGENCY","REPUBLIC POLYTECHNIC","SINGAPORE CUSTOMS","SCIENCE CENTRE BOARD","SINGAPORE CIVIL DEFENCE FORCE","SINGAPORE EXAMINATIONS AND ASSESSMENT BOARD","SINGAPORE FOOD AGENCY","SINGAPORE LAND AUTHORITY","SINGAPORE LABOUR FOUNDATION","SINGAPORE NURSING BOARD","SINGAPORE POLYTECHNIC","SECRETARIAT OF HEALTHCARE PROFESSIONAL BOARDS","SINGAPORE PHARMACY COUNCIL","SINGAPORE POLICE FORCE","SINGAPORE PRISON SERVICE","SINGAPORE SPORTS COUNCIL","SKILLSFUTURE SINGAPORE AGENCY","SINGAPORE TOURISM BOARD","TRADITIONAL CHINESE MEDICINE PRACTITIONERS BOARD","TOTE BOARD","TEMASEK POLYTECHNIC","URBAN REDEVELOPMENT AUTHORITY","VITAL","WORKFORCE SINGAPORE","YELLOW RIBBON SINGAPORE"]}},"type":"object"},"department":{"description":"Department within the agency.","properties":{"value":{"type":"string"}},"type":"object"}}}]},"type":["array"]}}},"Meta":{"title":"Meta","type":"object","required":["classification","source","lastupdated"],"properties":{"classification":{"default":"C","description":"Data classification of data field. Default 'C' - Confidential.","maxLength":1,"type":"string"},"lastupdated":{"description":"Last updated date of data field. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6.","format":"date","type":"string"},"source":{"description":"Source of data.\n\n- '1': Government-verified\n- '2': User provided\n- '3': Not Applicable (applies only to Person data, not Entity data)\n- '4': Verified by SingPass","enum":["1","2","3","4"],"maxLength":1,"type":"string"}}},"UnavailableFlag":{"title":"UnavailableFlag","type":"object","properties":{"unavailable":{"description":"Optional flag to indicate if data is unavailable from data source.\n\nNOTE:\n\n- This optional property will be only present with value true if there is no data available from the data source; i.e. record not found.\n\n- When this flag is true, no other data attributes will be present (other than classification, source, and lastupdated).\n\n- If data is available from the data source, this property will not be present.","type":"boolean"}}},"HealthcareProfessionProfile":{"title":"HealthcareProfessionProfile","type":"object","allOf":[{"$ref":"#/components/schemas/Meta"},{"$ref":"#/components/schemas/UnavailableFlag"},{"type":"object","properties":{"healthcare_professional_entity":{"type":"object","properties":{"code":{"type":"string"},"desc":{"type":"string"}}},"registration_number":{"description":"Public-facing professional registration number","type":"object","properties":{"value":{"type":"string"}}},"registrations":{"type":"array","items":{"$ref":"#/components/schemas/HealthcareProfessionRegistration"}}}}]},"HealthcareProfessionRegistration":{"title":"HealthcareProfessionRegistration","additionalProperties":false,"type":"object","description":"A single professional registration record.","properties":{"register_id":{"description":"Unique registration record identifier (PRS primary key).","type":"object","properties":{"value":{"type":"string"}}},"register_type":{"type":"object","properties":{"code":{"type":"string"},"desc":{"type":"string"}}},"registration_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- C_REG - Conditional Registration\n- FULL_REG - Full Registration\n- P_REG - Provisional Registration\n- PART1 - Part I\n- PART2_FOREIGN - Part II (Foreign-Trained)\n- PART2_LOCAL - Part II (Local-Trained)\n- R_REG - Restricted Registration\n- T_REG - Temporary Registration\n- '' - No data yet","enum":["C_REG","FULL_REG","P_REG","PART1","PART2_FOREIGN","PART2_LOCAL","R_REG","T_REG",""]},"desc":{"type":"string","enum":["Conditional Registration","Full Registration","Provisional Registration","Part I","Part II (Foreign-Trained)","Part II (Local-Trained)","Restricted Registration","Temporary Registration",""]}}},"practising_certificate_start_date":{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","type":"string","format":"date"}}},"practising_certificate_end_date":{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","type":"string","format":"date"}}},"practice_status":{"type":"object","properties":{"value":{"type":"string","enum":["ACTIVE","INACTIVE",""]}}},"registration_start_date":{"type":"object","properties":{"value":{"description":"Value of data field in YYYY-MM-DD format. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6","type":"string","format":"date"}}},"specialty_name":{"type":"object","properties":{"value":{"type":"string"}}},"specialty_type":{"type":"object","properties":{"code":{"type":"string","description":"Possible values:\n- SPETY - Specialty\n- SUB_SPETY - Subspecialty\n- '' - No data yet","enum":["SPETY","SUB_SPETY",""]},"desc":{"type":"string","enum":["Specialty","Subspecialty",""]}}}}}}}}
```

## The Meta object

```json
{"openapi":"3.1.0","info":{"title":"Myinfo v5","version":"2026-09-30"},"components":{"schemas":{"Meta":{"title":"Meta","type":"object","required":["classification","source","lastupdated"],"properties":{"classification":{"default":"C","description":"Data classification of data field. Default 'C' - Confidential.","maxLength":1,"type":"string"},"lastupdated":{"description":"Last updated date of data field. See \"full-date\" in https://datatracker.ietf.org/doc/html/rfc3339#section-5.6.","format":"date","type":"string"},"source":{"description":"Source of data.\n\n- '1': Government-verified\n- '2': User provided\n- '3': Not Applicable (applies only to Person data, not Entity data)\n- '4': Verified by SingPass","enum":["1","2","3","4"],"maxLength":1,"type":"string"}}}}}}
```

## The UnavailableFlag object

```json
{"openapi":"3.1.0","info":{"title":"Myinfo v5","version":"2026-09-30"},"components":{"schemas":{"UnavailableFlag":{"title":"UnavailableFlag","type":"object","properties":{"unavailable":{"description":"Optional flag to indicate if data is unavailable from data source.\n\nNOTE:\n\n- This optional property will be only present with value true if there is no data available from the data source; i.e. record not found.\n\n- When this flag is true, no other data attributes will be present (other than classification, source, and lastupdated).\n\n- If data is available from the data source, this property will not be present.","type":"boolean"}}}}}}
```

Error Response

If there was an error with the request, we will instead return a response body in `application/json` format with the following parameters:

| `error`             | An error code identifying the type of error that has occurred. | This will be an enum value. The possible values are detailed below. |
| ------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| `error_description` | A human-readable text description of the error.                | String. This is optional.                                           |

These parameters will also be returned in the `WWW-Authenticate` header if the `error` is `invalid_request`, `invalid_token`, or `invalid_dpop_proof`.

<details>

<summary>Sample error response body</summary>

```json
{
  "error": "invalid_dpop_proof",
  "error_description": "Failed to verify DPoP proof JWT"
}
```

</details>

<details>

<summary>Sample WWW-Authenticate header</summary>

```http
HTTP/1.1 401 Unauthorized
WWW-Authenticate: DPoP
  error="invalid_dpop_proof",
  error_description="Failed to verify DPoP proof JWT"
```

</details>

#### Possible error values

The table below lists the possible values of `error` that we may return:

| error                       | What this error indicates                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invalid_token`             | The access token is invalid or has expired. Note that the access token has a lifetime of 30 minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `invalid_dpop_proof`        | The `DPoP` header which you have provided is invalid, expired, or malformed. Read our [DPoP guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) and ensure that your implementation follows the instructions in the guide.                                                                                                                                                                                                                                                                                                                      |
| `invalid_request`           | <p>This could be due to one of the following:</p><ul><li>Your JWKS endpoint is not reachable, or the JWKS being returned is malformed., Read our guide on <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks#requirements-for-jwks">JWKS</a> and ensure that you follow the requirements.</li><li>You are trying to retrieve Myinfo data for a Singpass Foreign Account user, which is not possible.</li></ul>                                                                                                                                                |
| `server_error`              | <p>The server encountered an unexpected error. You should check <code>error\_description</code> to understand what was the cause of the error.<br><br>When you encounter this error, you may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative form-filling methods.</p>                                                                                                                                                                                                                                                                            |
| `upstream_dependency_error` | <p>This error can potentially be caused by your JWKS endpoint not being reachable. Read our guide on <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks#requirements-for-jwks">JWKS</a> and ensure that you follow the requirements. In particular, your JWKS endpoint must be publicly accessible and should respond in a timely manner.</p><p>If the cause was not your JWKS endpoint, you may perform up to 3 retries using an exponential backoff strategy. If the request still fails, you should guide users to alternative authentication methods.</p> |


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

* Verification of your [client assertions](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) (they are signed by one of your private keys). This is done during both the [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request) and [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange)
* Encryption of the [ID Token](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token)
* Encryption of the [Userinfo response](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#response)

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

When your backend calls our APIs, you will need to generate a client assertion to authenticate yourself. The generation of this client assertion should be done using the `private_key_jwt` mechanism specified in the [OIDC specifications](https://openid.net/specs/openid-connect-core-1_0-final.html#ClientAuthentication). This mechanism involves you building a client assertion by signing a JWT using one of your signing keys defined in your [JWKS](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks).

Client assertions need to be sent in the [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request) and the [Token Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange).

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
  "iat": 1756785377,
  "exp": 1756785493,
  "jti": "59e05e3c-9418-4e63-8119-a05157219b74"
}
```

</details>

### Overall JWT (Signed and Encoded)

The JWT should be signed using your private key to form a JSON Web Signature (JWS) in compact serialisation format. This is a format where the three parts of the JWS (the header, the payload, and the signature), are base64url encoded and concatenated together, using a dot (`.`) as the separator.

You must publish the public key corresponding to the private key you used to sign this JWT in your [JWKS](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks).

<details>

<summary>Sample Signed JWT (in Compact Serialisation Format)</summary>

{% hint style="info" %}
The signature segment below is illustrative — the actual signature must be generated by signing the header and payload with your private key.
{% endhint %}

{% code overflow="wrap" %}

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6Im15X2tleV9pZF8wMSJ9.eyJzdWIiOiJUNXNNNWE1M1lhdzNVUnlERXYyeTkxMjlDYkVsQ04yRiIsImF1ZCI6Imh0dHBzOi8vaWQuc2luZ3Bhc3MuZ292LnNnL2ZhcGkiLCJpc3MiOiJUNXNNNWE1M1lhdzNVUnlERXYyeTkxMjlDYkVsQ04yRiIsImlhdCI6MTc1Njc4NTM3NywiZXhwIjoxNzU2Nzg1NDkzLCJqdGkiOiI1OWUwNWUzYy05NDE4LTRlNjMtODExOS1hMDUxNTcyMTliNzQifQ.fQMHTVNeCsa_mK6pmfjfi0rxERxDtu6eiMFkkpFdQrirc3u9LxP1_-E_7yIalIhmot1NdBQxbA9s_VztlQUhTQ
```

{% endcode %}

</details>

### Validate Your Client Assertion

You can validate your Client Assertion using this online validator tool:

<https://developer.singpass.gov.sg/troubleshooting-tool>

This tool helps you:

* Verify JWT structure and compact format
* Check required header parameters (alg, typ, kid)
* Validate required payload claims
* Confirm signature validity
* Detect common implementation errors


# Proof Key for Code Exchange (PKCE)

## Overview

Proof Key for Code Exchange (PKCE) is a security mechanism specified in [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636). It ensures that only you, the requester of the authorization code, can use the authorization code during [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange).

PKCE works in tandem with [client assertions](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) and [DPoP](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) in order to prevent authorization code interception attacks, which is a type of attack where attackers gain access to the authorization code (e.g. via malware installed on the user's device) and use it to obtain a user's access token.

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


# Demonstrating Proof of Possession (DPoP)

## Overview

DPoP ([RFC 9449](https://www.rfc-editor.org/rfc/rfc9449.html)) protects your integration from:

1. Authorization code interception
2. Access token misuse or leakage

It works by binding the *authorization code* and *access token* to a private key that only your system controls. allowing only you to use them for [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange) and [Requesting For Userinfo](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo) respectively.

#### **When is DPoP Required?**

You must include a **DPoP proof JWT** in the DPoP request header for the following API calls:

* [Pushed Authorization Request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request)
* [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange)
* [Requesting for Userinfo](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo)

If DPoP is missing or invalid the request will be rejected

#### **Key Requirements**

{% hint style="warning" %}
You **must** use the same DPoP key pair across all three requests for a single authentication. You should generate a different ephemeral key for each authentication.
{% endhint %}

* Generate a **new** ephemeral DPoP key pair for each authentication session
* Use the **same key pair across all three requests** (PAR → Token → Userinfo) for that session
* Do not reuse the key pair across different login sessions

#### What Is the DPoP Proof JWT?

The DPoP Proof JWT is a signed JWT (JWS) that proves you own the private key bound to the token — without exposing the private key.

To implement:

* We recommend using a standard JWT library
* You may refer to [this list](https://www.jwt.io/libraries?support=sign\&algorithm=es256) to look for a suitable library for your programming language. To learn more about JWTs and their structure, you may read [this article](https://www.jwt.io/introduction).

### DPoP Proof JWT Structure and Requirements

#### JWT Header

The JWT header should contain the following parameters:

<table><thead><tr><th width="122.17578125">Parameter</th><th>Description</th><th>Data Type</th></tr></thead><tbody><tr><td><code>alg</code></td><td>The signature algorithm that you are using to sign this JWT</td><td><p>One of the following strings:</p><ul><li><code>ES256</code></li><li><code>ES384</code></li><li><code>ES512</code></li></ul></td></tr><tr><td><code>typ</code></td><td>The type of this JWT</td><td>Must be the string <code>dpop+jwt</code></td></tr><tr><td><code>jwk</code></td><td>The public key, in JSON Web Key format, that corresponds to the private key used to sign the JWT</td><td>Object in JSON Web Key format</td></tr></tbody></table>

<details>

<summary>Sample JWT header</summary>

```json
{
  "alg": "ES256",
  "typ": "dpop+jwt",
  "jwk": {
    "crv": "P-256",
    "kty": "EC",
    "x": "T59MDXABUkdP7DAvAnuZ3l-iLUylObl1v6DBqAp8LU0",
    "y": "D7NSWZW9_r2wZC10yobEiOgjoqDppoMdYSG3YV16QjU"
  }
}
```

</details>

#### JWT Payload

The JWT payload should contain the following claims:

<table><thead><tr><th width="88.7265625">Claim</th><th width="440.61328125">Description</th><th>Data type</th></tr></thead><tbody><tr><td><code>htm</code></td><td>The HTTP method of the request that you are making</td><td>Either the string <code>POST</code> or <code>GET</code></td></tr><tr><td><code>htu</code></td><td>The URL that you are making the request to.</td><td>URL</td></tr><tr><td><code>iat</code></td><td>The unix timestamp, in seconds, at which you generated this JWT.</td><td>This value must be a <a href="https://datatracker.ietf.org/doc/html/rfc7519#section-2"><code>NumericDate</code></a> type, representing seconds.</td></tr><tr><td><code>exp</code></td><td>The unix timestamp, in seconds, on or after which this JWT <strong>must not</strong> be accepted by us for processing.<br><br>Note also that this must be less than or equal to 2 minutes after <code>iat</code>.</td><td>Optional. This value must be a <a href="https://datatracker.ietf.org/doc/html/rfc7519#section-2"><code>NumericDate</code></a> type, representing seconds.</td></tr><tr><td><code>jti</code></td><td>A unique identifier for this token. This identifier must only be used once. You should generate a new <code>jti</code> value for every request</td><td>String</td></tr><tr><td><code>ath</code></td><td>Required only for the userinfo request. This should be the base64url-encoded SHA-256 hash of the access token.</td><td>A base64url-encoded string.</td></tr></tbody></table>

<details>

<summary>Sample JWT payload</summary>

```json
{
  "jti": "50ac59b2-a1e7-4bac-909b-68b692207b6c",
  "htm": "POST",
  "htu": "https://stg-id.singpass.gov.sg/fapi/par",
  "iat": 1771819829,
  "exp": 1771819949
}
```

</details>

### Signing and using the JWT

The JWT should be signed using your private DPoP key to form a JSON Web Signature (JWS) in compact serialisation format. This is a format where the three parts of the JWS (the header, the payload, and the signature), are base64url encoded and concatenated together, using a dot (`.`) as the separator.

The private key used to sign the JWT must correspond to the public key indicated in the `jwk` parameter in the JWT header.

This JWS should then be included in the `DPoP` request header when you are making requests that require DPoP.

```
DPoP: <your_signed_jwt>
```

### Validate Your DPoP Implementation

You can validate your DPoP proof JWT using this online validator tool:

<https://developer.singpass.gov.sg/troubleshooting-tool>

This tool helps you:

* Verify JWT structure and compact format
* Check required header parameters (alg, typ, jwk)
* Validate required payload claims
* Confirm signature validity
* Detect common implementation errors


# OpenID Provider Configuration

Singpass' authorization server exposes an endpoint from which you can retrieve metadata about how Singpass is configured as an OpenID Provider:

<table><thead><tr><th width="199">Environment</th><th>Discovery Endpoint</th></tr></thead><tbody><tr><td>Staging</td><td><a href="https://stg-id.singpass.gov.sg/fapi/.well-known/openid-configuration">https://stg-id.singpass.gov.sg/fapi/.well-known/openid-configuration</a></td></tr><tr><td>Production</td><td><a href="https://id.singpass.gov.sg/fapi/.well-known/openid-configuration">https://id.singpass.gov.sg/fapi/.well-known/openid-configuration</a></td></tr></tbody></table>

The metadata hosted at this endpoint is crucial for your integration. It tells you things like:

* The various endpoints and URIs that you will need, and
* Supported scopes, response types, and encryption/signing algorithms

Because [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) is part of the OIDC spec, if you are using an OpenID-certified relying party library, the library may automatically retrieve metadata from our discovery endpoint for you. In such cases, you may not be aware of this detail.

Please be aware, however, that Singpass' OpenID configuration is not static, and you should regularly fetch from our discovery endpoint to ensure freshness. At the same time, you should also avoid fetching from this endpoint too frequently, e.g. for every authentication request. Instead, consider caching responses for at least an hour.

{% hint style="warning" %}
Do not pin Singpass' TLS leaf certificates. Singpass reserves the right to rotate its TLS certificates without prior notice. Applications that pin the leaf certificate will break silently when rotation occurs. [Learn more](https://partnersupport.singpass.gov.sg/hc/en-sg/articles/43040167570457)
{% endhint %}


# Migration Guides

This section contains guides to help you migrate your existing integrations to be compliant with the new Authentication API.

If you are unsure about the type of your app, you may log in to the [Singpass Developer Portal](https://developer.singpass.gov.sg/). The app types of each of your apps will be visible on the dashboard page, once you log in.

If you use Myinfo Business (v1/v2) and retrieve person data through the Myinfo v3 Person API, follow the [Myinfo Business (v1/v2) Person v3 flows migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/migrating-mib-v1-v2-person-v3-to-myinfo-v5).

<table><thead><tr><th width="231.05078125">App Type</th><th>Migration Requirement</th></tr></thead><tbody><tr><td>Login / Myinfo (v5)</td><td><p>You <strong>do not need</strong> to create a new app/duplicate your app, unless there is a change in your user journey.</p><p>Refer to <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/login-myinfo-v5-apps">this section</a> for more info.</p></td></tr><tr><td>Myinfo (v3/v4)</td><td>You <strong>need</strong> to create a new app/duplicate your app to <strong>obtain a new client id.</strong> You may <a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/duplicate-an-app">duplicate your app</a>.<br><br>Refer to <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v3-apps">Myinfo (v3)</a> or <a href="https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v4-apps">Myinfo (v4)</a> for more info.</td></tr><tr><td>Myinfo Business (v1/v2)</td><td>Please refer to <a href="https://docs.corppass.gov.sg/technical-specifications/corppass-authorization-api-fapi-2.0/migration-guides/migration-guide-myinfo-business-v1-v2-to-v3-fapi-2.0">Myinfo Business migration guide here</a>.</td></tr><tr><td>Verify, Sign with Singpass<br><br>For WOG - Person-Basic, EDH</td><td>Migration is not required at the moment</td></tr></tbody></table>


# Login / Myinfo (v5) apps

## Overview

If you are migrating an existing Login or Myinfo (v5) app, there will not be any need for you to create a new app in the Singpass Developer Portal. Instead, you can integrate with the new authentication API using your existing app.

During the migration process, you can simultaneously have integrations with both the old authentication API and the new one. How this will work will be as follows:

* If you send the authorization request parameters via [pushed authorization request](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request), then the new API will be used for that authentication flow.
* If you send the authorization request parameters via a [browser redirect to the authorization endpoint](https://github.com/SingpassPX/dev-docs/tree/main/technical-specifications/singpass-authentication-api/1.-authorization-endpoint), then the old API will be used for that authentication flow.

This will allow you to test your new integration or to perform a staged rollout of the new integration in production without affecting the existing integration, so long as pushed authorization requests are only used when the new API is going to be used.

## Changes Required

Listed below are the changes that you will need to make to your existing integration for it to work with the new authentication API.

### General

#### 1. Implement Demonstration of Proof of Possession (DPoP)

DPoP is a security mechanism in which the access token and authorization code is bound to a private key that is known only to you, preventing malicious parties from using your code or token.

Read our [guide to DPoP](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) to understand how to implement it.

#### 2. Handle Authentication Error Responses

In the old Authentication API, we do not always redirect back to your redirect URL when an error occurs. In the new API, we will be redirecting back to your redirect URL on most errors, with an Authentication Error Response, which is specified in [section 3.1.2.6 of the OpenID specifications](https://openid.net/specs/openid-connect-core-1_0.html#AuthError).

You should refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/2.-handling-the-redirect) to understand how to handle these responses.

#### 3. Update custom scheme URLs

The new Authentication API no longer supports the use of custom scheme URLs (i.e. URLs that do not start with `https://` ) as redirect URLs or app launch URLs.

If you are currently integrating with Singpass via an Android or iOS app, and rely on such URLs for redirection back to the mobile app, you will need to change these URLs to use app-claimed HTTPS URLs instead. App-claimed HTTPS URLs are HTTPS URLs which, when opened on a mobile device, will launch your mobile app.

Android applications support app-claimed HTTPS URLs via Android App Links, while iOS applications support them via universal links. Read the [official Android documentation](https://developer.android.com/training/app-links) and the [official iOS documentation](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) to understand how to implement Android App Links and universal links respectively.

Once your applications support redirection via app-claimed HTTPS, you should update your app's configuration in the Singpass Developer Portal to add your new HTTPS URLs. Refer to our [Singpass Developer Portal User Guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) if you are unsure on how to do this.

You will also need to update your backend integration with us. Specifically, you will need to change these parameters in your authorization request:

1. The `redirect_uri` and `app_launch_url` parameters must be updated to use the new HTTPS URLs that you have configured.
2. The `redirect_uri_https_type` parameter in the authorization request should be added with a value of `app_claimed_https` , to indicate that the redirection is being done using an app-claimed HTTPS URL.

Once the backend changes are completed and deployed, you should proceed to remove the old custom scheme URLs from your app's configuration in the Singpass Developer Portal.

### Authorization Request

#### 1. Use pushed authorization request

In your existing integration, you would have sent the authorization request by redirecting the user to the authorization endpoint, with the authorization request parameters being included as query parameters.

In the new integration, you should instead send the authorization request parameters by first sending the authorization request parameters via a pushed authorization request, which will return a short-lived `request_uri` in the response. You should then redirect the user the user to the authorization endpoint, with the `request_uri`, together with your `client_id`, as query parameters.

For more details, you may refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request).

#### 2. Add parameters for Proof Key for Code Exchange (PKCE)

PKCE is required for all apps in the new API. If you are not yet sending `code_challenge` and `code_challenge_method` in your authentication request, you are required to do so for the new API.

Read our [guide on PKCE](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce) to better understand what you need to do.

#### 3. (Only for Login apps) Add authentication\_context\_type to the authentication request

If you are integrating using a Login app, you will need to add a new parameter called `authentication_context_type` into the authorization request parameters, which should be sent as part of the pushed authorization request. Read more about this new parameter in our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request#singpass-specific-parameters).

### Token Exchange

#### 1. Implement decryption of the ID token

In the new authentication API, all ID tokens will be encrypted. You will need to implement ID token decryption if you are currently receiving unencrypted ID tokens during token exchange. Additionally, you must add an encryption key to your JWKS if you do not already have one.

{% hint style="info" %}
You will be receiving unencrypted ID tokens if your app's profile type is set to "UUID Only". You can view your app's profile type in the [Singpass Developer Portal](mailto:undefined).
{% endhint %}

No changes are required if you are already performing decryption of the ID token.

You can refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token) to better understand how the ID token is being encrypted.

#### 2. Update parsing of the sub claim

Previously, the `sub` claim in the ID token contained comma-separated key-value pairs containing various attributes. It now contains only the user's UUID:

<table><thead><tr><th>Previous</th><th>New</th></tr></thead><tbody><tr><td><pre class="language-json"><code class="lang-json">{
  "sub": "s=S8829314B,u=1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9"
}
</code></pre></td><td><pre class="language-json"><code class="lang-json">{
  "sub": "1c0cee38-3a8f-4f8a-83bc-7a0e4c59d6a9"
}
</code></pre></td></tr></tbody></table>

Due to this change, you should remove any custom parsing logic that you have previously implemented to extract the values of each field from the `sub` claim. If you require only the user's UUID, you can now simply read the value of the `sub` claim without needing any more parsing. Read the next section if you require other details that was previously in the `sub` claim.

#### 3. (For Login apps only) Request for the new `user.identity` scope and read the new `sub_attributes` claim

In your current integration, you may be retrieving the following information from the `sub` claim in the ID token:

* The user's NRIC/FIN
* The user's foreign ID or the country of issuance for the foreign ID (for Singapore Foreign Account users)

In the new integration, this information is now instead returned in a newly introduced `sub_attributes` claim in the ID token. For this new claim to be returned, you must first update your app's configuration in the Singpass Developer Portal to request for the new `user.identity` scope for your app. Refer to our [Singpass Developer Portal User Guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) if you are unsure on how to do this.

Once the new scope has been approved, the `sub_attributes` claim will be returned in the ID token if you are using the new API. Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token#the-sub_account-claim) to understand the structure of this new claim.

{% hint style="warning" %}
If you are not retrieving and/or do not plan to retrieve NRIC/FIN or foreign ID/country of issuance from the ID token, you do not need to request for the `user.identity` scope.

Please note that you will need to provide justification if you want to request for the scope.
{% endhint %}

### Userinfo Request (For Myinfo apps only)

#### 1. Handle the new format of the userinfo response

The userinfo response will have a slightly different format. The format of the data itself remains unchanged - the only difference is that the data is now nested inside a `person_info` field.

You will thus need to update your parsing logic to extract the user's data from the `person_info` field, instead of from the root of the response data.

#### 2. Update Authorization header prefix to be DPoP instead of Bearer

In the old API, the Authorization header would have been sent as a bearer token, in this format:

```
Authorization: Bearer <your_access_token>
```

In the new API, it should be sent with a `DPoP` prefix instead:

```
Authorization: DPoP <your_access_token>
```


# Myinfo (v3) apps

## Overview

The Myinfo (v3) integration differs significantly from the new Authentication API, as while Myinfo (v3) wes based on OAuth 2.0, the new Authentication API is based on OIDC with the FAPI 2.0 Security Profile, which contains several extensions to the OAuth 2.0 flow.

Due to these differences, we recommend that you perform a new integration from scratch using one of the [certified OIDC Relying Party Libraries](https://openid.net/developers/certified-openid-connect-implementations/), instead of updating your existing integration. Doing so should simplify your integration. You can refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide) to understand how to perform a new integration.

Regardless of which approach you choose to take, this document will highlight all of the differences between your existing integration and the new integration.

## Creating New App

Before you start on the new integration, you must create a new Myinfo (v5) app on the Singpass Developer Portal. Your existing Myinfo (v3) app cannot be used directly for the new integration.

**Recommended:** Use the **Duplicate app** function to migrate your existing Myinfo (v3/v4) app to Myinfo v5. This carries over your existing configuration and does not require re-review or re-approval. See the [Duplicate an app guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/duplicate-an-app) for step-by-step instructions.

Alternatively, if you need to change your app name, purpose, scope selection, or user journey, create a new app from scratch using the [staging app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app) and [production app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app) guides.

There are two important differences between the setup for Myinfo (v3) apps and Myinfo (v5) apps:

1. Myinfo (v5) apps should only have a single purpose. If your current Myinfo (v3) app has multiple purposes, duplicate or create a new Myinfo (v5) app for each purpose.
2. Myinfo (v5) apps perform authentication and verification using JSON Web Key Sets (JWKS) instead of using X.509 public key certificates. You will be required to configure your JWKS instead of your certificate when creating your new Myinfo (v5) apps. Your JWKS must have at least one signing key and one encryption key.

## Changes Required

### General

#### 1. Implement Demonstrating of Proof of Possession (DPoP)

DPoP is a security mechanism in which the access token and authorization code is bound to a ephemeral private key that is known only to you, preventing malicious parties from using your code or token.

Read our [DPoP guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) for instructions on how to implement DPoP.

#### 2. Update custom scheme URLs

The new Authentication API no longer supports the use of custom scheme URLs (i.e. URLs that do not start with `https://` ) as redirect URLs or app launch URLs.

If you are currently integrating with Myinfo via an Android or iOS app, and rely on such URLs for redirection back to the mobile app, you will need to change these URLs to use app-claimed HTTPS URLs instead. App-claimed HTTPS URLs are HTTPS URLs which, when opened on a mobile device, will launch your mobile app.

Android applications support app-claimed HTTPS URLs via Android App Links, while iOS applications support them via universal links. Read the [official Android documentation](https://developer.android.com/training/app-links) and the [official iOS documentation](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) to understand how to implement Android App Links and universal links respectively.

Once your applications support redirection via app-claimed HTTPS, you should update your app's configuration in the Singpass Developer Portal to add your new HTTPS URLs. Refer to our [Singpass Developer Portal User Guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) if you are unsure on how to do this.

You will also need to update your backend integration with us. Specifically, you will need to change these parameters in your authorization request:

1. The `redirect_uri` and `app_launch_url` parameters must be updated to use the new HTTPS URLs that you have configured.
2. The `redirect_uri_https_type` parameter in the authorization request should be added with a value of `app_claimed_https` , to indicate that the redirection is being done using an app-claimed HTTPS URL.

Once the backend changes are completed and deployed, you should proceed to remove the old custom scheme URLs from your app's configuration in the Singpass Developer Portal.

### Authorization Request

#### 1. Use pushed authorization request

In your existing integration, you would have sent the authorization request by redirecting the user to the authorization endpoint, with the authorization request parameters being included as query parameters.

In the new integration, you should instead send the authorization request parameters by first sending the authorization request parameters via a pushed authorization request, which will return a short-lived `request_uri` in the response. You should then redirect the user the user to the authorization endpoint, with the `request_uri`, together with your `client_id`, as query parameters.

For more details, you may refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request).

#### 2. Remove parameters that are no longer used

There are some parameters in the authorization request which are no longer required in the new API. These parameters should be removed from the authorization request:

* `authmode`
* `purpose` (this will be configured in the Singpass Developer Portal instead of being sent for every request)
* `login_type`

#### 3. Update existing parameters

There are some parameters used in the Myinfo (v3) parameters which are still used in the new API, but they have been changed, as detailed below:

<table><thead><tr><th width="186.48046875">Old parameter name</th><th width="193.08203125">New parameter name</th><th>Other changes</th></tr></thead><tbody><tr><td>attributes</td><td>scope</td><td><p>This needs to be changed from a comma-separated string to a space-separated string, and <code>openid</code> has to be added. For example:</p><ul><li>old: <code>name,hanyupinyinname</code></li><li>new: <code>openid name hanyupinyinname</code></li></ul></td></tr><tr><td>appLaunchURL</td><td>app_launch_url</td><td>The app launch URL you are using will need to be pre-registered in the Singpass Developer Portal</td></tr></tbody></table>

#### 4. Add parameters for Proof of Key Code Exchange (PKCE)

You are required to implement PKCE for the authentication flow in the new API. Read our [PKCE guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce) for instructions on how to implement PKCE.

#### 5. Add nonce parameter

You are required to include a `nonce` in your authorization request for the new API. Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request#basic-oidc-parameters) to understand how the `nonce` should be generated and what it is used for.

### Token Exchange

#### 1. Add parameters for Proof of Key Code Exchange (PKCE)

As part of the PKCE implementation, you will need to include the `code_verifier` as part of the request body when making the request to the token endpoint. This must be the same `code_verifier` that you had used to generate the `code_challenge` when making the authorization request earlier.

#### 2. Authenticate using client assertion instead of PKI Signature

In the new API, you will authenticate yourself when calling the token endpoint by generating a client assertion instead of a PKI signature. Specifically:

* You should no longer send an `Authorization` header when calling the token endpoint
* You should no longer send the `client_secret` in the request body
* You will need to send `client_assertion` and `client_assertion_type` in the request body. Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange#request-body) to understand what the values of these parameters should be.

#### 3. Remove the state parameter

The new API does not support the `state` parameter in the request body, so it should be removed.

#### 4. Parse the ID token

In the new API, the token request returns an encrypted ID token in addition to the access token. You should decrypt this ID token and perform verification checks to ensure that it is legitimate.

Read our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token) to understand how to perform the decryption and what sort of verification checks are required.

### Userinfo Request

The userinfo request replaces the Person API call used in Myinfo (v3). Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#sample-request) for the full specifications of the new userinfo request.

Here's a quick comparison of the two endpoints:

<table><thead><tr><th width="99.50390625"></th><th>Userinfo</th><th>Person API</th></tr></thead><tbody><tr><td>Request</td><td><pre class="language-http" data-overflow="wrap"><code class="lang-http">GET /userinfo HTTP/1.1
Host: id.singpass.gov.sg
Authorization: DPoP eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJzdWIiOiJ1c2VyLWphbmUtZG9lIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vZGF0YSIsImV4cCI6MTc1NjczMDM4MCwiaWF0IjoxNzI1MTk0MzgwLCJqdGkiOiJ0eC0xMjMtYWJjIiwiY25mIjp7ImprdCI6Ik93SWlGaVl2T0NXRkpiV1hlbUdUZzRtU1NYQkNwZk9NaFhRV21XOTBVSEEifX0.dGhpcy1pcy1hLXBsYWNlaG9sZGVyLXNpZ25hdHVyZS1hcy1pdC1yZXF1aXJlcy1hLXByaXZhdGUta2V5
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiQXNWakh4elZ4MURaNnNKcEpzUnM2ek5YYXFmcFR3UmNfcXV0bWw0aEFJQSIsInkiOiI0SkhwVVZDRE5DaXhOTW9OclIzSElodFRzTWNfMF9NcmdpMzJxR3VoUkQ4In19.eyJqdGkiOiIyZmM3Y2Q4ZC0xN2IzLTRlYTUtYTg4ZC1lZWM0NTY5M2JhZDQiLCJodG0iOiJHRVQiLCJodHUiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy91c2VyaW5mbyIsImlhdCI6MTc1NjcwODI0N30.wBYjFQRzY2o5aG82LjR1X8qT9bZ-jK3c7hI5fE0gP9vR_7sU6tW5xV4yZ3aB2cE1dF0eG9hI8jJ7kL6mN5oP4qR
</code></pre></td><td><pre class="language-http" data-overflow="wrap"><code class="lang-http">GET /com/v3/person/{sub}?attributes=name,uinfin&#x26;client_id=EXAMPLE_CLIENT HTTP/1.1
Host: api.myinfo.gov.sg
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
IZcexfrAVQYA==",Bearer eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJzdWIiOiJ1c2VyLWphbmUtZG9lIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vZGF0YSIsImV4cCI6MTc1NjczMDM4MCwiaWF0IjoxNzI1MTk0MzgwLCJqdGkiOiJ0eC0xMjMtYWJjIiwiY25mIjp7ImprdCI6Ik93SWlGaVl2T0NXRkpiV1hlbUdUZzRtU1NYQkNwZk9NaFhRV21XOTBVSEEifX0.dGhpcy1pcy1hLXBsYWNlaG9sZGVyLXNpZ25hdHVyZS1hcy1pdC1yZXF1aXJlcy1hLXByaXZhdGUta2V5
</code></pre></td></tr><tr><td>Response</td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "person_info": {
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
    }
  },
  // above scopes are returned in the same format as the Myinfo Get Person response
  "iss": "https://id.singpass.gov.sg/fapi",
  "sub": "d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "iat": 1746678089
}
</code></pre></td><td><pre class="language-json"><code class="lang-json">{
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
  }
}
</code></pre></td></tr></tbody></table>

The exact changes required are listed below.

#### 1. Remove sub from the path

In Myinfo (v3), you were required to pass the `sub` from the access token as a path parameter when calling the Person API. This is no longer required in the new API. You should no longer perform any parsing of the access token.

If you still wish to obtain the UUID of the user, you should do so by parsing the ID token instead.

#### 2. Remove PKI Signature

PKI signature is no longer needed for the API call. Instead, authentication is done via [DPoP](#id-1.-implement-demonstration-of-proof-of-possession-dpop) and the access token.

Thus, you should update your Authorization header to only include the access token in the format `DPoP <your_access_token>`.

#### 3. Remove all query parameters

The new API does not require any query parameters in the userinfo request. All of the user's data belonging to the scopes requested during the Authorization request will be returned.

#### 4. Handle the new format of the userinfo response

The userinfo response has a slightly different format compared to the response of the Person API. The format of the data itself remains unchanged - the only difference is that the data is now nested inside a `person_info` field.

You will thus need to update your parsing logic to extract the user's data from the `person_info` field, instead of from the root of the response data.

#### 5. Update access token prefix

When calling the Person API, your access token would have had a `Bearer` prefix:

```
Authorization: Bearer <your_access_token>
```

In the new API, you should change this prefix to `DPoP`:

```
Authorization: DPoP <your_access_token>
```


# Myinfo (v4) apps

## Overview

The protocol used by Myinfo (v4) apps is largely similar to the one used by the new FAPI 2.0 API. The changes required mostly involve configuring new Myinfo (v5) apps, adopting Pushed Authorization Requests, and making minor changes to your request/response parsing.

## Creating New App

Before you start on the new integration, you must create a new Myinfo (v5) app on the Singpass Developer Portal. Your existing Myinfo (v4) app cannot be used directly for the new integration.

**Recommended:** Use the **Duplicate app** function to migrate your existing Myinfo (v4) app to Myinfo v5. This carries over your existing configuration and does not require re-review or re-approval. See the [Duplicate an app guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/duplicate-an-app) for step-by-step instructions.

Alternatively, if you need to change your app name, purpose, scope selection, or user journey, create a new app from scratch using the [staging app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app) and [production app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app) guides.

Note that Myinfo (v5) apps should only have a single purpose. If your current Myinfo (v4) app has multiple purposes, duplicate or create a new Myinfo (v5) app for each purpose.

## Changes Required

Listed below are the changes that you will need to make to your existing integration for it to work with the new authentication API.

### General

#### 1. Update custom scheme URLs

The new Authentication API no longer supports the use of custom scheme URLs (i.e. URLs that do not start with `https://` ) as redirect URLs or app launch URLs.

If you are currently integrating with Singpass via an Android or iOS app, and rely on such URLs for redirection back to the mobile app, you will need to change these URLs to use app-claimed HTTPS URLs instead. App-claimed HTTPS URLs are HTTPS URLs which, when opened on a mobile device, will launch your mobile app.

Android applications support app-claimed HTTPS URLs via Android App Links, while iOS applications support them via universal links. Read the [official Android documentation](https://developer.android.com/training/app-links) and the [official iOS documentation](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) to understand how to implement Android App Links and universal links respectively.

Once your applications support redirection via app-claimed HTTPS, you should update your app's configuration in the Singpass Developer Portal to add your new HTTPS URLs. Refer to our [Singpass Developer Portal User Guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) if you are unsure on how to do this.

You will also need to update your backend integration with us. Specifically, you will need to change these parameters in your authorization request:

1. The `redirect_uri` and `app_launch_url` parameters must be updated to use the new HTTPS URLs that you have configured.
2. The `redirect_uri_https_type` parameter in the authorization request should be added with a value of `app_claimed_https` , to indicate that the redirection is being done using an app-claimed HTTPS URL.

Once the backend changes are completed and deployed, you should proceed to remove the old custom scheme URLs from your app's configuration in the Singpass Developer Portal.

### Authorization Request

#### 1. Use pushed authorization request

In your existing integration, you would have sent the authorization request by redirecting the user to the authorization endpoint, with the authorization request parameters being included as query parameters.

In the new integration, you should instead send the authorization request parameters by first sending the authorization request parameters via a pushed authorization request, which will return a short-lived `request_uri` in the response. You should then redirect the user the user to the authorization endpoint, with the `request_uri`, together with your `client_id`, as query parameters.

Note that the DPoP header needs to be sent when making the pushed authorization request. The DPoP header that you send for this request should be generated in the same way as the DPoP header you currently generate when calling the token API for your Myinfo (v4) app.

For more details, you may refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/pages/wD2EDNbwA7OcSQ788qVw#id-1.-sending-the-pushed-authorization-request).

#### 2. Remove parameters that are no longer used

There are some parameters in the authorization request which are no longer required in the new API. These parameters should be removed from the authorization request:

* `subentity_id`
* `purpose_id` (this will be configured in the Singpass Developer Portal instead of being sent for every request)

#### 3. Ensure app\_launch\_url is pre-registered in the Singpass Developer Portal

In the new Authentication API, the app launch URLs must be pre-registered with us when you configure your app in the Singpass Developer Portal.

If you use the `app_launch_url` parameter, you will need to ensure that the value you are sending in this parameter has been pre-registered in your app's configuration.

#### 4. Add nonce and state parameter

You are required to include a `nonce` and `state` in your authorization request for the new API. Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request#basic-oidc-parameters) to understand how these parameters should be generated and what they are used for.

### Token Exchange

#### 1. Parse the ID token

In the new API, the token request returns an encrypted ID token in addition to the access token. You should decrypt this ID token and perform verification checks to ensure that it is legitimate.

Read our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token) to understand how to perform the decryption and what sort of verification checks are required.

#### 2. Update your client assertion implementation

You should no longer include `cnf.jkt` in the JWT payload for your client assertion. Aside from this change, the method to generate the client assertion should be the same as the method you are currently using for your Myinfo (v4) app.

Refer to our [guide on generating client assertions](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) for the full reference on generating client assertions for the new API.

### Userinfo Request

The userinfo request replaces the Person API call used in Myinfo (v4), but the authentication mechanism is the same. Refer to our [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#sample-request) to view a sample request.

Here's a quick comparison of the two endpoints:

<table><thead><tr><th width="99.50390625"></th><th>Userinfo</th><th>Person API</th></tr></thead><tbody><tr><td>Request</td><td><pre class="language-http" data-overflow="wrap"><code class="lang-http">GET /fapi/userinfo HTTP/1.1
Host: id.singpass.gov.sg
Authorization: DPoP eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJzdWIiOiJ1c2VyLWphbmUtZG9lIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vZGF0YSIsImV4cCI6MTc1NjczMDM4MCwiaWF0IjoxNzI1MTk0MzgwLCJqdGkiOiJ0eC0xMjMtYWJjIiwiY25mIjp7ImprdCI6Ik93SWlGaVl2T0NXRkpiV1hlbUdUZzRtU1NYQkNwZk9NaFhRV21XOTBVSEEifX0.dGhpcy1pcy1hLXBsYWNlaG9sZGVyLXNpZ25hdHVyZS1hcy1pdC1yZXF1aXJlcy1hLXByaXZhdGUta2V5
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiQXNWakh4elZ4MURaNnNKcEpzUnM2ek5YYXFmcFR3UmNfcXV0bWw0aEFJQSIsInkiOiI0SkhwVVZDRE5DaXhOTW9OclIzSElodFRzTWNfMF9NcmdpMzJxR3VoUkQ4In19.eyJqdGkiOiIyZmM3Y2Q4ZC0xN2IzLTRlYTUtYTg4ZC1lZWM0NTY5M2JhZDQiLCJodG0iOiJHRVQiLCJodHUiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy91c2VyaW5mbyIsImlhdCI6MTc1NjcwODI0N30.wBYjFQRzY2o5aG82LjR1X8qT9bZ-jK3c7hI5fE0gP9vR_7sU6tW5xV4yZ3aB2cE1dF0eG9hI8jJ7kL6mN5oP4qR
</code></pre></td><td><pre class="language-http" data-overflow="wrap"><code class="lang-http">GET /com/v4/person/{sub}?scope=name,uinfin HTTP/1.1
Host: api.myinfo.gov.sg
Authorization: DPoP eyJ0eXAiOiJhdCtqd3QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJzdWIiOiJ1c2VyLWphbmUtZG9lIiwiYXVkIjoiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20vZGF0YSIsImV4cCI6MTc1NjczMDM4MCwiaWF0IjoxNzI1MTk0MzgwLCJqdGkiOiJ0eC0xMjMtYWJjIiwiY25mIjp7ImprdCI6Ik93SWlGaVl2T0NXRkpiV1hlbUdUZzRtU1NYQkNwZk9NaFhRV21XOTBVSEEifX0.dGhpcy1pcy1hLXBsYWNlaG9sZGVyLXNpZ25hdHVyZS1hcy1pdC1yZXF1aXJlcy1hLXByaXZhdGUta2V5
DPoP: eyJhbGciOiJFUzI1NiIsInR5cCI6ImRwb3Arand0IiwiandrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYiLCJ4IjoiQXNWakh4elZ4MURaNnNKcEpzUnM2ek5YYXFmcFR3UmNfcXV0bWw0aEFJQSIsInkiOiI0SkhwVVZDRE5DaXhOTW9OclIzSElodFRzTWNfMF9NcmdpMzJxR3VoUkQ4In19.eyJqdGkiOiIyZmM3Y2Q4ZC0xN2IzLTRlYTUtYTg4ZC1lZWM0NTY5M2JhZDQiLCJodG0iOiJHRVQiLCJodHUiOiJodHRwczovL2lkLnNpbmdwYXNzLmdvdi5zZy91c2VyaW5mbyIsImlhdCI6MTc1NjcwODI0N30.wBYjFQRzY2o5aG82LjR1X8qT9bZ-jK3c7hI5fE0gP9vR_7sU6tW5xV4yZ3aB2cE1dF0eG9hI8jJ7kL6mN5oP4qR
</code></pre></td></tr><tr><td>Response</td><td><pre class="language-json" data-overflow="wrap"><code class="lang-json">{
  "person_info": {
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
    }
  },
  // above scopes are returned in the same format as the Myinfo Get Person response
  "iss": "https://id.singpass.gov.sg/fapi",
  "sub": "d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "iat": 1746678089
}
</code></pre></td><td><pre class="language-json"><code class="lang-json">{
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
  }
}
</code></pre></td></tr></tbody></table>

#### 1. Remove sub from the path

In Myinfo (v4), you were required to pass the `sub` from the access token as a path parameter when calling the Person API. This is no longer required in the new API. You should no longer perform any parsing of the access token.

If you still wish to obtain the UUID of the user, you should do so by parsing the ID token instead.

#### 2. Remove all query parameters

The new API does not require any query parameters in the userinfo request. All of the user's data belonging to the scopes requested during the Authorization request will be returned.

#### 3. Handle the new format of the userinfo response

The userinfo response has a slightly different format compared to the response of the Person API. The format of the data itself remains unchanged - the only difference is that the data is now nested inside a `person_info` field.

You will thus need to update your parsing logic to extract the user's data from the `person_info` field, instead of from the root of the response data.


# Myinfo Business (v1/v2) Person v3 flows

Migration guide for Myinfo Business (v1/v2) partners whose applications use the legacy Myinfo v3 APIs to retrieve individual information.

{% hint style="warning" %}

### Who this guide is for

This guide applies only to existing **Myinfo Business (v1/v2)** partners whose **Myinfo Business application** retrieves **individual information** using the legacy Myinfo v3 APIs.

Specifically, this guide applies if your application currently uses the following endpoints:

If your integration uses these endpoints, this guide explains how to migrate your individual retrieval flow to **Myinfo (v5)** using **OpenID Connect (OIDC)** and the **FAPI 2.0 Security Profile**.
{% endhint %}

| Endpoint                   | Purpose                                             |
| -------------------------- | --------------------------------------------------- |
| `GET /com/v3/authorise`    | Authenticate the user and obtain consent            |
| `POST /com/v3/token`       | Exchange the authorisation code for an access token |
| `GET /com/v3/person/{sub}` | Retrieve the individual's Myinfo information        |

{% hint style="info" %}

### What is not covered

This guide covers **only** the migration of the **individual information retrieval flow**.

It does **not** cover the migration of **Myinfo Business entity APIs**, including endpoints such as:

* `GET /biz/v2/entity-person/{uen}/{uuid}`
* Other Myinfo Business entity APIs

If your application uses these APIs, refer to the [**Myinfo Business (v1/v2) to v3 (FAPI 2.0) Migration Guide**](https://docs.corppass.gov.sg/technical-specifications/corppass-authorization-api-fapi-2.0/migration-guides/migration-guide-myinfo-business-v1-v2-to-v3-fapi-2.0). The entity retrieval flow has its own migration path and should be migrated separately.

If your application uses both the legacy Myinfo Person APIs and the Myinfo Business entity APIs, you will need to follow **both migration guides**.
{% endhint %}

## Overview

Some Myinfo Business partners use their Myinfo Business application to retrieve both:

* **Business entity information** through the Myinfo Business APIs.
* **Individual information** through the legacy Myinfo Person APIs.

These two retrieval flows are independent and have separate migration paths.

This guide covers **only the migration of the individual information retrieval flow** from the legacy Myinfo v3 APIs to **Myinfo (v5)**.

Because the Myinfo (v5) security model differs significantly from the legacy implementation, you must onboard a new Myinfo (v5) application and obtain a new client ID. Existing Myinfo v3 applications and credentials cannot be reused. Given these changes, Singpass recommends implementing the new flow using a certified OpenID Connect Relying Party library instead of modifying your existing Myinfo Business v1/v2 integration.

The table below summarises the key differences between the legacy and new implementations.

| Legacy mechanism (v1 / v2 / v3)                                                       | New mechanism (v5 / FAPI 2.0)                                          |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Authorization request via browser redirect with query parameters                      | **Pushed Authorization Request (PAR)** — RFC 9126                      |
| `PKI_SIGN` request signing (RSA signature over a base string) with X.509 certificates | **Client assertion** (`private_key_jwt`) + **JWKS**                    |
| `client_secret` in the token request                                                  | **Client assertion** (no shared secret)                                |
| Bearer access tokens                                                                  | **DPoP-bound** authorization codes & access tokens                     |
| No PKCE                                                                               | **PKCE (S256)** — mandatory                                            |
| Person API: `GET /com/v3/person/{sub}?attributes=…`                                   | **`GET /userinfo`** (no path or query parameters)                      |
| Access token only                                                                     | Access token **+ encrypted ID token** (must be decrypted and verified) |

## Before you start: create a new Myinfo (v5) app

Your existing Myinfo v3 credentials — `client_id`, `client_secret`, APP ID and PKI certificates — **cannot be reused**. Complete onboarding first.

1. **Create a new Myinfo (v5) app** on the [Singpass Developer Portal](https://developers.singpass.gov.sg/). Create a [staging app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app) for testing, then a [production app](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app) for go-live.
2. **One purpose per app.** Myinfo (v5) apps must have a **single purpose**. If your current v3 app serves multiple purposes, create **one v5 app per purpose**. The purpose is now configured in the portal and is no longer sent in each request.
3. **Configure a JWKS** (JSON Web Key Set) instead of uploading an X.509 certificate. Your JWKS must contain at least **one signing key** (for client assertions) and **one encryption key** (so Singpass can encrypt the ID token to you).
4. **Register HTTPS redirect URIs.** Only `https://` URLs are accepted — see [Replace custom scheme URLs](#replace-custom-scheme-urls-mobile-apps-only) for mobile apps.
5. **Map your attributes to v5 scopes.** Translate your current `attributes` list into the equivalent scopes from the Singpass Data Catalog, and confirm the scopes allowed for your app during onboarding.

## General changes

These apply across the whole flow.

### Implement DPoP (Demonstrating Proof of Possession)

DPoP binds your authorization code and access token to an **ephemeral private key** known only to you, so a stolen code or token cannot be replayed by another party.

Your application must:

* Generate an ephemeral EC key pair (e.g. P-256) per authentication flow.
* Attach a signed **`DPoP` header** — a JWT containing the HTTP method (`htm`), target URI (`htu`), a unique `jti` and `iat` — to the **pushed authorization request**, the **token request**, and the **userinfo request**.
* Reuse the same key pair for all three calls in a single flow so the token stays bound to it.

See the [DPoP guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) for the exact JWT structure.

### Replace custom scheme URLs (mobile apps only)

The new API **does not support custom scheme URLs** (anything that does not start with `https://`) as redirect or app-launch URLs.

If your Android/iOS app currently uses a custom scheme (e.g. `myapp://callback`):

1. Implement **app-claimed HTTPS URLs** — [Android App Links](https://developer.android.com/training/app-links) or [iOS Universal Links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app).
2. Register the new HTTPS URLs in the Developer Portal.
3. In the authorization request, set `redirect_uri` / `app_launch_url` to the new HTTPS URLs and add **`redirect_uri_https_type=app_claimed_https`**.
4. After deployment, remove the old custom-scheme URLs from your app configuration.

Note the rename: `appLaunchURL` → **`app_launch_url`**, which must be pre-registered in the portal.

## Step-by-step flow changes

### Step 1 — Authorization request: redirect → Pushed Authorization Request

**Old (v3):** your webpage redirected the browser to the authorise endpoint with all parameters in the query string.

**New (v5):** two sub-steps:

1. Send a **server-to-server `POST`** to the `pushed_authorization_request_endpoint` (published in Singpass's OpenID configuration), with an `application/x-www-form-urlencoded` body and a **DPoP header**. This returns a short-lived **`request_uri`**.
2. **Redirect the browser** to the authorization endpoint with only **two** query parameters: `client_id` and `request_uri`.

Parameter changes in the authorization request:

| Change                                                              | Detail                                                                                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Remove** `authmode`                                               | No longer used                                                                                                                                     |
| **Remove** `purpose`                                                | Configured per app in the Developer Portal                                                                                                         |
| **Remove** `login_type`                                             | No longer used                                                                                                                                     |
| **Rename** `attributes` → `scope`                                   | Change from **comma-separated** to **space-separated**, and prepend **`openid`**. Old: `name,hanyupinyinname` → New: `openid name hanyupinyinname` |
| **Rename** `appLaunchURL` → `app_launch_url`                        | Must be pre-registered (mobile)                                                                                                                    |
| **Add** PKCE                                                        | `code_challenge` (base64url SHA-256 of your `code_verifier`) and `code_challenge_method=S256`                                                      |
| **Add** `nonce`                                                     | A unique, unguessable value per request; echoed back in the ID token and must be verified                                                          |
| **Keep** `state`, `redirect_uri`, `client_id`, `response_type=code` | `state` still protects against CSRF and reconciles the callback                                                                                    |

### Step 2 — Callback handling

Conceptually unchanged: the user is redirected to your `redirect_uri` with `code` and `state`. Continue to verify that `state` matches the value you sent. Error callbacks (`error`, `error_description`) still apply.

### Step 3 — Token exchange

**Old (v3):** `POST /token` with a `PKI_SIGN` Authorization header, plus `client_secret`, `client_id`, `code`, `redirect_uri`, `grant_type` and `state` in the body.

**New (v5):** `POST` to the token endpoint with these changes:

| Change                                               | Detail                                                                                                                                            |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Remove** the `Authorization: PKI_SIGN …` header    | No more base-string request signing                                                                                                               |
| **Remove** `client_secret`                           | Replaced by client assertion                                                                                                                      |
| **Remove** `state`                                   | Not supported in the token request body                                                                                                           |
| **Add** `client_assertion` + `client_assertion_type` | `client_assertion` is a JWT signed with your **JWKS signing key**; `client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer` |
| **Add** `code_verifier`                              | The same verifier used to derive `code_challenge` in Step 1 (PKCE)                                                                                |
| **Add** `DPoP` header                                | Same key pair as used for the PAR                                                                                                                 |

**New — handling the ID token.** The token response now returns an **encrypted ID token** alongside the access token. You must:

1. **Decrypt** the ID token with your **JWKS encryption private key**.
2. **Verify** the inner JWS signature against Singpass's published JWKS.
3. **Validate** the `iss`, `aud` (your `client_id`), `exp` claims, and confirm `nonce` matches the value sent in Step 1.
4. If you need the user's **UUID** (`sub`), read it from the **ID token** — do **not** parse the access token.

{% hint style="info" %}
The access token has a lifetime of **30 minutes**.
{% endhint %}

### Step 4 — Person data retrieval: Person API → Userinfo

This is the core change for your team.

**Old — Myinfo v3 Person API:**

```http
GET /com/v3/person/{sub}?attributes=uinfin,name&client_id=YOUR_CLIENT HTTP/1.1
Host: api.myinfo.gov.sg
Authorization: PKI_SIGN app_id="...", nonce="...", signature_method="RS256",
               signature="...", timestamp="...",Bearer <access_token>
```

**New — Myinfo v5 Userinfo:**

```http
GET /userinfo HTTP/1.1
Host: id.singpass.gov.sg
Authorization: DPoP <access_token>
DPoP: <dpop_proof_jwt>
```

Required changes:

1. **Remove `sub` from the path.** The endpoint identifies the user from the token; you no longer parse the access token to build the URL.
2. **Remove the PKI signature.** Authentication is via DPoP + the access token only.
3. **Remove all query parameters** (`attributes`, `client_id`, `txnNo`). All data for the **scopes requested in Step 1** is returned — the request carries no attribute list.
4. **Change the token prefix** from `Bearer` to **`DPoP`**.
5. **Include the `DPoP` proof header**.

### Step 5 — Parsing the userinfo response

The **format of each attribute is unchanged** from the Person API (same `value` / `code`+`desc` / `source` / `classification` / `lastupdated` structure your parsers already handle). The only difference is that person data is now nested inside a **`person_info`** field, alongside standard OIDC claims.

{% tabs %}
{% tab title="Old (Person API — root level)" %}

```json
{
  "uinfin": { "lastupdated": "2024-09-26", "source": "1", "classification": "C", "value": "S9000001B" },
  "name":   { "lastupdated": "2024-09-26", "source": "1", "classification": "C", "value": "SOH HAO FENG" }
}
```

{% endtab %}

{% tab title="New (Userinfo — nested under person\_info)" %}

```json
{
  "person_info": {
    "uinfin": { "lastupdated": "2024-09-26", "source": "1", "classification": "C", "value": "S9000001B" },
    "name":   { "lastupdated": "2024-09-26", "source": "1", "classification": "C", "value": "SOH HAO FENG" }
  },
  "iss": "https://id.singpass.gov.sg/fapi",
  "sub": "d45d8f21-6178-4713-b962-8635ed2a945a",
  "aud": "T5sM5a53Yaw3URyDEv2y9129CbElCN2F",
  "iat": 1746678089
}
```

{% endtab %}
{% endtabs %}

**Action:** point your existing parsing logic at `response.person_info` instead of the response root. Your downstream mapping should otherwise be reusable.

## What you can decommission after cutover

Once the v5 flow is live and the v3 flow is retired:

* `PKI_SIGN` base-string construction and RSA-SHA256 request-signing code
* X.509 certificate management for API request signing
* `client_secret` storage and rotation for the person flow
* Access-token parsing used to extract `sub` for the Person API path
* Custom scheme URL handling (mobile)
* The v3 app registration itself, after Singpass confirms deactivation

{% hint style="success" %}
**Keep** your JWE/JWS decryption utilities — you will repurpose the concept (with new keys and algorithms) for **ID token decryption**, and your Myinfo Business Entity-Person flow still uses payload decryption per the biz v2 spec.
{% endhint %}

## Migration checklist

**Onboarding**

* [ ] New Myinfo (v5) staging app created (one per purpose)
* [ ] JWKS configured (≥ 1 signing key, ≥ 1 encryption key)
* [ ] HTTPS redirect URIs registered; app-claimed HTTPS set up for mobile
* [ ] Attributes mapped to v5 scopes; allowable scopes confirmed

**Build**

* [ ] Certified OIDC RP library integrated
* [ ] PAR implemented (server-to-server, with DPoP header)
* [ ] PKCE implemented (`code_challenge` / `code_verifier`, S256)
* [ ] `nonce` generation and verification implemented
* [ ] Client assertion (`private_key_jwt`) implemented for the token endpoint
* [ ] ID token decryption + signature verification + claim validation implemented
* [ ] Userinfo call implemented (`Authorization: DPoP`, DPoP proof header, no query params)
* [ ] Response parsing updated to read from `person_info`
* [ ] Old parameters removed: `authmode`, `purpose`, `login_type`, `state` (token request), `client_secret`, `PKI_SIGN`

**Test (staging)**

* [ ] End-to-end happy path with test accounts
* [ ] Negative tests: expired access token (30-min lifetime), invalid DPoP proof, mismatched `nonce`/`state`, replayed authorization code
* [ ] Consent-denied and browser-abandonment paths (verify `state` reconciliation)
* [ ] Mobile: App Links / Universal Links return-to-app verified on both platforms

**Cutover**

* [ ] Production app created and configured
* [ ] Staged rollout plan (run v3 and v5 in parallel where feasible)
* [ ] Monitoring/alerting on new error codes (`invalid_token`, `invalid_dpop_proof`, `invalid_request`)
* [ ] v3 person flow and legacy credentials decommissioned

## Common pitfalls

1. **Reusing the v3 app or credentials** — a new v5 app is mandatory; the old `client_id` will not work.
2. **Sending `purpose` in the request** — it now lives in the portal config.
3. **Comma-separated scopes** — the v5 `scope` is **space-separated** and must include `openid`.
4. **Missing the DPoP header on PAR or userinfo** — DPoP is required on *all three* calls, not just token exchange.
5. **Using `Bearer` on userinfo** — the prefix must be `DPoP`.
6. **Parsing the access token for `sub`** — treat it as opaque; read the UUID from the **ID token**.
7. **Reading person data from the response root** — it is now under `person_info`.
8. **JWKS with only one key** — you need both a **signing** key and an **encryption** key.
9. **Custom scheme redirect URLs** — rejected; mobile apps must use app-claimed HTTPS.

## References

* [Myinfo (v3) apps migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v3-apps)
* [Integration Guide (full v5 flow)](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide)
* [DPoP guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop)
* [PKCE guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce)
* [Userinfo request spec](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo)
* [Certified OIDC RP libraries](https://openid.net/developers/certified-openid-connect-implementations/)
* [Myinfo Business v2 spec (entity flow, unchanged)](https://public.cloud.myinfo.gov.sg/myinfobiz/myinfo-biz-specs-v2.0.html)


# Pricing

## Price Plans

#### **Government Agencies**

For Government Agencies, please refer to the official government pricing plan shared via WOG intranet here - <https://gccprod.sharepoint.com/sites/GOVTECH-digitalgov/Singpass-and-Corppass/SitePages/Price-Plan.aspx>

#### Private Organisations

For Private Organisations, pricing details are available on the Singpass Developer Portal.

1. Log in to developer.singpass.gov.sg
2. Navigate to the billing tab - <https://developer.singpass.gov.sg/billing>
3. Select the **Pricing Plan** tab to view the applicable pricing details

Detailed pricing rates are shown on separate tabs for **Singpass Login**, **Myinfo**, **Singpass Face Verification – AAL3**, and **Pricing Examples**. For answers to common pricing questions, refer to the [Singpass Pricing Model and Service-Level Subscription FAQ](https://partnersupport.singpass.gov.sg/hc/en-sg/articles/34880999253145-Singpass-Pricing-Model-and-Service-Level-Subscription-FAQ-for-Private-Organisations) on the Partner Support portal.

You may also refer to this [guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/service-agreement/view-singpass-service-agreement) for step-by-step instructions on how to access the price plan.

***

### Singpass Login Pricing

Singpass Login transactions are priced based on the authentication form factor used. Separate pricing tiers apply to:

* **QR code and Passkey** — the primary authentication methods
* **Username and password** — alternative login method
* **SMS OTP** — fallback authentication method

Specific per-transaction rates for each form factor are displayed on the **Singpass Login** tab of the Pricing Plan page in SDP.

***

### Myinfo Pricing Model

To reflect economies of scale and the varying value of data provided, Myinfo uses a differentiated pricing model based on the data scopes retrieved by an e-service.

**Updated Pricing Structure**

To better align cost with data value, Myinfo transactions are categorised into two pricing tiers:

#### Myinfo Standard

Applies to e-services that retrieve personal non-financial profile data scopes.

Examples include basic personal particulars and non-financial attributes.

#### Myinfo Plus

Applies to e-services that retrieve personal financial profile data scopes, including the following:

**CPF Data**\
• Ordinary Account\
• Medisave Account\
• Retirement Account\
• Special Account\
• CPF Contribution History (up to 15 months)\
• CPF Housing Withdrawal

**Income & Property Data**\
\
• NOA Basic (Latest Year)\
• NOA Basic (Last 2 Years)\
• NOA Detailed (Latest Year)\
• NOA Detailed (Last 2 Years)\
• Ownership of Private Residential Property

**CPF Investment Scheme**\
• CPF Investment Scheme Account\
• Number of Discounted Singtel Shares\
• Self-Awareness Questionnaire (SAQ) Participation Status

#### Important Notes

* Pricing is determined based on the highest-value data scope retrieved by the e-service.
* If your e-service retrieves any Myinfo Plus data scope, the transaction will be charged under Myinfo Plus.
* Detailed pricing rates are available in the Singpass Developer Portal.

### Singpass Face Verification (SFV) Pricing

This pricing applies to transactions where your service requires Singpass Face Verification (SFV) as an additional authentication factor to Login/Myinfo. This also applies to services that initiates SFV via acr\_values.

Charges are based on the number of successful SFV transactions per calendar month, and are billed in addition to any Login or Myinfo charges already incurred. SFV triggered by Singpass' fraud analytics is not billed.


# Understanding the Data


# Local Registered Birth Records and Sponsored Child Records

Local Registered Birth Records and Sponsored Child Records are available via Myinfo. Details available in [Myinfo data catalogue](https://docs.developer.singpass.gov.sg/singpass-developer-docs/data-catalog-myinfo/catalog). Note that the records are only based on ICA's electronic birth certificate records from 1985 onwards. If the children or sponsored children are 21 and above, only the Birth Cert Number or NRIC/FIN will be displayed.

Local Registered Birth Records refer to local Singapore registered birth records. Children birth records are available in both parents' Myinfo data.

Sponsored Child Records refer to children born outside Singapore. Sponsored children records are only available in the sponsoring parent's Myinfo data based on ICA's record.

You can derive son, daughter or guardian relationship using children birth or sponsored children records.

Spouse records are not available via Myinfo. If the marriage is registered in Singapore, Marriage Certificate Number and Marriage Date is available via Myinfo. We have observed partners retrieving both husband and wife's Marriage details to verify spouse relationship.


# CPF Contribution History (up to 15 months)

The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.

For each contribution record, the 4 fields (Paid for Month, Paid On, Employer Name, Contribution Total) will be provided.

Only Contribution(s) related to employment will be provided. Other contributions, such as self-employed or government top-ups, are presently excluded.

CPF will return the contributions received (or paid on) in the past 15 months up to the preceding month. Note that a member could have multiple contributions per month from the same employer.

1. Example 1: If the query is made in Mar-24, contribution provided will be for contribution received in the period from Jan-23 to March-24 (inclusive). This is provided that Mar-24 contribution had been received, else contribution provided will be Jan-23 to Feb-24.
2. Example 2: Assuming a member has a late CPF contribution for work done in Nov-22 (beyond Jan-23 to Mar-24) that was credited only in Jan-23. If the query is made in Mar-24, contribution provided will include the late contribution as it was received in the period from Jan-23 to Mar-24. The contribution period range of Jan-23 to Mar-24 (inclusive) remains.


# Notice of Assessment (Basic)

This refers to the taxpayer's total income after deducting allowable expenses and approved donations. Total income includes: (i) Trade (ii) Employment (iii) Rent (iv) Interest

This field will only return: (i) 1 yearly assessable income and

(ii) the corresponding year value. The yearly assessable income will be the latest available income up to the last 2 Years of Assessments.

To note:

i. Assessable Income details is only available for finalised assessment. Thus, income information will not be available if the subscriber has a Default Assessment (e.g. taxpayers who have not submitted their tax return).

ii. This may not be applicable for foreigners depending on their tax residency. For example, in the case of double tax treaties with other countries, foreigner may not need to pay Singapore tax.


# Notice of Assessment (Detailed)

Notice of Assessment (Detailed) data field, includes the following income breakdown:\
a) Employment\
b) Trade\
c) Rent\
d) Interest\
\
Additional details in this data field:\
a) Tax clearance : Indicator will be 'Y' for scenario where non-Singapore Citizen employee that ceases employment in Singapore, and goes on an overseas posting or plans to leave Singapore for more than three months. Only need to display this field if the value = 'Y'.\
\
b) Tax Category : Type of Income Tax Bill. For more details, click [here](https://www.iras.gov.sg/irashome/Individuals/Locals/Paying-your-taxes-Claiming-refunds/How-to-Read-Your-Tax-Bill/).


# Catalog

Scopes available are categorised under the following categories:


# Start Here

The catalog provides a comprehensive overview of available data attributes, mapping their availability across user segments and highlighting specific data nuances to ensure accurate business integration.

Not all data scopes are available for all user segments. Refer to each categories to find out more.

**User segments:**

* SC = Singapore Citizen
* PR = Permanent Resident
* FIN = Foreigners with Long-Term immigration passes in Singapore (e.g. Student's Pass, Employment Pass, Work Permit etc)
* SFA = Singpass Foreign Users. Note that Myinfo is not available for SFA and they can only access digital services provided by their SFA organisation. More information [here](https://ask.gov.sg/singpass/questions/clv0r4159009a8u3akuanq878?from=topics).

***

<details>

<summary>Data Nuances and Legacy Logic</summary>

You may also wish to take note of the following nuances:

<table><thead><tr><th width="229.3046875">Scenario</th><th>Description &#x26; Business Logic</th></tr></thead><tbody><tr><td>Non-Standard ISO Codes</td><td>Myinfo country and nationality codes do not strictly conform to ISO 3166-1 alpha-2. Refer to the <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> for the full list of possible values to avoid integration errors.</td></tr><tr><td>Historical Country Codes</td><td>You may encounter codes like "YU" (Yugoslavia). These represent birth records created prior to a country's dissolution. ICA does not retroactively update historical birth records.</td></tr><tr><td>Special Administrative Regions</td><td>"HK" (Hong Kong) and "MO" (Macau) may be returned as Nationalities for legacy users. These are valid historical assignments from ICA/MOM and are not retrospectively changed.</td></tr><tr><td>Variable DOB Granularity</td><td>Due to incomplete historical submissions, the Date of Birth (DOB) is not always a full date. Systems must be able to handle three formats: <code>YYYY-MM-DD</code>, <code>YYYY-MM</code>, or <code>YYYY</code>.</td></tr><tr><td>Revoked/Expired Pass information for FIN holders</td><td>Myinfo only returns <code>passtype</code>, <code>passstatus</code>, <code>passexpirydate</code> and <code>employmentsector</code> for FIN holders with a valid pass issued by ICA/MOM.<br><br>The scopes will be NULL if the FIN holder do not have a valid pass.</td></tr></tbody></table>

</details>

<details>

<summary>Handling Data Inquiries</summary>

Myinfo data is provided "as-is" from the source agency.

* **User Redirection**: If a user disputes the accuracy of the data (e.g., an outdated nationality), they must be directed to the Source Agency to perform an official update. Changes will reflect in Myinfo once the source record is updated (in about 1-2 days). The Source Agency of each data item can be found within each category tables below.

</details>

<details>

<summary>Data Freshness &#x26; Availability</summary>

* **Data at time of consent:** Myinfo data reflects the government record at the point of user consent. It is **not a live data feed.**
  * If a user updates their personal information, the changes will be reflected in about 1-2 days.
* **FIN holder Singpass access after employment ends:** FIN holders retain Singpass access for 3 months after pass expiry or cancellation date.

</details>


# Personal

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th>ID</th><th>Name</th><th width="253.4609375">Description</th><th>Data Available</th><th>Source</th></tr></thead><tbody><tr><td><code>uinfin</code></td><td>NRIC / FIN</td><td>NRIC number or FIN of user. NRIC number is the unique identifier given to every Singapore Citizens (SC) and Permanent Residents (PR), while FIN is the unique identifier for Foreigners.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>partialuinfin</code></td><td>Partial NRIC / FIN</td><td>Last 3 numerical digits and checksum of the NRIC/FIN number, prefixed with '*****' (e.g. "*****567A" from the full NRIC number of "S1234567A").</td><td>SC,PR,FIN</td><td>—</td></tr><tr><td><code>name</code></td><td>Principal Name</td><td>Includes Surname if any. Note that Principal Name does not represent the full name as printed on the NRIC/FIN card or Digital IC (Read <a href="https://partnersupport.singpass.gov.sg/hc/en-sg/articles/32683301388569-Does-Myinfo-Principal-Name-match-the-Full-Name-printed-on-the-NRIC-FIN-card-or-Digital-IC">here</a> for more info)</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>aliasname</code></td><td>Alias Name</td><td>Refers to an alternate/additional name of the user that is legally recognised.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>hanyupinyinname</code></td><td>Hanyu Pinyin Name</td><td>Refers to the officially romanised Chinese name of the user.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>hanyupinyinaliasname</code></td><td>Hanyu Pinyin Alias Name</td><td>Refers to the legally-recognised alternate officially romanised Chinese name of the user.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>marriedname</code></td><td>Married Name</td><td>Refers to the family name or surname adopted by the user upon marriage.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>sex</code></td><td>Sex</td><td>Gender of the user. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (SexCode) for list of possible values.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>race</code></td><td>Race</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>secondaryrace</code></td><td>Secondary Race</td><td>Refers to secondary racial category of the Person, if any. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>dialect</code></td><td>Dialect</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (DialectCode) for list of possible values.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>dob</code></td><td>Date of Birth</td><td>Date of Birth of Person.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>residentialstatus</code></td><td>Residential Status</td><td>Indicate if the user is a Citizen, PR or others. Blank value will be returned for FIN holder. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (ResidentialCode) for list of possible values.</td><td>SC,PR</td><td>ICA</td></tr><tr><td><code>nationality</code></td><td>Nationality / Citizenship</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (NationalityCitizenshipCode) for list of possible values.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>birthcountry</code></td><td>Country / Place of Birth</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (CountryPlaceCode) for list of possible values.</td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>passportnumber</code></td><td>Passport Number</td><td>Passport number of the user.</td><td>SC</td><td>ICA</td></tr><tr><td><code>passportexpirydate</code></td><td>Passport Expiry Date</td><td>Passport expiry date of the user.</td><td>SC</td><td>ICA</td></tr><tr><td><code>passtype</code></td><td>Pass Type</td><td><p>This refers to the pass type of a FIN holder.<br></p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (PassTypeCode) for list of possible values.<br></p><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td><code>passstatus</code></td><td>Pass Status</td><td><p>This refers to the pass status of a FIN holder.</p><p>Available values:</p><ul><li>Live</li><li>Approved. (Interim status in which the FIN holder has yet to receive the pass)</li></ul><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td><code>passexpirydate</code></td><td>Pass Expiry Date</td><td><p>This refers to the pass expiry date of a FIN holder.<br></p><p>Note that this only applies to a FIN holder with a valid pass issued by ICA/MOM.</p></td><td>FIN</td><td>ICA/MOM</td></tr><tr><td><code>employmentsector</code></td><td>Employment Sector</td><td><p>This refers to the employment sector of a FIN holder.<br></p><p>Note that this only applies to a FIN holder with a valid pass issued by MOM.</p></td><td>FIN</td><td>MOM</td></tr><tr><td><code>mobileno</code></td><td>Mobile Number</td><td>Mobile number must be made editable at digital services even though data source is Singpass.</td><td>SC,PR,FIN</td><td>Singpass</td></tr><tr><td><code>email</code></td><td>Email Address</td><td>Email address must be made editable at digital services even though data source is Singpass.</td><td>SC,PR,FIN</td><td>Singpass</td></tr><tr><td><code>regadd</code></td><td>Registered Address</td><td><p>For SC/PR - Registered address is the address that is printed on the NRIC card.<br></p><p>For FIN - Registered address is applicable for foreigners under the following<br>Pass Types:<br><strong>ICA-issued Passes</strong><br>- Long Term Visit Pass / Long Term Visit Pass +<br>- Student Pass<br>- Immigration Exemption Order<br><strong>MOM-issued Passes</strong><br>- S Pass<br>- Employment Pass<br>- Personalised Employment Pass<br>- EntrePass<br>- Dependent Pass</p></td><td>SC,PR,FIN</td><td>ICA/MOM</td></tr><tr><td><code>hdbtype</code></td><td>Type of HDB</td><td>Note that this is determined based on user's Registered Address (if it is a HDB flat). Has no association with HDB ownership. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> for list of possible values.</td><td>Available for SC, PR, and FIN</td><td>HDB</td></tr><tr><td><code>housingtype</code></td><td>Type of Housing</td><td>Note that this is determined based on user's Registered Address (if it is not a HDB flat). Has no association with housing ownership. Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> for list of possible values.</td><td>Available for SC, PR, and FIN</td><td>URA</td></tr></tbody></table>


# Finance

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th width="99">id</th><th width="158">name</th><th width="261.5078125">description</th><th>Data Available</th><th>Source</th><th data-hidden>subcategory</th></tr></thead><tbody><tr><td>cpfbalances.oa</td><td>CPF Balances - Ordinary Account</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p>The CPF balance here would include Ordinary Account (OA).</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>cpfbalances.ma</td><td>CPF Balances - Medisave Account</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p>The CPF balance here would include Medisave Account (MA).</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>cpfbalances.ra</td><td>CPF Balances - Retirement Account</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p>The CPF balance here would include Retirement Account (RA) if applicable to the user.</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>cpfbalances.sa</td><td>CPF Balances - Special Account</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p>The CPF balance here would include Special Account (SA).</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>cpfcontributions</td><td>CPF Contribution History (up to 15 months)</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p>For each contribution record, the 4 fields (Paid for Month, Paid On, Employer Name, Contribution Total) will be provided.</p><p>Only Contribution(s) related to employment will be provided. Other contributions, such as self-employed or government top-ups, are presently excluded.</p><p>CPF will return the contributions received (or paid on) in the past 15 months up to the preceding month. Note that a member could have multiple contributions per month from the same employer.</p><p><strong>1. Example 1:</strong></p><p>If the query is made in March-24, contribution provided will be for contribution received in the period from January-23 to March-24 (inclusive). This is provided that March-24 contribution had been received, else contribution provided will be January-23 to February-24.</p><p><strong>2. Example 2:</strong> Assuming a member has a late CPF contribution for work done in Nov-22 (beyond January-23 to March-24) that was credited only in Jan-23. If the query is made in March-24, contribution provided will include the late contribution as it was received in the period from January-23 to March-24. The contribution period range of January-23 to March-24 (inclusive) remains.</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>cpfhousingwithdrawal</td><td>CPF Housing Withdrawal</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by<br>contributions from employers and employees.</p><p><br>The CPF Housing Withdrawal data include the following for the purpose of financing a<br>HDB flat or private residential property:</p><p><br>a) Address: This is the registered address of property which withdrawal is made.</p><p><br>b) Principal Withdrawal Amount: This is the CPF principal amount user has<br>withdrawn under the CPF housing schemes.</p><p><br>c) Monthly Instalment Amount: This is the monthly CPF deduction for payment<br>of user's property.</p><p><br>d) Accrued Interest Amount: This is the interest that user would have earned<br>had user's savings remained in the CPF account.</p><p><br>e) Total Amount of CPF Allowed for Property: The maximum CPF savings allowed to be used for the<br>financing the property, excluding the amount used for stamp duty and legal fees.</p><p>Click <a href="https://docs.developer.singpass.gov.sg/docs/products/myinfo/data-display-guidelines">here</a> to refer to the CPF display guidelines.</p></td><td>SC,PR</td><td>CPFB</td><td></td></tr><tr><td>noa-basic</td><td>Notice of Assessment (Basic, Latest Year)</td><td><p>This refers to the taxpayer's total income after deducting allowable expenses and approved donations. Total income includes:</p><p>(i) Trade</p><p>(ii) Employment</p><p>(iii) Rent</p><p>(iv) Interest</p><p>This field will only return:</p><p>(i) 1 yearly assessable income and</p><p>(ii) the corresponding year value. The yearly assessable income will be the latest available income up to the last 2 Years of Assessments. If the subscriber does not have any assessment record for up to 2 back years, Myinfo will return the following:</p><p>a) Assessable Income= 'NA' or '-'</p><p>b) Year Assessed='NA'.</p><p>To note:</p><p>i. Assessable Income details is only available for finalised assessment. Thus, income information will not be available if the subscriber has a Default Assessment (e.g. taxpayers who have not submitted their tax return).</p><p>ii. This may not be applicable for foreigners depending on their tax residency. For example, in the case of double tax treaties with other countries, foreigner may not need to pay Singapore tax.</p></td><td>SC,PR,FIN</td><td>IRAS</td><td></td></tr><tr><td>noahistory-basic</td><td>Notice of Assessment (Basic, Last 2 Years)</td><td>Similar to 'Notice of Assessment (Basic, Latest Year)' data field, but for the last 2 years instead.</td><td>SC,PR,FIN</td><td>IRAS</td><td></td></tr><tr><td>noa</td><td>Notice of Assessment (Detailed, Latest Year)</td><td><p>Similar to 'Notice of Assessment (Basic, Latest Year)' data field, including the following income breakdown</p><p>a) Employment</p><p>b) Trade</p><p>c) Rent</p><p>d) Interest</p><p>Additional details in this data field:</p><p>a) Tax clearance : Indicator will be 'Y' for scenario where non-Singapore Citizen employee that ceases employment in Singapore, and goes on an overseas posting or plans to leave Singapore for more than three months. Only need to display this field if the value = 'Y'.</p><p>b) Tax Category : Type of Income Tax Bill. For more details, <a href="https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/receive-tax-bill-pay-tax-check-refunds/understanding-my-tax-assessment">click here</a>.</p></td><td>SC,PR,FIN</td><td>IRAS</td><td></td></tr><tr><td>noahistory</td><td>Notice of Assessment (Detailed, Last 2 Years)</td><td>Similar to 'Notice of Assessment (Basic, Latest Year)' data field, but for the last 2 years instead.</td><td>SC,PR,FIN</td><td>IRAS</td><td></td></tr><tr><td>ownerprivate</td><td>Ownership of Private Residential Property</td><td><p>This refers to the ownership of private residential property. Note that this does not include shophouses which are assessed as commercial properties.</p><p>This field will be 'Y', if the corresponding NRIC/FIN, in IRAS records, is a primarily, secondary or CC owner of an active private residential property and is required to pay property tax. Otherwise will be 'N'.</p><p>Where the NRIC/FIN is not found in IRAS records, it will be returned as 'NA'.</p></td><td>SC,PR</td><td>IRAS</td><td></td></tr><tr><td>cpfinvestmentscheme.account</td><td>CPF Investment Scheme - Account</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.</p><p><br>CPF savings can be used in these investment schemes - CPF Investment Scheme (CPFIS) &#x26; Special Discounted Shares (SDS) Scheme.</p><p><br>CPFIS account data includes Agent Bank under CPFIS-OA and Investment Account number which refer to the CPF Investment account that user has opened with one of the CPFIS-OA agent banks under the CPFIS.</p></td><td>SC,PR</td><td>CPFB</td><td>CPF Investment Scheme</td></tr><tr><td>cpfinvestmentscheme.sdsnetshareholdingqty</td><td>CPF Investment Scheme - Number of Discounted Singtel Shares</td><td>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.<br><br>CPF savings can be used in these investment schemes - CPF Investment Scheme (CPFIS) &#x26; Special Discounted Shares (SDS) Scheme.<br><br>Number of Discounted Singtel Shares refers to the number of discounted Singtel shareholdings held under the SDS Scheme.</td><td>SC,PR</td><td>CPFB</td><td>CPF Investment Scheme</td></tr><tr><td>cpfinvestmentscheme.saqparticipationstatus</td><td>CPF Investment Scheme - Self-Awareness Questionnaire (SAQ) Participation Status</td><td><p>The Central Provident Fund is a mandatory social security savings scheme funded by contributions from employers and employees.<br></p><p>CPF savings can be used in these investment schemes - CPF Investment Scheme (CPFIS) &#x26; Special Discounted Shares (SDS) Scheme.<br></p><p>Self-Awareness Questionnaire (SAQ) Participation Status refers to whether the user has taken the CPFIS Self-Awareness Questionnaire (SAQ) to help assess if CPFIS is suitable for the user.</p></td><td>SC,PR</td><td>CPFB</td><td>CPF Investment Scheme</td></tr></tbody></table>


# Education and Employment

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>employment</td><td>Name of Employer</td><td></td><td>FIN</td><td>MOM</td></tr><tr><td>occupation</td><td>Occupation</td><td>For FIN - Value will be returned in the description.</td><td>FIN</td><td>MOM</td></tr><tr><td>cpfemployers</td><td>CPF Employers</td><td><p>Employer Name for the CPF Contribution. Includes contribution month/year.</p><p>Only Contribution(s) related to employment will be provided. Other contributions, such as self-employed or government top-ups, are presently excluded.</p><p>CPF will return the contributions received (or paid on) in the past 15 months up to the preceding month. Note that a member could have multiple contributions per month from the same employer.</p></td><td>SC,PR</td><td>CPFB</td></tr><tr><td>academicqualifications.transcripts</td><td>Singapore-Cambridge Examination</td><td>Singapore-Cambridge (GCE N, O, A Levels) Examination results attained.</td><td>SC,PR,FIN</td><td>MOE</td></tr><tr><td>academicqualifications.certificates</td><td>Singapore-Cambridge Examination (OpenCert)</td><td><p>Singapore-Cambridge (GCE N, O, A Levels) Examination results attained. Data to be<br>returned in OpenCert format.</p><p><a href="https://www.opencerts.io">Click here</a> to find out about OpenCert format.</p></td><td>SC,PR,FIN</td><td>MOE</td></tr><tr><td>ltavocationallicences.tdvl.licencename</td><td>LTA Vocational Licences - TDVL Licence Name</td><td><p>A Taxi Driver's Vocational Licence allows one to drive a taxi.</p><p>Licence Name of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.tdvl.vocationallicencenumber</td><td>LTA Vocational Licences - TDVL Vocational Licence Number</td><td><p>A Taxi Driver's Vocational Licence allows one to drive a taxi.</p><p>Unique Vocational Licence Number for LTA Vocational Licence holder.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.tdvl.expirydate</td><td>LTA Vocational Licences - TDVL Expiry Date</td><td><p>A Taxi Driver's Vocational Licence allows one to drive a taxi.</p><p>Expiry date of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.tdvl.status</td><td>LTA Vocational Licences - TDVL Status</td><td><p>A Taxi Driver's Vocational Licence allows one to drive a taxi.</p><p>Status of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.pdvl.licencename</td><td>LTA Vocational Licences - PDVL Licence Name</td><td><p>A Private Hire Car Driver's Vocational Licence allows one to drive a private hire car.</p><p>Licence Name of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.pdvl.vocationallicencenumber</td><td>LTA Vocational Licences - PDVL Vocational Licence Number</td><td><p>A Private Hire Car Driver's Vocational Licence allows one to drive a private hire car.</p><p>Unique Vocational Licence Number for LTA Vocational Licence holder.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.pdvl.expirydate</td><td>LTA Vocational Licences - PDVL Expiry Date</td><td><p>A Private Hire Car Driver's Vocational Licence allows one to drive a private hire car.</p><p>Expiry date of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.pdvl.status</td><td>LTA Vocational Licences - PDVL Status</td><td><p>A Private Hire Car Driver's Vocational Licence allows one to drive a private hire car.</p><p>Status of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bavl.licencename</td><td>LTA Vocational Licences - BAVL Licence Name</td><td><p>A Bus Attendant's Vocational Licence allows one to work as a bus attendant on a school bus.</p><p>Licence Name of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bavl.vocationallicencenumber</td><td>LTA Vocational Licences - BAVL Vocational Licence Number</td><td><p>A Bus Attendant's Vocational Licence allows one to work as a bus attendant on a school bus.</p><p>Unique Vocational Licence Number for LTA Vocational Licence holder.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bavl.expirydate</td><td>LTA Vocational Licences - BAVL Expiry Date</td><td><p>A Bus Attendant's Vocational Licence allows one to work as a bus attendant on a school bus.</p><p>Expiry date of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bavl.status</td><td>LTA Vocational Licences - BAVL Status</td><td><p>A Bus Attendant's Vocational Licence allows one to work as a bus attendant on a school bus.</p><p>Status of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bdvl.licencename</td><td>LTA Vocational Licences - BDVL Licence Name</td><td><p>A Bus Driver's Vocational Licence allows one to drive a private hire bus/excursion bus/ school bus.</p><p>Licence Name of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bdvl.vocationallicencenumber</td><td>LTA Vocational Licences - BDVL Vocational Licence Number</td><td><p>A Bus Driver's Vocational Licence allows one to drive a private hire bus/excursion bus/ school bus.</p><p>Unique Vocational Licence Number for LTA Vocational Licence holder.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bdvl.expirydate</td><td>LTA Vocational Licences - BDVL Expiry Date</td><td><p>A Bus Driver's Vocational Licence allows one to drive a private hire bus/excursion bus/ school bus.</p><p>Expiry date of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.bdvl.status</td><td>LTA Vocational Licences - BDVL Status</td><td><p>A Bus Driver's Vocational Licence allows one to drive a private hire bus/excursion bus/ school bus.</p><p>Status of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.odvl.licencename</td><td>LTA Vocational Licences - ODVL Licence Name</td><td><p>An Omnibus Driver’s Vocational Licence allows one to drive an omnibus.</p><p>Licence Name of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.odvl.vocationallicencenumber</td><td>LTA Vocational Licences - ODVL Vocational Licence Number</td><td><p>An Omnibus Driver’s Vocational Licence allows one to drive an omnibus.</p><p>Unique Vocational Licence Number for LTA Vocational Licence holder.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.odvl.expirydate</td><td>LTA Vocational Licences - ODVL Expiry Date</td><td><p>An Omnibus Driver’s Vocational Licence allows one to drive an omnibus.</p><p>Expiry date of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr><tr><td>ltavocationallicences.odvl.status</td><td>LTA Vocational Licences - ODVL Status</td><td><p>An Omnibus Driver’s Vocational Licence allows one to drive an omnibus.</p><p>Status of LTA Vocational Licence.</p></td><td>SC,PR,FIN</td><td>LTA</td></tr></tbody></table>


# Family

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th width="113">id</th><th width="151">name</th><th width="249.2578125">description</th><th>Data Available</th><th>Source</th><th data-hidden>subcategory</th></tr></thead><tbody><tr><td>marital</td><td>Marital Status</td><td><p>Marital status is based on records that had been reasonably verified by the relevant Government agency upon receipt.</p><p>Marital Status must be made editable at digital services even though data source is MSF.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (MaritalStatusCode) for list of possible values.</p></td><td>SC,PR</td><td>MSF</td><td></td></tr><tr><td>marriagedate</td><td>Marriage Date</td><td><p>Marriage Date refers to the latest date of most recent Marriage.</p><p>Note that Marriage Date shall be made editable at digital services even though data source is MSF.</p></td><td>SC,PR</td><td>MSF</td><td></td></tr><tr><td>divorcedate</td><td>Divorce Date</td><td><p>Divorce Date refers to the latest date of most recent Divorce.</p><p>Note that Divorce Date shall be made editable at digital services even though data source is MSF.</p></td><td>SC,PR</td><td>MSF</td><td></td></tr><tr><td>marriagecertno</td><td>Marriage Certificate Number</td><td><p>This refers to the certificate number of the latest marriage.</p><p>Note that Marriage Certificate Number shall be made editable at digital services even though data source is MSF.</p></td><td>SC,PR</td><td>MSF</td><td></td></tr><tr><td>countryofmarriage</td><td>Country/Place of Marriage</td><td><p>This refers to the country/place of the latest marriage.</p><p>Note that Marriage Country/Place shall be made editable at digital services even though data source is MSF.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (CountryPlaceCode) for list of possible values.</p></td><td>SC,PR</td><td>MSF</td><td></td></tr><tr><td>childrenbirthrecords.birthcertno</td><td>Children Birth Records - Birth Cert Number</td><td><p>Birth Certificate Number is the unique identifier given for births in Singapore.</p><p>Note that the records are only based on ICA's electronic birth certificate records from 1985 onwards.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.name</td><td>Children Birth Records - Name</td><td><p>Name displayed on the Birth Certificate.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.aliasname</td><td>Children Birth Records - Alias Name</td><td><p>Alias Name displayed on the Birth Certificate.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.hanyupinyinname</td><td>Children Birth Records - Hanyu Pinyin Name</td><td><p>Hanyu Pinyin Name displayed on the Birth Certificate.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.hanyupinyinaliasname</td><td>Children Birth Records - Hanyu Pinyin Alias Name</td><td><p>Hanyu Pinyin Alias Name displayed on the Birth Certificate.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.marriedname</td><td>Children Birth Records - Married Name</td><td><p>Married Name displayed on the Birth Certificate.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.sex</td><td>Children Birth Records - Sex</td><td><p>Gender of the child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (SexCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.race</td><td>Children Birth Records - Race</td><td><p>Race of the child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.secondaryrace</td><td>Children Birth Records - Secondary Race</td><td><p>Secondary Race of the child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.dob</td><td>Children Birth Records - Date of Birth</td><td>This field will only be returned if the child's age is below 21.</td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.tob</td><td>Children Birth Records - Time of Birth</td><td>This field will only be returned if the child's age is below 21.</td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.dialect</td><td>Children Birth Records - Dialect</td><td><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (DialectCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.lifestatus</td><td>Children Birth Records - Life Status</td><td><p>Indicates the life status of the child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.vaccinationrequirements</td><td>Children Birth Records - Child Vaccination</td><td><p>The Child Vaccination data include the following:<br><br>a) Child Vaccination Requirement Fulfilled: This refers to whether a child has fulfilled the preschool vaccination minimum requirements. This data is based on Communicable Diseases Agency (CDA) National Immunisation Registry (NIR) records where the child is born from 2014 onwards.</p><p><br>b) Child Vaccination Requirement Code: Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (ChildVaccReqCode) for list of possible values.</p></td><td>SC,PR,FIN</td><td>CDA</td><td>Children Birth Records</td></tr><tr><td>childrenbirthrecords.sgcitizenatbirthind</td><td>Children Birth Records - Singapore Citizen at Birth Indicator</td><td><p>Indicates whether the child is a Singapore Citizen at the time of birth.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR,FIN</td><td>ICA</td><td>Children Birth Records</td></tr><tr><td>sponsoredchildrenrecords.nric</td><td>Sponsored Children Records - NRIC / FIN</td><td>NRIC / FIN is the unique identifier given to sponsor child whom have obtained citizenship or permanent residency or long-term visit pass via sponsorship by their parents.</td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.name</td><td>Sponsored Children Records - Name</td><td><p>Name of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.aliasname</td><td>Sponsored Children Records - Alias Name</td><td><p>Alias Name of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.hanyupinyinname</td><td>Sponsored Children Records - Hanyu Pinyin Name</td><td><p>Hanyu Pinyin Name of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.hanyupinyinaliasname</td><td>Sponsored Children Records - Hanyu Pinyin Alias Name</td><td><p>Hanyu Pinyin Alias Name of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.marriedname</td><td>Sponsored Children Records - Married Name</td><td><p>Married Name of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.sex</td><td>Sponsored Children Records - Sex</td><td><p>Gender of the Sponsored Child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (SexCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.race</td><td>Sponsored Children Records - Race</td><td><p>Race of the Sponsored Child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.secondaryrace</td><td>Sponsored Children Records - Secondary Race</td><td><p>Secondary Race of the Sponsored Child.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (RaceCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.dialect</td><td>Sponsored Children Records - Dialect</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (DialectCode) for list of possible values.</td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.dob</td><td>Sponsored Children Records - Date of Birth</td><td>This field will only be returned if the child's age is below 21.</td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.birthcountry</td><td>Sponsored Children Records - Country/Place of Birth</td><td><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (CountryPlaceCode) for list of possible values.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.lifestatus</td><td>Sponsored Children Records - Life Status</td><td><p>Indicates the life status of the Sponsored Child.</p><p>This field will only be returned if the child's age is below 21.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.residentialstatus</td><td>Sponsored Children Records - Residential Status</td><td><p>Indicates if the Sponsored Child is a Citizen, PR or others.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (ResidentialCode) for list of possible values.</p></td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.nationality</td><td>Sponsored Children Records - Nationality/Citizenship</td><td>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (NationalityCitizenshipCode) for list of possible values.</td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.scprgrantdate</td><td>Sponsored Children Records - SC / PR / LTVP Grant Date</td><td>Date when Sponsored child was granted Singapore Citizenship, Permanent Resident or Long Term Visit Pass.</td><td>SC,PR</td><td>ICA</td><td>Sponsored Children Records</td></tr><tr><td>sponsoredchildrenrecords.vaccinationrequirements</td><td>Sponsored Children Records - Child Vaccination</td><td><p>The Child Vaccination data include the following:<br></p><p>a) Child Vaccination Requirement Fulfilled: This refers to whether a child has fulfilled the preschool vaccination minimum requirements. This data is based on Communicable Diseases Agency (CDA) National Immunisation Registry (NIR) records where the child is born from 2014 onwards.<br></p><p>b) Child Vaccination Requirement Code: Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (ChildVaccReqCode) for list of possible values.</p></td><td>SC,PR,FIN</td><td>CDA</td><td>Sponsored Children Records</td></tr></tbody></table>

### Marital Status & Marriage Records

<table><thead><tr><th>ID</th><th>Name</th><th width="297.1875">Description</th><th width="277.76171875">Value</th><th>Data Available</th><th>Source</th></tr></thead><tbody><tr><td><code>marital</code></td><td>Marital Status</td><td>Marital status is based on records that had been reasonably verified by the relevant Government agency upon receipt.<br><br>Note: This field must be made editable on your digital service form even though source is Government Verified.<br><br>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (MaritalStatusCode) for list of possible values.</td><td>Object with <code>code</code> (string) and <code>desc</code> (string)<br><br><strong>Example:</strong> <code>{"code": "2", "desc": "MARRIED"}</code></td><td><strong>SC and PR only</strong> — not available for FIN</td><td>MSF</td></tr><tr><td><code>marriagedate</code></td><td>Marriage Date</td><td>Marriage Date refers to the latest date of most recent Marriage.<br><br>Note: This field must be made editable on your digital service form even though source is Government Verified.</td><td>String, format: date (<code>YYYY-MM-DD</code>)<br><br><strong>Example:</strong> <code>"2018-01-01"</code></td><td><strong>SC and PR only</strong> — not available for FIN</td><td>MSF</td></tr><tr><td><code>divorcedate</code></td><td>Divorce Date</td><td>Divorce Date refers to the latest date of most recent Divorce.<br><br>Note: This field must be made editable on your digital service form even though source is Government Verified.</td><td>String, format: date (<code>YYYY-MM-DD</code>)<br><br><strong>Example:</strong> <code>"2018-01-01"</code></td><td><strong>SC and PR only</strong> — not available for FIN</td><td>MSF</td></tr><tr><td><code>marriagecertno</code></td><td>Marriage Certificate Number</td><td>This refers to the certificate number of the latest marriage.<br><br>Note: This field must be made editable on your digital service form even though source is Government Verified.</td><td>String; maxLength: 50<br><br><strong>Example:</strong> <code>"123456789012345"</code></td><td><strong>SC and PR only</strong> — not available for FIN</td><td>MSF</td></tr><tr><td><code>countryofmarriage</code></td><td>Country/Place of Marriage</td><td>This refers to the country/place of the latest marriage.<br><br>Note: This field must be made editable on your digital service form even though source is Government Verified.<br><br>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (CountryPlaceCode) for list of possible values</td><td>Object with <code>code</code> (string) and <code>desc</code> (string, maxLength: 300)<br><br><strong>Example:</strong> <code>{"code": "SG", "desc": "SINGAPORE"}</code></td><td><strong>SC and PR only</strong> — not available for FIN</td><td>MSF</td></tr></tbody></table>


# Vehicle and Driving Licence

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th>id</th><th>name</th><th width="261.4375">description</th><th>Data Available</th><th>Source</th><th data-hidden>subcategory</th></tr></thead><tbody><tr><td>drivinglicence.comstatus</td><td>Driving Licence - Certificate of Merit Status</td><td>Status of Certificate of Merit (e.g. Y - Eligible, N - Not Eligible).</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.totaldemeritpoints</td><td>Driving Licence - Total Demerit Points</td><td>Total Demerit Points.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.suspension.startdate</td><td>Driving Licence - Suspension Start Date</td><td>Suspension Start Date.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.suspension.enddate</td><td>Driving Licence - Suspension End Date</td><td>Suspension End Date.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.disqualification.startdate</td><td>Driving Licence - Disqualification Start Date</td><td>Disqualification Start Date</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.disqualification.enddate</td><td>Driving Licence - Disqualification End Date</td><td>Disqualification End Date</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.revocation.startdate</td><td>Driving Licence - Revocation Start Date</td><td>Revocation Start Date</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.revocation.enddate</td><td>Driving Licence - Revocation End Date</td><td>Revocation End Date</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.pdl.validity</td><td>Driving Licence - Provisional Driving Licence Validity</td><td>Validity of PDL (e.g. V - Valid, E - Expired, I - Invalid, N - Not Holding PDL).</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.pdl.expirydate</td><td>Driving Licence - Provisional Driving Licence Expiry Date</td><td>PDL Expiry Date.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.pdl.classes</td><td>Driving Licence - Provisional Driving Licence Class</td><td>PDL Class.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.qdl.validity</td><td>Driving Licence - Qualified Driving Licence Validity</td><td>Validity of QDL (e.g. V - Valid, E - Expired, I - Invalid, N - Not Holding QDL).</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.qdl.expirydate</td><td>Driving Licence - Qualified Driving Licence Expiry Date</td><td>QDL Expiry Date.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.qdl.classes</td><td>Driving Licence - Qualified Driving Licence Class</td><td>QDL Class. Includes Issue Date (e.g. 2B, 2018-01-01).</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>drivinglicence.photocardserialno</td><td>Driving Licence - Photo Card Serial Number</td><td>Serial Number of the Photo Card.</td><td>SC,PR,FIN</td><td>TP</td><td>Driving Licence</td></tr><tr><td>vehicles.vehicleno</td><td>Vehicles - Vehicle Number</td><td>Vehicle Registration Number displayed on the vehicle number plates.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.type</td><td>Vehicles - Vehicle Type</td><td>Type of Vehicle such as 'MOTOR CAR', 'STATION /WAGON/JEEP/LAND ROVER'.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.iulabelno</td><td>Vehicles - IU Label Number</td><td>In-Vehicle Unit (IU) number of the device fitted in Singapore-registered vehicles for Electronic Road Pricing (ERP) gantries and Electronic Parking System (EPS) car parks.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.make</td><td>Vehicles - Vehicle Make</td><td>Vehicle Make such as 'TOYOTA', 'HONDA', 'AUDI'.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.model</td><td>Vehicles - Vehicle Model</td><td>Vehicle Model such as 'COROLLA ALTIS CLASSIC 1.6 CVT', 'HRV 1.5 DX CVT'.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.chassisno</td><td>Vehicles - Chassis Number</td><td>Vehicle Chassis Number.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.engineno</td><td>Vehicles - Engine Number</td><td>Vehicle Engine Number.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.motorno</td><td>Vehicles - Motor Number</td><td>Vehicle Motor Number.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.yearofmanufacture</td><td>Vehicles - Year of Manufacture</td><td>Manufacturing Year.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.firstregistrationdate</td><td>Vehicles - First Registration Date</td><td>Date when vehicle is registered with LTA.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.originalregistrationdate</td><td>Vehicles - Original Registration Date</td><td>Date when vehicle is first registered in the Country of Origin.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.coecategory</td><td>Vehicles - COE Category</td><td>Vehicle Certificate of Entitlement (COE) bid category.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.coeexpirydate</td><td>Vehicles - COE Expiry Date</td><td>Vehicle Certificate of Entitlement (COE) expiry date.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.roadtaxexpirydate</td><td>Vehicles - Road Tax Expiry Date</td><td></td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.quotapremium</td><td>Vehicles - Quota Premium</td><td>Actual Quota Premium (QP) amount payable for the COE upon registration, conversion or COE revalidation. For renewal of COE, the value will contain actual PQP paid.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.openmarketvalue</td><td>Vehicles - Open Market Value</td><td>Open Market Value is the value of manufacturer invoice price, freight and insurance.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.co2emission</td><td>Vehicles - CO2 Emission Rate</td><td>CO2 emission rate (e.g. 8040).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.status</td><td>Vehicles - Vehicle Status</td><td><p>Status of the Vehicle.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing </a>(VehicleStatus) for list of possible values.</p></td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.primarycolour</td><td>Vehicles - Primary Colour</td><td>Vehicle Primary Colour (e.g. BLACK).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.secondarycolour</td><td>Vehicles - Secondary Colour</td><td>Vehicle Secondary Colour (e.g. WHITE).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.attachment1</td><td>Vehicles - Attachment 1</td><td>Vehicle Attachment 1 (e.g. DISABLED).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.attachment2</td><td>Vehicles - Attachment 2</td><td>Vehicle Attachment 2 (e.g. WITH SUN ROOF).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.attachment3</td><td>Vehicles - Attachment 3</td><td>Vehicle Attachment 3 (e.g. SIDE CURTAIN).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.scheme</td><td>Vehicles - Vehicle Scheme</td><td>Vehicle Scheme (e.g. REVISED OFF-PEAK CAR).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.thcemission</td><td>Vehicles - THC Emission Rate</td><td>Total Hydro Carbon (THC) emission rate (e.g. 1011000).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.coemission</td><td>Vehicles - CO Emission Rate</td><td>Carbon Monoxide emission rate (e.g. 1100000).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.noxemission</td><td>Vehicles - NOx Emission Rate</td><td>Nitrogen Oxide (NOx) emission rate (e.g. 11000).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.pmemission</td><td>Vehicles - PM Emission Rate</td><td>Particulates (PM - Atmospheric Particulate Matter) emission rate (e.g. 7000).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.enginecapacity</td><td>Vehicles - Engine Capacity</td><td>Engine Capacity (E.g. 1600 = 1,600cc).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.powerrate</td><td>Vehicles - Power Rate</td><td>Power Rate. Applicable to Electric and Hybrid vehicles powered by electric motors. Unit is Kilowatt. (e.g. 1400).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.effectiveownership</td><td>Vehicles - Effective Date/Time of Ownership</td><td>Effective Date/Time of Ownership in DDMMYYYYHHMMSS format.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.propellant</td><td>Vehicles - Propellant</td><td>Propellant (e.g. Compressed Natural Gas, Diesel, Diesel-CNG, Diesel-Electric, Diesel-Electric (Plug-In), Electric, Gas, Liquefied Petroleum Gas (LPG), Petrol, Petrol-CNG, Petrol-Electric, Petrol-Electric (Plug-In), Petrol-LPG).</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.maximumunladenweight</td><td>Vehicles - Max Unladen Weight</td><td>Maximum Unladen Weight.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.maximumladenweight</td><td>Vehicles - Max Laden Weight</td><td>Maximum Laden Weight.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.minimumparfbenefit</td><td>Vehicles - Minimum PARF Benefit</td><td>Minimum PARF Benefit.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.nooftransfers</td><td>Vehicles - No. of Transfers</td><td>Number of Transfers.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr><tr><td>vehicles.vpc</td><td>Vehicles - Vehicle Parking Certificate</td><td>Vehicle Parking Certificate. Applicable for Heavy Vehicles.</td><td>SC,PR,FIN</td><td>LTA</td><td>Vehicles</td></tr></tbody></table>


# HDB Property

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th width="110">id</th><th width="145.98828125">name</th><th width="232.21484375">description</th><th>Data Available</th><th>Source</th><th data-hidden>subcategory</th></tr></thead><tbody><tr><td>hdbownership.noofowners</td><td>HDB Ownership - Number of Owners</td><td><p>Number of Owners.</p><p>Note that this does not include executors, administrators or trustees.</p></td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.address</td><td>HDB Ownership - Address</td><td>Flat Address.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.hdbtype</td><td>HDB Ownership - Type of HDB Dwelling</td><td><p>HDB Flat Type.</p><p>Refer to <a href="https://public.cloud.myinfo.gov.sg/dpp/frontend/assets/api-lib/myinfo/downloads/myinfo-api-code-tables.xlsx">Code Listing</a> (HDBTypeCode) for list of possible values.</p></td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.leasecommencementdate</td><td>HDB Ownership - Lease Commencement Date</td><td>Lease Period Start Date.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.termoflease</td><td>HDB Ownership - Term of Lease</td><td>Term of lease for the property computed from the lease commencement date.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.dateofpurchase</td><td>HDB Ownership - Date of Purchase</td><td>Effective Date of flat purchase.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.dateofownershiptransfer</td><td>HDB Ownership - Date of Transfer of Ownership</td><td><p>Effective date of partial transfer without monetary consideration (e.g. addition, deletion or substitution of a co-owner) for an HDB sold flat.</p><p>For partial transfer of flat where at least one of the current owner remains in the household, the Date of Purchase remains unchanged while the Date of Transfer of Ownership will be updated.</p><p>For outright transfer where there is a total change of all owner(s), only the Date of Purchase will be updated.</p></td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.loangranted</td><td>HDB Ownership - Loan Granted</td><td>The amount of housing loan granted to owner(s) by HDB.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.originalloanrepayment</td><td>HDB Ownership - Original Loan Repayment Period</td><td>The number of years for loan repayment opted by owner(s) at the time the loan is first granted to him/her.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.balanceloanrepayment</td><td>HDB Ownership - Balance Loan Repayment Period</td><td>The remaining number of year(s) and month(s) available to repay the loan.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.outstandingloanbalance</td><td>HDB Ownership - Outstanding HDB Loan Balance</td><td>Outstanding amount payable to HDB.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.monthlyloaninstalment</td><td>HDB Ownership - Monthly Loan Instalment</td><td>Monthly instalment payable to HDB.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.purchaseprice</td><td>HDB Ownership - Purchase Price</td><td>This refers to the price at which the flat owner paid for the flat.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr><tr><td>hdbownership.outstandinginstalment</td><td>HDB Ownership - Outstanding Instalment</td><td>This refers to the outstanding instalment owed by the flat owner(s) which includes the current month instalment. GST is not applicable. If there is advance payment, the value will be 0.</td><td>SC,PR,FIN</td><td>HDB</td><td>HDB Ownership</td></tr></tbody></table>


# Government Scheme

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

<table><thead><tr><th width="112">id</th><th width="144">name</th><th width="271.46484375">description</th><th width="100.9921875">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>pioneergen.eligibility</td><td>Pioneer Generation Eligibility</td><td>The Government has introduced the Pioneer Generation Package to honour and thank our pioneers for their hard work and dedication in making Singapore what it is today. The package includes a host of initiatives aimed at making healthcare affordable for our Pioneer Generation for life.</td><td>SC</td><td>MOF/CPFB</td></tr><tr><td>merdekagen.eligibility</td><td>Merdeka Generation Eligibility</td><td>The Government has introduced the Merdeka Generation Package to honour and thank our Merdeka Generation for their contributions. The package supports the aspirations of Merdeka Generation seniors in their silver years by helping them to stay active and healthy and providing them better peace of mind over future healthcare costs.</td><td>SC</td><td>MOF/CPFB</td></tr><tr><td>chas</td><td>Community Health Assist Scheme</td><td><p>The Community Health Assist Scheme (CHAS) enables all Singapore Citizens, including Pioneer Generation (PG) and Merdeka Generation (MG) cardholders, to receive subsidies for medical and/or dental care* at participating General Practitioner (GP) and dental clinics.</p><p>For patients with chronic conditions, CHAS complements the Chronic Disease Management Programme (CDMP), which allows for MediSave to be used for outpatient treatment (for the same set of chronic conditions) covered under CHAS. Besides enjoying CHAS subsidies for the treatment of their chronic conditions, patients can also tap on their MediSave to defray part of the cost of these treatments.</p><p>Patients who seek treatment for their chronic conditions at CHAS GP clinics can also receive subsidised rates for healthcare services such as Diabetic Foot Screening (DFS), Diabetic Retinal Photography (DRP) and nurse counselling at Community Health Centres (CHCs) and Primary Care Network (PCN) clinics.</p></td><td>SC</td><td>MOH</td></tr></tbody></table>


# Data for Government Agencies

{% hint style="info" %}
**Note:** MCR and POCDEX data scopes are only available to Singapore Government agencies, as the data is approved for sharing between government agencies only. These scopes are not available to private sector organisations.
{% endhint %}

{% hint style="warning" %}
**MCR and POCDEX scopes require explicit user consent.** User consent is required for MCR and POCDEX scopes. While consent may be suppressed for other Myinfo data requested by government agencies, users will always be shown a consent screen when MCR or POCDEX data is requested.
{% endhint %}

This page documents two government-exclusive data categories:

* **POCDEX (Public Officer Career Data Exchange)** — employment records of public officers, including job title, employment type, work email, agency, and department. Sourced from PSD.
* **MCR (Medical Council Register)** — healthcare professional registration records across seven regulatory boards (SMC, SDC, SNB, SPC, AHPC, OOB, TCMPB), including registration details, practising certificate validity, and specialty information.

{% hint style="info" %}
Download the [OpenAPI specification file](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo#person-information-openapi-specification) for the full list of Myinfo person data scopes, field structures, value types, accepted formats, and maximum field lengths. This serves as the technical reference for developers integrating with the Myinfo API.
{% endhint %}

## Public Officer Employments

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>public_officer_employments.title</td><td>Public Officer Employments - Job Title</td><td></td><td>SC,PR</td><td>PSD</td></tr><tr><td>public_officer_employments.type</td><td>Public Officer Employments - Employment Type</td><td></td><td>SC,PR</td><td>PSD</td></tr><tr><td>public_officer_employments.email</td><td>Public Officer Employments - Work Email</td><td>Work email address of the public officer</td><td>SC,PR</td><td>PSD</td></tr><tr><td>public_officer_employments.agency</td><td>Public Officer Employments - Agency</td><td></td><td>SC,PR</td><td>PSD</td></tr><tr><td>public_officer_employments.department</td><td>Public Officer Employments - Department</td><td></td><td>SC,PR</td><td>PSD</td></tr></tbody></table>

## Healthcare Profession - Medical (Singapore Medical Council)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.medical.healthcare_professional_entity</td><td>Medical Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registration_number</td><td>Medical Healthcare Entity - Registration Number</td><td>Public-facing professional registration number</td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.register_id</td><td>Medical Practising Certificate - Register ID</td><td>Unique registration record identifier (PRS primary key)</td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.register_type</td><td>Medical Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.registration_type</td><td>Medical Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.practising_certificate_start_date</td><td>Medical Practising Certificate - Validity Start Date</td><td>Value of data field in YYYY-MM-DD format.</td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.practising_certificate_end_date</td><td>Medical Practising Certificate - Validity End Date</td><td>Value of data field in YYYY-MM-DD format.</td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.practice_status</td><td>Medical Practising Certificate - Status</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.registration_start_date</td><td>Medical Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.specialty_name</td><td>Medical Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>SMC</td></tr><tr><td>healthcare_professions.medical.registrations.specialty_type</td><td>Medical Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>SMC</td></tr></tbody></table>

## Healthcare Profession - Dental (Singapore Dental Council)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.dental.healthcare_professional_entity</td><td>Dental Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registration_number</td><td>Dental Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.register_id</td><td>Dental Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.register_type</td><td>Dental Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.registration_type</td><td>Dental Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.practising_certificate_start_date</td><td>Dental Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.practising_certificate_end_date</td><td>Dental Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.practice_status</td><td>Dental Practising Certificate - Status</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.registration_start_date</td><td>Dental Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.specialty_name</td><td>Dental Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>SDC</td></tr><tr><td>healthcare_professions.dental.registrations.specialty_type</td><td>Dental Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>SDC</td></tr></tbody></table>

## Healthcare Profession - Nursing (Singapore Nursing Board)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.nursing.healthcare_professional_entity</td><td>Nursing Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registration_number</td><td>Nursing Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.register_id</td><td>Nursing Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.register_type</td><td>Nursing Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.registration_type</td><td>Nursing Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.practising_certificate_start_date</td><td>Nursing Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.practising_certificate_end_date</td><td>Nursing Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.practice_status</td><td>Nursing Practising Certificate - Status</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.registration_start_date</td><td>Nursing Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.specialty_name</td><td>Nursing Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>SNB</td></tr><tr><td>healthcare_professions.nursing.registrations.specialty_type</td><td>Nursing Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>SNB</td></tr></tbody></table>

## Healthcare Profession - Pharmacy (Singapore Pharmacy Council)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.pharmacy.healthcare_professional_entity</td><td>Pharmacy Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registration_number</td><td>Pharmacy Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.register_id</td><td>Pharmacy Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.register_type</td><td>Pharmacy Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.registration_type</td><td>Pharmacy Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.practising_certificate_start_date</td><td>Pharmacy Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.practising_certificate_end_date</td><td>Pharmacy Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.practice_status</td><td>Pharmacy Practising Certificate - Status</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.registration_start_date</td><td>Pharmacy Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.specialty_name</td><td>Pharmacy Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>SPC</td></tr><tr><td>healthcare_professions.pharmacy.registrations.specialty_type</td><td>Pharmacy Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>SPC</td></tr></tbody></table>

## Healthcare Profession - Allied Health (Allied Health Professions Council)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.allied_health.healthcare_professional_entity</td><td>Allied Health Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registration_number</td><td>Allied Health Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.register_id</td><td>Allied Health Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.register_type</td><td>Allied Health Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.registration_type</td><td>Allied Health Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.practising_certificate_start_date</td><td>Allied Health Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.practising_certificate_end_date</td><td>Allied Health Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.practice_status</td><td>Allied Health Practising Certificate - Status</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.registration_start_date</td><td>Allied Health Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.specialty_name</td><td>Allied Health Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>AHPC</td></tr><tr><td>healthcare_professions.allied_health.registrations.specialty_type</td><td>Allied Health Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>AHPC</td></tr></tbody></table>

## Healthcare Profession - Optometry and Opticianry (Optometrists & Opticians Board)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.optometry_opticianry.healthcare_professional_entity</td><td>Optometry and Opticianry Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registration_number</td><td>Optometry and Opticianry Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.register_id</td><td>Optometry and Opticianry Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.register_type</td><td>Optometry and Opticianry Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.registration_type</td><td>Optometry and Opticianry Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.practising_certificate_start_date</td><td>Optometry and Opticianry Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.practising_certificate_end_date</td><td>Optometry and Opticianry Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.practice_status</td><td>Optometry and Opticianry Practising Certificate - Status</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.registration_start_date</td><td>Optometry and Opticianry Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.specialty_name</td><td>Optometry and Opticianry Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>OOB</td></tr><tr><td>healthcare_professions.optometry_opticianry.registrations.specialty_type</td><td>Optometry and Opticianry Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>OOB</td></tr></tbody></table>

## Healthcare Profession - Traditional Chinese Medicine (TCM Practitioners Board)

<table><thead><tr><th width="149">id</th><th width="139.5390625">name</th><th width="254.9375">description</th><th width="120.5859375">Data Available</th><th>Source</th></tr></thead><tbody><tr><td>healthcare_professions.traditional_chinese_medicine.healthcare_professional_entity</td><td>Traditional Chinese Medicine Healthcare Entity - Name</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registration_number</td><td>Traditional Chinese Medicine Healthcare Entity - Registration Number</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.register_id</td><td>Traditional Chinese Medicine Practising Certificate - Register ID</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.register_type</td><td>Traditional Chinese Medicine Practising Certificate - Register Type</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.registration_type</td><td>Traditional Chinese Medicine Practising Certificate - Registration Type</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.practising_certificate_start_date</td><td>Traditional Chinese Medicine Practising Certificate - Validity Start Date</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.practising_certificate_end_date</td><td>Traditional Chinese Medicine Practising Certificate - Validity End Date</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.practice_status</td><td>Traditional Chinese Medicine Practising Certificate - Status</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.registration_start_date</td><td>Traditional Chinese Medicine Practising Certificate - Registration Date</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.specialty_name</td><td>Traditional Chinese Medicine Practising Certificate - Specialty Name</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.registrations.specialty_type</td><td>Traditional Chinese Medicine Practising Certificate - Specialty Type</td><td></td><td>SC,PR</td><td>TCMPB</td></tr><tr><td>healthcare_professions.traditional_chinese_medicine.practitioner_chinese_name</td><td>Traditional Chinese Medicine Practitioner - Chinese Name</td><td>Chinese name registered with MOH by the Traditional Chinese Medicine practitioner. Returns Chinese characters (e.g. 陈大文), or empty string ("") if unavailable.</td><td>SC,PR</td><td>MOH</td></tr></tbody></table>


# Overview

Guide to Navigating the Singpass Developer Portal (SDP)

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1cb5e4572aba97fb634d2458c16a6bc95bd5191f%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

The Singpass Developer Portal (SDP) is the central platform where organisations:

* **Create** and **manage** Singpass API applications
* **Configure** redirect URIs, JWK Urls, certificates, scopes, and other settings
* Access **billing** information, **test accounts**, and **services agreement**

This guide walks you through everything you need to know to navigate the portal efficiently.

Access to the SDP is necessary to begin integration with Singpass APIs.


# Getting Access


# Obtaining Access to the Singpass Developer Portal (SDP)

This page offers a guide to obtain access and login to SDP

To log in to the [Singpass Developer Portal](https://developer.singpass.gov.sg), your Singpass account must first be authorised via Corppass to act on behalf of your organisation.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-6c9f20c225b0d73028dec652d6503f65f122b69e%2Fscreen-1763450704432.gif?alt=media" alt=""><figcaption></figcaption></figure>

**Step 1 — Identify your Corppass Admin**

1. Visit [https://www.corppass.gov.sg](https://www.corppass.gov.sg/)
2. Go to Services → Find your Corppass Admin
3. Authenticate with Singpass
4. Search for your organisation using the Unique Entity Number (UEN)

This will show you who the **Corppass Admin(s)** are within your entity.<br>

**Step 2 — Request Access**

Contact your Corppass Admin and ask them to grant your Singpass account the necessary permissions to access:

* **Singpass Developer Portal**

Once the admin assigns the access rights, you will be able to log in to the Singpass Developer Portal.


# Logging in to the Singpass Developer Portal (SDP)

Before logging in, ensure your Singpass account has been authorised via Corppass to act on behalf of your organisation.

{% stepper %}
{% step %}

### Access the Portal

Go to <https://developer.singpass.gov.sg> and click **Log in** at the top of the page.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-766279b855b1f748d21166815aa04787f1946760%2F02-login-landing-page.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Authenticate and select your entity

Complete the Singpass authentication flow. After authentication, you will be prompted to select the entity (UEN) you are representing.

* If you are authorised for only one entity, the selection page will not appear.
* If you have access to multiple entities, choose the correct entity you want to transact for.

*Note: You will be logging in as a Business User.*

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c1369f4e21280de910defdc15948315f8e2d2dab%2F04-entity-selection.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Access the Dashboard

Click on the entity name. You will be redirected to the SDP Dashboard.

By default, the dashboard will display all Staging applications for that entity.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8514a3ef05d36c0d6060ffc3b36c0049a8d1e955%2F06-dashboard-post-login.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Toggling Between Staging and Production

After logging in to SDP, the dashboard defaults to the **Staging environment**, showing all your entity's staging apps.

{% stepper %}
{% step %}

### View your Staging dashboard

By default, the dashboard shows your **Staging** apps.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8124820784915bf6c89964a5c4bb392f7e879b69%2F02-dashboard-staging-default.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click the environment toggle

To switch environments, click the **environment toggle** at the top of the page:

* "Working with mock data in Staging"
* "Working with live data in Production"

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-9d7b05dfdd9b2eac1103f2ee635ace8a528b2b64%2F04-environment-toggle-staging.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### View your Production dashboard

The dashboard now shows your **Production** apps.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-efc7a08cbcf381167f22ad23665b6de72b461669%2F05-dashboard-production-view.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Service Agreement


# View Singpass Service Agreement

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)

{% stepper %}
{% step %}

### Open Service Agreement

Click the **profile icon** in the top menu and select **Service Agreement**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-0aeae850f6818bf79b9f0672d4cd7a35db4832c1%2FSvc%20Agreement%20Menu.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review the Service Agreement

You will be redirected to the Service Agreement review page.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-e55c5175ef9e6509e55e5c6d4ec2e7c3d5970ccb%2FView%20Svc%20Agreement.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Consent to Singpass Service Agreement

This applies to private-sector partners who do not have an existing Singpass Services Agreement.

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Production**.

{% stepper %}
{% step %}

### Open Service Agreement

Click the **profile icon** showing your UEN and select **Service Agreement**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-75fb645844188e2c7576f8c50fbf2cb5eeec3ba7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review the agreement and click Next

Read through the Service Agreement, then click **Next**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8d1b064342678182bf460d9c05dc9bb88e70e80e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Verify your company details

Confirm the company Point-of-Contact (POC) and Company/Entity Name shown.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4d22e83fbc8840de2d23c9846143cf7569de8f1a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Fill in contact details and click I agree

Under **Agreement accepted by**, your name and entity name are pre-filled. Fill in your job title, the agreement contact emails and the entity address. Fill in the billing contact details, then click **I agree**.

* Select **Same as entity address** to use the entity address as the billing address.
* At least one billing contact email must be verified before you can accept the agreement. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
* Agreement contact emails do not need to be verified.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-a63628f54d78e80c2261c82560a0d92b1757439a%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Agreement accepted

The Service Agreement is now accepted. You will see the confirmed POC and company/entity name.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-6aee2cd05ba154d8d62e34766b49f6347888d26e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Create your Production app

You can now create apps in the Production environment using **+ New App**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1cbe7ddfbf586a593720b1b38f3ac5c138a19d18%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# App Management


# Create Staging App

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Staging**.

### **Steps:**

{% stepper %}
{% step %}

### **Click + New App**

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-e5b675ca45d23db68fa9ee03f3f7faa129672a3f%2FScreenshot%202026-06-18%20at%209.53.57%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### **Select the App Type to create:**

* Singpass Login – for authentication use cases
* Singpass Myinfo – for form-filling use cases
* Myinfo Business - for form-filling (Corporate)
* Sign with Singpass - for digital signing

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-94eb48a8b531a0e7967d0aed8098da2237ebd86d%2FScreenshot%202026-06-18%20at%209.44.59%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Fill in the app details and click Next

You can toggle to preview the consent screen, Login screen and Singpass app that your users will see.

{% hint style="info" %}
App name must be **100 characters or fewer**.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8578ac5cf41f2a4f9061f0f9fb0e7528018f99e1%2Ffill%20info_stg.gif?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Provide the technical details and Click Next

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-49959c34d522d1af2d4742f3d0391671f29adbd3%2FScreenshot%202026-06-18%20at%209.57.52%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select the relevant scopes and Click Next

* OpenID is a mandatory scope
* For Login, only Email Address, Mobile Number, Principal Name and User Identity is available and allowed.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4f2ad7f71fab0ed724485a14ce64511b3346cb8c%2FScreenshot%202026-06-18%20at%209.59.42%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review and submit the app

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c245dac77c4edd9301e0507e7ffd2eb648bbcb13%2FScreenshot%202026-06-18%20at%209.59.52%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**FAPI 2.0 automatic migration notice**

If your app has been consistently sending FAPI 2.0-compliant traffic over the past 7 days, you may see an informational banner on your Dashboard and App Settings pages. This banner confirms that your app will be automatically migrated to FAPI 2.0 and that no action is required on your part. The legacy API will continue to be supported until 31 Dec 2026
{% endhint %}

<br>


# Edit Staging App

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Staging**.
* You have at least one Staging App to edit.

{% stepper %}
{% step %}

### Click on the App Name

Click the **App Name** link on your Dashboard — Staging view.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-76faa1751ab966a52632ae1aca7df362d475e2bd%2F02-staging-dashboard-app-list.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If your app has been consistently sending FAPI 2.0-compliant traffic over the past 7 days, you may see a grey informational banner on the Dashboard and on the App Settings page. This banner confirms that your app will be automatically migrated to FAPI 2.0. No action is required on your part. The legacy API will continue to be supported until 31 Dec 2026.
{% endhint %}
{% endstep %}

{% step %}

### Click Edit

You will be redirected to view the Staging App details. Click **Edit**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4c741b68fd7e1a5739c4b1d2e5261c0e9541ed68%2F04-staging-app-detail-view.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Update the app details and click Update

Edit the necessary details and click **Update**.

{% hint style="info" %}
The **Client External ID** is read-only and cannot be changed after the app is created.
{% endhint %}

{% hint style="info" %}
For Login and Myinfo (v5) apps, you can configure the following in the **Security** section:

* **Assurance level** — AAL 1 or AAL 2. Changing the assurance level resets **Allowed ACR values** to their defaults.
* **Allowed ACR values** — the assurance levels your app can request.
* **Authentication method** — how users sign in to your app.

AAL 3 (Singpass Face Verification) can only be set by Singpass. To request it, contact Singpass support.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b868137d19be5e2bc387fdb0b004ce72ab08f18d%2F06-staging-app-edit-form.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Create Staging Test Account

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Staging**.
* You have at least one Staging App.

{% stepper %}
{% step %}

### Click on the App Name

Click the **App Name** link on your Dashboard — Staging view.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-76faa1751ab966a52632ae1aca7df362d475e2bd%2F02-staging-dashboard-app-list.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Test Accounts

You will be redirected to view the Staging App details. On the left menu, click **Test Accounts**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-88b30207b8024e08a6400c74b619c6e7533d03b6%2F06-test-accounts-list.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Create

You will see the list of test accounts. Click **Create**.

{% hint style="info" %}
You can create a maximum of **5 test accounts**. Test accounts are not restricted to a specific app.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-88b30207b8024e08a6400c74b619c6e7533d03b6%2F06-test-accounts-list.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### View your new test account

A new test account is created and displayed. Click the eye icon to view the account password.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-7563934c5e053702bc0eed86ed781590cf50ac3c%2F08-test-account-created.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Create Production App

**Prerequisites:**

* You have to be successfully logged into [Singpass Developer Portal](https://developer.singpass.gov.sg) before you can create Production App.
* You have already toggled your Dashboard view to Production.
* The entity has already agreed to the Singpass Service Agreement.

### Steps:

{% stepper %}
{% step %}

### **Click + New App**

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-bfd30f0c5e82463d37025b2d17a447881a166657%2FScreenshot%202026-06-18%20at%2010.07.30%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select the App Type to create

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c3d565a32fb51e10031a4e83f89cba18ada2de13%2FScreenshot%202026-06-18%20at%209.45.07%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Fill in the App Details and click Next

You can toggle to preview the consent screen, Login screen and Singpass app that your users will see.

{% hint style="warning" %}
**At least one verified contact email is required.** In the Production environment, you can only submit an app, update an app, or change its status if at least one of its contact emails is verified. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-903a75e83a4b58dec2c967648de78895eb01519f%2Ffill%20info_prod.gif?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Provide the technical details and click Next

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-2255a33d018e6aefceba4ef36b5e628149a7837e%2FScreenshot%202026-06-18%20at%2010.24.26%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select the relevant data scopes and click Next

* OpenID is a mandatory scope
* For Login, only Email Address, Mobile Number, Principal Name and User Identity is available and allowed.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-36e02e90bda89ab38a1796836f96f6b1af0a1d0d%2FScreenshot%202026-06-18%20at%2010.07.48%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review the selected data scope and click Next

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d8b10abf8b0a9044ba845b636492035b3a89bd6d%2FScreenshot%202026-06-18%20at%2010.08.04%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Upload the User Journey and click Submit app

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-519227fc7b6131cf258d0dfdb1a9b5c1f16f804e%2FScreenshot%202026-06-18%20at%2010.17.32%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Check the acknowledgement checkbox and click Submit app

{% hint style="warning" %}
Do note that the approval process may take up to two weeks. Do factor in this time when planning your app launch.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-655976afa2fa125369c694552d263eeec0aa2875%2FScreenshot%202026-06-18%20at%2010.09.27%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

{% hint style="info" %}
**FAPI 2.0 automatic migration notice**

If your app has been consistently sending FAPI 2.0-compliant traffic over the past 7 days, you may see an informational banner on your Dashboard and App Settings pages. This banner confirms that your app will be automatically migrated to FAPI 2.0 and that no action is required on your part. The legacy API will continue to be supported until 31 Dec 2026
{% endhint %}


# Edit Production App

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Production**.
* You have at least one Production App with status **Activated**.

{% stepper %}
{% step %}

### Click on the App Name

Click the **App Name** link on your Dashboard — Production view.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-dcf1953c77ad56c11c83a8552d10dcf021ccadc1%2F02-production-dashboard.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If your app has been consistently sending FAPI 2.0-compliant traffic over the past 7 days, you may see a grey informational banner on the Dashboard and on the App Settings page. This banner confirms that your app will be automatically migrated to FAPI 2.0. No action is required on your part. The legacy API will continue to be supported until 31 Dec 2026.
{% endhint %}
{% endstep %}

{% step %}

### Click Edit

You will be redirected to view the Production App details. Click **Edit**.

{% hint style="info" %}
The **Edit** button is not visible for apps with status **Pending Approval**.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-278016b391cb954d6fcd9ab882f1c3bdc5520c5a%2F04-production-app-detail-with-edit-button.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-9ce292a22925208641f026df1551a9859aaad814%2F06-production-app-pending-no-edit-button.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Update the app details and click Update

Edit the necessary details and click **Update**.

{% hint style="warning" %}
**At least one verified contact email is required.** In the Production environment, you can only submit an app, update an app, or change its status if at least one of its contact emails is verified. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
{% endhint %}

{% hint style="info" %}
Changes to App name, User Journey, App Purpose, or Allowed Scopes will go through an approval process before being applied.
{% endhint %}

{% hint style="info" %}
For Login and Myinfo (v5) apps, the **Security** section shows the app's **Assurance level**, **Allowed ACR values** and **Authentication method**. These fields are managed by Singpass and cannot be edited in the Production environment. To request a change, contact Singpass support.

For other app types, **Authentication type** cannot be edited in the Production environment.
{% endhint %}

{% hint style="info" %}
The **Client External ID** is read-only and cannot be changed after the app is created.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-68f3110feb1232182cdb8c5c25f7b6053404f621%2F08-production-app-edit-form.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Deactivate Production App

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Production**.
* You have an existing Production App with status **Activated**.
* Your entity has agreed to the Singpass Services Agreement.

{% hint style="warning" %}
Deactivating an app **immediately stops all live transactions**. Users will not be able to log in or retrieve data via this app until it is reactivated.
{% endhint %}

{% stepper %}
{% step %}

### Click on the App Name

Click the **App Name** link on your Dashboard — Production view.

{% hint style="warning" %}
**At least one verified contact email is required.** In the Production environment, you can only submit an app, update an app, or change its status if at least one of its contact emails is verified. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-2dd32d954791ee5b7692174bed22f45c3ea82c61%2F02-production-dashboard-activated-app.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Deactivate App

You will be redirected to the app detail view. Click **Deactivate App**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d29dcbd39cd125b5c79777ac1a7fa7bd0f1bcaff%2F06-production-app-activated.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### App is now Deactivated

The app status updates to **Deactivated** and the **Activate App** option becomes available.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-540a3c48526db0104b047ceb093519e461c159d7%2F06-production-app-deactivated.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

***

### Reactivating a deactivated app

If you deactivated the app yourself, you can reactivate it at any time. See [Activate Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/activate-production-app) for steps.

{% hint style="info" %}
If your app was deactivated by a Singpass admin (status: **Suspended**), you will not be able to reactivate it yourself. Contact Singpass support to have it reinstated.
{% endhint %}


# Activate Production App

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)
* Switch your Dashboard view to **Production**.
* Your entity has agreed to the Singpass Services Agreement.

***

### App statuses and what you can do

| Status             | What it means                        | Can you activate?                                       |
| ------------------ | ------------------------------------ | ------------------------------------------------------- |
| **Deactivated**    | You deactivated the app              | Yes — click **Activate App**                            |
| **Suspended**      | Deactivated by a Singpass admin      | No — contact Singpass support to reinstate              |
| **Pending Review** | App is under review after submission | No — wait for approval before the Client ID can be used |

***

### Steps to activate a Deactivated app

{% stepper %}
{% step %}

### Click on the App Name

Click the **App Name** link on your Dashboard — Production view. Confirm the app status shows **Deactivated**.

{% hint style="warning" %}
**At least one verified contact email is required.** In the Production environment, you can only submit an app, update an app, or change its status if at least one of its contact emails is verified. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-7cb93e7a9d3ef62b35ecd46ade64df13f5e23e64%2F02-production-dashboard-deactivated-app.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Activate App

You will be redirected to the app detail view. Click **Activate App**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ae2868f86032f8c8e6e7c29a912b90719222aefa%2FScreenshot%202026-08-11%20at%2010.04.24%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### App is now Activated

The app status updates to **Activated** and the **Deactivate App** option becomes available.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-7baf1468c65d4e5281e6d6d53c3d143eedd35143%2FScreenshot%202026-08-11%20at%2010.04.30%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

***

### Suspended by admin

If your app has been suspended by a Singpass admin, the **Activate App** button will not be visible. A notice on the app detail page will indicate the suspension.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-e017beaf9ba58e866ecf8696156ebca8ca513682%2FScreenshot%202026-08-11%20at%2010.07.27%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
You cannot reactivate a suspended app yourself. Contact Singpass support to have the suspension reviewed and lifted.
{% endhint %}

***

### Pending Review

If your app is under review, the app detail page will show a **Pending Review** or **Pending Approval** status. There is no Activate button at this stage.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-2911a757ca48001553c3c0761986a3ccbd092307%2FScreenshot%202026-08-11%20at%2010.08.43%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Your **Client ID cannot be used** until the review is complete and the app status changes to **Activated**. Wait for the approval email before proceeding with your integration.
{% endhint %}


# Duplicate an app

{% hint style="info" %}
The following steps applies to **only Myinfo (v3/v4) apps**, both in **Staging and Production** environment.
{% endhint %}

**When to duplicate your app?**

Use the **Duplicate app** function to migrate your existing Myinfo (v3/v4) app to Myinfo v5. The duplicated app carries over all your existing configuration. No re-review or re-approval is required.

Note:

* You **cannot modify** the app name, purpose, scope selection and user journey when duplicating. If you need to change any of these, create a new app instead.
* You **can modify** your contact email, site URL, redirect URLs and JWKS endpoint/object when duplicating.
* You can duplicate Myinfo v3/v4 apps with status **Activated** or **Suspended**. Apps pending approval cannot be duplicated.

## Steps

{% stepper %}
{% step %}

### Click on Duplicate app

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1466b922969d49248cb7e33129569341c61c8ed3%2FScreenshot%202026-06-19%20at%204.36.54%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Select the relevant app purpose

If your existing Myinfo v3v4 app has multiple purposes, select one purpose per duplication and repeat the steps for each purpose.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-aef59a6346b2d9570ca5458d315b5f9e8fcacc35%2FScreenshot%202026-06-19%20at%204.36.59%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review the app name and purpose

Scroll down to review the app config details.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-d6110cc2eaae702538581d836e3b6388c626f20c%2FScreenshot%202026-06-19%20at%204.37.05%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Update contact email, click Next

You may update the contact emails of your app if needed.

{% hint style="warning" %}
When duplicating a Production app, at least one contact email must be verified. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails).
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-62a9cf14311ffb882ca3ec6da08e4510ab51c277%2FScreenshot%202026-06-19%20at%204.37.11%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Update Technical details, click Next

You may also update the technical details, such as redirect URLs and JWKS information.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4016c5a4e6d586873862287fec7d1e69003f4b7b%2FScreenshot%202026-06-19%20at%204.37.13%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Review scope selection, click Duplicate app

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ea80760b43504767e399a3ccda9572f7a7ecbf29%2FScreenshot%202026-06-19%20at%204.37.22%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### You have successfully duplicated your app

You can now use the new App ID for development works!

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ddc9da405124397052846d24ac5347e769ab5eba%2FScreenshot%202026-06-19%20at%204.37.53%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Managing Drafts

### Overview

Drafts allow you to save an incomplete app creation and return to finish it later. Progress is saved automatically as you work, so you do not need to complete app creation in a single session.

***

### Accessing your drafts

Your drafts appear at the top of your dashboard when you log in to SDP. Only drafts you created are visible to you — drafts created by other members of the same entity are not shown.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c6145161127f12d689ea6a4bf724fdfe369894dd%2FScreenshot%202026-07-15%20at%2011.23.51%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### How drafts work

* **Auto-save:** Your progress is saved automatically as you fill in each step. There is no manual save required. While a save is in progress, a **"Saving..."** indicator is shown in the form; once complete, it changes to show when the draft was last saved.
* **Multiple drafts:** You can have more than one draft open for the same product at the same time.
* **Resuming a draft:** Select a draft from your dashboard to continue where you left off.
* **Deleting a draft:** To remove a draft manually, select the draft from your dashboard and choose **Delete**.

***

### Draft expiry

Drafts expire after **30 days** of inactivity. Once expired, the draft is permanently deleted and cannot be recovered.

To help you track this:

* The expiry countdown for each draft is displayed on the draft card in SDP.
* You will receive an email notification **7 days before** a draft expires.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ec222a0e130631474a137641d8a326e9651e002a%2FScreenshot%202026-08-03%20at%209.02.30%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-1961de12ead4eba044ac0f09b36173ff37bd6640%2FScreenshot%202026-08-03%20at%209.06.54%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
**Expired drafts cannot be recovered**. If you receive an expiry reminder, review and submit your app accordingly before the deadline to avoid losing your progress.
{% endhint %}


# Understanding the App Config Fields


# App name & purpose

The **app name** is the name of your digital service/application. It appears on the consent page that your users see when they give consent to log in to your service. The app name must be **100 characters or fewer**.

The **app purpose** is only applicable for Myinfo apps and is also displayed on the consent page.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-6bb6b9c7b296c08d417c4200bc4d176d120c298b%2F02-config-app-name-field.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — App name field</p></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-cde1818a7cbd6c8817481653e381881f9abbcc87%2F04-config-app-purpose-field.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — App purpose field</p></figcaption></figure>


# App Use Case Description

This is the description of your digital service/application. Please describe your app's use case and purposes.

{% hint style="info" %}
The description indicated here will not appear on the consent page. It is for Singpass's administrative purposes.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-fda26f41c6bee70670abddd23acd582c3e8f1f41%2F06-config-app-description-field.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — Description field</p></figcaption></figure>


# Industry & App category

Select the industry your organisation operates in and the app category that best describes how your app integrates with Singpass. This helps us assess your user flow and configuration requirements.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b50d7ddd7e3fb3a2c662fa379586f4c19a9100d8%2F08-config-industry-app-category.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — Industry and App category fields</p></figcaption></figure>


# Contact Emails

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ac70dc29366d130766b7602f8658755169eefe41%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## Updating Your Application Contact Emails

Keep the contact email addresses for your Production application up to date in the Singpass Developer Portal. Singpass administrators use them for:

* Service announcements and changes
* Migration or compliance deadlines
* Technical or operational notifications
* Requests for action or clarification

### Update your Production contacts

Singpass primarily contacts the persons listed for your Production application. Keep these details accurate and update them when team members, responsibilities, or email addresses change.

Outdated contacts may cause your team to miss important updates or required actions. Where appropriate, use a monitored team or shared mailbox alongside individual addresses.

### How to update your contact emails

1. Sign in: Log in to the Singpass Developer Portal at `developer.singpass.gov.sg`.
2. Select Production: Open the Production environment.
3. Open your application: Select the application you want to update.
4. Edit details: Open the option to edit your Production application details.
5. Update and save: Review the contact email addresses, make changes, and save.

For detailed instructions, refer to the [guide on editing Production apps](https://app.gitbook.com/o/oIOKcTCZC2fptOuInlww/s/OV8xmtJpBBV1NehZlKZb/).

### Verifying your contact emails

Each contact email shows its verification status: **Verified recipients**, **Pending verification**, or **Unverified**.

* To verify a new email, enter it and click **Add and send verification email**. For an existing unverified email, click **Verify**.
* The recipient must open the verification link in the email. The link is valid for 14 days.
* If the link has expired, click **Resend** to send a new one. Resending is limited, and the portal shows when you can resend next.
* Emails are verified for your entity, so an email address verified once does not need to be verified again for your other apps.

{% hint style="warning" %}
In the Production environment, at least one contact email must be verified before you can submit a new app, update an app, or change its status. You cannot delete your last verified email — verify another email address first.
{% endhint %}

All listed contact emails receive Singpass communications, regardless of their verification status.

### Your responsibility

Review your Production contacts regularly and whenever your team changes. Keeping them current ensures the right people receive important Singpass communications and can act promptly.


# Site URL

This is the public URL of your application which users will access.

{% hint style="warning" %}
URL with IP address (e.g. <https://123.123.1.1>) is not allowed.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-7f79746a6930d161aed5fddfd1656db5bdf0f4f0%2F10-config-site-url-field.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — Site URL field</p></figcaption></figure>


# Redirect URL

A redirect URL is a URL in your digital service/application that Singpass will use to redirect users after they have been authenticated or when the ID Token is being returned.

{% hint style="warning" %}
URL with IP address (e.g. <https://123.123.1.1>) is not allowed.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-b8e242bc8942bf0c034c72e629999b3cef9a8e70%2F12-config-redirect-url-field.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — Redirect URL field</p></figcaption></figure>


# Token-based Authentication

Select the token-based authentication type. This will be used by Singpass for verification and encryption purposes. You can configure this using one of the following:

* **JWKS Endpoint** — provide a URL that hosts your JWKS

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-f060a4fb3e2e6a7099220113f528597a4020ea34%2F16-config-token-auth-jwks-endpoint.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — JWKS Endpoint option</p></figcaption></figure>

* **JWKS Object** — paste your JWKS JSON directly

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-fea4090f28bc4444af61a666b45b2bb091eef7cd%2F18-config-token-auth-jwks-object.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page — JWKS Object option</p></figcaption></figure>


# Allowed Scopes

This allows the selection of [scopes](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog) for your digital service/application.

{% hint style="info" %}
For production environment, every additional scope needs to be reviewed by the Singpass Admin and goes through an approval process.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-ce5a59894cf653175001efbaaa18dbd25d9dbb0f%2Fimage.png?alt=media" alt=""><figcaption><p>Singpass Developer Portal App Config Page - Allowed Scopes field</p></figcaption></figure>


# Billing & Finance


# Updating Billing Contact Information

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)

{% stepper %}
{% step %}

### Open Billing settings

In the **top menu**, click on the **profile icon** and select **Billing**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-12b59b077a44a7c7488770a805ba72786b902076%2F03-billing-profile-section.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Edit

Click the **Edit** button next to the billing contact details.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-441919a965ffc4645266ccfb1b6b861965aac8a7%2F05-billing-contact-edit-button.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Update contact details and click Update

Update the Login or Myinfo **billing contact details** as needed, then click **Update** to save your changes.

{% hint style="warning" %}
At least one billing contact email must be verified before you can save your changes. See [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails#verifying-your-contact-emails) for how verification works.
{% endhint %}

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-f6dfb95c68306d213d646d798974258420d74c7a%2F07-billing-contact-edit-form.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# How to View Production App Transactions

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg) using a Singpass account authorised to transact on behalf of your entity.
* Switch your Dashboard view to **Production**.

## Individual App Transactions

{% stepper %}
{% step %}

### Navigate to your Production Apps page

Switch your dashboard to Production to see all your production apps.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-04532901306605c24a0f5debc6a510e3514a0fba%2F02-production-apps-page.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click on the app

Click on the app for which you want to view transaction details.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8407da955b3902cf103b247e65d262691f3ebe1b%2F04-production-app-detail-analytics-menu.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Analytics

When the app page opens, locate the left menu and click **Analytics**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-0946f92614da26d1707330b25d2808f91f6936db%2F06-app-analytics-graph.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### View transaction graph

View your app's transaction graph and use filters to sort data by month and year.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-0946f92614da26d1707330b25d2808f91f6936db%2F06-app-analytics-graph.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

***

## Entity-Level Transactions

To view an overview of transactions across all your apps:

{% stepper %}
{% step %}

### Click View Entity Analytics

On the Production Apps page, beside your **Entity Name**, click **view entity analytics**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-bfcd49a0982623334496b8f15ed2ccefcea640cc%2F11-entity-analytics-tabs.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### View entity-level breakdown

Select the Month-Year and navigate between the **Login** and **Myinfo** tabs to view total transactions for your entity's apps.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-bfcd49a0982623334496b8f15ed2ccefcea640cc%2F11-entity-analytics-tabs.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# How to View Entity Transactions

The Entity Analytics page provides a breakdown of transactions across individual apps and shows how these contribute to the entity's overall transaction count.

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)

{% stepper %}
{% step %}

### Click Entity Analytics

From your dashboard, click **Entity Analytics** at the top right corner.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-8ab3b74ef84c3ef1c90cfc4c589b0a7effb916c3%2F02-dashboard-with-entity-analytics-button.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### View the transaction overview

The Entity Analytics overview shows total transactions for your entity.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-bfcd49a0982623334496b8f15ed2ccefcea640cc%2F11-entity-analytics-tabs.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Switch between Login and Myinfo tabs

* Click **Login** to view the transaction breakdown for Login apps by e-service.
* Click **Myinfo** to view the transaction breakdown for Myinfo apps by e-service.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-c336b26ebe9854023ecaa8d1ddd7263d62cbe857%2F06-entity-analytics-login-tab.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-2e94f3f28cbdf8ef3da63820cf16d65dc57d4582%2F10-export-usage-data-button.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Export usage data

Click **Export usage data** to download the transaction data.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-2e94f3f28cbdf8ef3da63820cf16d65dc57d4582%2F10-export-usage-data-button.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# How to View or Download Your Invoice

**Prerequisites:**

* Ensure you are logged in to the [Singpass Developer Portal](https://developer.singpass.gov.sg)

{% stepper %}
{% step %}

### Open Billing

Click the **profile icon** in the top menu and select **Billing**.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-87a49119ab206d882c7cf7ac9d21ff9791bda4d2%2F02-profile-icon-menu-billing.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Click Billing — Invoices

Navigate to the **Invoices** tab.

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-12b59b077a44a7c7488770a805ba72786b902076%2F03-billing-profile-section.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Search for your invoice

Search for your invoice by entering the month and year (e.g. Jul 2026).

<figure><img src="https://2816701917-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FW3T7d7fy7OGYkZf4zVKU%2Fuploads%2Fgit-blob-4aecd057038db24e2656eccee2cfbe1f85b5600d%2F06-invoice-search-page.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}


# Testing with Singpass App

Refer to guide below to test your integration with Staging Singpass App on QR authentication or 2FA Authentication.

{% embed url="<https://partnersupport.singpass.gov.sg/hc/en-sg/articles/33107472981657-Staging-Singpass-App-Installation-Tutorial-Guide#01HZ3YJQC5AF7BW8V4CXV5ZWQQ>" %}


# Myinfo Test Personas

We provide a set of Myinfo test personas with diverse attributes and metadata to help you simulate different user profiles when testing your Myinfo integration.

These test personas are intended solely for Myinfo data retrieval and verification testing.

### ⚠️ Important Usage Notes

* **Do not** use these test personas for **Singpass Login** applications.

  These accounts are not meant to be used to test Singpass Login flows.If you need to populate email addresses or mobile numbers to your [staging accounts](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-test-account) for Login flow testing, please use the following form: <https://go.gov.sg/sp-test-acc>
* Test persona details may change over time.

  The profile data associated with these personas is valid only at the time of testing. We may update, modify, or refresh persona attributes at any time without prior notice.
* Do not hardcode values.

  Your integration should not rely on fixed persona attributes (e.g. names, emails, addresses) and should handle changes gracefully.

## Singpass Login Credentials

*(For Myinfo testing only)*

> Username: \[UINFIN reflected in first column of file]\
> Password: `Userinfo@2024`

> These credentials are provided to support Myinfo test flows only and should not be used for production or Login app validation.

Download the full list of test personas below:

{% file src="/files/IPgiE15EWoUzi5Fe1upF" %}

Note: We updated the test profiles to reflect latest CPF transactions dates.


# Documentation Changelog

This page logs significant updates to the Singpass developer documentation. For API spec changes (FAPI 2.0 migration), refer to the [Changelog](https://docs.developer.singpass.gov.sg/docs/technical-specifications/changelog).

***

## November 2026

| Date   | Area                                | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 26 Nov | SDP — App Config Fields             | [Contact Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails) — new section on verifying contact emails: verification statuses, how to verify or resend, link validity, and the requirement for at least one verified email in Production                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 26 Nov | SDP — App Management                | [Create Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app), [Edit Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app), [Activate Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/activate-production-app), [Deactivate Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/deactivate-production-app), [Duplicate an App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/duplicate-an-app) — at least one verified contact email is now required to submit, update, or change the status of a Production app; suspended Myinfo v3/v4 apps can now be duplicated |
| 26 Nov | SDP — App Management                | [Edit Staging App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-staging-app), [Edit Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) — Assurance level, Allowed ACR values and Authentication method fields described for Login and Myinfo (v5) apps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 26 Nov | SDP — Billing and Service Agreement | [Updating Billing Contact Information](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/billing-and-finance/updating-billing-contact-information), [Consent to Singpass Service Agreement](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/service-agreement/consent-to-singpass-service-agreement) — at least one verified billing contact email is required; Service Agreement steps updated to match the current form                                                                                                                                                                                                                                                                                                                                                                                                    |
| 26 Nov | SDP — Getting Access                | [Logging in to SDP](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/getting-access/logging-in-to-the-singpass-developer-portal-sdp) — login step updated for the new portal homepage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 26 Nov | Integration Guide                   | [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange) — `invalid_grant` and `invalid_dpop_proof` causes clarified (single-use authorization codes, PKCE and DPoP key mismatch); note added that `expires_in` may not yet be returned in every environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 26 Nov | Integration Guide                   | [Authorization Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) — `urn:singpass:authentication:loa:1` documented as a staging-only `acr_values` option                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

***

## October 2026

| Date   | Area                     | Change                                                                                                                                                                                                                                                                                                                                 |
| ------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 15 Oct | Data Catalog             | [Data for Government Agencies](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog/government-only-data) — new scope `healthcare_professions.traditional_chinese_medicine.practitioner_chinese_name` (Traditional Chinese Medicine Practitioner - Chinese Name) added to TCM section; sourced from MOH EPC data    |
| 4 Oct  | Data Catalog             | New page: [Data for Government Agencies](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog/government-only-data) — POCDEX (public officer employment data from PSD) and MCR (healthcare professional registration across 7 regulatory boards) scopes documented; government-only, requires explicit user consent |
| 4 Oct  | Technical Specifications | OpenAPI YAML updated with POCDEX and MCR data schemas                                                                                                                                                                                                                                                                                  |
| 4 Oct  | Testing                  | [Myinfo test personas](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) updated with POCDEX and MCR test data                                                                                                                                                                                                 |

***

## September 2026

| Date   | Area              | Change                                                                                                                                                                                                                                                                             |
| ------ | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 18 Sep | Getting Started   | [Singpass Button Design Specification](https://docs.developer.singpass.gov.sg/docs/getting-started/singpass-button-design-specification) — button asset downloads refreshed; button type reference images updated                                                                  |
| 18 Sep | Getting Started   | [User Journey](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey) — Login and Myinfo user journey templates updated (September 2026 versions)                                                                                                               |
| 18 Sep | Migration Guides  | [Myinfo Business (v1/v2) Person v3 flows](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/migrating-mib-v1-v2-person-v3-to-myinfo-v5) — page title shortened; table formatting corrected                                                     |
| 15 Sep | Getting Started   | [Quick Start](https://docs.developer.singpass.gov.sg/docs/getting-started/quick-start), [Landing page](https://docs.developer.singpass.gov.sg/docs) — Sign with Singpass URL updated to point to Singpass developer docs                                                           |
| 3 Sep  | Integration Guide | [Authorization Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) — session timeout guidance added; applications should accommodate up to 10 minutes for users to complete the Singpass authentication flow |

***

## August 2026

| Date   | Area                     | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 24 Aug | SDP — App Management     | [Create Staging App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app), [Create Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-production-app), [Edit Staging App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-staging-app), [Edit Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) — FAPI 2.0 automatic migration notice added; explains the informational banner shown for apps with consistent FAPI 2.0 traffic; legacy API supported until 31 Dec 2026 |
| 24 Aug | Getting Started          | [App Logo](https://docs.developer.singpass.gov.sg/docs/getting-started/app-logo) — new sections added: logo preview shown during app creation wizard; logo pending-approval behaviour when a change request is under review                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 14 Aug | Technical Specifications | [Client Assertion guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) — `iat`/`exp` corrected to JSON numbers; compact JWT sample updated with correct payload (removed erroneous `code` field, added `jti`); validator tool description corrected (`jwk` → `kid`)                                                                                                                                                                                                                                                                                                                                                                         |
| 14 Aug | Integration Guide        | [Userinfo Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo) — `iat` field type corrected to Number; warning added that DPoP proof must include `ath` claim and `htu` must be `/fapi/userinfo`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 14 Aug | Integration Guide        | [Handling the Redirect](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/2.-handling-the-redirect) — successful redirect now correctly states three query parameters (`code`, `state`, `iss`)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 14 Aug | Integration Guide        | [Parsing the ID Token](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/4.-parsing-the-id-token) — dead anchor `#the-sub_account-claim` corrected to `#the-sub_attributes-claim`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 14 Aug | Migration Guides         | [Myinfo v4 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v4-apps) — userinfo comparison table corrected from `GET /userinfo` to `GET /fapi/userinfo`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 14 Aug | Getting Started          | New page: [Singpass Button Design Specification](https://docs.developer.singpass.gov.sg/docs/getting-started/singpass-button-design-specification) — button design specifications for developers and designers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 14 Aug | Getting Started          | New page: [Singpass Brand Guidelines](https://docs.developer.singpass.gov.sg/docs/getting-started/singpass-brand-guidelines) — brand guidelines consolidated into Getting Started                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 14 Aug | Products                 | [Singpass Button Guidelines](https://github.com/SingpassPX/dev-docs/tree/main/products/singpass-login/singpass-button-guidelines-for-developers-and-designers.md) page removed — content moved to [Singpass Button Design Specification](https://docs.developer.singpass.gov.sg/docs/getting-started/singpass-button-design-specification) under Getting Started                                                                                                                                                                                                                                                                                                                                                      |
| 14 Aug | Products                 | [Logo Download and Brand Guidelines](https://github.com/SingpassPX/dev-docs/tree/main/products/singpass-myinfo/logo-download-and-brand-guidelines.md) page removed — content moved to [Singpass Brand Guidelines](https://docs.developer.singpass.gov.sg/docs/getting-started/singpass-brand-guidelines) under Getting Started                                                                                                                                                                                                                                                                                                                                                                                        |
| 3 Aug  | Pricing                  | [Pricing](https://docs.developer.singpass.gov.sg/docs/pricing/pricing) page updated — Singpass Login is now priced by authentication form factor (QR/Passkey, Username/Password, SMS OTP); SFV pricing section added; Partner Support FAQ link added; references to the in-portal FAQ tab removed                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 3 Aug  | Integration Guide        | [`authentication_context_message`](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request#singpass-specific-parameters) allowable character set widened — now accepts all printable ASCII except `<`, `>`, `\`, and the backtick; max 100 characters unchanged                                                                                                                                                                                                                                                                                                                                                                                               |
| 3 Aug  | Pricing                  | [Pricing](https://docs.developer.singpass.gov.sg/docs/pricing/pricing) guide updated — all four tabs on the Pricing Plan page now listed, including the **Pricing Examples** tab                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3 Aug  | SDP — App Management     | [Managing Drafts](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/managing-drafts) guide updated — "Saving..." indicator and "Draft saved" label for auto-save described                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

***

## July 2026

| Date    | Area                     | Change                                                                                                                                                                                                                                                                                                                                                                |
| ------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 28 Jul  | SDP — App Management     | App name must be **100 characters or fewer** — documented in [App name & purpose](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/app-name) and [Create Staging App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/create-staging-app)                       |
| 28 Jul  | SDP — App Management     | **Client External ID** is read-only and cannot be changed after app creation — callout added to [Edit Staging App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-staging-app) and [Edit Production App](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/edit-production-app) |
| 28 Jul  | Integration Guide        | Code samples use the **staging** endpoint (`stg-id.singpass.gov.sg`) — callout added to [Authorization Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) and [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange)       |
| 28 Jul  | Technical Concepts       | Do not pin Singpass TLS leaf certificates — warning added to [OpenID Provider Configuration](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/openid-connect-discovery)                                                                                                                                                        |
| 28 Jul  | Migration Guides         | **Duplicate app** recommended as preferred migration path — updated in [Myinfo v3 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v3-apps) and [Myinfo v4 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v4-apps)                        |
| 21 Jul  | Migration Guides         | New guide: [Myinfo Business Person API → Myinfo v5](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/migrating-mib-v1-v2-person-v3-to-myinfo-v5)                                                                                                                                                                                 |
| 15 Jul  | SDP — App Management     | New page: [Managing Drafts](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/app-management/managing-drafts) — auto-save, 30-day expiry, 7-day email reminder                                                                                                                                                                                |
| 14 Jul  | Technical Specifications | Legacy Singpass Authentication API documentation retired — superseded by [FAPI 2.0 Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide)                                                                                                                                                                         |
| 2–6 Jul | Getting Started          | [App logo](https://docs.developer.singpass.gov.sg/docs/getting-started/app-logo) requirements page — minor copy updates                                                                                                                                                                                                                                               |

***

## June 2026

| Date   | Area              | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 30 Jun | Integration Guide | `iss` parameter documented in [auth redirect](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/2.-handling-the-redirect) responses                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 30 Jun | Data Catalog      | Corrections to [Family data catalog](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog/family)                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 24 Jun | Integration Guide | Userinfo endpoint URL corrected to `/fapi/userinfo` — see [The Userinfo Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo)                                                                                                                                                                                                                                                                                                                                                                                             |
| 23 Jun | Getting Started   | [Demo app and sample code](https://docs.developer.singpass.gov.sg/docs/getting-started/demo-app-and-sample-codes) links updated to FAPI 2.0 examples                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 16 Jun | Migration Guides  | [Login/Myinfo v5 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/login-myinfo-v5-apps) expanded with guidance on replacing custom scheme URLs with Universal Links / App Links                                                                                                                                                                                                                                                                                                                                                           |
| 15 Jun | Getting Started   | New page: [App Logo](https://docs.developer.singpass.gov.sg/docs/getting-started/app-logo) requirements — PNG, 256–512px, max 200KB, no padding. Effective **August 2026**                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 11 Jun | Products          | [Scheduled downtimes](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo/scheduled-downtimes) updated — CPFB 4th Sunday window (0000–0500) now in effect                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 10 Jun | Getting Started   | [User Journey](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey) — 4th template added for Login with Mandatory Face Verification (high-risk, submit via partner support portal)                                                                                                                                                                                                                                                                                                                                                                                         |
| 8 Jun  | Products          | [Login FAQ](https://docs.developer.singpass.gov.sg/docs/products/singpass-login/faq) and [Myinfo FAQ](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo/faq) refreshed — FAPI 2.0 deadlines, pricing, turnaround times                                                                                                                                                                                                                                                                                                                                                       |
| 8 Jun  | SDP — App Config  | New pages: [Allowed Scopes](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/allowed-scopes), [App Description](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/app-description), [Site URL](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/site-url), [Support Emails](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/understanding-the-app-config-fields/support-emails) |

{% hint style="warning" %}
**Breaking change (24 Jun):** The userinfo endpoint URL has changed to `/fapi/userinfo`. Update your integration if you are using a hardcoded path.
{% endhint %}

***

## May 2026

| Date   | Area               | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 28 May | Technical Concepts | [DPoP](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop): `exp` claim clarified as optional (RFC 9449); [JWKS](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/json-web-key-sets-jwks): key rotation guidance updated; [PKCE](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/proof-key-for-code-exchange-pkce): expanded |
| 11 May | Data Catalog       | New page: [Start Here](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog/start-here) — user segments, data nuances, handling behaviour                                                                                                                                                                                                                                                                                                                            |
| 6 May  | Data Catalog       | Myinfo v5 OpenAPI YAML download link added to all [catalog pages](https://docs.developer.singpass.gov.sg/docs/data-catalog-myinfo/catalog)                                                                                                                                                                                                                                                                                                                                              |
| 6 May  | Integration Guide  | [Userinfo request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo) fully rewritten for FAPI 2.0 — DPoP header, `ath` claim, `person_info` structure                                                                                                                                                                                                                                                                  |

***

## April 2026

| Date   | Area               | Change                                                                                                                                                                                                                                                                                                                                                 |
| ------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 27 Apr | Getting Started    | [User Journey](https://docs.developer.singpass.gov.sg/docs/getting-started/user-journey) — Myinfo Business template links to CorpPass docs                                                                                                                                                                                                             |
| 24 Apr | Products           | [Scheduled downtimes](https://docs.developer.singpass.gov.sg/docs/products/singpass-myinfo/scheduled-downtimes) — CPFB 4th Sunday window (0000–0500) documented                                                                                                                                                                                        |
| 21 Apr | Technical Concepts | [Client Assertion](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) expanded with additional JWT payload requirements; [DPoP](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) minor corrections |
| 20 Apr | Integration Guide  | Error code corrected to `upstream_dependency_error` in [Token Exchange](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/3.-token-exchange) and [Userinfo Request](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/5.-requesting-for-userinfo)                            |
| 18 Mar | SDP — Billing      | New page: How to view entity transactions                                                                                                                                                                                                                                                                                                              |

***

## March 2026

| Date   | Area               | Change                                                                                                                                                                                                                        |
| ------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 26 Mar | Integration Guide  | [`authentication_context_message`](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) character limit updated                                                   |
| 24 Mar | Migration Guides   | [Myinfo v4 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/myinfo-v4-apps) — client assertion incorrectly required `code` parameter; fixed                             |
| 18 Mar | Technical Concepts | [Client Assertion](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/generation-of-client-assertion) — `code` claim removed from sample JWT payload                                     |
| 11 Mar | Getting Started    | [Demo app and sample code](https://docs.developer.singpass.gov.sg/docs/getting-started/demo-app-and-sample-codes) links updated to FAPI 2.0-compliant examples                                                                |
| 5 Mar  | Migration Guides   | [Login/Myinfo v5 migration guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides/login-myinfo-v5-apps) — `user.identity` scope clarified as available to all app types, not Login only |

***

## February 2026

| Date     | Area                     | Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 26 Feb   | Integration Guide        | [`authentication_context_message`](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) allowable character set documented                                                                                                                                                                                                                                                                                   |
| 23 Feb   | Technical Concepts       | [DPoP guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts/demonstrating-proof-of-possession-dpop) substantially expanded — full JWT structure, per-request requirements, key lifecycle rules                                                                                                                                                                                                                                  |
| 13 Feb   | Integration Guide        | [`authentication_context_type`](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide/1.-authorization-request) full values table added — CPF, Banking, Other FIs, Telcos, generic                                                                                                                                                                                                                                                      |
| 10 Feb   | Technical Specifications | **FAPI 2.0 documentation published** — [Integration Guide](https://docs.developer.singpass.gov.sg/docs/technical-specifications/integration-guide), [Technical Concepts](https://docs.developer.singpass.gov.sg/docs/technical-specifications/technical-concepts), [Migration Guides](https://docs.developer.singpass.gov.sg/docs/technical-specifications/migration-guides). All new apps require FAPI 2.0. Existing integrations must migrate by **31 December 2026**. |
| 6–24 Feb | Testing                  | [Myinfo test personas](https://docs.developer.singpass.gov.sg/docs/testing/myinfo-test-personas) updated across multiple rounds — refreshed persona data and CSV download                                                                                                                                                                                                                                                                                                |


# Contact

If you have any other queries, please go to [partnersupport.singpass.gov.sg](http://partnersupport.singpass.gov.sg/) and submit a request.


# Overview of Sign

{% hint style="warning" %}
**Heads up!** — Sign with Singpass documentation has moved. From **16 September 2026**, <https://docs.sign.singpass.gov.sg/> will redirect to Singpass Developer Docs. Please update any saved bookmarks.
{% endhint %}

## Overview of Sign

#### **Sign** is a digital signing solution built on the Singpass ecosystem that allows users to sign documents such as contracts and other agreements remotely, via their Singpass App.

{% hint style="success" %}
Signatures made using Sign with Singpass are regarded as **Secure Electronic Signatures (SES)** under the Electronic Transactions Act 2010 (ETA). [Find out more about why SES is important](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/start-here/how-do-our-digital-signatures-work#digital-signatures-under-singapore-law-oes-vs-ses)
{% endhint %}

### <mark style="color:red;">**Benefits of using Sign**</mark>

#### Enhanced Protection

Singpass digital signatures guarantee that your signed documents cannot be forged or secretly changed. Unlike handwritten signatures that can be copied, each digital signature is uniquely tied to you through your Singpass digital identity, making it impossible for anyone else to replicate.

This means you can benefit from **extra protection** against common scams, such as:

* **Fake contract changes:** If someone tries to alter your contract after you sign it, the changes will be automatically detected and flagged
* **Forged signatures:** No one can pretend to be you on important transactions like property agreements or insurance forms

In addition, every document you sign carries its own proof of authenticity. This means that you can ascertain the authenticity of a signature years later even if the signing company no longer exists. [Find out more about digital signatures](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/start-here/how-do-our-digital-signatures-work#what-is-a-digital-signature)

{% hint style="danger" %}
**To protect yourself...**

You shouldn't rely on the appearance of a Singpass digital signature alone to judge a document's authenticity.

You can verify a document easily using any PDF reader to confirm who signed it and whether anything has been changed since signing. [Learn how to verify signatures](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures)
{% endhint %}

#### Legal Assurance of Secure Electronic Signatures (SES)

Digital signatures created through Sign are regarded as Secure Electronic Signatures (SES) under the Electronic Transactions Act (2010) (ETA). This means that they are given certain presumptions in the course of any legal proceedings.

> ***Extract from Section 19 of the Electronic Transactions Act (2010)***\
> \
> (2) In any proceedings involving a secure electronic signature, it is presumed, unless evidence to the contrary is adduced, that —
>
> \
> (a) the secure electronic signature is the signature of the person to whom it correlates; and\
> (b) the secure electronic signature was affixed by that person with the intention of signing or approving the electronic record.\
> \
> Source: [Singapore Statutes Online](https://sso.agc.gov.sg/Act/ETA2010?ProvIds=P13-#pr19-)

{% hint style="warning" %}
Users and relying parties should note the exclusions under the [First Schedule to the ETA.](https://sso.agc.gov.sg/Act/ETA2010?ProvIds=Sc1-#Sc1-)
{% endhint %}

#### Convenience of Remote Digital Signing

Parties can sign documents instantly and securely using their Singpass App, ensuring faster, more seamless transactions that are not limited to the constraints of space and time.

#### Cost-effective & Environmentally-friendly

Using Sign allows organisations to do away with wet-ink (physical) signatures, saving cost and time both for the organisation and the signatory. For example, organisations can significantly reduce the need for printing, scanning, and storing and shipping of physical documents.

Sign is currently offered free of charge, both for organisations to integrate with, and for users.

{% embed url="<https://www.youtube.com/watch?v=IostdtfKMhU>" %}

***

#### Find out more

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td>For Users</td><td><strong>How to Sign</strong></td><td></td><td></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/document-signing-v1/sign-docs">User Journey (V1)</a></td></tr><tr><td>Basics</td><td><strong>How do Digital Signatures work?</strong></td><td></td><td></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/start-here/how-do-our-digital-signatures-work">How do our Digital Signatures work?</a></td></tr><tr><td>For Relying Parties</td><td><strong>How to Get Started</strong></td><td></td><td></td><td><a href="https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/how-our-api-works">How our API works</a></td></tr></tbody></table>


# How do our Digital Signatures work?

## <mark style="color:red;">What is a Digital Signature?</mark>

A **digital signature** is a type of electronic signature created using asymmetric or public key cryptography. Unlike traditional signatures, digital signatures are not directly visible on electronic records (e.g. a PDF of the contract). Instead, a cryptographic hash is embedded within the record itself. However, a visual representation is often included when the record is printed.

Digital signatures **ensure the integrity** of an electronic record. If the record is **altered or tampered with** in any way, the digital signature becomes invalid because the cryptographic integrity is compromised. Conversely, if the record remains unchanged, the signature remains valid.

The integrity of digital signatures can easily be verified via standard PDF document readers, which will check that the document has not been modified since it was signed. *Find out more about verifying digital signatures made with Sign* [*here*](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures)*.*

<table><thead><tr><th width="444.82421875">Digital signatures</th><th>Other types of electronic signatures</th></tr></thead><tbody><tr><td><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-e4e1e85c44bbe258400b050d5888a203071b71ca%2Fimage%20(49).png?alt=media" alt="Example of a visual representation of a digital signature on a PDF document, and the checks performed by Adobe Acrobat that the document has not been modified" data-size="original"></td><td><ul><li>Attaching a digital image of a handwritten signature to an electronic document.</li><li>Using a finger or stylus to draw a signature on a touchscreen.</li><li>Typing a name at the end of an electronic document.</li><li>Selecting an "I agree" checkbox.</li></ul></td></tr></tbody></table>

## <mark style="color:red;">Digital Signatures under Singapore law: OES vs SES</mark>

In Singapore, digital signatures may either be regarded as **ordinary electronic signatures (OES)** or **secure electronic signatures (SES).**

{% hint style="success" %}
**Why is it important to that your digital signature is considered SES?**

If you receive a document with a digital signature that qualifies as a Secure Electronic Signature (SES), it can **benefit from legal presumptions** under Singapore law.

This **shifts the burden of proof** to the counterparty to show that: (i) the signature is not theirs; (ii) they did not intend to sign the document; or (iii) the document was altered after signing.

In short, the counterparty (who allegedly signed) will be presumed to have signed the document unless they can prove otherwise.
{% endhint %}

One of the ways for a digital signature to be considered an SES is if it fulfils the following criteria to be:

* unique to the person using it;
* capable of identifying such person;
* created in a manner or using a means under the sole control of the person using it; and
* linked to the electronic record to which it relates in a manner such that if the record was changed the electronic signature would be invalidated (i.e. tamper-proof).

Alternatively, a digital signature can be considered SES if the certificate used to create it was issued by a public agency approved by the Minister to act as a Certification Authority.

✅ **Signatures created through Sign are regarded as Secure Electronic Signatures** under the [Electronics Transaction Act 2010 (ETA)](https://sso.agc.gov.sg/Act/ETA2010?ProvIds=P13) as they meet both of the methods listed above.

❌ **All other electronic or digital signatures that&#x20;*****do not*****&#x20;meet the criteria to be an SES prescribed under the ETA are considered OES.** This is because the process of signing is less secure, which may make establishing the authenticity of the signature difficult in the future. For example, an impersonator might mimic the declarant by placing an image of their signature that they obtained from some other source, or by typing their name on a statutory declaration. Detecting such impersonation can be difficult for the person requesting the signature, especially if it is their first time meeting the person, or if the signing is done remotely (e.g. via email, online platforms, etc).

{% hint style="info" %}

### **How are digital signatures different from physical (wet-ink) signatures?**

**Digital signatures are resistant to tampering or forgery**. While a wet ink signature can be scanned and tampered with or forged, digital signatures cannot be easily modified or forged once created, as they are cryptographically linked to the signed document through a hash. This provides additional safeguards beyond a visual representation, unlike traditional wet-ink signatures.

The authenticity of Sign with Singpass signatures can be verified via standard PDF document readers, which will check that the document has not been modified since it was signed. *Find out more about verifying digital signatures* [*here*](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures)*.*
{% endhint %}

## <mark style="color:red;">How does Sign create SES-eligible signatures?</mark>

Sign with Singpass signatures use **Public-Key Infrastructure (PKI).**

Public Key Infrastructure (PKI) involves the use of a **pair of cryptographic keys**: a **private key** (kept secret by the signer, on the Singpass app) and a **public key** (embedded in the Singpass signing certificate). The private key is used to create a digital signature, which is a unique encrypted code tied to the document. The public key can be used by the recipient of the document to verify the authenticity of the digital signature. GovTech issues the Singpass signing certificate, which ties the identity of the signer to the public key.

**This process ensures that only the holder of the private key is able to sign the document.**


# Frequently Asked Questions

## General

<details>

<summary>How can I use Sign with Singpass?</summary>

Organisations (such as government agencies, financial institutions, and private businesses) who are integrated with our service can request for you to sign documents using your Singpass.

If the organization/application you are transacting with offers Sign with Singpass, you should see a button like this:

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-8298f96e7ea9111c1baff651efe62e4f83db7412%2Fimage%20(54).png?alt=media" alt="Sign with Singpass buttons"><figcaption><p>Sign with Singpass buttons</p></figcaption></figure>

By clicking on it, you will be guided through the process of signing with your Singpass. See our guide on [How to Sign](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/how-to-sign).

</details>

<details>

<summary>Who can use Sign?</summary>

Anyone with the Singpass App can sign documents using Sign.

Both government agencies and private businesses can integrate with Sign. To join us as a digital signing partner, please visit the [onboarding](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/how-our-api-works) section.

</details>

<details>

<summary>Can I sign without a Singpass App?</summary>

No, you are required to have the Singpass App in order to sign documents.

</details>

<details>

<summary>What is the difference between Secure Electronic Signatures and Ordinary Electronic Signatures?</summary>

Ordinary Electronic Signatures (OES) is a broad category that refers to electronic signatures that are not SES.

Under Section 19 of the Electronic Transactions Act (2010), **secure electronic signatures are accorded the following presumptions:**

(a) the secure electronic signature is the signature of the person to whom it correlates; and

(b) the secure electronic signature was affixed by that person with the intention of signing or approving the electronic record.

[Source](https://sso.agc.gov.sg/Act/ETA2010?ProvIds=P13-#pr18-)

</details>

## Authenticity

<details>

<summary>How to verify signatures?</summary>

Refer to this [section](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures) on verifying signatures.

</details>

<details>

<summary>When I opened the document on Adobe PDF reader, it says that the signature is corrupted.</summary>

Refer to this [section](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures) on verifying signatures. When downloading the document onto your device, please ensure that you do not have a firewall that is modifying the file in transit (content disarm and reconstruction), as that will affect the integrity of the signature.

</details>

<details>

<summary>"Certificate validity is unknown"?</summary>

If you see "Certificate validity is unknown", this is because you do not have the Singpass root signing certificate on your device. Please refer to this [guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures/loading-singpass-root-signing-certificate) to install the Singpass root signing certificate.

</details>

<details>

<summary>If I delete my Singpass account, will my signature still be valid?</summary>

Yes, the signature will continue to be valid.

</details>

<details>

<summary>If the signer migrates, will the signature still be valid?</summary>

Yes. The document can be traced back to the signer.

</details>

<details>

<summary>How can I know if my signature is secure and protected?</summary>

Digital signatures rely on **public-key cryptography**, a method that uses a pair of keys:

* **Private Key**: A secret key known only to the signer. It is used to create the signature.
* **Public Key**: A key that is made publicly available through the Singpass signing certificate. It is used to verify the signature.

**Private keys are stored securely on the Singpass mobile app and can only be accessed by the user.**

Furthermore, it is **computationally infeasible to replicate the cryptographic process** (hashing and encryption) used to generate the signature.

Lastly, the signer's public key is validated by Singpass. Singpass verifies the identity of the signer and that the public key is associated with the correct person.

</details>

<details>

<summary>Can a document's details be altered after it is signed?</summary>

If there are unauthorised modifications to the document after it is signed, the digital signature will be invalid.

As digital signatures are **cryptographically linked to the signed document** through a **hash,** the hash value will change if there are unauthorised modifications to the document after signing, and the signature will be deemed to be invalid.

</details>

## Others

<details>

<summary>Is there any cost to using Sign with Singpass?</summary>

Sign with Singpass is currently free of charge, both for organisations integrating with us, as well as for signers.

</details>

<details>

<summary><strong>Can I sign from overseas?</strong></summary>

As long as you have access to your Singpass App, you will be able to Sign with Singpass.

</details>

{% hint style="warning" %}
If you have a question and are unable to find an answer in this FAQ, please submit your question on our [Singpass Q\&A site](https://ask.gov.sg/singpass) to seek further assistance.
{% endhint %}


# How to sign

You may find related FAQs at the [bottom of this page](#you-may-have-some-questions).

{% hint style="warning" %}
The following guide is for applications which have implemented the newest version of Sign with Singpass. If you are **not** redirected to a new page when you click the Sign with Singpass button, please [refer to this guide on how to sign](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/document-signing-v1/sign-docs) instead.
{% endhint %}

## Learn through our interactive demo!

{% embed url="<https://app.arcade.software/share/M5dRwckzpXJlf8yH9DoE>" %}

## Or, here's a step-by-step guide

#### 1. If you've clicked the "Sign with Singpass" button, you will be directed to our Singpass portal to complete the signing of your document.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-6efde817523494b96be5f3dc61911683872ec418%2FFrame%201%20\(2\).png?alt=media)

#### 2. Authenticate your identity with Singpass before you can access the document.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-da03b87de80782754ab22a16ddb8f3d6d2b8681e%2FFrame%202.png?alt=media\&token=f2ed3f59-e400-4fc3-a536-9b76f2e83065)

#### 3. Scan/Tap the QR code to enter the Sign portal using your Singpass App .

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c0f3a13aa73bde9a5025aef4383ed6cb8c9aec63%2FFrame%203%20\(3\).png?alt=media)

#### 4. Approve the log in request on your Singpass App.

![](https://image.mux.com/ScS6tro518ZEOnRgBZRCNzzc11J018EwANJafdJzvePM/animated.gif?start=0\&end=5.553333\&width=640\&fps=30)

#### 5. Upon successful authentication, you can begin reviewing the document.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-8f6eb8ddfdc12786d7cf0db7fc505f9f1e4000fa%2FFrame%204%20\(1\).png?alt=media)

#### 6. Use the navigation panel to locate the fields in the document that require your signature.

This panel is on the right of your desktop screen. For mobile users, it will be at the bottom.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-36a3db62109a17cd292f9a514b58d2cbbec5919b%2FFrame%205%20\(1\).png?alt=media)

#### 7. Click on each field in the document once to 'review' them.

For mobile, you can also tap the 'Mark as reviewed' button to review each field.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-ad1f3ea65b11b3035f204f49b017ee4511aaab18%2FFrame%206.png?alt=media\&token=bac981a6-0c8f-4aaf-800c-0b8b3d7ce289)

#### 8. Select and review the remaining signature field(s) to complete the reviewing step.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-b80fff81c22e7acbcb248b87e791234d06c52cb6%2FFrame%207.png?alt=media\&token=590eb054-67bd-4aa5-a5fa-cd4f5324c094)

#### 9. You will be able to perform the signing once all fields are reviewed (Sign button will be activated).

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-31e3ffb5d905cf04a6968a8406b439ca95d321cd%2FFrame%208.png?alt=media\&token=4c33c981-0fde-44b7-991b-9d5c90220b35)

#### 10. Selecting the Sign button will bring up a Sign QR code. Scan/Tap the QR code to enter the Sign portal using your Singpass App .

![](https://image.mux.com/sxQ4Weh5QO52fv15FsE9v1OEX9sqd8kIa4Q5p8nKDcQ/animated.gif?start=0\&end=3.533333\&width=640\&fps=30)

#### 11. Approve the sign request on your Singpass App.

![](https://image.mux.com/UJdgGDYCYEahtauHU4JTdtpwiDRbuYAaOveW7eKtTzA/animated.gif?start=0\&end=4.8\&width=640\&fps=30)

#### 12. Document is successfully signed! At this point, you may exit the Sign portal.

At this point, you can also click 'View Signed Document' if you want to view the signed document before leaving the Sign portal.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-cc2438356ab3bd32ec71b3041a2cada72a2bb2a9%2FFrame%209.png?alt=media\&token=c3ec038d-f8f1-4fea-888d-d8cb179189e4)

![](https://image.mux.com/uwfDWl013eitl2uAY84VrhNwQ8RggeGVRLwROzrNZKsA/animated.gif?start=47.177\&end=49.799\&width=640\&fps=30)

#### 13. Return to the document sender's portal as the final step.

![](https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1349b634a9ea637c45e08e99c776060f5a371301%2FFrame%2010.png?alt=media\&token=45733a26-6d08-4550-aef8-55d50e766b09)

## You may have some questions...

<details>

<summary>Why do I have to scan QR code twice? What’s the difference?</summary>

The first QR code you scan (in Step 3) is to verify your identity with Singpass and log in to the Sign portal. This protects your data privacy by ensuring that the document and any sensitive contents can only be seen by the intended parties.

The second QR code you scan (in Step 10; which comes with a 4-digit reference code) is for you to perform the signing of document.

</details>

<details>

<summary>What is the reference code for during the signing?</summary>

The purpose of the reference code is to allow users to verify that they are signing the correct document, when the code on their Singpass App matches that which is shown in the Sign Portal.

</details>

<details>

<summary>What happens if I reject the signing on my Singpass App?</summary>

If you **reject** the signing (Click 'Reject' in Step 8), the Sign Portal will continue to stay in 'pending sign' mode. You have to (i) refresh the Portal to get a new QR code or (ii) return back to the organization's webpage to restart the process.

</details>

<details>

<summary>How do I retrieve the signed document?</summary>

You may retrieve the signed document from the organisation's (document sender) platform.

</details>

<details>

<summary>Why can’t I log in?</summary>

You might not be able to log in if i) you are not the intended signer for this document, or ii) someone else has logged into the portal to access the document before you.

If you believe this is an error, please contact the organization/document sender to request for a new signing session.

</details>

<details>

<summary>Why can’t I sign?</summary>

You might not be able to sign if the document has already been signed, or if you are not the intended signer for this document.

If you believe this is an error, please contact the organization/document sender for assistance.

</details>


# Verifying Sign with Singpass Signatures

Sign with Singpass signatures can be verified using PDF reader software, such as **Adobe Acrobat Reader** application ([download here](https://get.adobe.com/uk/reader/)).

{% hint style="warning" %}
Please ensure that the document has not been modified since your signature has been created, as this will invalidate the signature.
{% endhint %}

## Verifying signatures with Adobe Acrobat Reader <a href="#verifying-signatures" id="verifying-signatures"></a>

Please follow the steps below to verify a Sign with Singpass signature.

{% stepper %}
{% step %}

#### **Open up signed document on Adobe Acrobat Reader**

{% endstep %}

{% step %}

#### **Check if green tick with "Signed and all signatures are valid"**

{% hint style="warning" %}
If you see "Certificate validity is unknown", this is because you do not have the Singpass root signing certificate on your device. Please refer to this [guide](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures/loading-singpass-root-signing-certificate) to install the Singpass root signing certificate.
{% endhint %}

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-eb77a79f5767e0d52075bc77c49eb1fd9178b093%2FFrame%20427319133.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Go to signature panel

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-0144344c7b822af1fa29b79091f0ddbe21e9f874%2FFrame%20427319137.png?alt=media" alt=""><figcaption></figcaption></figure>

In signature panel, each signature should show:

* Document has not been modified
* Signer's identity is valid
* The signature includes an embedded timestamp
* Signature is long term validation (LTV) enabled

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-e563339bb8311c528a3254ff1859e44d9273043c%2FFrame%20427319134.png?alt=media" alt=""><figcaption></figcaption></figure>

Document owner should "click to view this version" to visually inspect that the contents of the document version is signed correctly.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-67cc2526139c69379673f405a033c0f03c2eed2d%2FFrame%20427319140.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

#### Right-click on each signature and select "Show Signature Properties".

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-f27bc2c5985d776e8cbc8f543c4e656b8773ac4f%2FFrame%20427319135.png?alt=media" alt=""><figcaption></figcaption></figure>

The following modal should appear, and it will tell you:

* The name of the signer (e.g. "MICHAEL ONG")
* The time the document was signed

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-9daeb1079077facba80091cc4a20d71db92b2c6f%2FShow%20Signer's%20Certificate.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

If you select "Show Signer's Certificate" at the bottom, you will see another modal with details about the certificate. Ensure that the the following details are correct:

* Singapore National Root CA - B1
* Singapore NDI Intermediate CA 1 - B2
* Signer's full name (as per NRIC)

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-3a18d9655fb5425d675a38b048e987ab737e40d1%2FFrame%20427319138.png?alt=media" alt=""><figcaption></figcaption></figure>

Click the full name and then "details".

Check under "Subject" that signer's name and last 4 characters of NRIC is correct.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-15d1e602c1b505ee1c58341ccc93c1e95e70975b%2FFrame%20427319139.png?alt=media" alt=""><figcaption></figcaption></figure>

\ <br>
{% endstep %}
{% endstepper %}


# Loading Singpass Root Signing Certificate

In order to verify if a Sign with Singpass signature is valid, see [here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-users/verifying-sign-with-singpass-signatures).

Before that, the Singpass root signing certificate must be installed on your device and configured for your Adobe Acrobat Reader:

* You can download the **Adobe Acrobat Reader** application [here](https://get.adobe.com/uk/reader/)
* If you do not have the Singpass root signing certificate on your device, please follow the steps below.

{% hint style="success" %}
For **government agencies**, this should already be automatically available on your GSIB. If it is not, please raise a ticket to AFM to push “GSSP\_Acrobat Reader Digital Signature Fix\_2.0” to the agency's GSIBs.

For the rest of the agencies, you may follow the steps below or approach your IT department to push the certificates so that it applies across your agency.
{% endhint %}

### Automatically load the certificate

{% stepper %}
{% step %}
**Go to** [**GovTech CA Repository**](https://repository.nca.gov.sg/) **and download "Singapore National Root CA - B1 FDF"**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-86e7a85804661a30f7f30611df07a277ef2d0588%2Fimage%20(47).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Also download the "\[Legacy] Singapore National Root CA - G1 FDF" file**

{% hint style="info" %}
The Legacy cert is needed in case you are validating signatures that were performed prior to March 2025.
{% endhint %}

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c399610b3db966446ce481fb5d57561a3c41843d%2Fimage%20(58).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Open both of the files downloaded.**

This should automatically load the certificates into your Adobe Acrobat reader.
{% endstep %}

{% step %}
**All done!**

Open up a document generated by Sign and you should be able to see the the green tick and the words "Signed and all signatures are valid".

{% hint style="warning" %}
If you are still facing issues, please attempt to load the certificate with the instructions in the next section: [Manually load the certificate](#manually-load-the-certificate)
{% endhint %}

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-eb77a79f5767e0d52075bc77c49eb1fd9178b093%2FFrame%20427319133.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}
{% endstepper %}

### Manually load the certificate

{% hint style="warning" %}
***Still can't seem to verify after completing the steps?***

**From 13 Feb 2025, all new Singpass signing certificates are issued by the GovTech CA.** Prior to this, Singpass App users would have been issued signing certificates by Assurity Trusted Solution Pte Ltd (ATS), GovTech's wholly-owned subsidiary and an Accredited CA under the Electronic Transactions Act (2010).

If you are unable to verify the document signature, the document may have been signed with the legacy ATS certificates.\
\
**Please follow the same steps above and load the ATS root cert by downloading it** [**here**](https://product.assurity.sg/nca/) **under the section "NCA Root Cert"** (you may download either "SNRCA-G1.cer" or "SNRCA-G1.crl").
{% endhint %}

{% stepper %}
{% step %}
**Go to** [**GovTech CA Repository**](https://repository.nca.gov.sg/) **and download Singapore National Root CA - B1 Certificate.**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c1cdaf0ce61f24100087422ce0254489f208fe7f%2FFrame%20427319122%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### Certificates Staging Environment

For staging environment, download the certificate below.

CER Format

{% file src="/files/NqWLlBRZMydzvfgNi9QU" %}
Singapore National Root CA - B1 CER format
{% endfile %}

CRT Format

{% file src="/files/C677xaxyPsycnGlickL8" %}
Singapore National Root CA - B1 CRT format
{% endfile %}
{% endstep %}

{% step %}
**In your folder that you have chosen, you should find the file RCA-B1.crt**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-33cad62964c0df6da2f3762bbeebb524933d1bce%2FFrame%20427319123%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Open Adobe PDF reader.**

If you do not have this, you may download and install [here](https://get.adobe.com/uk/reader/).
{% endstep %}

{% step %}
**Click "Acrobat Reader" on the top left.**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-0143c2043e57c8bc5dd3166c903319468918c958%2FFrame%20427319124%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Navigate to "Preferences"**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-16b84753c328a2e5fe4c80d9aebc6acf7f01d663%2FFrame%20427319125.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Under Categories, find and click "Signatures".**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-e9c5e77298453800da4c3ce3686b6b7f97f914fc%2FFrame%20427319126%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Click "more" under Identities and Trusted Certificates**.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-10b6bbef58b27234b1776049c1594ed1c05af984%2FFrame%20427319127%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Click on "Trusted Certificates"**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-8917bad555831bd73e372caf1dfba39cfac12093%2FFrame%20427319128%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Click Import**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-5cef86f63dae3524d4895778cacb48cfcd1397c5%2FFrame%20427319129%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Under Contacts, click "Browse" and choose the certificate you have downloaded earlier. Click on "Singapore National Root CA - B1" that is loaded.**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-629662a0cf7a16a756439faf384af0d7adebc45f%2FFrame%204273191210%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Under Certificates, click on Singapore National Root CA - B1 and then click Trust**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-4be7abbef8339245aff0923545a6b71ed122431f%2FFrame%204273191211%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Check "Use this certificate as a trusted root" with a tick and press OK**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-8333be45eb3cf9b38bd677d0502e9b2fd51fa100%2FFrame%204273191212%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Click on Import**

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-c58a7f95981b482c95aa8a332707e77ff86739ca%2FFrame%204273191313%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

You should now be able to see Singapore National Root CA - B1 under your Trusted Certificates.

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-4d15f82a491141a48d318c7f4159e331456e649f%2FFrame%204273191313b%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
**Enable certification revocation checking**

This can be found under Preferences > Signatures > Verification

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-81b85bac65470e6c6a91ca4b61e47c612c2bbe3e%2FFrame%204273191214%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-27e0dc636e10eefb04448f3caf782ee66d785f5d%2FFrame%204273191314b.png?alt=media" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}

### All done!

{% endstep %}
{% endstepper %}


# Use Cases

## <mark style="color:red;">Why Use Sign?</mark>

### :white\_check\_mark: **Greater trust & assurance**

Compared to other electronic signing options, signatures produced by Sign are considered as [Secure Electronic Signatures (SES)](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/start-here/how-do-our-digital-signatures-work#digital-signatures-under-singapore-law-oes-vs-ses).

### :white\_check\_mark: **Convenience for your users**

Enable remote signing with a seamless experience for your users, who can sign documents through their familiar Singpass mobile app - no new downloads required.

### :white\_check\_mark: **Faster time-to-market**

Easy and quick integration

* Our API is designed to minimise integration effort. Get started with our demo code, which is under 100 lines! [Check out our useful developer tools here](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3#developer-tools)
* Ship quickly - beta users have tested complete end-to-end signing flows within 2 weeks.

{% hint style="success" %}
For **government agencies**, Sign can also ensure your agency's compliance with IM8, with respect to Circular Minute No. 5/2021 on the Use of Electronic Signatures ([link to circular, accessible via intranet only](https://intranet.mof.gov.sg/portal/IM/Circulars/ICT/Circular-Minutes/2021/Use-of-Electronic-Signatures.aspx))
{% endhint %}

## <mark style="color:red;">Examples of current use cases for Sign include:</mark>

* Appointing your Lasting Power of Attorney (LPA), under the [Office of the Public Guardian Online (OPGO)](https://opg-eservice.msf.gov.sg/)
* Bank and insurance documents
* Contracts
* Declarations
* Legal documents, via [e-Litigation](https://www.elitigation.sg/) or MinLaw's [Legal Technology Platform (LTP)](https://ltpi.mlaw.gov.sg/)

{% hint style="warning" %}
**Under the First Schedule to the Electronics Transaction Act 2010 (ETA), the following use cases are excluded from the operation of Part II of the ETA. Sign with Singpass should not be used to create Secure Electronic Signatures in relation to these matters:**

1. The creation or execution of a will
2. The creation, performance or enforcement of an indenture, declaration of trust or power of attorney, with the exception of implied, constructive and resulting trusts and a lasting power of attorney defined under section 2(1) of the Mental Capacity Act 2008
3. Any contract for the sale or other disposition of immovable property, or any interest in such property
4. The conveyance of immovable property or the transfer of any interest in immovable property.

(Source: [Singapore Statutes Online](https://sso.agc.gov.sg/Act/ETA2010?ProvIds=Sc1-#Sc1-))

*The above is not intended to be legal advice. Please seek your own legal advice if necessary.*
{% endhint %}


# How our API works

## Integrate Sign into your applications using our APIs

{% hint style="info" %}
If your organization is not capable of integrating directly with Sign APIs, you can consider approaching our [Digital Signing Partners](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/digital-signing-partners).
{% endhint %}

#### To get started on integration:

* [Read the documentation](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/api-documentation/sign-v3)
* [Check the onboarding requirements](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/onboard)

This diagram illustrates at a high-level how your application and your users will interact with Sign:

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-1d1f78974932faee46dfeef6ab22bc27c7264ad6%2FSign%20API%20graphic%20V2%20(16_9).png?alt=media" alt=""><figcaption></figcaption></figure>

## Conduct Code

Before integrating Sign into your application, please ensure that you adhere to the following principles:

### <mark style="color:red;">What you see is what you sign</mark>

* You should always ensure that the user knows what they are signing before being directed to Sign.
* You should never use this system to misrepresent intended documents which your user plans to sign.

### <mark style="color:red;">PDPA & Applicable Regulations</mark>

* Protect, retain and transfer data retrieved according to the Personal Data Protection Act (PDPA), relevant industry regulations and applicable legislation.

### <mark style="color:red;">Lawful purposes</mark>

* Use Sign for lawful purposes only. Singpass reserves the right to terminate the integration if Sign is used for any unlawful purpose.

### <mark style="color:red;">Accessibility</mark>

* You should ensure that your user always has a fallback option if they are unable to use Singpass to sign (e.g. other forms of electronic signatures, or a physical option)


# Singpass Services Agreement

Relying Parties (RPs) who wish to use Sign with Singpass in their production environments will first have to accept the Singpass Services Agreement, which can be found on the [Singpass Developer Portal (SDP).](https://developer.singpass.gov.sg/)

After logging into SDP, follow these instructions to submit your [Consent to the Singpass Services Agreement](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/consent-to-singpass-service-agreement)

{% hint style="info" %}
**If you do not have an SDP account,** please follow these instructions to [obtain an SDP account](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/obtain-access-to-sdp)
{% endhint %}

## Obtaining the acknowledgement

If you have previously consented to the agreement, you can log into SDP to [view the Singpass Services Agreement](https://docs.developer.singpass.gov.sg/docs/singpass-developer-portal-sdp/user-guide/view-singpass-service-agreement).

**In order to submit a** [**request for production access**](https://docs.developer.singpass.gov.sg/docs/singpass-developer-docs/sign-with-singpass/for-relying-parties/onboard#request-for-production-access)**,** you will need to take a screenshot of this page (sample below).

{% hint style="warning" %}
Please ensure that the **entity name** reflected in the screenshot is the same as the **company name** entered in the onboarding form.
{% endhint %}

<figure><img src="https://3146998070-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYUqAI09tBnmTJ02qSo9L%2Fuploads%2Fgit-blob-0bf9b57364cdfe7ea4bce20320cedaa8f240e18f%2Fimage%20(1)%20(2).png?alt=media" alt=""><figcaption><p>Sample screenshot</p></figcaption></figure>




---

[Next Page](https://docs.developer.singpass.gov.sg/docs/llms-full.txt/1)

