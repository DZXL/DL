from sklearn.datasets import load_diabetes
import numpy as np

from preprocess import preprocess_data

def test_preprocess_types():
    X, Y = load_diabetes(return_X_y=True)
    X_train, X_test, Y_train, Y_test = preprocess_data(np.array(X), np.array(Y), 0.8)
    assert type(X_train) is np.ndarray
    assert type(X_test) is np.ndarray
    assert type(Y_train) is np.ndarray
    assert type(Y_test) is np.ndarray
    print("Process types test passed!")

def test_preprocess_shapes():
    X, Y = load_diabetes(return_X_y=True)
    X_train, X_test, Y_train, Y_test = preprocess_data(np.array(X), np.array(Y), 0.8)

    assert X_train.shape == (353, 10)
    assert Y_train.shape == (353, 1)
    assert X_test.shape == (89, 10)
    assert Y_test.shape == (89, 1)
    print("Preprocess shapes test passed!")


if __name__ == '__main__':
    '''
    Uncomment the tests you would like to run for sanity checks throughout the assignment
    '''

    ### Preprocess types test ###
    test_preprocess_types()

    ### Preprocess shapes test ###
    test_preprocess_shapes()
