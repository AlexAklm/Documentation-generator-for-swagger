from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class XML(SwaggerObject):
    name: str
    namespace: str
    prefix: str
    attribute: bool
    wrapped: bool

    def __init__(self,
                 name: str,
                 namespace: str,
                 prefix: str,
                 attribute: str,
                 wrapped: str):
        self.name = name
        self.namespace = namespace
        self.prefix = prefix
        self.attribute = bool
        self.wrapped = bool