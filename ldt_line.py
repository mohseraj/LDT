

class LDTLine:
    def __init__(self, values):
        # values = {'seq': '1345', 'size': '4"', ...}
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


def create_line(row) -> LDTLine:

    pass
