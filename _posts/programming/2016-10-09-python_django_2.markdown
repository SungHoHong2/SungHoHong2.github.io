---
published: true
title: Django Image Upload
layout: post
category: programming
permalink: /programming/
---


### Adding User-Uploaded Images 

<hr>

#### Required steps to setup ImageField

1. add ImageField to the model
2. Install Pillow - an image-processing library necessary for Image field 
3. Migrate changes 
4. Update settings.py to add a media director y
5. Add a special debugging URL to urls.py to server our media files locally 

<br>

#### app/models

```python

from django.db import models

# Create your models here.
class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits= 10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    img_url = models.ImageField(upload_to='treasure_images', default='media/default.png')


```

<br>

#### shell

- install pillow for uploading the image 

```

pip install pillow 
migrations 

```

<br>

#### settings.py

- add the directory path for saving images

```

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

```

<br>

#### apps/urls.py

- save images in local 

```python

from django.conf.urls import url
from django.conf import settings
from django.views.static import  serve

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT>)
    ]

```

<br>

#### apps/templates/index.html

- changing form type for uploading files

```html 

       <form enctype="multipart/form-data" action="post_url/" method="post">
            <input type="submit" value = "submit">
        </form>

```


<br>

#### apps/views.py

- add request files for uploading the image file in the forms.py

```python 

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')


```

<br>

#### apps/forms.py

```python 

from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'material','location','image']


```


<hr>


<br>


### Adding Users

<hr>

#### Model Relationships

1. One-to-One relationship
2. One-to-Many Relationship
    - Users need to created as this model
3. Many-to-Many Relationship 


#### app/models.py

```python 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits= 10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')

```

<br>

#### app/views.py


``` python

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()

    return HttpResponseRedirect('/')
    
    
def profile(request, username):
    user = User.objects.get(username = username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html', {'username' : username, 'treasures' : treasures>)


```



<br>

#### app/urls.py


```python 


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^post_url/$', views.post_treasure, name='post_treasure'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT>)
    ]

```



<hr>

<br> 

### Login Ability 

<hr>

#### app/views.py
 
``` python

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('Account is disabled ')
            else:
                print('password is incorrect')
    else:
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form' : form>)

    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

```

<br>

#### app/forms.py 

``` python 

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length = 64)
    password = forms.CharField(widget=forms.PasswordInput())
    
```

<br>

#### app/urls.py

```python

urlpatterns = [
    url(r'^login/$', views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]

```

<br>

#### app/templates/base.html


```html

<< extends 'base.html' >>
<< load staticfiles >>

<< block content >>

        << for treasure in treasures >>
            <div class = 'content_box col-xs-4'>
                <p><a href="<treasure.id>">< treasure.name > </a> </p>
                <p><a href="user/< treasure.user.username >"> by: < treasure.user.username ></a></p>
                <p><img class='content_image' src="<treasure.image.url>" alt=""></p>
            </div>
        << endfor >>

        <div class="col-xs-12">
        <form enctype="multipart/form-data" action="post_url/" method="post">
            << csrf_token >>
            < form.as_p >
            <input type="submit" value = "submit">
        </form>
        </div>

<< endblock >>

```

<hr>

<br>

### Ajax 


<hr>

#### main_app/static/jsfile

```javascript

$(document).ready(function(){

    $('button').click(function(e){

        e.preventDefault();
        var element = $(this);

        $.ajax({
            url : '/like_treasure/',
            type : 'GET',
            data : { treasure_id : element.attr('data_id')},
            success : function(response){
                    element.html('likes '+ response)
            }
        })

    });

})

/* 
    IF POST 
    We need to add the csrfToken by using cookie 
*/


$(document).ready(function(){

    $('button').click(function(e){

        e.preventDefault();
        var element = $(this);

        var csrftoken = getCookie('csrftoken')

        $.ajax({
            beforeSend: function(xhr, settings){
                if(!csrfSafeMethod(settings.type) && !this.crossDomain){
                    xhr.setRequestHeader('X-CSRFToken', csrftoken)
                }
            },

            url : '/like_treasure/',
            type : 'POST',
            data : { treasure_id : element.attr('data_id')},
            success : function(response){
                    element.html('likes '+ response)
            }
        })

    });

})


function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie != ''){
        var cookies = document.cookie.split(';');

        $(cookies).each(function(index, cookie){

            if (cookie.substring(0, name.length+1)== (name + '=')){
                       cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            }

        })
    }
    return cookieValue;
}

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


```


<br>

#### main_app/views.py

```python 

def like_treasure(request):
    treasure_id = request.GET.get('treasure_id', None)
    likes = 0

    if treasure_id:
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()
    return HttpResponse(likes)


```


<br>


#### main_app/models.py

```python 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treasure(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits= 10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
    likes = models.IntegerField(default=0)

```




