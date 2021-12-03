from metadata import Metadata

# Testing class
metadata = Metadata(load=False)
# metadata.log_model(
#     {
#         "name": "SVM Model",
#         "version": "1.0.0",
#         "path": "./models/",
#         "score": 93.8,
#         "inputs": [0, 0, 0]
#     })

metadata.log_model("RNN Model", version="1.0.0", path="./models/", 
                    score=93.8, inputs= [0, 0, 0])

print(metadata.metadata)