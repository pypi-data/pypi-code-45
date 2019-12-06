from importlib._bootstrap_external import SourceFileLoader

class ModelLoader():
    #Loading model variable from file with name set by convention as 'model'
    def load_model_from_external_file(self,filepath):
        model_file = SourceFileLoader('conf', filepath).load_module()
        return model_file.model

