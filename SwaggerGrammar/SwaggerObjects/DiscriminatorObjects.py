from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class Discriminator(SwaggerObject):
    propertyName: str
    mapping: dict[str, str]

    def __init__(self, propertyName: str, mapping: dict[str, str]):
        self.propertyName = propertyName
        self.mapping = mapping