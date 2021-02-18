from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='bytesviewapi',
    version='0.1.2',
    packages=['bytesviewapi'],
    description='Python library for bytesview client-API Call',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/algodommedia/bytesviewapi-python',
    author='Bytesview',
    author_email='contact@bytesview.com',
    license='MIT',
    install_requires=["requests<3.0.0"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',    
    python_requires='>=3.5',
    keywords=[
        'byteviewapi',
        'senitment',
        ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
      ] 

)
