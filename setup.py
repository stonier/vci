
import sys
from setuptools import find_packages
from setuptools import setup

extras_require = {
    'packaging': ['stdeb', 'twine']
}

setup(
    name='vci',
    version="0.2.7",
    packages=find_packages(exclude=['tests*', 'docs*']),
    author='Daniel Stonier',
    author_email='d.stonier@gmail.com',
    maintainer='Daniel Stonier',
    maintainer_email='d.stonier@gmail.com',
    url='http://github.com/stonier/vci',
    keywords=['vcs'],
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
    install_requires=["distro", "pyyaml"],
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'vci = vci:main',
        ],
    },
)
