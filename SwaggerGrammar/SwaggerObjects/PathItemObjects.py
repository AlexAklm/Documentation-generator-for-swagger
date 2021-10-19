from SwaggerGrammar.SwaggerObjects.SwaggerObject import SwaggerObject
from OperationsObjects import Operations
from ServerObjects import Server
from ParameterObjects import Parameter


class PathItem(SwaggerObject):
    ref: str
    summary: str
    description: str
    get: Operations
    put: Operations
    post: Operations
    delete: Operations
    options: Operations
    head: Operations
    patch: Operations
    trace: Operations
    servers: list[Server]
    parameters: list[Parameter]

    def __init__(self,
                 ref: str,
                 summary: str,
                 description: str,
                 get: Operations,
                 put: Operations,
                 post: Operations,
                 delete: Operations,
                 options: Operations,
                 head: Operations,
                 patch: Operations,
                 trace: Operations,
                 servers: list[Server],
                 parameters: list[Parameter]
                 ):
        self.ref = ref
        self.summary = summary
        self.description = description
        self.get = get
        self.put = put
        self.post = post
        self.delete = delete
        self.options = options
        self.head = head
        self.patch = patch
        self.trace = trace
        self.servers = servers
        self.parameters = parameters
