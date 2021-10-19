from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from HeaderObjects import Header


class Encoding(SwaggerObject):
    contentType: str
    headers: dict[str, Header]
    style: str
    explode: bool
    allowReserved: bool


    def __init__(self,
                 contentType: str,
                 headers: dict[str, Header],
                 style: str,
                 explode: bool,
                 allowReserved: bool):
        self.contentType = contentType
        self.headers = headers
        self.style = style
        self.explode = explode
        self.allowReserved = allowReserved