from visualization_core.graph_utils import GraphUtils


class GraphVisualizationAttacher():

    #
    #   Get module_visualization_maps_map as map {module:visualization_maps}
    #
    #   Attaches visualization maps to FunctionNodes
    #
    @staticmethod
    def attach_visualizations_to_graph(root_node, module_visualization_maps_map):
        function_nodes_list = []
        GraphUtils.flatten_function_nodes(root_node, function_nodes_list)

        module_nodes_map = {function_node.associated_module:function_node for function_node in function_nodes_list}
        for module in module_visualization_maps_map.keys():
            module_nodes_map[module].add_visualization_maps(module_visualization_maps_map[module])







