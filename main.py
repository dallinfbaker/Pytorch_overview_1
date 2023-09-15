import torch
from network import BasicNeuralNetwork
from trainer import train

def main():
    
    model = BasicNeuralNetwork()
    
    model = train(model)
    torch.save(model.state_dict(), 'tripleAddModel.pt')
    
    x = [3,5,7]
    print(f'\n\nAdding these numbers together: {x}')
    x = torch.Tensor(x)
    result = model(x).item()
    print(f'Model result: {result}')

    # You can load the model with this code 
    #   if you want to evaluate things with it (model.eval())
    # model.load_state_dict(torch.load('tripleAddModel.pt'))

main()
    