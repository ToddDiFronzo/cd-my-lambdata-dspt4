# setup.py file
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="gangster_granny",
    version="1.0",
    author="Todd DiFronzo",
    author_email="fonze@aol.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/cardstud/cd-my-lambdata-dspt4",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)