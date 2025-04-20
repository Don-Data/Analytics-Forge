from setuptools import find_packages, setup

setup(
    name="forge_orchestration",
    packages=find_packages(exclude=["forge_orchestration_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
