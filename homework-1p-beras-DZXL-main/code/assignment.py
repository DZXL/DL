from types import SimpleNamespace

import beras
import numpy as np


class SingleLayerModel(beras.Model):
    """
    Implemented in beras/model.py

    def __init__(self, layers):
    def compile(self, optimizer, loss_fn, acc_fn):
    def fit(self, x, y, epochs, batch_size):
    (TODO) def evaluate(self, x, y, batch_size):
    """

    def __init__(self, single_layer):
        self.layer = single_layer

    @property
    def weights(self) -> list[beras.Tensor]:
        return self.layer.weights

    def call(self, inputs: beras.Tensor) -> beras.Tensor:
        """Forward pass in single layer model. It's helpful to note that the layer is initialized above, and
        you can refer to it with self.layer. You can call a layer by doing var = layer(input)."""
        ## TODO: Roadmap 6. b)
        ##       What does it mean to call the model?
        ## HINT: Check out the Callable class in core_cheat_sheet.md
        return self.layer(inputs)

    def get_input_gradients(self) -> list[beras.Tensor]:
        return super().get_input_gradients()

    def get_weight_gradients(self) -> list[beras.Tensor]:
        return super().get_weight_gradients()


def get_single_layer_model_components():
    """ TODO
    Returns a simple single-layer model. 

    :return: A SimpleNamespace with accessible fields containing model and epochs
    """

    from beras.layers import Dense
    from beras.losses import MeanSquaredError
    from beras.optimizers import BasicOptimizer

    ## TODO: Roadmap 6
    ##       Initalize the model!
    ## HINT: Check out the imports
    single_layer = Dense(input_size=10, output_size=1, initializer="normal")
    model = SingleLayerModel(single_layer)

    model.compile(
        optimizer = BasicOptimizer(learning_rate=0.5),  ## TODO: Initalize an optimizer.
        loss_fn= MeanSquaredError()
    ## TODO: Initialize a Loss function
    )
    return SimpleNamespace(model=model, epochs=200) ##TODO Pick a nubmer of epochs!


if __name__ == "__main__":
    """
    Read in Diabetes data, initialize your model, and train and test your model.
    """
    from preprocess import preprocess_data
    from sklearn.datasets import load_diabetes

    X, Y = load_diabetes(return_X_y=True)

    train_inputs, test_inputs, train_labels, test_labels = preprocess_data(np.array(X), np.array(Y), 0.8)

    args = get_single_layer_model_components()

    train_losses = args.model.fit(
        train_inputs,
        train_labels,
        epochs=args.epochs,
    )

    test_losses = args.model.evaluate(
        test_inputs,
        test_labels,
    )

    # from visualize import visualize_metrics
    # visualize_metrics(train_losses, title="Training Losses over Epochs")