from setuptools import setup, find_packages

setup(
    name='beam-client-python',
    version='0.0.1',
    url='https://github.com/MCProHosting/beam-client-python',
    author='Connor Peet',
    author_email='connor@connorpeet.com',
    description='Simple chat bot framework for Beam.',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['ws4py', 'requests', 'tornado']
)
