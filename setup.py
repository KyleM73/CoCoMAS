from setuptools import setup, find_packages

setup(
    name="cocomas",
    version="0.1",
    description="Competancy Conditioned Multi Agent Search",
    url="https://github.com/KyleM73/cocomas",
    license="MIT",
    author="Kyle Morgenstein",
    author_email="kylem@utexas.edu",
    packages=find_packages(),
    install_requires=["numpy", "torch"],
)
