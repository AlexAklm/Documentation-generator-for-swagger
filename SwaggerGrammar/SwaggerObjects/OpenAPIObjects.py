from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from InfoObjects import Info
from PathsObjects import Paths
from ServerObjects import Server


class OpenAPI(SwaggerObject):
    openapi: str
    info: Info
    servers: list[Server]
    paths: Paths

    def __init__(self, api: str, info: Info, servers: list, paths: Paths):
        self.openapi = api
        self.info = info
        self.servers = servers
        self.paths = paths
