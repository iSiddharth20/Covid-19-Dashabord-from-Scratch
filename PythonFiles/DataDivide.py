#!/usr/bin/python3

# Importing Data into the program
from DataSource import df_final,df_final_sum
from IPython.display import HTML
import pandas as pd

path = '../'

def table_create(data):
	# Converting Data Frame to HTML Code
	converted_str = data.to_html(classes='table table-stripped',index=False)
	converted_str = converted_str[60:-8]
	converted_str = '<table id="example" style="width:100%" class="table table-striped table-bordered"> '+converted_str+' </table>'
	
	# Removing Unnecessary Content
	converted_str = converted_str.replace('\n',' ')
	converted_str = converted_str.replace('<td>','<td align="right">')

	# Returning the Content
	return converted_str

# Saving Full Data to HTML Table Code
data_complete = table_create(df_final)

# Processing Data Frame to Get sum of Columns
df = pd.DataFrame(df_final_sum)
# Saving Summed Data to HTML Table Code
data_sum = table_create(df.T)