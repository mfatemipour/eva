from flask import Flask, Request
# from werkzeug.datastructures import ImmutableOrderedMultiDict

class Eva(Flask):
    def __init__(self, import_name=__package__, domain=None,
                 auth=None, redis=None,
                 url_converters=None, json_encoder=None):
        super(Eva, self).__init__(import_name)
        self.domain = domain