Description
===========

This project reproduces django-odesk issue #12 filled on https://github.com/solex/django-odesk/issues/12

Steps to reproduce
==================

#. Obtain oDesk API keys at https://www.odesk.com/services/api/keys
#. Copy issue12/local_settings.py.def to issue12/local_settings.py and fill in obtained keys.
#. syncdb
#. runserver
#. open http://localhost:8000/
#. login with oDesk account using the link
#. check expiration time of oekey cookie in developer's console (or firebug)
#. set local system time later than expiration time above
#. reload the page
#. see 403 server error and missing oekey cookie in developer's console
