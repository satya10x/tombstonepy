import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='tombstone',
	version='0.1',
	packages=['tombstone','tombstone.modules'],
	include_package_data=True,
	license='BSD License',  # example license
	description='A static blog generation library built around cherrypy',
	long_description=README,
	url='http://www.example.com/',
	author='H1ccup',
	author_email='yourname@example.com',
	classifiers=[
		'Environment :: Web Environment',
		'Framework :: Cherrypy',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License', # example license
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		# Replace these appropriately if you are stuck on Python 2.
		'Programming Language :: Python :: 2.7',
	],
)
