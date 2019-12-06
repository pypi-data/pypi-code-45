
class PluginRepository():
    _instance = None

    def __init__(self) -> None:
        super().__init__()
        self.plugins_map = {}

    def add_plugin(self, plugin):
        self.plugins_map[plugin.name] = plugin

    def get_plugin(self, name):
        return self.plugins_map[name]

    def get_all_plugins(self):
        return self.plugins_map.values()

    def get_all_names(self):
        return self.plugins_map.keys()


def get_plugin_repository():
    if PluginRepository._instance is None:
        PluginRepository._instance = PluginRepository()
    return PluginRepository._instance