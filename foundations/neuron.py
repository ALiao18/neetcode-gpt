import numpy as np
from numpy.typing import NDArray


class Solution:
    def forward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, activation: str) -> float:
        # x: 1D input array
        # w: 1D weight array (same length as x)
        # b: scalar bias
        # activation: "sigmoid" or "relu"
        #
        def sigmoid(z):
            return 1/(1+np.exp(-z))
        
        def ReLU(z):
            return max(0.0, z)
        # Pre-activation: z = dot(x, w) + b

        z = np.dot(x, w)+b
        
        if activation == "sigmoid":
            answer = sigmoid(z)
        elif activation == "relu":
            answer = ReLU(z)
        
        return round(answer, 5)
