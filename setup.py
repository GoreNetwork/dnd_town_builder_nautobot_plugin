from setuptools import find_packages, setup


setup(
    name='dnd_town_builder_nautobot_plugin',
    version='0.1',
    description='A Nautobot plugin for building DnD towns',
    author='Daniel',
    packages=find_packages(),
    include_package_data=True,
)