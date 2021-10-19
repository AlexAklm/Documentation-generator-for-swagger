from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from SchemaObjects import Schema
from ExampleObjects import Example


class Parameter(SwaggerObject):
    name: str
    In: str
    description: str
    required: bool
    deprecated: bool
    allowEmptyValue: bool
    style: str
    explode: bool
    allowReserved: bool
    schema: Schema
    examples: dict[str, Example]

    def __init__(self,
                 name: str,
                 In: str,
                 description: str,
                 required: bool,
                 deprecated: bool,
                 allowEmptyValue: bool):
        self.name = name
        self.description = description
        self.In = In
        self.required = required
        self.deprecated = deprecated
        self.allowEmptyValue = allowEmptyValue