from setuptools import setup

setup(
    name="github-user-repo-query-9000",
    version="0.0.1",
    author="Arianna Trautmann",
    author_email="ari.trautmann@gmail.com",
    python_requires=">3.9",
    install_requires=[
        "starlette==0.13.0",
        "uvicorn==0.17.5",
        "websockets==10.2",
        "requests>=2.27.1"
    ]
)