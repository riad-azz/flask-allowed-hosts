from setuptools import setup

long_description = open('README.md').read()
long_description_content_type = 'text/markdown'

setup(
    name='flask-allowed-hosts',
    version='1.1.0',
    packages=['flask_allowed_hosts'],
    install_requires=[
        'Flask',
    ],
    url='https://github.com/riad-azz/flask-allowed-hosts',
    license='MIT',
    author='Riadh Azzoun',
    author_email='riadh.azzoun@hotmail.com',
    description='A Flask extension to limit access to your routes by using allowed hostnames and IP addresses.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    keywords=["flask", "allowed hosts", "web development", "security", "flask extension", "ip validation",
              "host validation", "hostnames validation"],
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
