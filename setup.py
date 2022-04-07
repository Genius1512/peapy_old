import os
import setuptools


setuptools.setup(
    name="peapy",
    version="0.2.3",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=["pygame", "rich", "mouse", "keyboard"],
    packages=["peapy"],
)
