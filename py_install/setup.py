from setuptools import find_packages, setup

setup(
    name='Rosmaster_Lib',
    version='3.3.9',
    author='Yahboom Team',
    packages=find_packages(),
    install_requires=[
        'pyserial>=3.5',
        # Add other dependencies here
    ],
)

# cd py_install
# sudo python3 setup.py install
