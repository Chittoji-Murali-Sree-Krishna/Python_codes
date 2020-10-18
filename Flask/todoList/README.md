# todoList
## static/css
- this main.css file
## templates
1. base.html is the parent for other html files
1. todo.html has the main todo app
1. update.html , this is to update the todo when we clicked update button
```html
<!--I  am using ginger syntax for linking and retriving data and stuff -->
<link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}"><!--for css linking-->
<b>todo.html, update.html</b>
{% extends 'base.html' %}<!--using this for rendeing the templates in the main template instead of having different templates for each-->
{% if task|length < 1 %}
<p> it will not rernder anything</p>
{% else %}
<p>this will render the todo/tasks</p>
{% for task in tasks %}<!--we are getting this from app .py from the route return-->
<p>the new tasks will update the div tag</p>
```
