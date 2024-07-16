import torch
from torch import nn


# Build Model
# Create linear regression model class
class LinearRegressionModel(nn.Module):  # <- almost everything in Pytorch
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.rand(1,  # <- start with a random w and try to adjust it to the ideal w
                                               requires_grad=True,  # <- can this parameter be updated via gradient
                                               # descent ?
                                               dtype=torch.float))  # <- Pytorch love the datatype torch.float32

        self.bias = nn.Parameter(torch.rand(1,  # <- start with a random b and try to adjust it to the ideal b
                                            requires_grad=True,  # <- can this parameter be updated via gradient
                                            dtype=torch.float))  # <- Pytorch love the datatype torch.float32

    # Forward method to define the computation in the model
    def forward(self, x: torch.Tensor) -> torch.Tensor:  # <- "x" is the input data
        return self.weights * x + self.bias  # Linear regression formula wx + b
