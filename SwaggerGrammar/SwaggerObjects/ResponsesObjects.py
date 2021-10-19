from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from ResponseObjects import Response


class Responses(SwaggerObject):
    default: Response
    httpStatusCode: dict[str, Response]

    def __init__(self, default: Response, statusCode: dict[str, Response]):
        self.default = default
        self.httpStatusCode = statusCode
