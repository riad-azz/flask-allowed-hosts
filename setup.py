from setuptools import setup

long_description = open('README.md').read()
long_description_content_type = 'text/markdown'

setup(
    name='flask-allowedhosts',
    version='1.0.1',
    packages=['flask_allowedhosts'],
    install_requires=[
        'Flask',
    ],
    url='https://github.com/riad-azz/flask-allowedhosts',
    license='MIT',
    author='Riadh Azzoun',
    author_email='riadh.azzoun@hotmail.com',
    description='A Flask extension to limit access to your routes by using allowed hosts.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    keywords=["flask", "allowed hosts", "web development", "security"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Security",
        "Operating System :: OS Independent",
    ],
)