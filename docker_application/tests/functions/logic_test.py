import unittest
from docker_application.functions.logic import SimpleAppLogic

class SimpleAppLogicTest(unittest.TestCase):
    def test_clean_input_data_points(self):
        self.assertTrue(SimpleAppLogic.clean_input_data_points())
    def test_fit_input_data(self):
        self.assertTrue(SimpleAppLogic.fit_input_data())