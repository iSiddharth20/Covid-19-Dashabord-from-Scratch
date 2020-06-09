# Covid-19 Dashabord from Scratch
Covid-19 Dashboard for India without using any API. 
Website is created from Scratch using Basic Concepts of Python.

* Live Version : [Click Here](https://covid19dashboard.social/)

# How to Use the Code

* Python-3 is Must.
* Use the 'requirements.txt' to install all necessary Packages.
* Run 'Main.py' from the 'PythonFiles' folder.

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