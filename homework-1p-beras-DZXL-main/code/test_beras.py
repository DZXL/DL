import numpy as np
import tensorflow as tf
import beras

from sklearn.metrics import mean_squared_error
from preprocess import preprocess_data


def test_dense_forward():
    # init both
    student_dense = beras.layers.Dense(3, 3)
    tf_dense = tf.keras.layers.Dense(3)

    # tf call
    dummy_data = np.ones((2, 3))  # Change to random data?
    tf_out = tf_dense(dummy_data, training=False)

    # pull weights
    student_dense.w, student_dense.b = [
        beras.core.Variable(tf_var.numpy()) for tf_var in tf_dense.weights
    ]

    # student call
    student_out = student_dense(dummy_data)

    assert np.allclose(tf_out.numpy(), student_out)
    print("Dense forward test passed!")


def test_dense_input_gradients():
    input_data = tf.Variable(tf.ones((1, 3)))
    tf_dense = tf.keras.layers.Dense(1)

    with tf.GradientTape() as tape:
        out = tf_dense(input_data)
    tf_grad = tape.gradient(out, input_data)

    student_dense = beras.layers.Dense(3, 1)
    student_dense.w, student_dense.b = [
        beras.core.Variable(tf_var.numpy()) for tf_var in tf_dense.weights
    ]

    _ = student_dense(np.ones((1, 3)))

    assert np.allclose(
        tf_grad.numpy(), student_dense.get_input_gradients()[0].transpose()
    )
    print("Dense input gradients test passed!")


def test_mse_forward():
    beras_mse = beras.MeanSquaredError()

    x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
    y = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

    # assert np.allclose(tensorflow_mse(x, y).numpy(), beras_mse(x, y))
    assert np.allclose(mean_squared_error(x, y), beras_mse(x, y))

    x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
    y = np.array([[3, 2, 1], [6, 5, 4]], dtype=np.float32)

    # assert np.allclose(tensorflow_mse(x, y).numpy(), beras_mse(x, y))
    assert np.allclose(mean_squared_error(x, y), beras_mse(x, y))
    print("MSE forward test passed!")


if __name__ == "__main__":
    """
    Uncomment the tests you would like to run for sanity checks throughout the assignment
    """

    ### Dense Forward Pass Test ###
    test_dense_forward()

    ### Dense Input Gradients Test ###
    test_dense_input_gradients()

    ### MSE Forward Pass Test ###
    test_mse_forward()
