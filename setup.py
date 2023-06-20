import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="arithmetic-abdDev", # Replace with your own username
    version="0.0.1",
    author="Abdullah",
    author_email="devopabd@gmail.com",
    description="A simple test arithmetic package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/createwithabd/arithmetic_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)