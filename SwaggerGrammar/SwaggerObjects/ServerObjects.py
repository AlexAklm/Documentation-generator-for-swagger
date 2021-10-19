from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class Server(SwaggerObject):
    url: str
    description: str
    variables: dict

    def __init__(self, url: str, description: str, variables: dict):
        self.url = url
        self.description = description
        self.variables = variables
