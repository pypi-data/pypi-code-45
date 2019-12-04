from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

class extract:
    def __init__(self,path):
        self.path=path
    def preprocess(self):
        df=pd.read_csv('github_class_data.csv')
        X=df.drop(columns=['side_effect','Unnamed: 0'],axis=1)
        Y=df['side_effect']
        Y=Y.apply(lambda x: x.strip('[]').replace("'","").split(', '))
        #print(Y)
        X.fillna(X.mean(), inplace=True)
        mlb = MultiLabelBinarizer()
        y=mlb.fit_transform(Y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
        return X_train, X_test, y_train, y_test,mlb
        