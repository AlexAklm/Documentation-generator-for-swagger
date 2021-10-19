from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class OAuthFlow(SwaggerObject):
    authorizationUrl: str
    tokenUrl: str
    refreshUrl: str
    scopes: dict[str, str]

    def __init__(self,
                 authorizationUrl: str,
                 tokenUrl: str,
                 refreshUrl: str,
                 scopes: dict[str, str]):
        self.authorizationUrl = authorizationUrl
        self.tokenUrl = tokenUrl
        self.refreshUrl = refreshUrl
        self.scopes = scopes
