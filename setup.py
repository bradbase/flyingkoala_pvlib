"""

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flyingkoala_pvlib",
    version="0.0.1b0",
    author="Bradley van Ree",
    author_email="flyingkoala@bradbase.net",
    description="A library which supplies FlyingKoala with the capability to interface the Photovotaic calculation library PVLib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['xls',
        'excel',
        'spreadsheet',
        'workbook',
        'vba',
        'macro',
        'data analysis',
        'analysis'
        'reading excel',
        'excel formula',
        'excel formulas',
        'excel equations',
        'excel equation',
        'formula',
        'formulas',
        'equation',
        'equations',
        'pandas',
        'timeseries',
        'time series',
        'energy',
        'research',
        'visualization',
        'scenario analysis',
        'modelling',
        'model',
        'unit testing',
        'testing',
        'audit'],
    url="https://github.com/bradbase/flyingkoala_pvlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
    install_requires=[
            'FlyingKoala >= 0.0.9b0',
            'pvlib >= 0.7.2'
        ]
)
