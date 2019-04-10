People App using vue.js & django/drf
====================================

Misc notes:
Developed on Ubuntu 16.04.3, running inside VirtualBox
Python 3.5.2 (default Python 3 on Ubuntu 16.04)
Uses SQLite for database functionalty

Installation
------------
-   download source code
-   cd (to where requirements.txt is)
-   create and activate virtualenv; https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
``` {.sourceCode .bash}
$ python3 -m virtualenv penv
$ source env/bin/activate
```

``` {.sourceCode .bash}
$ pip install -r requirements.txt
```

-   cd people (to where manage.py is)
``` {.sourceCode .bash}
$ python manage.py migrate
```

-   for a dev instance, can use username=admin, password=admin
``` {.sourceCode .bash}
python manage.py createsuperuser
```

-   via django admin, can create another non-admin user if desired, example username=appuser, password=test2019
