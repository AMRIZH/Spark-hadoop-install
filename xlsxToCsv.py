import pandas as pd

# Baca file .xlsx
df = pd.read_excel("Online Retail.xlsx", engine="openpyxl")

# Simpan sebagai .csv
df.to_csv("Online Retail.csv", index=False)
