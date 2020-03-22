# my_lambdata/assignment.py (OOP approach w/ inheritance)
import pandas
class CustomFrame(pandas.DataFrame):
    """
    Param: my_df (pandas.DataFrame) containing a column called "abbrev"
    """
    def add_state_names(self):
        """
        Adds corresponding state names to a dataframe.
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
        self["name"] = self["abbrev"].map(names_map)
if __name__ == "__main__":
    print("--------------")

    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(custom_df.head())
    custom_df.add_state_names()
    print(custom_df.head())
    