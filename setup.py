import os
from pathlib import Path
from setuptools import setup
 

README=Path("README.rst").read_text(encoding="utf-8")
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'djangorest_auth',
    version = '0.1',
    packages = ['djangorest_auth'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Bootstrap your spa startup with this amazing django rest authentication reusable app',
    long_description = README,
    url = 'https://github.com/israelabraham/djangorest-auth',
    author = 'Abram 🐼',
    author_email = 'israelvictory87@gmail.com',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    install_requires=[
        "django",
        "djangorestframework",
        "djangorestframework-simplejwt",
        "rest-api-payload",
        "django-environ",
    ],
)
