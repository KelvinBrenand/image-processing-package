from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_KBrenand",
    version="0.0.1",
    author="Kelvin Brenand",
    author_email="brenand.kelvin@gmail.com",
    description="This package performs a few image operations like Sobel and Saturation.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KelvinBrenand/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)