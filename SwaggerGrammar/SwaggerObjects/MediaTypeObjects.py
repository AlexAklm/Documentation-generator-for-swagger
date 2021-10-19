from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from SchemaObjects import Schema
from ExampleObjects import Example
from EncodingObjects import Encoding


class MediaType(SwaggerObject):
    schema: Schema
    examples: dict[str, Example]
    encoding: dict[str, Encoding]

    def __init__(self,
                 schema: Schema,
                 examples: dict[str, Example],
                 encoding: dict[str, Encoding]):
        self.schema = schema
        self.examples = examples
        self.encoding = encoding