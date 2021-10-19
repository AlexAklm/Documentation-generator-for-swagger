from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class SecurityRequirement(SwaggerObject):
    value: dict[str, list[str]]

    def __init__(self, value: dict[str, list[str]]):
        self.value = value