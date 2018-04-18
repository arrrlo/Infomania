from setuptools import setup

setup(
    name='Infomania',
    description='Get updates about events from various websites',
    version="0.3.0",
    url='https://github.com/arrrlo/infomania',

    author='Ivan Arar',
    author_email='ivan.arar@gmail.com',

    packages=['infomania'],
    install_requires=[
        'beautifulsoup4==4.4.0',
        'requests==2.9.1',
        'click==6.3',
    ],

    entry_points={
        'console_scripts': [
            'infomania=infomania.cli:cli'
        ],
    },
)
