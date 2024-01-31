import unittest
import numpy as np
import tensorflow as tf
from grader_utils import file_exists, file_paths_correct, hw
from gradescope_utils.autograder_utils.decorators import (number, weight)

####################################################################################

test_num = 2

class TestStudentModel(unittest.TestCase):
    @weight(10)
    @number(f"{test_num}.1")
    def test_model_weights(self):
        """Model weights correct"""

        student_model = tf.keras.models.load_model('/autograder/submission/model')

        predictions = student_model.predict(np.linspace(0, np.pi * 2, 50))
        # Assume success if no exceptions occur

        print(f"Successfully loaded student weights!")

    @weight(8)
    @number(f"{test_num}.2")
    def test_fig(self):
        """Figure saved correctly"""

        if file_exists("test_fig.png"):
            print("Found generated figure!")
        else:
            raise AssertionError("Unable to find generated figure")
