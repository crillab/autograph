# ##############################################################################
#  Copyright © 2021 Univ Artois & CNRS, Exakis Nelite                          #
#                                                                              #
#  Permission is hereby granted, free of charge, to any person                 #
#  obtaining a copy of this software and associated documentation              #
#  files (the “Software”), to deal in the Software without                     #
#  restriction, including without limitation the rights to use,                #
#  copy, modify, merge, publish, distribute, sublicense, and/or sell           #
#  copies of the Software, and to permit persons to whom the                   #
#  Software is furnished to do so, subject to the following                    #
#  conditions:                                                                 #
#                                                                              #
#  The above copyright notice and this permission notice shall be              #
#  included in all copies or substantial portions of the Software.             #
#                                                                              #
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,             #
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES             #
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                    #
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT                 #
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,                #
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING                #
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR               #
#  OTHER DEALINGS IN THE SOFTWARE.                                             #
# ##############################################################################

"""
Setup script for deploying Metrics on PyPI and allowing to install it using pip.
"""


from setuptools import setup
from typing import List

import autograph


def readme() -> str:
    """
    Reads the README file of the project to use it as long description.

    :return: The long description of Metrics.
    """
    with open('README.md') as file:
        return file.read()


def requirements() -> List[str]:
    """
    Reads the requirements file of the project to use its content to determine
    the dependencies of the package.

    :return: The dependencies of Metrics.
    """
    return [
        "Pillow==8.2.0",
        "cycler==0.10.0",
        "kiwisolver==1.3.1",
        "matplotlib==3.4.1",
        "nose==1.3.7",
        "numpy==1.20.2",
        "pip==20.1.1",
        "plotly==4.14.3",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "retrying==1.3.3",
        "setuptools==44.1.1",
        "six==1.15.0"
    ]


setup(
    name='crillab-autograph',
    version=autograph.__version__,
    packages=[
        'autograph.core',
        'autograph.wrapper',
        'autograph'
    ],

    description=autograph.__summary__,
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords=autograph.__keywords__,

    author=autograph.__author__,
    author_email=autograph.__email__,
    url=autograph.__uri__,

    install_requires=requirements(),

    test_suite='nose.collector',
    tests_require=['nose'],

    scripts=[
    ],

    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent'
    ],
    license=autograph.__license__,

    include_package_data=True,
    zip_safe=False
)
