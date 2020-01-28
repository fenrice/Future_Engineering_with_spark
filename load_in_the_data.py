'''
Reading in data is the first step to using PySpark for data science! Let's leverage the new industry standard of parquet files!
'''
# Read the file into a dataframe
df = spark.read.parquet('Real_Estate.parq')
# Print columns in dataframe
print(df.columns)
