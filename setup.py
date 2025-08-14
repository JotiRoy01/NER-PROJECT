#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Professional setup.py for a Python project using a src/ layout.
Supports:
- Dynamic version from src/NER/__version__.py
- Optional extras (dev, test, docs)
- CLI entry points
- Safe file loading
"""

import io
import sys
from pathlib import Path
from setuptools import find_packages, setup

# -------------------------------------------------------------------
# 1. Minimum Python version check
# -------------------------------------------------------------------
MIN_PYTHON = (3, 8)
if sys.version_info < MIN_PYTHON:
    sys.exit(f"Python {'.'.join(map(str, MIN_PYTHON))} or higher is required.")

# -------------------------------------------------------------------
# 2. Project metadata
# -------------------------------------------------------------------
NAME = "ner_project"
DESCRIPTION = "An advanced Named Entity Recognition (NER) deep learning project"
URL = "https://github.com/JotiRoy01/NER-PROJECT"
EMAIL = "jotiroygit@example.com"
AUTHOR = "Joti Roy"
REQUIRES_PYTHON = ">=" + ".".join(map(str, MIN_PYTHON))

# -------------------------------------------------------------------
# 3. Load the package version from __version__.py
# -------------------------------------------------------------------
def load_version():
    version_file = Path(__file__).parent / "src" / "NER" / "__version__.py"
    about = {}
    with open(version_file, "r", encoding="utf-8") as f:
        exec(f.read(), about)
    return about["__version__"]

VERSION = load_version()

# -------------------------------------------------------------------
# 4. Load requirements safely
# -------------------------------------------------------------------
def load_requirements(filename):
    path = Path(__file__).parent / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return [
                line.strip() for line in f
                if line.strip() and not line.startswith("#")
            ]
    return []

INSTALL_REQUIRES = load_requirements("requirements.txt")

# -------------------------------------------------------------------
# 5. Optional dependencies (extras)
# -------------------------------------------------------------------
EXTRAS_REQUIRE = {
    "dev": [
        "black>=24.0",      # Auto code formatting
        "flake8>=6.0.0",    # Linting for style and errors
        "isort>=5.12.0",    # Sort imports
    ],
    "test": [
        "pytest>=7.0.0",     # Test runner
        "pytest-cov>=4.0.0", # Test coverage reports
        "pytest-mock>=3.6.0" # Mocking in tests
    ],
    "docs": [
        "sphinx>=7.0.0",     # Documentation generator
        "furo>=2023.7.26",   # Sphinx theme
    ],
}

# -------------------------------------------------------------------
# 6. Load long description from README.md
# -------------------------------------------------------------------
def load_long_description():
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        with io.open(readme_path, encoding="utf-8") as f:
            return f.read()
    return DESCRIPTION

LONG_DESCRIPTION = load_long_description()

# -------------------------------------------------------------------
# 7. Setup configuration
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
    package_dir={"": "src"},  # src layout mapping
    packages=find_packages(where="src", exclude=["tests*", "docs"]),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ner-train=NER.cli:train_model",   # Train CLI
            "ner-predict=NER.cli:predict_text" # Predict CLI
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
