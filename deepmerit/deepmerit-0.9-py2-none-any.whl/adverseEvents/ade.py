from extract_data import extract
from classify_events import LogReg,RandomFor,SVC,Gauss
import pandas as pd


class execute():
    def __init__(self,path):
        self.path=path
        self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1=extract(path).preprocess()
    
    def Logistic(self):
        print(LogReg(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1).model())
    
    def RandomForest(self):
        print(RandomFor(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1).model())
        
    def SVM(self):
        print(SVC(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1).model())
        
    def Gaussian(self):
        print(Gauss(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1).model())
    