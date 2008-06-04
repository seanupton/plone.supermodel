from zope.interface import Interface
from zope import schema

class IXMLToSchema(Interface):
    """Functionality to parse an XML representation of a schema and return
    an interface representation with zope.schema fields.
    
    A file can be parsed purely for a schema. This allows syntax like:
    
        class IMyType( xml_schema('schema.xml') ):
            pass
        
    To get more detailed information, including hints for setting up form
    widgets, use the full version:
    
        model = load_file('schema.xml')
    """
    
    def xml_schema(filename, schema=u"", policy=u""):
        """Given a filename relative to the current module, return an
        interface representing the schema contained in that file. If there
        are multiple <schema /> blocks, return the unnamed one, unless 
        a name is supplied, in which case the 'name' attribute of the schema
        will be matched to the schema name.
        
        The policy argument can be used to pick a different parsing policy.
        Policies must be registered as named utilities providing
        ISchemaPolicy.
        
        Raises a KeyError if the schema cannot be found.
        Raises an IOError if the file cannot be opened.
        """
    
    def load_file(filename, reload=False, policy=u""):
        """Return a model definition as contained in the given XML file, 
        which is read relative to the current module (unless it is an 
        absolute path).
        
        The return value is a dict with keys:
        
         - schemata -- a dict with keys of schema names and values of schema
            interfaces; one of the keys will be u"" (the default schema)
         - widgets -- a dict with keys of schema names and values of dicts,
            which in turn use field names as keys and contain widget hints
            as values
            
        If reload is True, reload a schema even if it's cached. If policy
        is given, it can be used to select a custom schema parsing policy.
        Policies must be registered as named utilities providing
        ISchemaPolicy.
        """
    
    def load_string(model, policy=u""):
        """Load a model from a string rather than a file.
        """
    
    def serialize_schema(schema, name=u""):
        """Return an XML string representing the given schema interface. This
        is a convenience method around the serialize_model() method, below.
        """
    def serialize_model(model):
        """Return an XML string representing the given model, as returned by
        the load_file() or load_string() method.
        """

class ISchemaPolicy(Interface):
    """A utility that provides some basic attributes of the generated
    schemata. Provide a custom one to make policy decisions about where
    generated schemata live, what bases they have and how they are named.
    """

    def module(schema_name, tree):
        """Return the module name to use.
        """
        
    def bases(schema_name, tree):
        """Return the bases to use.
        """
        
    def name(schema_name, tree):
        """Return the schema name to use
        """
        
class IFieldExportImportHandler(Interface):
    """Named utilities corresponding to node names should be registered for
    this interface. They will be called upon to build a schema fields out of
    DOM ndoes.
    """
    
    def read(node):
        """Read a field from the node and return a new instance
        """
        
    def write(field, field_name, field_type):
        """Create and return a new node representing the given field
        """