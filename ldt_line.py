"""
We need a dict where the key is the spec name and the value is the value
And we need another where the key is the cell index and the value is the spec name
"""

class LDTLine:
    def __init__(self, values):
        self.seq = values['seq']
        self.size = values['size']
        self.cls = LineCls(values['class'])
        self.sch = LineSch(values['sch'])
        self.ins_spec = values['ins_spec']
        self.service = values['service']
        self.from_ = values['from']
        self.to = values['to']
        self.dt = values['dt']
        self.dp = values['dp']
        self.phase = values['phase']
        self.ot = values['ot']
        self.op = values['op']



class LineCls:
    def __init__(self, name):
        self.name = name


class LineSch:
    def __init__(self, name):
        self.line = name
        self.wt = 0
