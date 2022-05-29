import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv("cars_details_2022.csv")
print(df)
Profile=ProfileReport(df)
Profile.to_file(output_file="cars_details_2022.html")
