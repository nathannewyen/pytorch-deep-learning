import torch
from torch import nn
import matplotib.pyplot as plt

# Check version of PyTorch
torch.__version__

# Create *known* parameters
weight = 0.7
bias = 0.3

# Create
start = 0
end = 1
step = 0.02
x = torch.arange(start, end, step)
y = weight * x + bias

print(x[:10], y[:10])
