from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from MediaTypeObjects import MediaType


class RequestBody(SwaggerObject):
    description: str
    content: dict[str, MediaType]
    required: bool

    def __init__(self,
                 description: str,
                 content: dict[str, MediaType],
                 required: bool):
        self.description = description
        self.content = content
        self.required = required