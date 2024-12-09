"""Setup file"""

import os

from setuptools import find_packages, setup


def load_metadata():
    """get the metadata for the package."""
    metadata = {}
    with open(os.path.join("src", "mpyez", "version.py")) as f:
        exec(f.read(), metadata)
    return metadata


metadata_ = load_metadata()

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

setup(name=metadata_['__name__'],
      version=metadata_['__version__'],
      author=metadata_['__author__'],
      author_email=metadata_['__email__'],
      license=metadata_['__license__'],
      url=metadata_['__url__'],
      description=metadata_['__description__'],
      packages=find_packages(where="src", exclude=["test"]),
      package_dir={"": "src"},
      long_description=readme,
      long_description_content_type="text/markdown",
      python_requires=">=3.9",
      install_requires=["numpy<2.3.0", "matplotlib", "setuptools"],
      classifiers=["License :: OSI Approved :: MIT License",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Programming Language :: Python :: 3.11",
                   "Programming Language :: Python :: 3.12"],
      )
