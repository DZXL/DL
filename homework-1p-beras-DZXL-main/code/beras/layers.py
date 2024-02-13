import numpy as np

from typing import Literal
from beras.core import Diffable, Variable, Tensor

DENSE_INITIALIZERS = Literal["zero", "normal", "xavier", "kaiming", "xavier uniform", "kaiming uniform"]

class Dense(Diffable):
    """
    This class represents a Dense (or Fully Connected) layer.

    TODO: Roadmap 2.
        - weights
        - call
        - get_input_gradients
        - get_weight_gradients
        - _initialize_weights
    """

    def __init__(self, input_size, output_size, initializer: DENSE_INITIALIZERS = "normal"):
        self.w, self.b = self._initialize_weight(initializer, input_size, output_size)

    @property
    def weights(self) -> list[Tensor]:
        return [self.w, self.b]
        
    def call(self, x: Tensor) -> Tensor:
        self.x=x
        predict_y=x@self.w+self.b
        return Tensor(predict_y)

    def get_input_gradients(self) -> list[Tensor]:
        """
        TODO: Return the gradient of this layer with respect to its input, as a list
        You should have as many gradients as inputs (just one)

        returns: a list of gradients in the same order as its inputs
        """
        return [self.w]
        
    

    def get_weight_gradients(self,dout) -> list[Tensor]:
        """
        TODO: Return the gradients of this layer with respect to its weights (and biases).
        Hint: you might notice one of our gradients involves the input. Check out the core_cheat_sheet.md for some tips on how to get access to those values!
        Hint: work through the math on a piece of paper first! You might find it helpful if you do the calculation with respect to a single input.

        returns: a list of gradients (returned in the same order as self.weights())
        """
        dw = self.x.T @dout
        db = np.sum(dout, axis=0,keepdims=True)
        return [Tensor(dw), Tensor(db)]

    @staticmethod
    def _initialize_weight(initializer, input_size, output_size) -> tuple[Variable, Variable]:
        """
        TODO: return the initialized weight, bias Variables as according to the initializer.

        initializer: string representing which initializer to use. see below for details
        input_size: size of latent dimension of input
        output_size: size of latent dimension of output
        returns: weight, bias as **Variable**s.

        Initializes the values of the weights and biases. The bias weights should always start at zero.
        However, the weights should follow the given distribution defined by the initializer parameter
        (zero, normal, xavier, or kaiming). You can do this with an if statement
        cycling through each option!

        Details on each weight initialization option:
            - Zero: Weights and biases contain only 0's. Generally a bad idea since the gradient update
            will be the same for each weight so all weights will have the same values.
            - Normal: Weights are initialized according to a normal distribution.
            - Xavier: Goal is to initialize the weights so that the variance of the activations are the
            same across every layer. This helps to prevent exploding or vanishing gradients. Typically
            works better for layers with tanh or sigmoid activation.
            - Kaiming: Similar purpose as Xavier initialization. Typically works better for layers
            with ReLU activation.
        """

        initializer = initializer.lower()
        assert initializer in (
            "zero",
            "normal",
            "xavier",
            "kaiming",
            "xavier uniform",
            "kaiming uniform",
        ), f"Unknown dense weight initialization strategy '{initializer}' requested"

        io_size = (input_size, output_size)
        # HINT: self.w and self.b are both 2-dimensional tensors
        bias=np.zeros(output_size)
        if initializer=="zero":
            weights=np.zeros(io_size)
        elif initializer=="normal":
            weights=np.random.normal(0,1,io_size)
        elif initializer=="xavier":
            std = np.sqrt(2 / (input_size + output_size))
            weights=np.random.normal(0,std,io_size)
        elif initializer=="kaiming":
            std = np.sqrt(2 / input_size)
            weights=np.random.normal(0,std,io_size)
     
        return Variable(weights),Variable(bias)
