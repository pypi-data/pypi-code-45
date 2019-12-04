import logging
import types
import json
import pprint
from google.cloud import datastore
from pymacaron_core.swagger.apipool import ApiPool
from pymacaron.exceptions import PyMacaronException
from pymacaron.monitor import monitor


log = logging.getLogger(__name__)


db = None


GCLOUD_CLIENT = None

def set_datastore_client(client):
    global GCLOUD_CLIENT
    GCLOUD_CLIENT = client

def _get_client():
    global GCLOUD_CLIENT
    assert GCLOUD_CLIENT
    return GCLOUD_CLIENT

# Exception raised if no item found
class DatastoreItemNotFound(PyMacaronException):
    pass


# keep a mapping of entity name to which pymacaron object class to instantiate
# it into

model_to_persistent_class = {}

class PersistentSwaggerObject():

    @staticmethod
    def setup(childclass):
        """setup() is called to initialize persistence against a given Entity (aka
        table). The following class attributes must be set in the child class of
        PersistentSwaggerObject:

        * 'api_name': Name of the swagger api in which the searialized model is defined

        * 'model_name': Name of the swagger data model being serialized

        * 'table_name': Name of the Datastore Entity being serialized to

        * 'primary_key': The main indexing property of that Entity

        * 'secondary_keys': All other Entity properties that Datastore should
          build index for. Any property that is not the primary_key or in secondary_keys will be
          excluded form indexing.

        setup() sets the child class's attributes:

        * 'api': The pymacaron-core.swagger.api.API instance describing the API
          in which the serialized object is defined.

        * 'model': The constructor class for the Pymacaron Model being serialized.
        """

        if not hasattr(childclass, 'api'):
            api_name = getattr(childclass, 'api_name')
            model_name = getattr(childclass, 'model_name')
            table_name = getattr(childclass, 'table_name')
            primary_key = getattr(childclass, 'primary_key')
            secondary_keys = getattr(childclass, 'secondary_keys')

            assert api_name
            assert model_name
            assert table_name
            assert primary_key
            assert secondary_keys is not None

            log.info("Initializing %s with api_name=%s, model_name=%s, table_name=%s, primary_key=%s, secondary_keys=%s" % (
                childclass.__name__,
                api_name,
                model_name,
                table_name,
                primary_key,
                secondary_keys,
            ))

            global model_to_persistent_class
            model_to_persistent_class[model_name] = childclass

            api = getattr(ApiPool, api_name)
            model = getattr(getattr(api, 'model'), model_name)

            setattr(childclass, 'api', api)
            setattr(childclass, 'model', model)


    @classmethod
    def load_from_db(childclass, key_value):

        PersistentSwaggerObject.setup(childclass)

        result = None
        with monitor(kind='Datastore', method='load_from_db'):
            client = _get_client()
            k = client.key(childclass.table_name, key_value)
            result = client.get(k)

        if result is None:
            raise DatastoreItemNotFound("Entities %s has no item with %s=%s" % (childclass.table_name, childclass.primary_key, key_value))

        return childclass.to_model(result)


    @classmethod
    def import_childclass(self, object):
        log.debug("__persistence_class__: %s" % object.__persistence_class__)
        components = object.__persistence_class__.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod


    def save_to_db(self):
        global model_to_persistent_class

        # Do we need to run setup on the persistence class?
        if self.__class__.__name__ not in model_to_persistent_class:
            c = PersistentSwaggerObject.import_childclass(self)
            c.setup(c)

        childclass = model_to_persistent_class[self.__class__.__name__]

        j = childclass.api.model_to_json(self)
        log.debug("Storing json into Datastore/%s: %s" % (childclass.table_name, json.dumps(j, indent=2)))

        with monitor(kind='Datastore', method='save_to_db'):
            client = _get_client()

            # Figure out which keys not to index
            index_keys = childclass.secondary_keys + [childclass.primary_key]
            exclude_from_indexes = [k for k in list(j.keys()) if k not in index_keys]

            key_value = getattr(self, childclass.primary_key)
            assert key_value is not None
            key = client.key(childclass.table_name, key_value)

            entity = datastore.Entity(key=key, exclude_from_indexes=exclude_from_indexes)
            entity.update(j)

            client.put(entity)


    @classmethod
    def to_model(childclass, item):
        PersistentSwaggerObject.setup(childclass)

        if '__persistence_class__' in item:
            del item['__persistence_class__']

        # Convert from python dict to Swagger object
        item = childclass.api.json_to_model(childclass.model_name, item)

        # Monkey-patch this model so we can store it later
        item.save_to_db = types.MethodType(childclass.save_to_db, item)

        log.info("Loaded %s from table %s: %s" % (childclass.model_name, childclass.table_name, pprint.pformat(item, indent=4)))
        return item
