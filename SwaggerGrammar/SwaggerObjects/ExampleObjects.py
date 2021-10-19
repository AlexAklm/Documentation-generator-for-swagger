from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class Example(SwaggerObject):
    summary: str
    description: str
    externalValue: str

    def __init__(self,
                 summary: str,
                 description: str,
                 externalValue: str,
                 value):
        self.value = value
        self.summary = summary
        self.description = description
        self.externalValue = externalValue
