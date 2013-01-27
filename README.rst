Description
===========

This project reproduces django-odesk issue #12 filled on https://github.com/solex/django-odesk/issues/12

Steps to reproduce
==================

1. Obtain oDesk API keys at https://www.odesk.com/services/api/keys
1. Copy issue12/local_settings.py.def to issue12/local_settings.py and fill in obtained keys.
1. syncdb
1. runserver
1. open http://localhost:8000/
1. login with oDesk account using the link
1. check expiration time of oekey cookie in developer's console (or firebug)
1. set local system time later than expiration time above
1. reload the page
1. see 403 server error and missing oekey cookie in developer's console
