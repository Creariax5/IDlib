from setuptools import find_packages, setup
setup(
    name='IDlib',
    packages=find_packages(include=['IDlib']),
    version='0.1.0',
    description='Systeme of id',
    author='Florian',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
