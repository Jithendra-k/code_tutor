from setuptools import setup, find_packages

setup(
    name="code_tutor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "crewai",
        "langchain",
        "anthropic",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
        ],
    },
)