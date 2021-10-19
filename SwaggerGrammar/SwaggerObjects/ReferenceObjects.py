from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
# TODO: Write $ + ref


class Reference(SwaggerObject):
    ref: str

    def __init__(self, ref: str):
        self.ref = ref