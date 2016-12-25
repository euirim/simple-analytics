from utils import add_suffix

class GATable(object):
    
    def __init__(self, table_id, api_key, start_date, end_date, metrics):
        self.table_id = table_id
        self.api_key = api_key
        # start and end dates in the format YYYY-MM-DD
        self.start_date = start_date
        self.end_date = end_date
        # comma separated list of analytics metrics (no ga: suffix required)
        self.metrics = add_suffix(metrics, "ga:")
        
        self.dimensions = None
        self.filters = None
        self.sampling_level = None
        self.sort = None
        return
