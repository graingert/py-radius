from setuptools import setup

setup(
    name = 'radius',
    version = '0.0.1',
    description = 'RADIUS authentication module',
    long_description = 'A pure Python module that implements client side RADIUS ' \
                       'authentication, as defined by RFC2865.',
    author = 'Stuart Bishop',
    author_email = 'zen@shangri-la.dropbear.id.au',
    maintainer = 'Thomas Grainger',
    maintainer_email = 'radius@graingert.co.uk',
    url = 'http://github.com/graingert/py-radius',
    py_modules = ["radius"],
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
    ]
)
