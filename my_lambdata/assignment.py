# my_lambdata/assignment.py (functional approach)



# State abbreviation -> Full Name and vise versa. FL -> Florida 
# (Handle Washing DC and territories like Puerto Rico, etc)
# take a pandas dataframe that has state abbreviations
# ... and write a function to add corresponding state names

import pandas

def add_state_names(my_df):
    """
    Adds corresponding state names to a data frame

    Param: my_df (pandas.DataFrame) containing a column called "abbrev"
    """
   
    new_df = my_df.copy()   # so we dont overwite original dataframe
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

    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df


if __name__ == "__main__":

    print("---------------")
    df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC", "NV", "FL"]})
    print(df.head())
    new_df = add_state_names(df)
    print(new_df.head())

    print("---------------")
    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA", "AK", "WY"]})
    print(df2.head())
    new_df2 = add_state_names(df2)
    print(new_df2.head())