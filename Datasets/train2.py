from ultralytics import YOLO, checks, hub
checks()

hub.login('ade296fbf87fd8c16e83613dbdf8a8ac4341c16c50')

model = YOLO('https://hub.ultralytics.com/models/7wtKn9bQ3pXJ0oN5oeuo')
results = model.train()