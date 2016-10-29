from setuptools import setup

__version__ = '1.61'

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
    install_requires=['randomlineaccess==1.04', 'requests'],
    entry_points={
        'console_scripts': ['pwdgen=pwdgen.command_line:main'],
    }
)
