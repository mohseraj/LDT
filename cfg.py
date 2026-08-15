import json

class Config:
    def __init__(self, path: 'cfg.json'):
        self.json = None
        with open(path, 'r') as f:
            self.json = json.load(f)
