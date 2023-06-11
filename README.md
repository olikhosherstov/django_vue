# This is booking system project.

The Backend is built on Django.
The Frontend is built on Vue 3.

The Vue 3 project is located in the vue_template directory.
To link Django with Vue 3, you need to place the Vue 3 build in the /static/ directory. 
index.html of the build should be placed in the templates directory. 
After that, the index.html of the Vue 3 build is rendered by the index method in the views.py file. 
Accordingly, the call to the index method is written in the urls.py file. 
In order for Django to support Vue 3 routing, you need to write re_path(r'^.*$', index) in the urls.py file

