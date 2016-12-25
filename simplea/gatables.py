class GATable(object):
    
    # start and end dates in the format YYYY-MM-DD
    def __init__(self, table_id, api_key, start_date, end_date, metrics):
        self.table_id = table_id
        self.api_key = api_key
        self.start_date = start_date
        self.end_date = end_date
        # comma separated list of analytics metrics (no ga: suffix required)
        self.metrics = metrics 
        return
