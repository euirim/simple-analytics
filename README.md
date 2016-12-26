# simple-analytics
A simple python interface for Google's Analytics API (v3)

## Usage Example
```python
>>> gat = GATable(table_id="xxx", start_date="2016-10-3",
        end_date="2016-10-11", metrics="sessions")
>>> gat.initialize("google_api_key_file")
>>> gat.dims("pageTitle").order_by("-sessions").get(3)
[["Title1", 10], ["Title2", 7], ["Title3", 3]]
```
