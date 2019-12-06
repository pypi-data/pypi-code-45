from visualization_core.interfaces.VisualizationTechnique import GraphVisualizationTechnique


class FeatureMapsPlugin(GraphVisualizationTechnique):
    def __init__(self, name) -> None:
        super().__init__(name)

    def is_applicable_for(self, model):
        return True

    def get_module_visualizations_list_map(self,model):
        super().get_module_visualizations_list_map(model)


