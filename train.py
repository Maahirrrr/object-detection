
from hub_sdk import HUBClient

credentials = {"ade296fbf87fd8c16e83613dbdf8a8ac4341c16c50": "ade296fbf87fd8c16e83613dbdf8a8ac4341c16c50"}
client = HUBClient(credentials)

# Select the dataset
dataset = client.dataset("https://hub.ultralytics.com/models/L46gXaIsW1PvLTuJ8uCv")  # Substitute with the real dataset ID

# Upload the dataset file
dataset.upload_dataset(file="https://hub.ultralytics.com/models/L46gXaIsW1PvLTuJ8uC")  # Make sure to specify the correct file path
print("Dataset has been uploaded.")