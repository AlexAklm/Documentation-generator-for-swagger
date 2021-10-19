from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from ExternalDocumentationObjects import ExternalDocumentation
from ParameterObjects import Parameter
from RequestBodyObjects import RequestBody
from ResponsesObjects import Responses
from CallbackObjects import Callback
from SecurityRequirementObjects import SecurityRequirement
from ServerObjects import Server


class Operations(SwaggerObject):
    tags: list[str]
    summary: str
    description: str
    externalDocs: ExternalDocumentation
    operationId: str
    parameters: list[Parameter]
    requestBody: RequestBody
    responses: Responses
    callbacks: dict[str, Callback]
    deprecated: bool
    security: list[SecurityRequirement]
    servers: list[Server]

    def __init__(self,
                 tags: list[str],
                 summary: str,
                 description: str,
                 externalDocs: ExternalDocumentation,
                 operationId: str,
                 parameters: list[Parameter],
                 requestBody: RequestBody,
                 responses: Responses,
                 callbacks: dict[str, Callback],
                 deprecated: bool,
                 security: list[SecurityRequirement],
                 servers: list[Server]
                 ):
        self.tags = tags
        self.summary = summary
        self.externalDocs = externalDocs
        self.description = description
        self.operationId = operationId
        self.parameters = parameters
        self.requestBody = requestBody
        self.responses = responses
        self.callbacks = callbacks
        self.deprecated = deprecated
        self.security = security
        self.servers = servers
