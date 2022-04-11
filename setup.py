import os
import setuptools


setuptools.setup(
    name="peapy",
    version="1.0.2",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=["pygame", "keyboard", "mouse", "shapely"],
    packages=["peapy"],
)
