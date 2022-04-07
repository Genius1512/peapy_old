import os
import setuptools


requirements = (
    open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r")
    .read()
    .split("\n")
)


setuptools.setup(
    name="peapy",
    version="0.0.1",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=requirements,
    packages=["peapy"],
)
