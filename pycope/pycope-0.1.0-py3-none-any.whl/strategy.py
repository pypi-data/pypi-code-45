class Strategy(object):
    def __init__(self, executable, field_prioritizers=[]):
        """
        :param executable: The function that this strategy is for.
        :param field_prioritizers: Functions that must take in a mapping of names 
            to values (fields) and produce a priority number. These functions 
            define the context that this strategy is valid for.
        """
        self._field_prioritizers = field_prioritizers
        self._executable = executable
        self._index = 0
    
    def get_priority(self, fields):
        """
        Counts up votes for the provided fields based on the 
        _field_prioritizers.
        :param fields: An immutable mapping of names to values.
        :returns: The number of votes
        """
        return sum(map(
            lambda prioritizer: prioritizer(fields), 
            self._field_prioritizers))
    
    def execute(self, *args, **kwargs):
        """
        Executes the executable associated with this strategy.
        Arguments and return values are passed through.
        """
        return self._executable(*args, **kwargs)
