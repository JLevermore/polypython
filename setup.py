from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="polypython",
    version="0.0.0.0.1",
    author="Joseph M Levermore",
    author_email="j.levermore@imperial.ac.uk",
    description="Analysis of Raman spectral images for plastic content.",
    license='MIT',
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/JLevermore/polypython",
    packages=find_packages(),
    install_requires=['numpy','matplotlib','scipy','seaborn'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)