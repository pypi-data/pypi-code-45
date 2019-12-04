

class Dataset():

    def __init__(self, input_file=''):
        self.input_file = input_file


    def load_data(self, input_file):

        with open(input_file, 'r') as f:
            f.readline()


    def normalize(self, data, norm_method=''):
        pass


    def save_data(self, data, output_file=''):
        pass


