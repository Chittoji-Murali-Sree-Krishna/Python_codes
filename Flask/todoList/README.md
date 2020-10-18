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
# app.py
```python
from flask_sqlalchemy import SQLAlchemy #for using the database we have to install flask_SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db' 
db = SQLAlchemy(app) #this will create the database
#for creating models in database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True) #this will generate id for each and every task so that it will be easy to update or delete the task
    content = db.Column(db.String(200), nullable=False) # for content
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # for the date
    if request.method == 'POST':
    #then only it initialize the process
    #i use try and except for errors 
```#for update and delete we have use the id to make it unique from others so routing will be
@app.route('/delete/<int:id>')
@app.route('/update/<int:id>')
