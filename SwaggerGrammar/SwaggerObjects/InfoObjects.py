from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from ContactObjects import Contact
from LicenseObjects import License


class Info(SwaggerObject):
    title: str
    description: str
    termsOfService: str
    contact: Contact
    license: License
    version: str

    def __init__(self, title: str,
                 descriptions: str,
                 terms: str,
                 contact: Contact,
                 license: License,
                 version: str):
        self.title = title
        self.description = descriptions
        self.termsOfService = terms
        self.contact = contact
        self.license = license
        self.version = version
