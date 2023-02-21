from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Fast change between projects'

setup(
    name="startwork",
    version=VERSION,
    author="JorbFreire",
    author_email="",
    description=DESCRIPTION,
    include_package_data=True,
    packages=find_packages(),
    install_requires=["inquirer==3.1.2"],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)
