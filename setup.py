from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='awsglue-dev',
    version='0.0.0.post20211102',
    description='Python interfaces to the AWS Glue ETL library for use as a local dependency.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
