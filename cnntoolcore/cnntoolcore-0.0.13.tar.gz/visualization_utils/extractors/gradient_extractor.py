from visualization_utils.hook_utils import HookUtils


class GradientExtractor:

    def __init__(self, model):
        self.module_input_gradient_map = None
        self.module_output_gradient_map = None
        self.model = model
        HookUtils.deep_hook_register(model, self.gradient_hook, 'backward')

    def extract(self, input_image):
        self.module_input_gradient_map = {}
        self.module_output_gradient_map = {}
        self.model.forward(input_image)

    def get_module_input_and_output_gradient_map(self):
        if self.module_input_gradient_map == None or self.module_output_gradient_map == None:
            raise ValueError()
        else:
            return self.module_input_gradient_map, self.module_output_gradient_map

    def gradient_hook(self, module, input, output):
        self.module_input_gradient_map[module] = input[0]
        self.module_output_gradient_map[module] = output
