import os
from pathlib import Path
from setuptools import setup
 

README=Path("README.md").read_text(encoding="utf-8")
 
# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name = 'djangorest_auth',
    version = '1.0',
    packages = ['djangorest_auth'],
    include_package_data = True,
    license = 'MIT License',
    description = '🔐 Authentication routes as a service.',
    long_description = README,
    long_description_content_type='text/markdown',
    url = 'https://github.com/israelabraham/djangorest-auth',
    author = 'Abram 🐼',
    author_email = 'israelvictory87@gmail.com',
    classifiers =[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
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
    python_requires=">=3.6",
    install_requires=[
        "django>=2.2",
        "djangorestframework",
        "djangorestframework-simplejwt",
        "django-rest-passwordreset",
        "rest-api-payload",
        "django-cors-headers",
        "django-hashid-field",
        "django-environ",
    ],
)

