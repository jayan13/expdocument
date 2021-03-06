from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in expdocument/__init__.py
from expdocument import __version__ as version

setup(
	name="expdocument",
	version=version,
	description="Manage expirable documents and notification",
	author="alantechnologies",
	author_email="jayakumar@alantechnologies.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
