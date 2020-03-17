# my_lambdata/assignment.py (functional approach)

import pandas

def add_state_names(my_def):

    if __name__ == "__main__":

        print("---------------")
        df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
        print(df.head())
        new_df = add_state_names(df)
        print(new_df.head())

        print("---------------")
        df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
        print(df2.head())
        new_df2 = add_state_names(df2)
        print(new_df2.head())