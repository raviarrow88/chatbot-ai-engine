# Chatbot AI Engine

AI Engine for Chatbots in the platform. The AI engine is expected to
read the webpages(html), books(books), and discussion forums (Q&A).
The job of this Engine is to take any data it finds, and it organises 
and stores the html structure into question/request and answer/response
format 


## Technical Stack 

1. Flask http://flask.pocoo.org/ - Flask is a microframework for Python 
based on Werkzeug, Jinja 2 and good intentions. 
2. MongoDB http://mongodb.org/ - A NoSQL database


## Example of how it works:

Lets say, there is a html data of structure from the url 
http://manual.gromacs.org/documentation/2016.1/user-guide/mdp-options.html

```
<h2>General information<a class="headerlink" 
href="#general-information" title="Permalink to this headline">¶</a></h2>

<p>Default values are given in parentheses, or listed first among
choices. The first option in the list is always the default
option. Units are given in square brackets. The difference between a
dash and an underscore is ignored.</p>

<p>A <a class="reference internal" href="file-formats.html#mdp">
<span class="std std-ref">sample mdp file</span></a> is available. 
This should beappropriate to start a normal simulation. Edit it to 
suit your specific needs and desires.</p>

```

Now, the engine should save the data as a json of 

```json
{
'url': 'http://manual.gromacs.org/documentation/2016.1/user-guide/mdp-options.html',
'tool_name': 'gromacs',
'version': '2016.1',
'type': 'webpage',
'h2': 'Generawl information',
'p': [
    'Default values are given in parentheses, or listed first among
    choices. The first option in the list is always the default
    option. Units are given in square brackets. The difference between a
    dash and an underscore is ignored.',
    'A sample mdp file is available. This should beappropriate to start a 
    normal simulation. Edit it to suit your specific needs and desires.'
],
'attachements': [
    
],
'updated_at' : '2016-01-22 00:00:00.123131',
'scraped_at' : '2016-11-22 23:10:40.679767',
'cross_references': [], #references from this data to other data via., links
}
```


## Setting up for Developement

1. Install all the requirements using the command `pip install -r requirements/requirements-dev.txt` 


## Code Description

1. server - webserver that hosts APIs and creates User Interface, built on
Django
2. engines - for reading the html, books, discussion forums(Q&A)
3. docs - documentation generated from the code


