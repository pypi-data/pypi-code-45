import sys
sys.path.append("src/model")
from train import train_audio_set

import torch
from torch.autograd import Variable

def test(dnn, testLoader):
    correct = 0
    total = 0
    for data in testLoader:
        labels = Variable(data[:,0])
        data = Variable(data[:,1:].float())
        outputs = dnn(data)
        predicted = torch.argmax(outputs.data, 1)
        total = labels.size(0)
        correct = (predicted == labels.long()).sum()
    
    accuracy = 100 * correct / total
    print(f'Accuracy of the network on the data: {accuracy}%')
    return accuracy

if __name__ == '__main__':
    MIN_ACCURACY = 70
    for data_set in [
        "FreeSound"
    ]:
        dnn, testLoader = train_audio_set(FILE_NAME=f"{data_set}_TEST")
        accuracy = test(dnn, testLoader)
        assert accuracy >= MIN_ACCURACY