class Field:
    def __init__(self, name, bits, default, description):
        self.name = name
        self.bits = bits
        self.default = default
        self.description = description

        if ':' in bits:
            high, low = map(int, bits.split(':'))
        else:
            high = low = int(bits)
            
        self.high = high
        self.low = low
        self.width = high - low + 1
        self.mask = ((1 << self.width) - 1) << low
        self.shift = low

class Register:
    def __init__(self, name, offset, access, fields):
        self.name = name
        self.offset = offset
        self.access = access
        self.fields = fields
