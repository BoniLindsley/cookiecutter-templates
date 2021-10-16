#!/usr/bin/env python3

# Standard libraries.
import setuptools  # type: ignore

setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.project_short_description}}",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license="MIT",
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_name}} = {{cookiecutter.project_slug}}.__main__:main",
        ],
    },
    extras_require={
        "dev": [
            "black",
            "coverage[toml]",
            "mypy",
            "pytest",
            "recommonmark",
            "sphinx",
            "tox",
            "types-pkg_resources",
            "types-six",
        ],
    },
    python_requires=">= 3.9",
)
