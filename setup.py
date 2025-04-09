from setuptools import setup, find_packages

setup(
    name="library-management-system",
    version="1.0.0",
    author="ahmeddcc",
    description="نظام إدارة المكتبات الشامل",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ahmeddcc/library-management-system",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)