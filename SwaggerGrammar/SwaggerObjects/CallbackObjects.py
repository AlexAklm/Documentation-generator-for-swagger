from SwaggerGrammar.SwaggerObjects.ExpressionObjects import Expression
from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class Callback(SwaggerObject):
    expression: Expression

    def __init__(self, expression: Expression):
        self.expression = expression