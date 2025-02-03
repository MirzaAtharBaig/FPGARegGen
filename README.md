# FPGARegGen 🔥🧱

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Automate FPGA register mapping and interface code generation with YAML-defined specifications**

---

## 🚀 Why FPGARegGen?

Modern FPGA development requires perfect synchronization between hardware registers and software interfaces. RegForge eliminates manual coding errors by automatically generating:

- **VHDL/Verilog** register map packages
- **C/C++ header files** for firmware
- **Markdown documentation** 
- Bitmask calculations & access control logic

From a single YAML source of truth!

---

## ✨ Features

- **Declarative YAML Specification** - Define registers and fields in human-readable format
- **Multi-Format Output** - Simultaneous VHDL, Verilog, C, and Markdown generation
- **Smart Bitmask Calculation** - Automatic mask/shift computation for bit fields
- **Access Control** - Native support for RO/RW register types
- **Documentation First** - Auto-generated markdown with field descriptions
- **FPGA/ASIC Agnostic** - Works with any HDL workflow

---

## 📦 Installation

```bash
pip install FPGARegGen
