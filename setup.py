from setuptools import setup, find_packages

setup(
    name='randomquote',
    version='0.1',
    description='Get a random quote',
    url='http://github.com/trstringer/python3-random-quote',
    author='Thomas Stringer',
    author_email='github@trstringer.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=['rq=src.main:display_quote']
    )
)
