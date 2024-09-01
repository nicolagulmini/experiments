import torch
import torch.nn as nn
import torch.optim as optim

# Definizione di una rete neurale semplice
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(2, 2)

    def forward(self, x):
        return self.fc1(x)

    def train_and_ev(self, target, x):
    	output = self(x)
    	#print('before training', output)
    	optimizer = optim.SGD(self.parameters(), lr=0.01)
    	loss_fn = nn.MSELoss()
    	optimizer.zero_grad()
    	loss = loss_fn(output, target)
    	loss.backward()
    	optimizer.step()
    	#print('after training', self(x))
    	return self(x)