django-project-template
=======================

Use this template to create a new Django project like this:

django-admin.py startproject _project name_ --extension=py,pp --template=https://github.com/Harvard-University-iCommons/django-project-template/archive/master.zip

## Customizations

* Added top-level `static` and `http_static` directories.  Common assets used across multiple apps (e.g. jQuery, Bootstrap) can be stored in `static`.  For production serving, static assets from both the top-level static directory and all app-level static directories are collected into `http_static`.
* Added `settings` and `requirements` directories under the project subdirectory.  Inside those directories there are settings and requirements files for each environment: local, test, qa, production. Each of these environment-specific files inherits from a common base file. 
* Sensitive data in settings (passwords, keys) are expected to be passed to the app via environment variables.  The `settings/base.py` file contains a helper method for retrieving these values from the environment. 

