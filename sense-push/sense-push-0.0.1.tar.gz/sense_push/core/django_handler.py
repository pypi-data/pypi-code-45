import sense_core as sd


class DjangoPushDataHandler(object):

    def __init__(self, model_map):
        self.model_map = model_map

    def _get_model(self, database, table):
        key = "{0}_{1}".format(database, table)
        model = self.model_map.get(key)
        if model:
            return model
        return self.model_map.get(table)

    def insert(self, database, table, data):
        model = self._get_model(database, table)
        if not model:
            return
        model.objects.update_or_create(**data)
        sd.log_info("insert data table={0} data={1}".format(table, data))

    def update(self, database, table, data):
        model = self._get_model(database, table)
        if not model:
            return
        model.objects.update_or_create(**data)
        sd.log_info("update data table={0} data={1}".format(table, data))

    def delete(self, database, table, data):
        model = self._get_model(database, table)
        if not model:
            return
