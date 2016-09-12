from setuptools import setup

setup(
    name='purgedirs',
    version='0.0.1',
    py_modules=['purgedirs'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    purgedirs=purgedirs:cli
    ''')
