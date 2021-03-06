"""
Flask-Social
============

Oauth provider login and APIs for use with
`Flask-Security <http://packages.python.org/Flask-Security/>`_

Resources
---------

- `Documentation <http://packages.python.org/Flask-Social/>`_
- `Issue Tracker <http://github.com/mattupstate/flask-social/issues>`_
- `Code <http://github.com/mattupstate/flask-social/>`_
- `Development Version
  <http://github.com/mattupstate/flask-rq/zipball/develop#egg=Flask-Social-dev>`_

"""
from setuptools import setup

setup(
    name='Flask-Social',
    version='2.0.0',
    url='https://github.com/mattupstate/flask-social',
    license='MIT',
    author='Matthew Wright',
    author_email='matt@nobien.net',
    description='Simple OAuth provider integration for Flask-Security',
    long_description=__doc__,
    packages=[
        'flask_social',
        'flask_social.providers'
    ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask-Security>=3.0.0',
        'Flask-OAuthlib>=0.9.5'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
        'Flask-SQLAlchemy',
        'Flask-MongoEngine',
        'Flask-Peewee'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
