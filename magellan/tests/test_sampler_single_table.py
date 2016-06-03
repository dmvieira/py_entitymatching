# coding=utf-8
import os
from nose.tools import *
import unittest
import pandas as pd
import six

from magellan.utils.generic_helper import get_install_path
import magellan.catalog.catalog_manager as cm
from magellan.io.parsers import read_csv_metadata
from magellan.sampler.single_table import sample_table

datasets_path = os.sep.join([get_install_path(), 'datasets', 'test_datasets'])
path_a = os.sep.join([datasets_path, 'A.csv'])
path_b = os.sep.join([datasets_path, 'B.csv'])
path_c = os.sep.join([datasets_path, 'C.csv'])

class SamplerSingleTableTestCases(unittest.TestCase):
    def test_sample_table_valid_1(self):
        A = read_csv_metadata(path_a)
        B = read_csv_metadata(path_b, key='ID')
        C = read_csv_metadata(path_c, ltable=A, rtable=B)
        D = sample_table(C, 10, False)
        self.assertEqual(cm.get_all_properties(C), cm.get_all_properties(D))
        self.assertEqual(len(D), 10)

    def test_sample_table_valid_2(self):
        A = read_csv_metadata(path_a)
        B = read_csv_metadata(path_b, key='ID')
        C = read_csv_metadata(path_c, ltable=A, rtable=B)
        D = sample_table(C, 10, True)
        self.assertEqual(cm.get_all_properties(C), cm.get_all_properties(D))
        self.assertEqual(len(D), 10)

    @raises(AssertionError)
    def test_sample_table_invalid_df(self):
        A = read_csv_metadata(path_a)
        B = read_csv_metadata(path_b, key='ID')
        C = read_csv_metadata(path_c, ltable=A, rtable=B)
        D = sample_table(None, 10, True)
        # self.assertEqual(cm.get_all_properties(C), cm.get_all_properties(D))
        # self.assertEqual(len(D), 10)

    @raises(AssertionError)
    def test_sample_table_invalid_size(self):
        A = read_csv_metadata(path_a)
        B = read_csv_metadata(path_b, key='ID')
        C = read_csv_metadata(path_c, ltable=A, rtable=B)
        D = sample_table(C, len(C)+1, True)

    @raises(AssertionError)
    def test_sample_table_invalid_df_sz0(self):
        # A = read_csv_metadata(path_a)
        # B = read_csv_metadata(path_b, key='ID')
        # C = read_csv_metadata(path_c, ltable=A, rtable=B)
        D = sample_table(pd.DataFrame(), 1, True)