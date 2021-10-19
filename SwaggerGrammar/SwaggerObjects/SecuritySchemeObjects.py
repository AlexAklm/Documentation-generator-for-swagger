from SwaggerObject import SwaggerObject
from OAuthFlowsObjects import OAuthFlows

# TODO: Replace "In" to "in"


class SecurityScheme(SwaggerObject):
    type: str
    description: str
    name: str
    In: str
    scheme: str
    bearerFormat: str
    flows: OAuthFlows
    openIdConnectUrl: str

    def __init__(self,
                 type: str,
                 description: str,
                 name: str,
                 In: str,
                 scheme: str,
                 bearerFormat: str,
                 flows: OAuthFlows,
                 openIdConnectUrl: str):
        self.type = type
        self.description = description
        self.name = name
        self.In = In
        self.scheme = scheme
        self.bearerFormat = bearerFormat
        self.flows = flows
        self.openIdConnectUrl = openIdConnectUrl
