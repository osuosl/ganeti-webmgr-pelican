Getting started
###############
:slug: index
:index: index
:url:
:save_as: index.html

1. **Install dependencies:** 
	Python, Pip, Fabric, and Viruatlenv
2. **Get the Ganeti Web Manager code:** 
			 Clone from the `repository <https://github.com/osuosl/ganeti_webmgr>`_  or download a `release tarball <link>`_
3. **Deploy fabric environment:** 

.. code-block:: bash

	fab dev deploy

*or*

.. code-block:: bash

	fab prod deploy

4. **Configure Settings:** 
	Copy **settings.py.dist** to **settings.py** and make any modifications
5. **Sync database, then run the server:**

.. code-block:: bash

	./manage.py syncdb -migrate

*then*

.. code-block:: bash

	./manage.py runserver


