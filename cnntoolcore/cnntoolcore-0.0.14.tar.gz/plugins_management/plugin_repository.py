import inspect
import sys

from plugins.feature_maps.input_feature_maps_plugin import InputFeatureMapsPlugin
from plugins.feature_maps.output_feature_maps_plugin import OutputFeatureMapsPlugin


class PluginRepository():
    _instance = None

    def __init__(self) -> None:
        super().__init__()
        self.plugins_map = {}
        self.scan_plugins_package()


    def scan_plugins_package(self):
        self.add_plugin(InputFeatureMapsPlugin())
        self.add_plugin(OutputFeatureMapsPlugin())

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


if __name__ == "__main__":
    repo = get_plugin_repository()

    for plugin in repo.get_all_plugins():
        print(plugin.name)