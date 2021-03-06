#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name="Delivery Trackers",
    version="0.1.dev0",
#     url="https://github.com/tomerghelber/delivery-trackers",
    author="Tomer Ghelber",
#     author_email="",
    license="OSI Approved :: GNU General Public License v3 (GPLv3)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open("requirements.in").readlines(),
    description="Library to track deliveries.",
    long_description=open("README.md").read(),
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Typing :: Typed",
    ]
)
