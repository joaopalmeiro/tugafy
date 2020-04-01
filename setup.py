import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()
REQUIREMENTS = (HERE / "requirements.txt").read_text().split()

setup(
    name="tugafy",
    version="0.0.1",
    description="A simple Python package to get an English (en)–Portuguese (pt-PT) dictionary for Data Science and Machine Learning terms.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopalmeiro/tugafy",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points={"console_scripts": ["tugafy=tugafy.__main__:main",]},
)
