import glob
import os
import unittest

from grader_utils import file_exists, file_paths_correct, hw
from gradescope_utils.autograder_utils.decorators import number, weight, partial_credit

test_num = 1


class TestFilePaths(unittest.TestCase):
    @weight(1)
    @number(f"{test_num}.1")
    def test_file_paths(self):
        """Are File Paths Correct?"""

        error_msg = (
            "\nFile paths are not correct\n"
            "\t- Please check that are files are of the form code/something.py\n"
            "\t- Ex: code/assignment.py"
        )
        try:
            os.chdir(f"/autograder/submission/code")
            if not file_paths_correct(glob.glob("*.py")):
                raise AssertionError(error_msg)
        except:
            raise AssertionError(error_msg)


class TestCheckREADME(unittest.TestCase):
    @weight(1)
    @number(f"{test_num}.2")
    def test_contains_README(self):
        """README.md Exists"""
        found, found_files = file_exists("README.md", True)
        if not found:
            raise AssertionError("Submission must contain a README.md TEST")