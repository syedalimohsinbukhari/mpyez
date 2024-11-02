"""Setup file"""

from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='mpyez',
    version='0.0.7',
    packages=find_packages(where="src", exclude=['*tests*']),
    url='https://github.com/syedalimohsinbukhari/mpyez',
    license='MIT',
    author='Syed Ali Mohsin Bukhari',
    author_email='syedali.b@outlook.com',
    description='Common use backend for python done easy.',
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.9, <3.12",
    install_requires=["numpy==1.26.4", "matplotlib", "setuptools"],
    include_package_data=True,
    classifiers=["License :: OSI Approved :: MIT License",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Programming Language :: Python :: 3.11"],
)
