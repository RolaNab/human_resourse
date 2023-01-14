from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in human_resourse/__init__.py
from human_resourse import __version__ as version

setup(
	name="human_resourse",
	version=version,
	description="Human Resourse Desc",
	author="Rola",
	author_email="rola.nabulsi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
