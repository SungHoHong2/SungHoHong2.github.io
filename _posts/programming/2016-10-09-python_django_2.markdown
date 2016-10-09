---
published: true
title: Django Image Upload
layout: post
category: programming
permalink: /programming/
---


### Adding User-Uploaded Images 

<hr>

Required steps to setup ImageField

1. add ImageField to the model
2. Install Pillow - an image-processing library necessary for Image field 
3. Migrate changes 
4. Update settings.py to add a media director y
5. Add a special debugging URL to urls.py to server our media files locally 

<br>

app/models

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

shell

- install pillow for uploading the image 

```

pip install pillow 
migrations 

```

<br>

settings.py

- add the directory path for saving images

```

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

```

<br>

apps/urls.py

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
        url(r'^media/(?P<path>.*)$', serve, {'document_root' : settings.MEDIA_ROOT})
    ]

```

<br>

apps/templates/index.html

- changing form type for uploading files

```html 

       <form enctype="multipart/form-data" action="post_url/" method="post">
            <input type="submit" value = "submit">
        </form>

```


<br>

apps/views.py

- add request files for uploading the image file in the forms.py

```python 

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')


```

<br>

apps/forms.py

```python 

from django import forms
from .models import Treasure

class TreasureForm(forms.ModelForm):
    class Meta:
        model = Treasure
        fields = ['name', 'value', 'material','location','image']


```


<hr>





