from setuptools import setup

setup(
    name='flask-allowedhosts',
    version='1.0.0',
    packages=['flask_allowedhosts'],
    install_requires=[
        'Flask',
    ],
    url='https://github.com/riad-azz/flask-allowedhosts',
    license='MIT',
    author='Riadh Azzoun',
    author_email='riadh.azzoun@hotmail.com',
    description='A Flask extension to limit access to your routes by using allowed hosts.',
)