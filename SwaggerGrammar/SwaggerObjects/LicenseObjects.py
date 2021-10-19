from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class License(SwaggerObject):
    name: str
    url: str

    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url