"""Write a hand-authored, fully SYNTHETIC seed set of support tickets and Slack threads.

Each scenario is based on a real section of the official docs (error-code tables, FAQs,
migration guides, JWKS/DPoP requirements). All agencies, people and identifiers are
fictional. Dates and resolution times come from a fixed random seed so the Insights
charts are reproducible.

    python scripts/seed_synthetic.py            # writes data/synthetic/*.jsonl

To create more varied data with an LLM instead, use scripts/generate_synthetic.py.
"""
from __future__ import annotations

import json
import random
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core.config import SYNTHETIC_DIR  # noqa: E402

# (product, category, environment, flow_step, error_code, subject, description, resolution, tags, escalated)
SINGPASS_TICKETS = [
    ("Singpass Login", "Keys & JWKS", "Staging", "Token request", "invalid_client",
     "Token endpoint returns invalid_client after key rotation",
     "Partner rotated their signing key and now every token request fails with invalid_client. "
     "The new key was added to their hosted JWKS but the client assertion header still references the old kid.",
     "The client assertion was signed with the new private key but the JWT header `kid` still pointed to the "
     "retired key. Advised partner to set `kid` to the new key's ID, keep the old key published in the JWKS "
     "until all in-flight assertions expire, and never reuse a previously used `kid`.",
     ["jwks", "key-rotation", "client-assertion"], False),
    ("Singpass Login", "Keys & JWKS", "Staging", "JWKS / key setup", "invalid_client",
     "JWKS rejected: RSA keys not accepted",
     "Partner's JWKS contains RSA keys (kty=RSA). Registration in the developer portal keeps failing validation.",
     "Singpass requires EC keys only (`kty`=`EC`, `crv` P-256/P-384/P-521). Partner regenerated an EC P-256 "
     "signing key (`use`=`sig`) and an encryption key (`use`=`enc`, `alg`=`ECDH-ES+A256KW`).",
     ["jwks", "ec-keys"], False),
    ("Singpass Login", "Keys & JWKS", "Production", "JWKS / key setup", None,
     "Security review flagged private key exposed in JWKS",
     "During a security review the partner noticed their public JWKS endpoint returns the `d` parameter for one key.",
     "The `d` property is the private key and must never be in the JWKS. Advised immediate removal, generation "
     "of a fresh key pair with a new `kid`, and rotation. Treated as a security incident on partner side.",
     ["jwks", "security"], True),
    ("Singpass Login", "Authentication flow", "Staging", "Token request", "invalid_dpop_proof",
     "invalid_dpop_proof on token request",
     "Partner migrating to FAPI 2.0 gets invalid_dpop_proof from the token endpoint. They reuse the same DPoP proof "
     "JWT they generated for the PAR request.",
     "A DPoP proof is bound to the HTTP method and URL (`htm`, `htu`) and must carry a fresh `jti` and `iat`. "
     "Partner now generates a new DPoP proof per request, with `htu` set to the token endpoint, using the same "
     "DPoP key pair throughout the session.",
     ["dpop", "fapi2"], False),
    ("Singpass Login", "Authentication flow", "Staging", "Token request", "invalid_grant",
     "invalid_grant when exchanging authorization code",
     "Token exchange intermittently fails with invalid_grant. Partner's load balancer retries failed requests.",
     "Authorization codes are single-use and short-lived. The retry re-submitted an already-used code. Also "
     "confirmed `code_verifier` matched the PKCE `code_challenge` sent in PAR. Advised disabling automatic retries "
     "on the token call.",
     ["pkce", "authorization-code"], False),
    ("Singpass Login", "Authentication flow", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "PAR rejected: redirect_uri mismatch",
     "PAR call returns invalid_request. Partner sends `redirect_uri=https://app.example.gov.sg/callback/` but "
     "registered the URL without the trailing slash.",
     "`redirect_uri` must exactly match a redirect URL registered for the app in the Singpass Developer Portal. "
     "Partner updated the registered URL in staging.",
     ["redirect-uri", "par"], False),
    ("Singpass Login", "Migration", "Staging", "Authorization redirect / callback", None,
     "Mobile app redirect with custom scheme no longer works",
     "Partner's mobile app used `myapp://callback` as the redirect URL. After moving to the new FAPI 2.0 "
     "specification the portal will not accept it.",
     "Custom scheme URLs are no longer supported. Partner must use app-claimed https URLs — Universal Links (iOS) "
     "and App Links (Android) — for redirect and app-launch URLs.",
     ["mobile", "custom-scheme", "fapi2"], False),
    ("Singpass Login", "Authentication flow", "Production", "ID token decryption / validation", None,
     "Cannot decrypt ID token",
     "Partner gets a JWE back from the token endpoint and their library fails with 'no matching key'.",
     "The ID token is encrypted to the partner's `enc` key from their JWKS. Their JWKS had two `enc` keys and the "
     "library ignored the JWE header `kid`. Advised selecting the decryption key by `kid`, then verifying the "
     "inner JWS against Singpass's JWKS.",
     ["id-token", "jwe"], False),
    ("Singpass Login", "Authentication flow", "Staging", "Authorization redirect / callback", "access_denied",
     "Users returned with error=access_denied",
     "Partner sees redirects with `error=access_denied` and wants to know if this is a Singpass outage.",
     "Under the new API Singpass redirects back with an Authentication Error Response in more scenarios, e.g. when "
     "the user cancels. Partner should display a friendly error page and allow retry, not treat it as an outage.",
     ["error-handling", "redirect"], False),
    ("Singpass Login", "Authentication flow", "Staging", "ID token decryption / validation", None,
     "amr claim values changed after migration",
     "Partner's authorisation logic checks `amr` for specific values and now fails after migrating.",
     "The `amr` claim values changed with the new specifications (see Changelog > Changes in amr claim values). "
     "Partner updated their mapping and stopped relying on a fixed list.",
     ["amr", "id-token", "fapi2"], False),
    ("Singpass Myinfo (v5)", "Myinfo data", "Production", "Userinfo request", None,
     "CPF data missing early Sunday morning",
     "A partner reports users could not retrieve CPF contributions between 0000–0800hrs on the first Sunday of "
     "the month.",
     "This falls within CPFB's scheduled downtime (1st Sunday of the month, 0000–0800hrs). Advised partner to show "
     "a maintenance message and let users retry later or fill in manually.",
     ["myinfo", "downtime", "cpf"], False),
    ("Singpass Myinfo (v5)", "Myinfo data", "Production", "Userinfo request", None,
     "NOA data unavailable Wednesday 3am",
     "Users cannot fetch Notice of Assessment on Wednesday around 0300hrs.",
     "IRAS has scheduled downtime every Wednesday 0200–0600hrs. No data is returned during the window. Partner "
     "added downtime-aware messaging.",
     ["myinfo", "downtime", "iras"], False),
    ("Singpass Myinfo (v5)", "Myinfo data", "Staging", "Userinfo request", None,
     "Field returned with unavailable: true",
     "Partner's parser crashes because `hdbtype` comes back as `{\"unavailable\": true}` without a value.",
     "The UnavailableFlag indicates no record exists at the data source. Partner must handle attributes with "
     "`unavailable: true` and treat them as empty/not applicable.",
     ["myinfo", "parsing"], False),
    ("Singpass Myinfo (v5)", "Migration", "Staging", "Onboarding / Developer Portal", None,
     "How to migrate Myinfo v3 app to v5",
     "Agency with an existing Myinfo v3 integration asks what changes are needed to move to v5.",
     "Pointed to the Migration Guide for Myinfo (v3) apps: create a new app in the Singpass Developer Portal, "
     "switch to FAPI 2.0 (PAR, PKCE, DPoP, client assertion with EC keys), use the userinfo endpoint for person "
     "data, and update scope names.",
     ["migration", "myinfo-v3"], False),
    ("Myinfo v3/v4 (legacy)", "Migration", "Production", "Token request", "invalid_client",
     "Legacy v4 app failing after certificate expiry",
     "Partner on Myinfo v4 reports token calls failing after their signing certificate expired.",
     "Advised updating keys per legacy JWKS guidance as a stop-gap, and to plan migration to Myinfo v5 since the "
     "v3/v4 APIs are legacy.",
     ["legacy", "migration"], True),
    ("Developer Portal", "Configuration / Portal", "Production", "Production go-live", None,
     "Cannot create production app",
     "Partner's staging app is complete but the 'Create Production App' option is greyed out.",
     "Production apps require an accepted Singpass Service Agreement and completed app details (name, purpose, "
     "category, contacts). Partner's entity had not accepted the service agreement in the SDP.",
     ["portal", "go-live"], False),
    ("Developer Portal", "Configuration / Portal", "Staging", "Onboarding / Developer Portal", None,
     "Requested scope not available in portal",
     "Partner cannot find a Myinfo scope they need in the Allowed Scopes list.",
     "Scopes shown depend on the app's approved purpose. Partner must justify the data needed; additional scopes "
     "require review against Myinfo key principles (data minimisation).",
     ["scopes", "portal"], False),
    ("Singpass Login", "Network & TLS", "Production", "JWKS / key setup", "invalid_client",
     "Intermittent auth failures — slow JWKS endpoint",
     "About 5% of logins fail. Partner's JWKS URL is hosted behind a cold-starting serverless function.",
     "A hosted JWKS must be publicly reachable at all times and respond within 3 seconds; otherwise users fail to "
     "authenticate. Partner moved JWKS to static hosting with caching.",
     ["jwks", "latency"], True),
    ("Singpass Login", "Authentication flow", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "PAR fails: missing code_challenge",
     "Partner's older OIDC library does not send PKCE parameters.",
     "PKCE is enforced: `code_challenge` with `code_challenge_method=S256` must be in the PAR request and the "
     "`code_verifier` in the token request. Partner upgraded the library.",
     ["pkce", "par"], False),
    ("Singpass Face Verification", "Onboarding & Compliance", "Staging", "Onboarding / Developer Portal", None,
     "Eligibility for Singpass Face Verification",
     "Partner asks whether they can use SFV for in-person counter verification.",
     "Shared SFV integration guide and use-case criteria; partner to submit use case for review.",
     ["sfv", "onboarding"], False),
    ("Sign with Singpass", "Authentication flow", "Staging", "Not sure", None,
     "Sign webhook not received",
     "Partner initiated a sign request but never received the success-signing webhook.",
     "Webhook URL must be publicly reachable over https. Partner's firewall blocked inbound calls. Also advised "
     "calling Get Signing Result as fallback.",
     ["sign", "webhook"], False),
    ("Singpass Login", "Onboarding & Compliance", "Staging", "Onboarding / Developer Portal", None,
     "Button design approval",
     "Partner wants to use a custom-coloured Singpass login button.",
     "Must follow the Singpass Button Design Specification and brand guidelines; colour changes are not allowed.",
     ["branding"], False),
]

CORPPASS_TICKETS = [
    ("Corppass Login", "Authentication flow", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "PAR rejected for Myinfo Business app with authentication_context_type",
     "Partner reuses their Corppass Login PAR code for a Myinfo Business app and gets invalid_request.",
     "`authentication_context_type` and `authentication_context_message` apply only to Corppass Login apps. "
     "If provided for a Myinfo Business application the request is rejected. Partner removed the parameters for "
     "the Myinfo Business client.",
     ["par", "myinfo-business"], False),
    ("Corppass Login", "Authentication flow", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "authentication_context_type value rejected",
     "Partner sends `authentication_context_type=APP_LOGIN` and receives invalid_request.",
     "The value must be one of the types allow-listed for the client ID. Partner requested the right context "
     "type to be configured for their digital service.",
     ["par", "auth-context"], False),
    ("Corppass Login", "Authentication flow", "Staging", "Pushed Authorization Request (PAR)", "invalid_dpop_proof",
     "invalid_dpop_proof on PAR endpoint",
     "Partner's PAR call returns 401 invalid_dpop_proof. Their server clock is 4 minutes behind.",
     "DPoP proofs are rejected if expired or with invalid claims. The skewed `iat` made the proof look stale. "
     "Partner enabled NTP sync and generates a fresh proof per request.",
     ["dpop", "clock-skew"], False),
    ("Corppass Login", "Keys & JWKS", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "invalid_request — JWKS endpoint unreachable",
     "Every PAR request fails with invalid_request, though parameters look correct.",
     "One listed cause is that Corppass cannot reach the client's JWKS endpoint. Partner's JWKS was on an "
     "internal-only host. Moved it to a publicly accessible URL.",
     ["jwks", "par"], True),
    ("Corppass Login", "Keys & JWKS", "Production", "Token request", "invalid_client",
     "invalid_client after rotating keys",
     "Partner rotated keys in production; token requests now fail with invalid_client.",
     "The client's JWKS did not yet contain the new signing key when they began signing with it. Advised to "
     "publish new keys first, wait for caches to refresh, then switch signing, and remove old keys later.",
     ["key-rotation", "jwks"], False),
    ("Corppass Login", "Network & TLS", "Production", "Token request", None,
     "Outage after Corppass certificate rotation",
     "Partner's backend suddenly cannot connect to Corppass endpoints with TLS handshake errors.",
     "Partner pinned the Corppass TLS leaf certificate. Corppass rotates certificates periodically without notice. "
     "Advised removing the pin and trusting AWS root CAs.",
     ["tls", "certificate-pinning"], True),
    ("Corppass Login", "Network & TLS", "Production", "Not sure", None,
     "Request for Corppass IP addresses to whitelist",
     "Partner's network team wants a fixed list of Corppass IPs for outbound firewall rules.",
     "Corppass runs on AWS CloudFront with a dynamic IP pool, so whitelisting by IP is not advised. Recommended "
     "domain-based whitelisting.",
     ["firewall", "network"], False),
    ("Corppass Login", "Network & TLS", "Staging", "Pushed Authorization Request (PAR)", "invalid_request",
     "invalid_request due to TLS cipher suite",
     "A legacy Java 8 backend gets invalid_request from PAR although parameters are valid.",
     "The TLS cipher suite used was not compliant with FAPI 2.0 security requirements. Partner upgraded the JVM "
     "and restricted to compliant ciphers.",
     ["tls", "fapi2"], False),
    ("Corppass Login", "Configuration / Portal", "Staging", "Authorization redirect / callback", "invalid_request",
     "Callback URL mismatch between staging and production",
     "Login works in staging but fails in production with invalid_request.",
     "The production digital service did not have the production callback URL registered. `redirect_uri` must "
     "match a registered Callback URL exactly, including https. Configure in both environments.",
     ["callback-url", "cdp"], False),
    ("Corppass Developer Portal (CDP)", "Configuration / Portal", "Production", "Onboarding / Developer Portal", None,
     "Cannot log in to CDP",
     "Developer receives an access error when logging in to the Corppass Developer Portal.",
     "User must log in as a Business User and be authorised for the CDP digital service by their entity's "
     "Corppass Admin. Admin assigned the access.",
     ["cdp", "access"], False),
    ("Corppass Developer Portal (CDP)", "Configuration / Portal", "Staging", "Onboarding / Developer Portal", None,
     "Logged in to CDP but no digital services listed",
     "Developer can log in to CDP but sees no digital services.",
     "They were in the Production environment while the service was created in Staging, and also lacked the role "
     "to view services. Switched environment and admin assigned roles.",
     ["cdp", "roles"], False),
    ("Corppass Developer Portal (CDP)", "Configuration / Portal", "Staging", "Onboarding / Developer Portal", None,
     "Difference between CDP and Agency Admin portal",
     "Agency asks whether to configure their digital service in CDP or the Corppass Agency Admin portal.",
     "Explained the split using the FAQ 'How is CDP different from Corppass AA Portal?'. Technical configuration "
     "(JWKS, callback URLs) is in CDP.",
     ["cdp"], False),
    ("Myinfo Business", "Myinfo data", "Staging", "Userinfo request", "invalid_token",
     "Userinfo returns invalid_token",
     "Partner calls userinfo with `Authorization: Bearer <token>` and receives invalid_token.",
     "Access tokens are DPoP-bound. Partner must send `Authorization: DPoP <token>` plus a DPoP proof including the "
     "`ath` (access token hash) claim.",
     ["dpop", "userinfo"], False),
    ("Myinfo Business", "Myinfo data", "Production", "Userinfo request", None,
     "Entity financials missing for newly incorporated company",
     "Partner expects `financials` for a company incorporated two months ago and gets no data.",
     "Newly incorporated entities may not yet have records at the source. Partner should handle empty/unavailable "
     "data and allow manual input.",
     ["entity-data"], False),
    ("Myinfo Business", "Migration", "Staging", "Onboarding / Developer Portal", None,
     "Migrating Myinfo Business v2 with Person v3 flow",
     "Partner on Myinfo Business v2 also retrieves applicant data via Person v3 and asks how to migrate.",
     "Followed the 'Myinfo Business (v1/v2) Person v3 flows' guide: create a new Myinfo (v5) app first, then apply "
     "the step-by-step flow changes and migration checklist.",
     ["migration", "myinfo-business"], False),
    ("Myinfo Business", "Onboarding & Compliance", "Staging", "Onboarding / Developer Portal", None,
     "Data minimisation feedback on scope request",
     "Partner's request for shareholders, appointments and financials scopes was sent back for revision.",
     "Myinfo Business key principles require requesting only the data needed for the stated purpose. Partner "
     "narrowed the scopes and justified each.",
     ["scopes", "key-principles"], False),
    ("Corppass Login", "Authentication flow", "Staging", "ID token decryption / validation", None,
     "Nonce mismatch in ID token",
     "Partner's ID token validation fails on nonce in a multi-tab scenario.",
     "Nonce and state must be unique per authorisation session and stored per session. The second tab overwrote "
     "the stored nonce. Partner keyed session storage by state.",
     ["nonce", "id-token"], False),
    ("Corppass Login", "Authentication flow", "Staging", "Authorization redirect / callback", "access_denied",
     "User has no access to digital service",
     "Business users are redirected back with access_denied.",
     "The user's entity admin had not assigned the digital service to the user in Corppass. Advised partner to show "
     "guidance to contact their Corppass Admin.",
     ["authorisation", "access"], False),
    ("Authorization Info API", "Authentication flow", "Staging", "Userinfo request", None,
     "Where to get the user's roles for my service",
     "Partner needs the user's role/authorisation for their digital service.",
     "Request the `authinfo` scope; authorisation details are returned as `auth_info`. Third-party authorisation "
     "appears in `tp_auth_info`.",
     ["auth-info", "scopes"], False),
    ("Corppass Login", "Availability / Incident", "Production", "Token request", "temporarily_unavailable",
     "Token endpoint returning 503 temporarily_unavailable",
     "Partner sees a spike of 503 temporarily_unavailable on token calls for 10 minutes.",
     "Matches a short maintenance/high-load window. Advised exponential backoff retry and checking the status "
     "channel. No partner-side change.",
     ["incident", "retry"], True),
    ("Corppass Login", "Keys & JWKS", "Staging", "JWKS / key setup", None,
     "JWKS configuration for multiple digital services",
     "Agency with 3 digital services asks whether they can share one JWKS.",
     "Pointed to 'JWKS Configurations' in the onboarding notes; each digital service registers its JWKS endpoint, "
     "keys must have unique kids.",
     ["jwks", "cdp"], False),
]

SINGPASS_SLACK = [
    ("partner-support", "Singpass Login", "DPoP htu mismatch on token endpoint",
     [("Support officer", "Partner getting invalid_dpop_proof only in staging, prod fine. Any idea?"),
      ("Engineer", "Check `htu` — must be the exact token endpoint URL from the discovery doc for that environment."),
      ("Support officer", "They hardcoded the prod URL in the DPoP builder 🤦"),
      ("Engineer", "Yep. Tell them to read endpoints from `.well-known/openid-configuration` per env.")],
     "Partner fixed `htu` by reading endpoints from OpenID discovery per environment."),
    ("partner-support", "Singpass Login", "Client assertion exp too long",
     [("Support officer", "Partner sets client assertion exp = iat + 1 hour. Token call fails invalid_client."),
      ("Engineer", "Assertion must be short-lived — see Generation of Client Assertion for exp limits. Also aud must be the issuer."),
      ("Support officer", "Shared the doc. They'll set a ~2 min expiry.")],
     "Short-lived assertion with correct `aud` resolved invalid_client."),
    ("integration-eng", "Singpass Myinfo (v5)", "Spike of empty CPF fields on Sunday",
     [("Support officer", "Several agencies report empty CPF data this morning."),
      ("Engineer", "1st Sunday — CPFB downtime 0000–0800. Expected."),
      ("Support officer", "Will reply with the scheduled downtime page link.")],
     "Classified as scheduled downtime, not an incident."),
    ("partner-support", "Singpass Login", "Universal links for redirect",
     [("Support officer", "Bank app asking how to keep deep-linking without custom scheme."),
      ("Engineer", "Universal Links / App Links with https redirect URLs. Custom schemes are dropped in FAPI 2.0.")],
     "Partner moved to app-claimed https URLs."),
    ("integration-eng", "Singpass Login", "JWKS caching on our side",
     [("Support officer", "Partner added a new key but still failing — how long do we cache JWKS?"),
      ("Engineer", "Tell them to keep publishing both old and new keys during rotation and not to reuse kids. See Key Rotation section.")],
     "Advised overlap period during key rotation."),
    ("partner-support", "Developer Portal", "Duplicate app vs create new",
     [("Support officer", "Partner wants a second app with same config for another product line."),
      ("Engineer", "SDP has 'Duplicate an app' — cheaper than recreating, but redirect URLs/scopes still need review.")],
     "Partner used Duplicate an app."),
]

CORPPASS_SLACK = [
    ("corppass-support", "Corppass Login", "invalid_request but params look fine",
     [("Support officer", "Partner PAR returns invalid_request, all params validated."),
      ("Engineer", "Check JWKS reachability and TLS cipher suite — both surface as invalid_request on PAR."),
      ("Support officer", "JWKS was behind their VPN. Fixed.")],
     "JWKS endpoint was not publicly reachable."),
    ("corppass-support", "Myinfo Business", "Bearer vs DPoP on userinfo",
     [("Support officer", "Userinfo invalid_token for MIB partner."),
      ("Engineer", "Tokens are DPoP-bound. Use `Authorization: DPoP` + proof with `ath`.")],
     "Partner switched to DPoP authorization scheme."),
    ("corppass-support", "Corppass Login", "Certificate pinning outage",
     [("Support officer", "Two partners down after our cert rotation this morning."),
      ("Engineer", "They're pinning leaf certs. Point them to the TLS Certificates FAQ — trust AWS root CAs."),
      ("Support officer", "Sending advisory to both.")],
     "Partners removed leaf certificate pinning."),
    ("corppass-support", "Corppass Developer Portal (CDP)", "Developer cannot see services in CDP",
     [("Support officer", "Dev logged in to CDP, no services visible."),
      ("Engineer", "Usually wrong environment toggle or missing role. Ask their Corppass Admin.")],
     "Environment toggle + role assignment."),
    ("corppass-support", "Corppass Login", "auth context for MIB apps",
     [("Support officer", "MIB partner sends authentication_context_type and gets rejected."),
      ("Engineer", "Only for Corppass Login apps. Remove it for MIB.")],
     "Parameter removed for Myinfo Business client."),
    ("corppass-support", "Corppass Login", "Firewall whitelist request",
     [("Support officer", "Partner wants our IP list."),
      ("Engineer", "CloudFront — dynamic IPs. Whitelist by domain. There's an FAQ for it.")],
     "Domain-based whitelisting recommended."),
]

CATEGORY_HOURS = {"Authentication flow": (2, 30), "Keys & JWKS": (3, 48), "Configuration / Portal": (1, 24),
                  "Myinfo data": (1, 20), "Migration": (8, 120), "Network & TLS": (4, 72),
                  "Onboarding & Compliance": (6, 96), "Availability / Incident": (1, 8)}


def build(domain: str, tickets: list, slack: list, prefix: str, rng: random.Random):
    start = date(2025, 6, 1)
    span = (date(2026, 11, 15) - start).days
    out_t = []
    for i, (prod, cat, env, step, err, subj, desc, res, tags, esc) in enumerate(tickets, 1):
        lo, hi = CATEGORY_HOURS[cat]
        hrs = round(rng.uniform(lo, hi) * (1.8 if esc else 1.0), 1)
        out_t.append({"id": f"{prefix}-{1000 + i}", "product": prod, "category": cat, "environment": env,
                      "flow_step": step, "error_code": err, "subject": subj, "description": desc,
                      "resolution": res, "resolution_time_hrs": hrs, "escalated_to_engineer": esc,
                      "created_at": (start + timedelta(days=rng.randrange(span))).isoformat(),
                      "tags": tags, "synthetic": True})
    out_s = []
    for i, (ch, prod, topic, msgs, outcome) in enumerate(slack, 1):
        out_s.append({"id": f"{prefix}-S{100 + i}", "channel": ch, "product": prod, "topic": topic,
                      "messages": [{"role": r, "text": t} for r, t in msgs], "outcome": outcome,
                      "created_at": (start + timedelta(days=rng.randrange(span))).isoformat(),
                      "synthetic": True})
    SYNTHETIC_DIR.mkdir(parents=True, exist_ok=True)
    for name, rows in ((f"{domain}_tickets.jsonl", out_t), (f"{domain}_slack.jsonl", out_s)):
        (SYNTHETIC_DIR / name).write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n")
    print(f"{domain}: {len(out_t)} tickets, {len(out_s)} slack threads")


if __name__ == "__main__":
    rng = random.Random(42)
    build("singpass", SINGPASS_TICKETS, SINGPASS_SLACK, "SP", rng)
    build("corppass", CORPPASS_TICKETS, CORPPASS_SLACK, "CP", rng)
