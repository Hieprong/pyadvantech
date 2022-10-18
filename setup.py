import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyadvantech',
    version='0.2.2',
    author="Paul Weimer",
    author_email="weimerpaul99@gmail.com",
    description="A custom USB driver for Advantech USB-4718",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hieprong/pyadvantech",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'matplotlib',
        'libusb',
        'pyusb',
        'tqdm',
        'numpy',
    ],
)
