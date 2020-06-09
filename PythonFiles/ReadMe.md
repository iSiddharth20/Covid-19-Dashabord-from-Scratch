# How does this Work?

* 'DataSource.py' 
	+ Collects data from Ministry of Health and Family Welfare, India.
	+ Cleans the Data and saves it as a CSV File.
	+ Creates a DataFrame which will be shown on the Dashboard as a Table.
	+ Updates 'LastUpdated' string which will be shown on Dashboard.

* 'DataDivide.py' 
	+ Collects DataFrame from 'DataSource.py'.
	+ Converts the DataFrame to HTML Table Code.
	+ Aligns the Table Contents.

* 'Main.py' 
	+ Collects HTML Table Code from 'DataDivide.py'.
	+ Collects 'LastUpdated' from 'DataSource.py'.
	+ Combines all obtained data into Pre-Existing HTML Code in string format.
	+ Creates a Large String which basically is the Entire WebPage.
	+ Exports this String into a file with '.html' extention.