from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from OAuthFlowObjects import OAuthFlow


class OAuthFlows(SwaggerObject):
    implicit: OAuthFlow
    password: OAuthFlow
    clientCredentials: OAuthFlow
    authorizationCode: OAuthFlow

    def __init__(self,
                 implicit: OAuthFlow,
                 password: OAuthFlow,
                 clientCredentials: OAuthFlow,
                 authorizationCode: OAuthFlow):
        self.implicit = implicit
        self.password = password
        self.clientCredentials = clientCredentials
        self.authorizationCode = authorizationCode
