import setuptools


setuptools.setup(
    name="peapy",
    version="1.1.15",
    author="Silvan Schmidt",
    description="A python game engine",
    install_requires=["pygame==2.1.3.dev2", "keyboard", "mouse", "shapely~=1.8.1.post1"],
    packages=["peapy"],
)
