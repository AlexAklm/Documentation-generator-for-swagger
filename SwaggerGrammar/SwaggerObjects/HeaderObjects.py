from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from SwaggerGrammar.SwaggerObjects.ExternalDocumentationObjects import ExternalDocumentation


class Header(SwaggerObject):
    name: str
    description: str
    externalDocs: ExternalDocumentation

    def __init__(self, name: str, description: str, exDocs: ExternalDocumentation):
        self.name = name
        self.description = description
        self.externalDocs = exDocs
