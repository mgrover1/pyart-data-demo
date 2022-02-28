#!/usr/bin/env python3

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()
setup(
    maintainer='ARM Development Team',
    maintainer_email='',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='Provides utility functions for accessing data repository for PyART',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    package_data={'pyart_datasets': ['registry.txt']},
    keywords='Pythia, Pooch',
    name='pyart-datasets',
    packages=find_packages(include=['pyart_datasets', 'pyart_datasets.*']),
    entry_points={},
    url='https://github.com/mgrover1/pyart-datasets',
    project_urls={
        'Documentation': 'https://github.com/mgrover1/pyart-datasets',
        'Source': 'https://github.com/mgrover1/pyart-datasets',
        'Tracker': 'https://github.com/mgrover1/pyart-datasets/issues',
    },
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    zip_safe=False,
)