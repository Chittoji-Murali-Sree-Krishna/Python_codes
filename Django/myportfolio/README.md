# myportfolio
- this the main project, just to showcase my portfolio
## setting.py
```python
INATALLED_APPS = [
'port', #i am using only this because i dont have much to show in this project just my portfolio
]
```
- for images and static pages
```python
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```
## urls.py
```python
path('', include('port.urls')),
```
# port
- this is for my portfolio
## templates
### port
1. **home.html** _this the base parent page for other html pages_
2. **aboutme.html** _this is aboutme page_
3. **myprojects.html** _this contains my projects_
4. **todo** _for my todo page_
## models.py
- here we are using todo so we need a model to take that and store in databse
```python
class Task(models.Model):
    title = models.CharField(max_length=200) #we are setting the maximum lenght for the input
    complete = models.BooleanField(default=False) #this is wheter to check todo is completed or not
    created = models.DateTimeField(auto_now_add=True) #we use date time for each and every field so that they will have when its created

def __str__(self):
    return self.title 
```
## urls.py
- this will have urls for the views
## views.py
1. **home**
>for home page
2. **aboutme**
>for aboutme page
3. **myprojects**
>for myprojects page
4. **todo**
>for todo page and we have to check whether the page is valid or no
```python
tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo/')
    context = {'tasks':tasks, 'form':form}
```
## admin.py
>hence we are using the backend we also need to register task using admin
```python
admin.site.register(Task)
```
