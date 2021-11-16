from setuptools import find_namespace_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


with open("README.md") as f:
    long_description = f.read()

setup(
    name="rpsGame.py",
    description="Rock Paper Scissors",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    include_package_data=True,
    url="https://github.com/BZattera/GameTheory",
    author="Benedetta Zattera",
    author_email="benedetta.zattera@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
