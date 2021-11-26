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

    def _generate_id(self, name: str) -> str:
        """Generate an MD5 hash from string
        """
        ID = hashlib.md5(name.encode('utf-8')).hexdigest()
        return str(ID)


    def log_model(self, model: dict) -> str:
        """Add model data into metadata
        """
        if model.get("name"):
            print(model.get("name"))
            ID = self.generate_ID(model.get("name"))
        else:
            return None

        # Put model data into models dictionary
        self.models[ID] = model
        # Save model dictionary into metadata
        self.metadata["models"] = self.models

        # Save metadata to disk
        self._save_metadata(self.metadata, self._data_filepath)

        return ID



