import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="subject_classification_spanish",
    version="0.0.9",
    author="Hugo J. Bello",
    author_email="hjbello.wk@gmail.com",
    description="Subject and topic analysis for sentences in spanish",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/news-scrapers/subject-classification-spanish",
    packages=setuptools.find_packages(),
    package_data={'subject_classification_spanish': ['saved_models/*']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)