from utils import add_suffix

class GATable(object):
    
    def __init__(self, table_id, api_key, 
            start_date, end_date, metrics, sampling_level="FASTER"):
        self.table_id = table_id
        self.api_key = api_key
        # start and end dates in the format YYYY-MM-DD
        self.start_date = start_date
        self.end_date = end_date
        # comma separated list of analytics metrics (no ga: suffix required)
        self.metrics = add_suffix(metrics, "ga:")
        
        self.dims = None # dimensions
        self.filters = None
        self.sampling_level = sampling_level
        self.sort = None
        return

    def adjust_dates(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        return

    def filter(self, filters):
        # if existing filters exists, append
        if self.filters is not None:
            self.filters += "," + add_suffix(filters, "ga:")
        else:
            self.filters = add_suffix(filters, "ga:")
        return

    def dims(self, dims):
        """set dimensions (dims short for dimensions)."""
        if self.dims is not None:
            self.dims += "," + add_suffix(dims, "ga:")
        else:
            self.dims = add_suffix(dims, "ga:")
        return

    def order_by(self, sort):
        if self.sort not None:
            self.sort += "," + add_suffix(sort, "ga:")
        else:
            self.sort = add_suffix(sort, "ga:")
        return

    def get_url(self, max_results):
        return 

    def get_response(self, max_results):
        return

    def get(self, max_results):
        return
