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

    def test_fit_input_data__degree_1(self):
        data_string = "-2,0;-8,6;5,2;-9,-9;-8,-2;-9,-5;-2,-2;-1,-7;-1,-9;9,-6"
        expected_x = [-2, -8, 5, -9, -8, -9, -2, -1, -1, 9]
        expected_y = [0, 6, 2, -9, -2, -5, -2, -7, -9, -6]
        expected_x_fit = [-12., -9.333, -6.666, -4., -1.333, 1.333, 4., 6.666, 9.333, 12]
        expected_y_fit = [-2.833, -2.937, -3.041, -3.145, -3.249, -3.353, -3.457, -3.561, -3.665, -3.769]
        returned_x, returned_y, returned_x_fit, returned_y_fit = \
            SimpleAppLogic.fit_input_data(data_string, fit_degree=1, n_fit_points=10)
        returned_x_fit, returned_y_fit = list(returned_x_fit), list(returned_y_fit)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
        for i in range(len(expected_x_fit)):
            self.assertAlmostEqual(expected_x_fit[i], returned_x_fit[i], delta=1e-3)
            self.assertAlmostEqual(expected_y_fit[i], returned_y_fit[i], delta=1e-3)

    def test_fit_input_data__degree_1_with_data_clean(self):
        data_string = "-2x,0;-8,6;5,2;-9,-9;-8,-2;-9,-5;-2,-2;-1,-7;-1,-9;9,-6,1"
        expected_x = [-8, 5, -9, -8, -9, -2, -1, -1]
        expected_y = [6, 2, -9, -2, -5, -2, -7, -9]
        expected_x_fit = [-12.0, -9.778, -7.556, -5.333, -3.111, -0.889, 1.333, 3.556, 5.778, 8.0]
        expected_y_fit = [-3.963, -3.762, -3.561, -3.359, -3.158, -2.957, -2.755, -2.554, -2.353, -2.151]
        returned_x, returned_y, returned_x_fit, returned_y_fit = \
            SimpleAppLogic.fit_input_data(data_string, fit_degree=1, n_fit_points=10)
        returned_x_fit, returned_y_fit = list(returned_x_fit), list(returned_y_fit)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
        for i in range(len(expected_x_fit)):
            self.assertAlmostEqual(expected_x_fit[i], returned_x_fit[i], delta=1e-3)
            self.assertAlmostEqual(expected_y_fit[i], returned_y_fit[i], delta=1e-3)
    def test_fit_input_data__degree_2(self):
        data_string = "-2,0;-8,6;5,2;-9,-9;-8,-2;-9,-5;-2,-2;-1,-7;-1,-9;9,-6"
        expected_x = [-2, -8, 5, -9, -8, -9, -2, -1, -1, 9]
        expected_y = [0, 6, 2, -9, -2, -5, -2, -7, -9, -6]
        expected_x_fit = [-12., -9.333, -6.666, -4., -1.333, 1.333, 4., 6.666, 9.333, 12]
        expected_y_fit = [-3.321, -3.132, -3.023, -2.994, -3.044, -3.174, -3.384, -3.674, -4.043, -4.493]
        returned_x, returned_y, returned_x_fit, returned_y_fit = \
            SimpleAppLogic.fit_input_data(data_string, fit_degree=2, n_fit_points=10)
        returned_x_fit, returned_y_fit = list(returned_x_fit), list(returned_y_fit)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
        for i in range(len(expected_x_fit)):
            self.assertAlmostEqual(expected_x_fit[i], returned_x_fit[i], delta=1e-3)
            self.assertAlmostEqual(expected_y_fit[i], returned_y_fit[i], delta=1e-3)

    def test_fit_input_data__degree_3(self):
        data_string = "-2,0;-8,6;5,2;-9,-9;-8,-2;-9,-5;-2,-2;-1,-7;-1,-9;9,-6"
        expected_x = [-2, -8, 5, -9, -8, -9, -2, -1, -1, 9]
        expected_y = [0, 6, 2, -9, -2, -5, -2, -7, -9, -6]
        expected_x_fit = [-12., -9.333, -6.666, -4., -1.333, 1.333, 4., 6.666, 9.333, 12]
        expected_y_fit = [-1.008, -2.762, -3.479, -3.492, -3.133, -2.733, -2.627, -3.146, -4.622, -7.387]
        returned_x, returned_y, returned_x_fit, returned_y_fit = \
            SimpleAppLogic.fit_input_data(data_string, fit_degree=3, n_fit_points=10)
        returned_x_fit, returned_y_fit = list(returned_x_fit), list(returned_y_fit)
        self.assertListEqual(returned_x, expected_x)
        self.assertListEqual(returned_y, expected_y)
        for i in range(len(expected_x_fit)):
            self.assertAlmostEqual(expected_x_fit[i], returned_x_fit[i], delta=1e-3)
            self.assertAlmostEqual(expected_y_fit[i], returned_y_fit[i], delta=1e-3)