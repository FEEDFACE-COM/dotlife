from setuptools import setup

from dotlife import about

setup(
    name=about.NAME,
    version=about.VERSION,
    description="",
    author="Folkert",
    author_email="folkert@feedface.com",
    url="www.feedface.com",
    packages= [ about.NAME ],
    package_dir={about.NAME: about.NAME},
    scripts=[
        'scripts/oledlife',
        'scripts/fliplife'
    ],
    install_requires=[
        'pyserial',
        'hid',
    ],
)
