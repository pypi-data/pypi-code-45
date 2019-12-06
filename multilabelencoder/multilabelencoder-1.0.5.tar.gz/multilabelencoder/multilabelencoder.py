import pickle
from sklearn.preprocessing import LabelEncoder

#customized label encoder
class MultiColumnLabelEncoder:    
    def __init__(self, columns = None):
        self.columns = columns # list of column to encode
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''        
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                print('column', col)
                encoder = LabelEncoder()
                output[col] = encoder.fit_transform(output[col])
        else:
            for colname, col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        
        return output
    def fit_transform(self, X, y=None):
        return self.fit(X, y).transform(X)
    def save(self, fileName):
        """Save thing to a file."""
        f = open(fileName,"wb")
        pickle.dump(self,f)
        f.close()
    def load(fileName):
        """Return a thing loaded from a file."""
        f = open(fileName,"r")
        obj = pickle.load(f)
        f.close()
        return obj
    # make load a static method
    load = staticmethod(load)
    
#if __name__ == "__main__":
    # code for standalone use
#    encoder = MultiColumnLabelEncoder()
    #MultiColumnLabelEncoder.__module__ = "score"
#    encoder.save("encoder.pkl")
