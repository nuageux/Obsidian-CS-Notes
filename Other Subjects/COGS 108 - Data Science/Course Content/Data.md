Data Structures Review
- Structured Data
	- Can be stored in database SQL
	- tables with rows and columns
	- requires a relational key
	- 5-10% of all data
- Semi-Structured Data
	- not in a relational database but has organizational properties
	- CSV, XML, JSON
- Unstructured Data
	- non-tabular data
	- 80% of the world's data
	- images, text, audio, videos

Python Webscraping
- Use "BeautifulSoup" tool

Tidy Data
- formatting "untidy" data so it works with most actual databases
	- also allows datasets to be combined
- "data wrangling"
- must be nothing missing
	- repeat values if the original data just uses one cell for multiple rows/column
- one table for each type of data
- if multiple tables, must have a primary key to relate them
- NOT the same as **clean** data.
	- "clean data" refers to correctly marking data, like accidentally swapping day and month formats in the same date column.

# Data Intuition
- Fermi Estimation
- "Wisdom of the Crowds"
	- The average person's guess is usually true, given independence of the collected responses.
	- Diversity of opinion
	- Decentralization: people are able to specialize and draw on local knowledge
	- Aggregation: some mechanism exists for turning private judgments into a collective decision
- Covering Python's pandas package (panel data... i guess...)
	- DataFrame objects
		- each column of which contains a pandas Series object
- 