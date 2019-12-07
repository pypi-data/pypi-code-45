from plugins_management.plugin_repository import get_plugin_repository


class PluginSelector():
    @staticmethod
    def get_all_plugin_names():
        return get_plugin_repository().get_all_plugins()

    @staticmethod
    def get_selected_plugins(name_list):
        repository = get_plugin_repository()
        return [repository.get_plugin(name) for name in name_list]