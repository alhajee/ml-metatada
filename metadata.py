import os
import hashlib
import joblib

class Metadata:    

    def __init__(self, load=False) -> None:

        # Directory of the raw data files
        self._data_root = './data'
        
        # Make directory if it doesn't exist
        if not os.path.exists(self._data_root):
            os.makedirs(self._data_root)

        # Full path of metadata
        self._data_filepath = os.path.join(self._data_root, "main.metadata")

        self.features = []
        self.schema = []
        self.models = {}
        
        self.metadata = {
            "features": self.features,
            "schema": self.schema,
            "models": self.models
        }
