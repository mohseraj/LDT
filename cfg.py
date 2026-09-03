import json

class Config:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, path='cfg.json'):
        self.json = None
        with open(path, 'r') as f:
            self.json = json.load(f)

        self.col_letter_map = self.json['specname_colletter']
        self.colx_map = self.json['specname_colx']
        self.core_specs = self.json['core_specs']


shared = Config()