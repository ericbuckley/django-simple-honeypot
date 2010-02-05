author: eric buckley <eric.buckley@gmail.com>

Just add this app to your project and put it in your installed apps tuple.
======================
django simple honeypot
======================

The django simple honeypot is a simple CharField that you can use
in any of your forms to produce a hidden input field that is to 
be left blank.  The purpose of this field is to stop bots from 
attempting to spam your form.  Typically bots attempt to fill out
all of the fields in a form, so if one fills this field the clean
method will raise a validation exception.

See: http://en.wikipedia.org/wiki/Honeypot_%28computing%29

Installation
============

#. Export django-simple-honeypot and place it into a folder within your project,
    you can label the folder whatever you'd like, as you will need to use that
    name to import the Honeypot field.
    
#. Alternatvly you can use the git to put the app right into your project
    (if your project is already using git, you'll have to use the submodule 
    command)
    
    ``git clone git@github.com:ericbuckley/django-simple-honeypot.git honeypot``
    
# In your forms.py file import the Honeypot field
    
    ``from honeypot.fields import Honeypot``