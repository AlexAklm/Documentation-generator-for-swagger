from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from ExternalDocumentationObjects import ExternalDocumentation


class Tag(SwaggerObject):
    name: str
    description: str
    externalDocs: ExternalDocumentation

    def __init__(self,
                 name: str,
                 description: str,
                 externalDocs: ExternalDocumentation):
        self.name = name
        self.description = description
        self.externalDocs = externalDocs