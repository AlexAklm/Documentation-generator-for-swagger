from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class ExternalDocumentation(SwaggerObject):
    url: str
    description: str

    def __init__(self, url: str, description: str):
        self.url = url
        self.description = description