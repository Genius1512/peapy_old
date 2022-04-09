import os
import setuptools


setuptools.setup(
    name="peapy",
    version="1.0.0",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=["pygame", "rich", "mouse", "keyboard", "shapely"],
    packages=["peapy"],
)
