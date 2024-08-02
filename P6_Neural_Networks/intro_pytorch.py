import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

# Feel free to import other packages, if needed.
# As long as they are supported by CSL machines.


def get_data_loader(training = True):
    """
    TODO: implement this function.

    INPUT: 
        An optional boolean argument (default value is True for training dataset)

    RETURNS:
        Dataloader for the training set (if training = True) or the test set (if training = False)
    """
    transform=transforms.Compose([
         transforms.ToTensor(),
         transforms.Normalize((0.1307,), (0.3081,))
         ])
    train_set = datasets.FashionMNIST('./data', train=True, download=True,transform = transform)
    test_set = datasets.FashionMNIST('./data', train=False, transform = transform)
    if(training==True):
        loader = torch.utils.data.DataLoader(train_set, shuffle=True, batch_size = 64)
    else:
        loader = torch.utils.data.DataLoader(test_set, shuffle=False, batch_size = 64)
    return loader



def build_model():
    """
    TODO: implement this function.

    INPUT: 
        None

    RETURNS:
        An untrained neural network model
    """
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28*28, 128),
        nn.ReLU(),
        nn.Linear(128, 64),
		nn.ReLU(),
		nn.Linear(64, 10)
        )
    return model

def train_model(model, train_loader, criterion, T):
    """
    TODO: implement this function.

    INPUT: 
        model - the model produced by the previous function
        train_loader  - the train DataLoader produced by the first function
        criterion   - cross-entropy 
        T - number of epochs for training

    RETURNS:
        None
    """
    opt = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    model.train()
    
    for i in range(T):
        running_loss = 0.0
        correct = 0
        total = 0
        for j, data in enumerate(train_loader, 0):
            opt.zero_grad()
            inputs, labels = data
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            opt.step()
            running_loss += loss.item()*train_loader.batch_size
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        print(f'Train Epoch: {i} Accuracy: {correct}/{total}'
                + f'({100 * correct / total:.2f}%) Loss: {running_loss/total:.3f}')
		

def evaluate_model(model, test_loader, criterion, show_loss = True):
    """
    TODO: implement this function.

    INPUT: 
        model - the the trained model produced by the previous function
        test_loader    - the test DataLoader
        criterion   - cropy-entropy 

    RETURNS:
        None
    """
    model.eval()
    correct = 0
    total = 0
    running_loss = 0.0
    with torch.no_grad():  
        for data, labels in test_loader:
            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            loss = criterion(outputs, labels)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            running_loss += loss.item()*labels.size(0)
		
    if show_loss==True:
        print(f'Average loss: {running_loss/total:.4f}')
        print(f'Accuracy: {correct*100/total:.2f}%')
    else:
        print(f'Accuracy: {correct*100/total:.2f}%')

    


def predict_label(model, test_images, index):
    """
    TODO: implement this function.

    INPUT: 
        model - the trained model
        test_images   -  a tensor. test image set of shape Nx1x28x28
        index   -  specific index  i of the image to be tested: 0 <= i <= N - 1


    RETURNS:
        None
    """
    instance = test_images[index]
    logits = model(instance)

    class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt'
                   ,'Sneaker','Bag','Ankle Boot']
    prob = F.softmax(logits, dim=1)
    sorted,ind = torch.sort(prob, dim=1)
    for i in range(3):
        print(f'{class_names[int(ind[0][9-i])]}: {float(sorted[0][9-i])*100:.2f}%')

