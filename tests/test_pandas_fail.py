import pandas as pd
import os


def test_pandas_fail():
    data = pd.read_csv(os.path.join(os.path.dirname(__file__),
                       "..", "data", "students.csv"))

    usernames = data["UIDs"]

    assert "LB818" in usernames