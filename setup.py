import os.path
import pathlib
from setuptools import setup

pkg_dir = pathlib.Path(os.path.dirname(__file__))
version_file = pkg_dir / 'pwdgen' / '.version'
__version__ = open(str(version_file)).read().strip()

long_description = """
Quickly generate secure passwords and passphrases.
"""

setup(
    name="pwdgen",
    packages=["pwdgen"],
    version=__version__,
    description="Quickly generate secure passwords and passphrases.",
    author="Bryce Drennan",
    author_email="pwdgen@brycedrennan.org",
    url="https://github.com/brycedrennan/pwdgen",
    download_url='https://github.com/brycedrennan/pwdgen/tarball/' + __version__,
    keywords=["password", "passphrase"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Topic :: Utilities",
    ],
    license='MIT',
    long_description=long_description,
    install_requires=['randomlineaccess==1.04'],
    entry_points={
        'console_scripts': ['pwdgen=pwdgen.command_line:main'],
    }
)
