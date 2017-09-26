import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..', '..'))

from unittest import TestCase
from import_data.build import load_data
from data_splitter.build import data_splitter
from fit_reg_model.build import linear_regression

class TestLinear_regression(TestCase):
    def test_linear_regression(self):

        data = load_data('../../data/house_prices_multivariate.csv')
        X, y = data_splitter(data)
        reg_model = linear_regression(X, y)
        self.assertEqual(reg_model.coef_.shape[0], 34)