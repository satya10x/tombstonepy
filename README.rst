tombstone-py
========

Python module to remove dead code and log execution time of modules.

Installation
------------

tombstone-py requires a running Redis server. See `Redis's quickstart
<http://redis.io/topics/quickstart>`_ for installation instructions.

To install tombstone-py, simply:

.. code-block:: bash

    $ sudo python setup.py install 


Getting Started
---------------

.. code-block:: pycon

import tombstone
import datetime

class HelloWorld:
def __init__(self):
	pass

#time isn't a necessary argument. If not provided, it takes the current time.
# module name needs to be there
@tombstone.logs(module_name="HelloWorld", time=datetime.datetime.now())
def test_it(self):
	print "dance basanti"

hel = HelloWorld()
hel.test_it()

API Reference
-------------

from tombstone import Tomb
print Tomb.get_data() # gets json data which contains module name,
# function name, average execution time,
# usage count and last usage date time string
 
#Clear data for the function
Tomb.remove_data("module_name:function_name")
# Clear all data
Tomb.remove_all_data()