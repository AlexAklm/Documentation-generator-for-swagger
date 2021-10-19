from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from PathItemObjects import PathItem


class Paths(SwaggerObject):
    pathName: str
    pathsItem: PathItem

    def __init__(self, pathName: str, pathsItem: PathItem):
        self.pathName = pathName
        self.pathsItem = pathsItem
