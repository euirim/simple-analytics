# simple-analytics
A simple python interface for Google's Analytics Reports API (v3).

## About
Using Google Analytics Reports API (v3) to read analytics data can be hard to setup on python. simple-analytics provides a very simple interface, inspired by Django's ORM, to easily interact with this api, making queries of simple and moderate complexity a breeze. 

### Usage Example
```python
>>> gat = GATable(table_id="xxx", start_date="2016-10-3",
        end_date="2016-10-11", metrics="sessions")

>>> gat.initialize("google_api_key_file")

>>> gat.set_dims("pageTitle").order_by("-sessions").get(3)

[["Title1", 10], ["Title2", 7], ["Title3", 3]]
```
