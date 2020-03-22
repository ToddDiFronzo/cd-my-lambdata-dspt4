# test/assignment_test.py

import unittest

from my_lambdata.assignment4 import CustomFrame



def test_add_state_names():
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    assert "name" not in list(custom_df.columns)

    custom_df.add_state_names()
    assert "name" in list(custom_df.columns)

    assert custom_df["abbrev"][0] == "CA"
    assert custom_df["name"][0] == "California"
