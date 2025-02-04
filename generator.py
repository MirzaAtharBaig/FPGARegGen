import os
from jinja2 import Environment, FileSystemLoader
from importlib.resources import files

class CodeGenerator:
    TEMPLATES = {
        'vhdl': ('vhdl.j2', '_regs.vhd'),
        'verilog': ('verilog.j2', '_regs.v'),
        'c_header': ('c_header.j2', '_regs.h'),
        'markdown': ('markdown.j2', '_regs.md')
    }

    def __init__(self):
        template_dir = files('regforge.templates')
        self.env = Environment(loader=FileSystemLoader(template_dir),
                             trim_blocks=True,
                             lstrip_blocks=True)

    def generate(self, module_name, registers, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
        for tpl_type, (tpl_file, suffix) in self.TEMPLATES.items():
            template = self.env.get_template(tpl_file)
            content = template.render(
                module=module_name,
                registers=registers
            )
            filename = f"{module_name}{suffix}"
            output_path = os.path.join(output_dir, filename)
            
            with open(output_path, 'w') as f:
                f.write(content)
