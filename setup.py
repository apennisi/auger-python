import setuptools

setuptools.setup(
    name="auger-python",
    version="0.1.34",
    author="Chris Laffra",
    author_email="laffra@gmail.com",
    maintainer="Andrea Pennisi",
    maintainer_email="andrea.pennisi@gmail.com",
    description="Automatically generate unit tests for Python code",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/apennisi/auger-python",
    packages=[
        'auger',
        'auger.generator'
    ],
    install_requires=[
        'funcsigs',
        'mock',
        'six',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.x 2.x",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
