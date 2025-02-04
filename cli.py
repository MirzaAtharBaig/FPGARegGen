import argparse
from .parser import parse_yaml
from .generator import CodeGenerator

def main():
    parser = argparse.ArgumentParser(description='RegForge: FPGA Interface Code Generator')
    parser.add_argument('input', help='Input YAML specification file')
    parser.add_argument('-o', '--output', default='output', help='Output directory')
    args = parser.parse_args()

    module_name, registers = parse_yaml(args.input)
    generator = CodeGenerator()
    generator.generate(module_name, registers, args.output)
    
    print(f"Generated files in {args.output}")

if __name__ == '__main__':
    main()
