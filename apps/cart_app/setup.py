import os
from setuptools import setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
 
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name='cart-app',
    version='1.0.0',
    packages=['cart'],
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to store items/products, adding, removing and listing them',
    long_description=README,
    url='http://www.example.com/',
    author='Paul Cheeseman',
    author_email='Paul@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6.1',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    
    #install_requires = NONE
)