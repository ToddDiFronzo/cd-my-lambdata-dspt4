# my_lambdata/assignment.py (OOP approach)



# State abbreviation -> Full Name and vise versa. FL -> Florida 
# (Handle Washing DC and territories like Puerto Rico, etc)
# take a pandas dataframe that has state abbreviations
# ... and write a function to add corresponding state names


import pandas

class DataProcessor():
    def __init__(self, my_df):
        """
        Param: my_df (pandas.DataFrame) containing a column called "abbrev"
        """
        self.df = my_df.copy()

    def add_state_names(self):
        """ Adds corresponding state names to dataframe.

        Param: my_df (pandas.DataFrame) containing a column called "abbrev"
        """
        
        # type(new_df["abbrev"]) #> <class 'pandas.core.series.Series'>
        # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        names_map = {
            "AL": "Alabama",
            "AK": "Alaska",
            "AZ": "Arizona",
            "AR": "Arkanasas",
            "CA": "California",
            "CT": "Connecticut",
            "CO": "Colorado",
            "DC": "Washington D.C.",
            "DE": "Delaware",
            "FL": "Florida",
            "GA": "Georgia",
            "HI": "Hawaii",
            "ID": "Idaho",
            "IL": "Illinois",
            "IN": "Indiana",
            "IA": "Iowa",
            "KS": "Kansas",
            "KY": "Kentucky",
            "LA": "Louisiana",
            "ME": "Maine",
            "MD": "Maryland",
            "MA": "Massachusetts",
            "MI": "Michigan",
            "MN": "Minnesota",
            "MS": "Mississippi",
            "MO": "Missouri",
            "MT": "Montana",
            "NE": "Nebraska",
            "NV": "Nevada",
            "NH": "New Hampshire",
            "NJ": "New Jersey",
            "NM": "New Mexico",
            "NY": "New York",
            "NC": "North Carolina",
            "ND": "North Dakota",
            "OH": "Ohio",
            "OK": "Oklahoma",
            "OR": "Oregon",
            "PA": "Pennsylvania",
            "RI": "Rhode Island",
            "SC": "South Carolina",
            "SD": "South Dakota",
            "TN": "Tennessee",
            "TX": "Texas",
            "UT": "Utah",
            "VT": "Vermont",
            "VA": "Virginia",
            "WA": "Washington",
            "WV": "West Virginia",
            "WI": "Wisconsin",
            "WY": "Wyoming"}

        self_df["name"] = self_df["abbrev"].map(names_map)
        

    if __name__ == "__main__":

        print("---------------")
        df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
        
        processor = DataProcessor(df1)
        print(processor.df.head())

        processor.add_state_names()
        print(processor.df.head())

        #print("---------------")
        #df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
        #print(df2.head())
        #new_df2 = add_state_names(df2)
        #print(new_df2.head())