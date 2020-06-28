
import sys
from setuptools import find_packages
from setuptools import setup
from vci import __version__

setup(
    name='vci',
    version=__version__,
    packages=find_packages(exclude=['tests*', 'docs*']),
    # check into catkin_tools/ckx_tools for a smarter, but complicated method
    author='Daniel Stonier',
    author_email='d.stonier@gmail.com',
    maintainer='Daniel Stonier',
    maintainer_email='d.stonier@gmail.com',
    url='http://github.com/stonier/vci',
    keywords=['catkin'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Topic :: Utilities'
    ],
    description="version control management from an index of listed workspaces",
    long_description="Version control index handling from a yaml file on the internet (e.g. github).",
    license='BSD',
    # test_suite='tests',
    entry_points={
        'console_scripts': [
            'vci = vci:main',
        ],
    },
)
