import os
import pathlib
import numpy as np
import pandas as pd
from fredapi import Fred

pathlib.Path("./data").mkdir(parents=True, exist_ok=True)

api_key = os.environ['FRED_API_KEY']

fred = Fred(api_key)
sp500 = fred.get_series('SP500')
sp500.to_csv(f'{os.getcwd()}/data/sp500.csv')
print("Success!")
     
