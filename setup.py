import setuptools

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="conflux",
    version="0.0.1",
    author="Bella Zhong",
    author_email="abigailzhong219@gmail.com",
    description="Search Engine",
    url="https://github.com/BellaZ0317/Conflux",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
