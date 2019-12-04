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
        self._insert0(database, table, data, "insert")

    def _insert0(self, database, table, data, action):
        model_item = self._get_model(database, table)
        if not model_item:
            return
        model = model_item['model']
        data2 = self._build_update_data(data, model_item)
        model.objects.update_or_create(**data2)
        sd.log_info(action + " data table={0} data={1}".format(table, data))

    def update(self, database, table, data):
        self._insert0(database, table, data, "update")

    def _build_update_data(self, data, model_item):
        after = data.get('after')
        if after:
            data = after
        res = self.build_primary_keys(data, model_item['primary'])
        if not res:
            sd.log_error("build_primary_keys failed for data={0} primary={1}".format(data, model_item['primary']))
            return None
        res = self.build_update_params(res, data)
        return res

    def build_update_params(self, res, data):
        res['defaults'] = data
        return res

    def build_primary_keys(self, data, primary_keys):
        res = {}
        for key in primary_keys:
            val = data.pop(key)
            if val is None:
                return None
            res[key] = val
        return res

    def delete(self, database, table, data):
        model_item = self._get_model(database, table)
        if not model_item:
            return
        model = model_item['model']
