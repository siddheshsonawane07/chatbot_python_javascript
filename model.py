import torch
import torch.nm as nn

class NeuralNet(nn.Module):
    def __init__(self,input_size,hidden_size,num_classes):
        self.l1 = nn.linear(input_size,hidden_size)
        self.l2 = nn.linear(input_size,hidden_size)
        self.l3 = nn.linear(input_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, X):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.relu(out)

        return out