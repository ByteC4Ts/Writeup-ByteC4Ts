# 1 - req

- `GET site:8080/`

# 1 - resp

- A `/flag` endpoint for SSO Login.

```html
<a class="btn" href="/flag">SSO Login</a>
```

# 2 - req

- `GET site:8080/flag`

# 2 - resp

- A `302` redirect to the SSO server `site:8081/sso?SAMLRequest=...&RelayState=...`.

`SAMLRequest` is a base64-encoded, deflated SAML AuthnRequest:

```xml

<samlp:AuthnRequest
        xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
        xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="id-b9a6f13d624281f35a404a8500cbf9a8775cc4ac"
        Version="2.0" IssueInstant="2025-11-29T03:57:23.616Z" Destination="http://web.heroctf.fr:8081/sso"
        AssertionConsumerServiceURL="http://web.heroctf.fr:8080/saml/acs"
        ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST">
    <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">http://web.heroctf.fr:8080/saml/metadata
    </saml:Issuer>
    <samlp:NameIDPolicy Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient" AllowCreate="true"/>
</samlp:AuthnRequest>
```

`RelayState`:

```
cpeFK8sMOjlMQJQ6FCC1mjYet1WQ6rcKknhd7rNlLEI8hOJBeyAAq_fR
```

- `Set-Cookie: saml_cpeFK8sMOjlMQJQ6FCC1mjYet1WQ6rcKknhd7rNlLEI8hOJBeyAAq_fR=...`

cookie key is the same as the `RelayState`.

cookie value is a JWT:

```json
{
  "alg": "RS256",
  "typ": "JWT"
}

{
  "aud": "http://web.heroctf.fr:8080",
  "exp": 1764388733,
  "iat": 1764388643,
  "iss": "http://web.heroctf.fr:8080",
  "nbf": 1764388643,
  "sub": "cpeFK8sMOjlMQJQ6FCC1mjYet1WQ6rcKknhd7rNlLEI8hOJBeyAAq_fR",
  "id": "id-b9a6f13d624281f35a404a8500cbf9a8775cc4ac",
  "uri": "/flag",
  "saml-authn-request": true
}
```

# 3 - req

- `GET site:8081/sso?SAMLRequest=...&RelayState=...`

Just forwarding the `302` redirect from step 2.

# 3 - resp

```html

<html>
<p></p>
<form method="post" action="http://web.heroctf.fr:8081/sso">
    <input type="text" name="user" placeholder="user" value=""/>
    <input type="password" name="password" placeholder="password" value=""/>
    <input type="hidden" name="SAMLRequest" value="..."/>
    <input type="hidden" name="RelayState" value="..."/>
    <input type="submit" value="Log In"/>
</form>
</html>
```

Here the `SAMLRequest` is only base64-encoded (not deflated), the raw XML is the same as in step 2.

# 4 - req

- `POST site:8081/sso`
- form data: `user=...&password=...&SAMLRequest=...&RelayState=...`

# 4 - resp

```html

<html>
<form method="post" action="http://web.heroctf.fr:8080/saml/acs" id="SAMLResponseForm">
    <input type="hidden" name="SAMLResponse" value="...">
    <input type="hidden" name="RelayState" value="..."/>
    <input id="SAMLSubmitButton" type="submit" value="Continue"/>
</form>
<script>document.getElementById('SAMLSubmitButton').style.visibility = 'hidden';</script>
<script>document.getElementById('SAMLResponseForm').submit();</script>
</html>
```

`SAMLResponse` is a base64-encoded SAML Response:

```xml

<samlp:Response
        xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
        xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
        xmlns:xs="http://www.w3.org/2001/XMLSchema" ID="id-d965d7ca5771c37fbfc59d9a443839c6084854c0" Version="2.0"
        IssueInstant="2025-11-29T03:57:38.851Z" Destination="http://web.heroctf.fr:8080/saml/acs">
    <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">http://web.heroctf.fr:8081/metadata
    </saml:Issuer>
    <samlp:Status>
        <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
    </samlp:Status>
    <saml:Assertion
            xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" ID="id-57e95d654fc1a97630e160e413263951de904926"
            IssueInstant="2025-11-29T03:57:38.93Z" Version="2.0">
        <saml:Issuer Format="urn:oasis:names:tc:SAML:2.0:nameid-format:entity">http://web.heroctf.fr:8081/metadata
        </saml:Issuer>
        <ds:Signature
                xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
            <ds:SignedInfo>
                <ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                <ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
                <ds:Reference URI="#id-57e95d654fc1a97630e160e413263951de904926">
                    <ds:Transforms>
                        <ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"/>
                        <ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
                    </ds:Transforms>
                    <ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
                    <ds:DigestValue>szmdOaLZHPDW0sq3k4urIpuFBfk=</ds:DigestValue>
                </ds:Reference>
            </ds:SignedInfo>
            <ds:SignatureValue>
                Pjol+GhNS192ZHRBAVh7PTN93oGfLwTzoqmvvAeUcSlArkT2udMsnodPm1C3KkXHLgth8FgMTo8OPketRPCGs9+zdZHtWpKSGcamfY210BNmfyRskmhhkl96m3BX5nLjsu/Hb36vJWz7AXqSzHhypU0+32462IV/gQBq8eLn4IDSM3asuTyuhJE6nA9YzG4ct3dv6a/hv5czEPofdI9FAaOntNXhOZoZ/fOptYHkhXMfVQPsSfD5i2Ya1JblXbVvtogTMPyP8UZEU4BxqLKc+UEIRNnaBNRLGYkFDX9G3KyAByQ0B3e54HhjJ3RFTzj774Grg4bb5dsaozvQX08IaA==
            </ds:SignatureValue>
            <ds:KeyInfo>
                <ds:X509Data>
                    <ds:X509Certificate>
                        MIIC6TCCAdGgAwIBAgIIHZfD7gkxJacwDQYJKoZIhvcNAQELBQAwGTEXMBUGA1UEAxMOc2FtbC1pZHAtbG9jYWwwHhcNMjUxMTI3MTEzMDA2WhcNMjYxMTI3MTIzMDA2WjAZMRcwFQYDVQQDEw5zYW1sLWlkcC1sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMBk6y4ZleHh8Zm5dSme/7Ma27xBxBvFJox+TD0bwhkV420fDiVi5sAhHtDBG8OXuHWgZn868GzuM2f5jWSHqaYVQ0wisYXj17aIdqOwTivxkfmdtQrNckzLAxtsUMMIfI8jW+b9HIK7frx7zhyMm02a6BA2CGmRmDbd0Svo+GdjPRgJQOYqELOpAUiaTQOf3zbjqafagNzJz9YCvcgamy2eAIfYNBlBDe6MFiGu29U/ta14Ru3wV5F0ICV3L1E2Zb15eHCAQhT49hceBiNLWXXQWfX9XpOc911aWFqwoUSfdBgNc0uBfBK1MA+bGzzKCKgoTLwpCDecVOQfNcDdEIcCAwEAAaM1MDMwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAA/Ud68YxqM4n+3meEOCJfPwWkdP6Y8vG+x91k56oLBFwgoHsq3aGNpwbFgtGmPO0XtWRt8AsCtjD7CXXdf63jR26E6GsQsY+VtnJkrca7OlCy4fJd4rPuDC/JPPWlbc28qOTURKK4tLLGqn49FBlXvBlDCh4InQQrGuAgikJiyDEk6qxeYpcMppgwbmFCMe/BcSn3ZAKPJTg/npU4SMebk104vePapyk4Rs6nEoMLPufe1H6vul00zzY3CEd/q/Wx9Gnj+n4uD04ugJKoamYD0NrGVYnLD/cLzA19JGurJX/QZf4CIvjLBu2HKfcnVCRwdL+qKWu7xD0We08yP2zcI=
                    </ds:X509Certificate>
                </ds:X509Data>
            </ds:KeyInfo>
        </ds:Signature>
        <saml:Subject>
            <saml:NameID Format="urn:oasis:names:tc:SAML:2.0:nameid-format:transient"
                         NameQualifier="http://web.heroctf.fr:8081/metadata"
                         SPNameQualifier="http://web.heroctf.fr:8080/saml/metadata"/>
            <saml:SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer">
                <saml:SubjectConfirmationData Address="89.185.27.152:43285"
                                              InResponseTo="id-b9a6f13d624281f35a404a8500cbf9a8775cc4ac"
                                              NotOnOrAfter="2025-11-29T03:59:08.851Z"
                                              Recipient="http://web.heroctf.fr:8080/saml/acs"/>
            </saml:SubjectConfirmation>
        </saml:Subject>
        <saml:Conditions NotBefore="2025-11-29T03:57:23.616Z" NotOnOrAfter="2025-11-29T03:58:53.616Z">
            <saml:AudienceRestriction>
                <saml:Audience>http://web.heroctf.fr:8080/saml/metadata</saml:Audience>
            </saml:AudienceRestriction>
        </saml:Conditions>
        <saml:AuthnStatement AuthnInstant="2025-11-29T03:57:38.93Z"
                             SessionIndex="3fde6497798f1cecba2ea2d3a4b159026d4ea8686188b09c64e515933f858a33">
            <saml:SubjectLocality Address="89.185.27.152:43285"/>
            <saml:AuthnContext>
                <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
                </saml:AuthnContextClassRef>
            </saml:AuthnContext>
        </saml:AuthnStatement>
        <saml:AttributeStatement>
            <saml:Attribute FriendlyName="uid" Name="urn:oid:0.9.2342.19200300.100.1.1"
                            NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
                <saml:AttributeValue
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">user
                </saml:AttributeValue>
            </saml:Attribute>
            <saml:Attribute FriendlyName="eduPersonAffiliation" Name="urn:oid:1.3.6.1.4.1.5923.1.1.1.1"
                            NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
                <saml:AttributeValue
                        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="xs:string">Users
                </saml:AttributeValue>
            </saml:Attribute>
        </saml:AttributeStatement>
    </saml:Assertion>
</samlp:Response>
```

The auto-submitting form will `POST` this SAML Response to the endpoint `site:8080/saml/acs`.

# 5 - req

- `POST site:8080/saml/acs`
- form data: `SAMLResponse=...&RelayState=...`
- `Cookie: saml_cpeFK8sMOjlMQJQ6FCC1mjYet1WQ6rcKknhd7rNlLEI8hOJBeyAAq_fR=...`

# 5 - resp

- A `302` redirect to `/flag` with `Set-Cookie: saml_cpeFK8sMOjlMQJQ6FCC1mjYet1WQ6rcKknhd7rNlLEI8hOJBeyAAq_fR=...`
  containing a new JWT:

```json
{
  "alg": "RS256",
  "typ": "JWT"
}

{
  "aud": "http://web.heroctf.fr:8080",
  "exp": 1764392259,
  "iat": 1764388659,
  "iss": "http://web.heroctf.fr:8080",
  "nbf": 1764388659,
  "attr": {
    "SessionIndex": [
      "3fde6497798f1cecba2ea2d3a4b159026d4ea8686188b09c64e515933f858a33"
    ],
    "eduPersonAffiliation": [
      "Users"
    ],
    "uid": [
      "user"
    ]
  },
  "saml-session": true
}
```
