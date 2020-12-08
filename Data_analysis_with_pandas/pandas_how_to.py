import pandas

# Read .csv files with pandas
df1 = pandas.read_csv(r"data\supermarkets.csv")

# Read .json files with pandas
df2 = pandas.read_json(r"data\supermarkets.json")

# Read .xlsx files with pandas
# Implemented a work around using openpyxl due to changes done with newest version of python
df3 = pandas.read_excel(r"data\supermarkets.xlsx", sheet_name=0)

# Read .txt files seperated by commas with pandas
df4 = pandas.read_csv(r"data\supermarkets-commas.txt")

# Read .txt files seperated by other seperators with pandas
df5 = pandas.read_csv(r"data\supermarkets-semi-colons.txt", sep=";")

# Read from a file that does not have a header line
# If the file has no header line, to make sure the table is correct you need to state that the header = None
df6 = pandas.read_csv("data\supermarkets-commas.txt", header=None)
# to set the names of columbs
df6.columns = ["ID", "Address", "City", "State", "County", "Names", "Employee NR"]

#------------------------------------------------------------------------------------------------------------
# Creates a new list
df7 = df6.set_index("ID", drop=False)
# If you asign another columb to serve as index, then unless specified the old column, that served as 
# the index before gets removed from the table
# To prevent that, need to pass argument drop=False (true by default)
df8 = df7.set_index("State", inplace=False, drop=False)

# Filter out specific info/prefrom a select query
# To get info out of the table based on columns
#.loc[range of items(1:3 or a:d), which column you are looking for("State")]
df7.loc[0:, "State"]

# To get info out of the table based on rows/index <- More common
#.iloc[range of rows(0:3 or 1:), which column you are looking for to display(1 or 1:10)]
df7.iloc[1:3, 1]

# Deleting items from table
# Deleteing columbs
# .drop(Name of column to drop("City"), 1(This let's pandas know you are about to drop the columb))
df_drop_col = df7.drop("City", 1)
df_drop_col = df7.drop(df7.columns[1:3], 1) # based on column order of the given table
df_drop_col

# Deleteing rows
# .drop(index of row to drop("City" or 0), 0(This let's pandas know you are about to drop a row))
df_drop_row = df7.drop("USA", 0) # will not work due to the Country column is not the key/index column
df_drop_row = df7.drop(df7.index[1:3], 0) # based on index of the given table
df_drop_row

# Adding columns to the data frame - will update current table permenantly 
# When adding a new column you also need to pass the exact amount of values as the amount of indexes
# in your table -> len(df.index)
df7["Continent"] = ["Asia", "Asia", "Asia", "Asia", "Asia", "Asia"]
# To make it faster can use following
df7["Continent"] = df7.shape[0] * ["North America"]
df7
# When adding a new row, you can use data from another column and concatinate with a constant 
df7["Continent"] = df7["County"] + "," + "North America"
df7

# Adding a new row
# Will swap the rows and columns
df7_t= df7.T
# Then you can add a new column
df7["My Address"] = ["City", "Country", 10, 7, "Shop", "State", "Continent"]
# Then you swap the rows and columns again
df7 = df7_t

# To update an already existing row, the process is the same, except the name of the new column needs
# to be the same as an already existing column
df7_t= df7.T
# Then you can add a new column
df7["3666 21st St"] = ["City", "Country", 10, 7, "Shop", "State", "Continent"]
# Then you swap the rows and columns again
df7 = df7_t