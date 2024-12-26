from setuptools import setup, find_packages
setup(
    name='puff-adder', 
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    description='A Python library for signals and observers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Oarabile Koore',
    url='https://github.com/yourusername/puff-adder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)