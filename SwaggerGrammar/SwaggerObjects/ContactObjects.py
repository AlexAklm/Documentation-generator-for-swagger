from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject


class Contact(SwaggerObject):
    name: str
    url: str
    email: str

    def __init__(self, name: str, url: str, email: str):
        self.name = name
        self.url = url
        self.email = email