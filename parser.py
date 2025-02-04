import yaml
from .models import Register, Field

def parse_yaml(file_path):
    with open(file_path) as f:
        spec = yaml.safe_load(f)
    
    module_name = spec.get('module', 'FPGA_MODULE')
    registers = []
    
    for reg in spec['registers']:
        fields = [Field(
            name=f['name'],
            bits=f['bits'],
            default=f['default'],
            description=f.get('description', '')
        ) for f in reg['fields']]
        
        registers.append(Register(
            name=reg['name'],
            offset=reg['offset'],
            access=reg['access'],
            fields=fields
        ))
    
    return module_name, registers
