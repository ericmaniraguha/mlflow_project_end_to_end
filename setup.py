# Import the setuptools module, which is necessary for packaging and distribution.
import setuptools

# Open and read the content of the README.md file to be used as the long description.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version number of the package.
__version__ = "0.0.0"

# Define various metadata for the package.
REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "emanirag@andrew.cmu.edu"

# Use setuptools.setup() to configure the package and its metadata.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # Specify the directory structure of the package.
    package_dir={"": "src"},
    # Automatically find and include all packages under the 'src' directory.
    packages=setuptools.find_packages(where="src")
)
