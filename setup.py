from setuptools import setup


with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='pythonic-data-structures',
    packages=['DataStructures'],
    version='0.1',
    description='Python-based implementations for many data structures.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Nikolay Stanchev',
    author_email='nikist97.ns@gmail.com',
    url='https://github.com/nikist97/Python-DataStructures',
    keywords=['data structures', 'data', 'structures', 'python', 'abstract', 'generic', 'graph', 'heap', 'queue', 'stack'],
    license="Apache 2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3'
)
