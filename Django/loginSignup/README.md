# loginSignup
- this is main project
## settings.py
- installed appps 
```python
INSTALLED_APPS = [
    'crispy_forms',
    'main.apps.MainConfig',
    'register.apps.RegisterConfig',
]
```
- crispy forms for clean building the signup and login page because we can use bootstrap4 instead of bootstrap2
```python
CRISPY_TEMPLATE_PACK='bootstrap4'
```
- we use these for redirecting the pages after loggin and logout if not the will choose there own
```python
LOGIN_REDIRECT_URL = '/' 
LOGOUT_REDIRECT_URL = '/'
```
## urls.py
- we are import register views as reg views so that we can use more views
```python
from register import views as regviews
```
- urls
```python
urlpatterns = [
    path('signup/', regviews.signup, name='signup'),
    path('', include('main.urls')),
    path('',include('django.contrib.auth.urls')),
]
```
- ~~for login and logout we dont need a url because django have built in urls for those~~
# main
- this is the normal app which have a home page
## templates
   ### main
   - home.html parent file for other html files
   - this home page will show both login and signup pages inside it
   ## urls.py
   - routing  the home page 
   ## views.py
   - rendering the home page


# register
- this contains login/signup/logout stuff but we dont use urls in this app becaue django has prebuild functions for it
## templates
### register
- this has the signup page
### registration
- this has the login page
- we are using the name as registration because by default django searches for registration page
## forms.py
- this is to set the signup page page formatted and also can manage the required fields
```python
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```
## views.py
- we are using only signup view to modify it, but other stuff will be managed by django itself
- we check the response method if it is post we will save else it will not save
