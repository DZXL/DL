import numpy as np
 
def preprocess_data(features: np.ndarray, labels: np.ndarray, split_percentage: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Splits data into training and testing data

    features: input features to be fed to a model. dimensions [num_samples, input_size]
    labels: labels associated with the input features. dimensions [num_samples,]
    split percentage: a decimal value representing the percentage of the number of samples which should become training samples
    returns: training features, testing features, training labels, testing labels
    """

    assert len(features) == len(labels)
    
    ## TODO: Roadmap 1.


    ##       Split the samples in features and labels into training and testing datasets
    ## HINT: Check out the numpy documentation below for indexing into and reshaping numpy arrays!
    ## [1] Indexing: https://numpy.org/doc/stable/user/basics.indexing.html
    ## [2] Reshaping: https://numpy.org/doc/stable/reference/generated/numpy.reshape.html

    
    n_samples = len(features)
    labels=labels.reshape(n_samples,1)
    n_train = int(n_samples * split_percentage)
    
    indices = np.random.permutation(n_samples)
    train_indices = indices[:n_train]
    test_indices = indices[n_train:]
    
    fe_train = features[train_indices]
    la_train = labels[train_indices]
    
    fe_test = features[test_indices]
    la_test = labels[test_indices]
    
    return fe_train, fe_test, la_train, la_test





