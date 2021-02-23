from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    README = f.read()

setup(
    name="CPAW",
    descriptions=(
        "CPAW, `The Cryptic Game Python API Wrapper`, is a pyton wrapper",
        "for accessing to the Cryptic Game."
    ),
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/citharus/CPAW",
    author="citharus",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities"
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    keywords="api wrapper, cryptic-game",
    pyton_requires=">=3.0",
    install_requires=["json", "websocket-client"],
    project_urls={
        "Bug Reports": "https://github.com/citharus/CPAW/issues",
        "Source": "https://github.com/citharus/CPAW"
    }
)
