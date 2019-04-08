from setuptools import setup


setup(
    name="jgscm",
    description="Jupyter Google Cloud Storage ContentsManager",
    version="0.1.10-hail",
    license="MIT",
    author="Vadim Markovtsev",
    author_email="vadim@sourced.tech",
    url="https://github.com/src-d/jgscm",
    download_url="https://github.com/src-d/jgscm",
    packages=["jgscm"],
    keywords=["jupyter", "ipython", "gcloud", "gcs"],
    install_requires=["google-api-python-client>=1.7",
                      "google-cloud-storage>=1.14",
                      "notebook>=5.7", "nbformat>=4.4",
                      "tornado>=6.0", "traitlets>=4.3"],
    package_data={"": ["requirements.txt", "LICENSE", "README.md"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries"
    ]
)
