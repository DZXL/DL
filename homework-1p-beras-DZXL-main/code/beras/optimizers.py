class BasicOptimizer:
    """
    This class represents a basic optimizer which simply applies the scaled gradients to the weights.

    TODO: Roadmap 5.
        - apply_gradients 
    """
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def apply_gradients(self, weights, grads):
        """
        TODO: given weights and grads, scale and then apply the gradients to (only trainable) weights
        You can assume that grads[i] is the gradient for weights[i]

        weights: the weights in the model we are training
        grads: the gradients ot those weights
        return: None
        """
        for weight, grad in zip(weights, grads):
            # 检查权重是否为可训练的

            # Ensure gradient shape matches parameter shape
            grad2 = grad.reshape(weight.shape)
            if weight.trainable:
            # Perform the update
                weight -= self.learning_rate * grad2
