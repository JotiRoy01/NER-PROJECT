#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advanced setup.py for packaging NER project with a src/ layout.
"""

import io
import sys
from pathlib import Path
from setuptools import find_packages, setup

# -------------------------------------------------------------------
# 1. Ensure compatible Python version
# -------------------------------------------------------------------
MIN_PYTHON = (3, 8)
if sys.version_info < MIN_PYTHON:
    sys.exit(f"Python {'.'.join(map(str, MIN_PYTHON))} or higher is required.")

# -------------------------------------------------------------------
# 2. Project Metadata
# -------------------------------------------------------------------
NAME = "ner_project"
DESCRIPTION = "An advanced Named Entity Recognition (NER) deep learning project"
URL = "https://github.com/JotiRoy01/NER-PROJECT"
EMAIL = "jotiroygit@example.com"
AUTHOR = "Joti Roy"
REQUIRES_PYTHON = ">=" + ".".join(map(str, MIN_PYTHON))

# -------------------------------------------------------------------
# 3. Load the package's __version__.py module
# -------------------------------------------------------------------
def load_version():
    version_path = Path(__file__).parent / "src" / "NER" / "__version__.py"
    about = {}
    with open(version_path, "r", encoding="utf-8") as f:
        exec(f.read(), about)
    return about["__version__"]

VERSION = load_version()

# -------------------------------------------------------------------
# 4. Load requirements
# -------------------------------------------------------------------
def load_requirements(filename):
    requirements_path = Path(__file__).parent / filename
    if requirements_path.exists():
        with open(requirements_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

INSTALL_REQUIRES = load_requirements("requirements.txt")

EXTRAS_REQUIRE = {
    "dev": [
        "black>=24.0",
        "flake8>=6.0.0",
        "isort>=5.12.0",
    ],
    "test": [
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
    ],
    "docs": [
        "sphinx>=7.0.0",
        "furo>=2023.7.26",
    ],
}

# -------------------------------------------------------------------
# 5. Load long description from README.md
# -------------------------------------------------------------------
def load_long_description():
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        with io.open(readme_path, encoding="utf-8") as f:
            return f.read()
    return DESCRIPTION

LONG_DESCRIPTION = load_long_description()

# -------------------------------------------------------------------
# 6. Setup configuration
# -------------------------------------------------------------------
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    python_requires=REQUIRES_PYTHON,
    package_dir={"": "src"},  # important for src layout
    packages=find_packages(where="src", exclude=["tests*", "docs"]),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ner-train=NER.cli:train_model",
            "ner-predict=NER.cli:predict_text",
        ],
    },
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        f"Programming Language :: Python :: {MIN_PYTHON[0]}.{MIN_PYTHON[1]}",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="ner, nlp, deep learning, pytorch, machine learning",
    project_urls={
        "Bug Tracker": f"{URL}/issues",
        "Documentation": f"{URL}/wiki",
        "Source Code": URL,
    },
)
