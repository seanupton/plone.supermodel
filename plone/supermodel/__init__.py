from StringIO import StringIO

from zope.interface import moduleProvides

from plone.supermodel.interfaces import IXMLToSchema
from plone.supermodel import parser
from plone.supermodel import serializer
from plone.supermodel import utils

# Cache models by absolute filename
_model_cache = {}

def xml_schema(filename, schema=u"", policy=u"", _frame=2):
    return load_file(filename, policy=policy, _frame=_frame+1)[u"schemata"][schema]

def load_file(filename, reload=False, policy=u"", _frame=2):
    global _model_cache
    path = utils.relative_to_calling_package(filename, _frame)
    if reload or path not in _model_cache:
        _model_cache[path] = parser.parse(path, policy=policy)    
    return _model_cache[path]

def load_string(model, policy=u""):
    return parser.parse(StringIO(model), policy=policy)
    
def serialize_schema(schema, name=u""):
    return serialize_model(dict(widgets={},
                               schemata={name : schema},
                              ))
def serialize_model(model):
    return serializer.serialize(model) 

moduleProvides(IXMLToSchema)

__all__ = ('xml_schema', 'load_file', 'load_string', 'serialize_schema', 'serialize_model',)