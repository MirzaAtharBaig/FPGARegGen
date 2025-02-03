# FPGARegGen 🔥🧱

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Automate FPGA register mapping and interface code generation with YAML-defined specifications**

![FPGARegGen Workflow](https://raw.githubusercontent.com/yourusername/FPGARegGen/main/docs/workflow.png)

## 🚀 Why FPGARegGen?

Modern FPGA development requires perfect synchronization between hardware registers and software interfaces. FPGARegGen eliminates manual coding errors by automatically generating:

- **VHDL/Verilog** register map packages
- **C/C++ header files** for firmware
- **Markdown documentation** 
- Bitmask calculations & access control logic

From a single YAML source of truth!

## ✨ Features

- **Declarative YAML Specification** - Define registers and fields in human-readable format
- **Multi-Format Output** - Generate VHDL, Verilog, C, and Markdown simultaneously
- **Smart Bitmask Calculation** - Automatic mask/shift computation for bit fields
- **Access Control** - Native support for RO/RW register types
- **Documentation First** - Auto-generated markdown with field descriptions
- **FPGA/ASIC Agnostic** - Works with any HDL workflow

## 📦 Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/FPGARegGen.git
cd FPGARegGen
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

**Requirements:**
- Python 3.8+
- PyYAML
- Jinja2

## 🛠 Usage

1. Create register specification (`registers.yaml`):
```yaml
module: PWM_CONTROLLER
registers:
  - name: CONFIG
    offset: 0x00
    access: RW
    fields:
      - name: ENABLE
        bits: "0"
        default: 0x0
        description: PWM Enable bit
        
      - name: PRESCALER
        bits: "7:4"
        default: 0xF
        description: Clock divider setting
```

2. Generate interface files:
```bash
python FPGARegGen.py registers.yaml -o generated/
```

## 📂 Output Structure
```
generated/
├── PWM_CONTROLLER_regs.vhd      # VHDL package
├── PWM_CONTROLLER_regs.v        # Verilog module
├── PWM_CONTROLLER_regs.h        # C header
└── PWM_CONTROLLER_regs.md       # Documentation
```

## 🎯 Key Generated Artifacts
| File Type          | Contains                                  | Use Case                |
|---------------------|-------------------------------------------|-------------------------|
| `.vhd`/`.v`        | Register addresses, masks, access types  | FPGA Implementation     |
| `.h`               | Base addresses, bit positions            | Firmware Development    |
| `.md`              | Register field descriptions              | Design Documentation    |


## 🤝 Contributing
Contributions welcome! Please follow our guidelines:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License
Distributed under MIT License. See `LICENSE` for more information.

## 📬 Contact
Maintainer: [Mirza Athar Baig](https://www.linkedin.com/in/mirza-athar-baig/)

Project Link: [https://github.com/yourusername/FPGARegGen](https://github.com/yourusername/FPGARegGen)
