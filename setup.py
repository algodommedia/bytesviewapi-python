from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='bytesviewapi',
    version='0.0.1',
    packages=['bytesviewapi'],
    description='Python library for bytesview client-API Call',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sanjeev',
    license='MIT',
    install_requires=["requests<3.0.0", "jsonlib-python3"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',    
    python_requires='==3.6.9',
    keywords=[
        'byteviewapi',
        'senitment',
        ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS independent',
      ] 

)
