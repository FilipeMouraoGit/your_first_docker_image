import unittest
from docker_application.functions.logic import SimpleAppLogic

class SimpleAppLogicTest(unittest.TestCase):
    def test_clean_input_data_points__simple_run(self):
        data_string = "-1,2;3,-4;5.3,6.1;7,8;9,10"
        expected_x = [-1, 3, 5.3, 7, 9]
        expected_y = [2, -4, 6.1, 8, 10]
        returned_x, returned_y = SimpleAppLogic._clean_input_data_points(data_string)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)

    def test_clean_input_data_points__cleaning_non_numbers_data_points(self):
        data_string = "-1,a;3,-4!;5.3[,6.1x;7..,8;',a;\,1;9,10"
        expected_x = [9]
        expected_y = [10]
        returned_x, returned_y = SimpleAppLogic._clean_input_data_points(data_string)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
    def test_clean_input_data_points__non_tuple_data_points(self):
        data_string = "-1,2,3;-4;5.3,,6.1;7,8,;;9,10;1,2,3,4,5"
        expected_x = [9]
        expected_y = [10]
        returned_x, returned_y = SimpleAppLogic._clean_input_data_points(data_string)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
    def test_fit_input_data(self):
        self.assertTrue(SimpleAppLogic.fit_input_data())