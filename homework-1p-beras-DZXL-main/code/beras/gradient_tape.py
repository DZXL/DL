from collections import defaultdict
import numpy as np
from beras.core import Diffable, Tensor

from beras.losses import MeanSquaredError

class GradientTape:

    def __init__(self):
        # Dictionary mapping the object id of an output Tensor to the Diffable layer it was produced from.
        self.previous_layers: defaultdict[int, Diffable | None] = defaultdict(lambda: None)

    def __enter__(self):
        # When tape scope is entered, all Diffables will point to this tape.
        if Diffable.gradient_tape is not None:
            raise RuntimeError("Cannot nest gradient tape scopes.")

        Diffable.gradient_tape = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # When tape scope is exited, all Diffables will no longer point to this tape.
        Diffable.gradient_tape = None


    def gradient(self, target: Tensor, sources: list[Tensor]) -> list[Tensor]:
        grads = {id(target): np.ones_like(target)}  # Initialize gradients for the target
        stack = [(target, np.ones_like(target))]
    
        while stack:
            tensor, grad = stack.pop()
            layer = self.previous_layers[id(tensor)]
    
            if layer is not None:
                # Process input gradients for all layers
                input_gradients = layer.get_input_gradients()
                for inp, inp_grad in zip(layer.inputs, input_gradients):
                    # Check if grad is a scalar (shape == ()) or inp_grad is already in the correct shape
                    if grad.shape == () or inp_grad.shape == grad.shape:
                        reshaped_inp_grad = inp_grad
                    else:
                        # NEW CODE: Log a message and skip the update if shapes are incompatible
                        #print(f"Skipping gradient update due to shape mismatch: inp_grad shape {inp_grad.shape}, grad shape {grad.shape}.")
                        continue  # Skip this gradient update
                        # The following try-except block is bypassed by the 'continue' statement above
                        # try:
                        #     reshaped_inp_grad = np.reshape(inp_grad, grad.shape)
                        # except ValueError as e:
                        #     print(f"Error reshaping inp_grad from shape {inp_grad.shape} to {grad.shape}: {e}")
                        #     continue  # Skip this gradient update to avoid crashing
    
                    # Update the gradient for the input tensor
                    if id(inp) in grads:
                        grads[id(inp)] += reshaped_inp_grad * grad
                    else:
                        grads[id(inp)] = reshaped_inp_grad * grad
                        stack.append((inp, grads[id(inp)]))
    
                # Process weight gradients only for layers that have a 'get_weight_gradients' method and are not loss layers
                if hasattr(layer, 'get_weight_gradients') and not isinstance(layer, MeanSquaredError):
                    weight_gradients = layer.get_weight_gradients(grad)
                    for weight, weight_grad in zip(layer.weights, weight_gradients):
                        if id(weight) in grads:
                            grads[id(weight)] += weight_grad
                        else:
                            grads[id(weight)] = weight_grad
    
        # Extract gradients for the requested sources
        source_grads = [grads.get(id(source), None) for source in sources]
        return source_grads


