from setuptools import find_packages, setup

setup(
    name='record_batcher',
    packages=find_packages(include=['record_batcher']),
    version='1.0.0',
    description='FSA1',
    author='Lauri Naalisvaara',
    license='none',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.2.2'],
    test_suite='tests',
)