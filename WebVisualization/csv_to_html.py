#Convert a CSV file into an HTML file
import pandas as pd

df = pd.read_csv("cities.csv")

df.to_html("cititestable.html")