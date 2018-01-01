# from eva import Eva
#
# hr_schema = {
#   "title": "HR-RuleSet",
#   "type": "object",
#   "properties": {
#       "npls": {
#           "description": "a set of named prefix list to use when needed",
#           "type": "array",
#           "items": {
#               "title": "npl",
#               "type": "object",
#               "properties":{
#                   "name" : {
#                       "type":"string",
#                       "pattern" : "^[_a-zA-Z][_a-zA-Z0-9]{0,30}$"
#                   },
#                   "prefixes" : {
#                       "type" : "array",
#                       "items" : {
#                           "type" : "string",
#                           "pattern" : "^([a-z]|[0-9])*(\\*)?$"
#                       },
#                       "minItems": 1
#                   }
#               }
#           }
#       },
#       "taggers": {
#           "description": "use theses criteria to set various flags",
#           "type": "array",
#           "items": {
#               "title": "tagger",
#               "type": "object",
#               "properties":{
#                   "parameters" : {
#                       "type":"object",
#                       "properties":{
#                         "SRI-Calling": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "SRI-Sc": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "SRI-Msisdn": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "Dest-Msc": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "IMSI": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "MT-Sc": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "MT-Calling": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "A-Number": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         },
#                         "B-Number": {
#                             "type":"string",
#                             "pattern" : "^((@[_a-zA-Z][_a-zA-Z0-9]{0,30})|(([a-z]|[0-9])*(\\*)?))$"
#                         }
#                       }
#                   },
#                   "set_flags" : {
#                       "type" : "array",
#                       "items" : {
#                           "type" : "string",
#                           "pattern" : "^[_A-Z][A-Z0-9]{0,30}$"
#                       },
#                       "minItems": 1
#                   }
#               },
#               "required": ["parameters", "set_flags"]
#           }
#       },
#       "rules":{
#           "type": "array",
#           "items": {
#               "title": "rule",
#               "type" : "object",
#               "properties":{
#                   "id":{
#                       "type": "string",
#                       "pattern": "^[_a-zA-Z][_a-zA-Z0-9]{0,30}$"
#                   },
#                   "flags":{
#                       "type" : "array",
#                           "items" : {
#                               "type" : "string",
#                               "pattern" : "^(~)?[_A-Z][A-Z0-9]{0,30}$"
#                           },
#                           "minItems": 0
#                   },
#                     "action":{
#                         "type":"object",
#                         "properties":{
#                             "type": "string",
#                             "parameters":{
#                                 "type":"object",
#                                 "properties":{}
#                             }
#                         }
#                     }
#               }
#           }
#       },
#
#       "default_rule":{
#             "type": "object",
#             "properties":{
#                 "action":{
#                     "type":"object",
#                     "properties":{
#                         "type": "string",
#                         "parameters":{
#                             "type":"object",
#                             "properties":{}
#                         }
#                     }
#                 }
#              }
#       },
#
#       "cdr":{
#           "type": "array",
#           "items":{
#               "type":"object",
#               "properties":{
#                   "tag":{
#                       "type":"string",
#                       "pattern": "^[_a-zA-Z][_a-zA-Z0-9]{0,30}$"
#                   },
#                   "flags":{
#                       "type" : "array",
#                       "items" : {
#                           "type" : "string",
#                           "pattern" : "^(~)?[_A-Z][A-Z0-9]{0,30}$"
#                           },
#                       "minItems": 0
#                   }
#               }
#           }
#       }
#   },
#   "required":["npls", "taggers", "rules", "default_rule", "cdr"]
# }

simple_schema = {
    "title": "simple",
    "type": "string"
}

domain = {
  "simple": simple_schema
}
#
#
# app = Eva(domain=domain)
# app.run()
#

from flask import Flask

def hello_endpoint(id, subpath):
    return '{}, {}'.format(id, subpath)

class Eva(Flask):
    def __init__(self, import_name=__package__, domain=None,
                 auth=None, redis=None,
                 url_converters=None, json_encoder=None):
        super(Eva, self).__init__(import_name)
        self.domain = domain
        self.url_map.strict_slashes = False
        self.add_url_rule('/index/<int:id>/<path:subpath>','/index', hello_endpoint)


app = Eva(__name__, domain=domain)

app.run()

