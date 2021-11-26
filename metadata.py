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

        # Load saved metadata from disk
        if load is True:
            self._load_metadata(self._data_filepath)


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


    def log_model(self, name: str, path: str=None, score:float=None, 
                version: str=None, inputs: list=None) -> str:
        """Add model data into metadata

            Args:
                name - model name
                path - path of model in disk
                score - score of model (Eg. Test-set Accuracy)
                version - version of model
                inputs - Expected format of model input

            Returns:
                ID - unique hash generated for the model
            
            Throws:
                None - if name is not supplied
        """

        if name is not None:
            ID = self._generate_id(name)
            
            model = dict()

            model['name'] = name
            model['version'] = version
            model['path'] = path
            model['score'] = score
            model['inputs'] = inputs

            # Put model data into models dictionary
            self.models[ID] = model
            # Save model dictionary into metadata
            self.metadata["models"] = self.models

            # Save metadata to disk
            self._save_metadata(self.metadata, self._data_filepath)

        else:
            return None
        return ID


    def _save_metadata(self, metadata, path: str) -> None:
        joblib.dump(self.metadata, path)


    def _load_metadata(self, path: str) -> None:
        self.metadata = joblib.load(path)

