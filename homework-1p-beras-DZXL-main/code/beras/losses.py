import numpy as np

from beras.core import Diffable, Tensor


class MeanSquaredError(Diffable):
    """
    This class represents a loss layer which performs Mean Squared Error

    TODO: Roadmap 3.
        - call
        - input gradients
    """

    def call(self, y_pred: Tensor, y_true: Tensor) -> Tensor:
        """
        TODO: Find the Mean Squared Error of y_pred and y_true

        y_pred: the predicted labels
        y_true: the true labels
        returns: the MeanSquaredError as a Tensor
        """
        self.y_pred = y_pred
        self.y_true = y_true
        mse=np.mean((y_true-y_pred)**2)
        return Tensor(mse)

    def get_input_gradients(self) -> list[Tensor]:
        """
        TODO: Return the gradients of the layer in the same order as the inputs of call
        i.e. return the gradient of the layer w.r.t y_pred, the gradient of the layer w.r.t. y_true

        returns: a list of input gradients in the same order as the input arguments of the call function.
        HINT: What would the gradients be with respect to a scalar?
        """
        dy_pred=2/len(self.y_pred)*(self.y_pred - self.y_true)
        
        
        return [Tensor(dy_pred)]

    def get_weight_gradients(self) -> list[Tensor]:
        return []

    def weights(self) -> list[Tensor]:
        return []
