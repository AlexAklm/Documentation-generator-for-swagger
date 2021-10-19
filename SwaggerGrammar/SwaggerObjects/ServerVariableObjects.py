from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class ServerVariable(SwaggerObject):
    enum: list[str]
    default: str
    description: str

    def __init__(self, enum: list[str], default: str, description: str):
        self.enum = enum
        self.default = default
        self.description = description
