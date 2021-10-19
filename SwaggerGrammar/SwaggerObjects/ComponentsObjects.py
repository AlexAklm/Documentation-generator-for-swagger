from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from SchemaObjects import Schema
from ResponseObjects import Response
from ParameterObjects import Parameter
from RequestBodyObjects import RequestBody
from HeaderObjects import Header
from ExampleObjects import Example
from LinkObjects import Link
from CallbackObjects import Callback
from SecuritySchemeObjects import SecurityScheme
from ReferenceObjects import Reference


class Components(SwaggerObject):
    schemes: dict[str, Schema]
    responses: dict[str, Response]
    parameters: dict[str, Parameter]
    examples: dict[str, Example]
    requestBodies: dict[str, RequestBody]
    headers: dict[str, Header]
    securitySchemes: dict[str, SecurityScheme]
    links: dict[str, Link]
    callbacks: dict[str, Callback]

    def __init__(self,
                 schemes: dict[str, Schema],
                 responses: dict[str, Response],
                 parameters: dict[str, Parameter],
                 examples: dict[str, Example],
                 requestBodies: dict[str, RequestBody],
                 headers: dict[str, Header],
                 securitySchemes: dict[str, SecurityScheme],
                 links: dict[str, Link],
                 callbacks: dict[str, Callback]
                ):
        self.schemes = schemes
        self.responses = responses
        self.parameters = parameters
        self.examples = examples
        self.requestBodies = requestBodies
        self.headers = headers
        self.securitySchemes = securitySchemes
        self.links = links
        self.callbacks = callbacks
