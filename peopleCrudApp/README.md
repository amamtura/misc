People App using Vue.js & Django/DRF
====================================

Misc notes:
-   Developed on Ubuntu 16.04.3, running inside VirtualBox
-   Python 3.5.2 (default Python 3 on Ubuntu 16.04)
-   Uses Django as the web framework and Django Rest Framework for API functionality
-   Uses SQLite for database functionalty
-   Uses Vue.js, Bootstrap on the front-end

Installation
------------
-   download source code
-   cd (to where requirements.txt is)
-   create and activate virtualenv; https://packaging.python.org/guides/installing-using-pip-and-virtualenv/
``` {.sourceCode .bash}
$ python3 -m virtualenv penv
$ source penv/bin/activate
```

-   install all python app dependencies inside the newly created virtual environment
``` {.sourceCode .bash}
$ pip install -r requirements.txt
```

-   create SQLite database (change directory to where manage.py is)
``` {.sourceCode .bash}
$ cd people
$ python manage.py migrate
```

-   for a dev instance, can create a django super user, example username=admin, password=admin
``` {.sourceCode .bash}
python manage.py createsuperuser
```
-   start the dev/local server
``` {.sourceCode .bash}
python manage.py runserver
```

-   also from within django admin webapp (http://localhost:8000/admin/), can create another non-admin user if desired, example username=appuser, password=test2019

-   note: Django Rest Framework is exposed for local dev/testing at http://localhost:8000/api/persons/

-   finally the "People App" for CRUD is available at http://localhost:8000/persons/

App and Dev notes
-----------------
1.  Django provides a nice, ready to use admin webapp, which via theme-ing etc could even be used as a full fledged user facing webapp
(esp for internal facing business solutions). Django's web framework features allow for rapid development of lots of functionality wih
minimal coding effort.

2.  Since the task called for the front-end and back-end to interact via an API, I choose Django Rest Framework. Additionally, I needed
a front end technology and so being adventurous I choose Vue.js as a learning exercise. This is my very first stab at trying to use Vue.js
so please excuse any potential non-optimal code or mistakes. I know I need to spend time with Vue.js so that I learn and effectively
apply various associated concepts of "Data driven view", "Components", binding, validation interaction between server/client etc

3.  I used various blogs/tutorials, official documentation, stack overflow threads, general searches on the web to bring all the 3 main parts
of the app (Django backend, DRF API and Vue.js frontend) up to the current state where all the basics are working.

4.  I am aware that currently certain bugs exist in the code, there could be some usability issues/improvements and pieces of code could be re-factored
for better design possibly (e.g. DRY). No software is ever "finished" so at this point I am submitting the app in a working state.
Always open to suggestions to improve code and most definitely fix issues/bugs.

5.  Among other things, for any project I would most definitely want to spend some time to add unit tests and for a case like this at least
API endpoints test. Also, example features I would add is "pagination", "confirm on delete action". Also, I don't have experience with front-end
frameworks but it looks like Axios or Fetch API might be a better choice than "vue-resource"'s http functionality.

6.  The app features include: API for persons "list", create, read (one record), update, delete; Django's admin webapp "out-of-the-box",
DRF's API dev/test webapp, CRUD webapp using Vue.js and BootStrap 4.x

7.  API url examples:
-   GET /api/persons/              (list all persons)
-   GET /api/persons/?order_by=id  (list all, sorted)
-   GET /api/persons/4             (get person)
-   POST /api/persons/             (create person)
-   PUT /api/persons/2             (update person)
-   DELETE /api/persons/5          (delete person)

