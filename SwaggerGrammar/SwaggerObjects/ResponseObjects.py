from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from HeaderObjects import Header
from MediaTypeObjects import MediaType
from LinkObjects import Link


class Response(SwaggerObject):
    description: str
    headers: dict[str, Header]
    content: dict[str, MediaType]
    links: dict[str, Link]

    def __init__(self,
                 description: str,
                 headers: dict[str, Header],
                 content: dict[str, MediaType],
                 links: dict[str, Link]):

        self.description = description
        self.headers = headers
        self.content = content
        self.links = links