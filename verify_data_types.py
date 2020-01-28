'''
In the age of data we have access to more attributes than we ever had before. 
To handle all of them we will build a lot of automation but at a minimum requires that their datatypes be correct.
In this exercise we will validate a dictionary of attributes and their datatypes to see if they are correct.
This dictionary is stored in the variable validation_dict and is available in your workspace.

INSTRUCTIONS
=Using df create a list of attribute and datatype tuples with dtypes called actual_dtypes_list.
=Iterate through actual_dtypes_list, checking if the column names exist in the dictionary of expected dtypes validation_dict.
=For the keys that exist in the dictionary, check their dtypes and print those that match.
'''

# create list of actual dtypes to check
actual_dtypes_list = df.dtypes
print(actual_dtypes_list)

# Iterate through the list of actual dtypes tuples
for attribute_tuple in actual_dtypes_list:
  
  # Check if column name is dictionary of expected dtypes
  col_name = attribute_tuple[0]
  if col_name in validation_dict:

    # Compare attribute types
    col_type = attribute_tuple[1]
    if col_type == validation_dict[col_name]:
      print(col_name + ' has expected dtype.')
