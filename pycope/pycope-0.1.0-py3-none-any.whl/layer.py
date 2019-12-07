class Layer(object):
    def __init__(self, context, fields_to_add={}, fields_to_remove=[]):
        """
        :param context: The context that will be affected by the layer.
        :param fields_to_add: A mapping of field names to field values. They will
            be added to this layer.
        :param fields_to_remove: Field names that should be removed from this layer.
        """
        self.__context = context
        self.__fields_to_add = fields_to_add
        self.__fields_to_remove = fields_to_remove
     
    def __enter__(self):
        """The layer's information is injected into the associated context."""
        self.__context.push_layer(self.__fields_to_add, self.__fields_to_remove)
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        """The last injected layer is removed from the context."""
        self.__context.pop_layer()
        