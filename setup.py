from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='historical_timelines',
    version='0.2.1',
    description='A Python package for making historical timelines',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='darthbeep',
    author_email='darthbeep@gmail.com',
    packages=['historical_timelines'],
    install_requires=[
        'bokeh',
    ],
)
