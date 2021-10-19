from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from SwaggerGrammar.SwaggerObjects.ExpressionObjects import Expression
from SwaggerGrammar.SwaggerObjects.ServerObjects import Server


class Link(SwaggerObject):
    operationRef: str
    operationId: str
    parameters: dict[str, Expression]
    requestBody: Expression
    description: str
    server: Server