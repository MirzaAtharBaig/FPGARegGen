from setuptools import setup, find_packages

setup(
    name='FPGARegGen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['PyYAML', 'Jinja2'],
    entry_points={
        'console_scripts': ['FPGARegGen=FPGARegGen.cli:main']
    },
    package_data={
        'FPGARegGen': ['templates/*.j2'],
    },
    include_package_data=True,
)
