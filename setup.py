import setuptools


setuptools.setup(
    name="peapy",
    version="1.1.0",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=["pygame==2.1.3.dev4", "keyboard", "mouse", "shapely"],
    packages=["peapy"],
)
