import pandas

#
df1 = pandas.read_csv(r"data\supermarkets.csv")

#
df2 = pandas.read_json(r"data\supermarkets.json")

#
# Implemented a work around using openpyxl due to changes done with newest version of python
df3 = pandas.read_excel(r"data\supermarkets.xlsx", sheet_name=0)

#
df4 = pandas.read_csv(r"data\supermarkets-commas.txt")

#
df5 = pandas.read_csv(r"data\supermarkets-semi-colons.txt", sep=";")

# If the file has no header line, to make sure the table is correct you need to state that the header = None
df6 = pandas.read_csv("data\supermarkets-commas.txt", header=None)
# to set the names of columbs
df6.columns = ["ID", "Address", "City", "State", "County", "Names", "Employee NR"]

#
df7 = df6.set_index("ID", drop=False)
# If you asign another columb to serve as index, then unless specified the old column, that served as 
# the index before gets removed from the table
# To prevent that, need to pass argument drop=False (true by default)
df8 = df7.set_index("State", inplace=False, drop=False)