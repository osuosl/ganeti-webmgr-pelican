====
Home
====
:slug: index
:Index: index

Getting Started
===============

1. Install dependencies: 
	Python, Pip, Fabric, and Viruatlenv
2. Get the Ganeti Web Manager code: 
	Clone from the `repository <https://github.com/osuosl/ganeti_webmgr>`_  or download a `release tarball <link>`_
3. Deploy fabric environment: 

.. raw:: html
    
    <p class="code">fab dev deploy</p>  or <p class="code">fab prod deploy</p><br><br>

4. Configure Settings: 
	Copy settings.py.dist to settings.py and make any modifications
5. Sync database, then run the server:

.. raw:: html
	
    <p class="code">./manage.py syncdb -migrate</p>  then  <p class="code">./manage.py runserver</p>


