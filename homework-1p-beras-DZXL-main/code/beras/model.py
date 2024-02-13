from abc import abstractmethod

from beras.core import Diffable, Tensor
from beras.gradient_tape import GradientTape

class Model(Diffable):
    """
    This class represents a standard beras model. You will subclass this class to make actual Models!

    TODO: Roadmap 6. a)
        - evaluate
    """

    def __init__(self, layers):
        """
        Initialize all trainable parameters and take layers as inputs
        """
        # Initialize all trainable parameters
        self.layers = layers

    @property
    def weights(self) -> list[Tensor]:
        weights = []
        for layer in self.layers:
            weights += layer.weights
        return weights

    def compile(self, optimizer, loss_fn):
        """
        "Compile" the model by taking in the optimizers, loss, and accuracy functions.
        In more optimized DL implementations, this will have more involved processes
        that make the components extremely efficient but very inflexible.
        """
        self.optimizer      = optimizer
        self.compiled_loss  = loss_fn

    def fit(self, x, y, epochs) -> list[Tensor]:
        """
        Trains the model by iterating over the input dataset and feeding input batches
        into the batch_step method with training. At the end, the metrics are returned.
        """
        losses = []
        for e in range(epochs):
            with GradientTape() as tape:
                pred = self.call(x)
                loss = self.compiled_loss(pred, y)
            grads = tape.gradient(loss, self.trainable_variables)
            self.optimizer.apply_gradients(self.trainable_variables, grads)
            losses.append(loss)
            print(f"Epoch {e}: Loss = {loss}")

        return {"loss": losses}


    def evaluate(self, x, y) -> Tensor:
        """
        X is the dataset inputs, Y is the dataset labels.
        Evaluates the model. Should be called on the testing set to evaluate accuracy of 
        the model using the metrics output from the fit method.
        """
        ## TODO: Implement evaluate similarly to fit. Try to match the printing/aggregation logic.
        preds = self.call(x)  # 获取模型的预测结果
        loss = self.compiled_loss(preds, y)  # 计算损失
        return Tensor(loss)
        
    

    @abstractmethod
    def call(self, inputs) -> Tensor:
        """You will implement this in the SequentialModel class in assignment.py"""
        return
