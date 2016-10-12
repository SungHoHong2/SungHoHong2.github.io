---
published: true
title: Django Models
layout: post
category: programming
permalink: /programming/
---


<hr>

### Choices 

``` python 

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    # Selecting choices

    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    )

    shirt_size = models.CharField(max_length=1, choices = SHIRT_SIZES)

```


```
>>> p1.shirt_size
'S'

>>> p1.get_shirt_size_display()
'Small'

```

<hr>

<br>



<hr>

### returning the list of strings 


```
>>> Fruit.objects.values_list('name')
<QuerySet [('Apple',), ('Pear',)]>

>>> Fruit.objects.values_list('name', flat=True)
<QuerySet ['Apple', 'Pear']>

```

<hr>


<br>



<hr>

### Many to One Relationship 


```python

from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person =models.ForeignKey(Person, on_delete= models.CASCADE )
    group = models.ForeignKey(Group, on_delete= models.CASCADE )
    date_joined = models.DateField
    invite_reason = models.CharField(max_length=64)

```



```

>>> from models_2.models import Membership
>>> from models_2.models import Group
>>> 
>>> 
>>> ringo = Person.objects.create(name = 'Ringo Starr')
>>> paul = Person.objects.create(name = 'Paul McCartney')
>>> beatles = Group.objects.create(name = 'The Beatles')



>>> m1= Membership(person = ringo, group = beatles, invite_reason = 'new drummer')
>>> m1.save()


***** Group calls the Members 

>>> beatles.members.all()
<QuerySet [<Person: Person object>]>

>>> Group.objects.get(id=1).members.all()
<QuerySet [<Person: Person object>]>

>>> Group.objects.get(id=1).members.first()
<Person: Person object>

>>> Group.objects.get(id=1).members.get(id=1)
<Person: Person object>



***** Member calls the Group 

>>> ringo.group_set.all()
<QuerySet [<Group: Group object>]>

>>> Person.objects.first().group_set.all().first()
<Group: Group object>




****** Things that won't work 

beatles.members.add(join)
beatles.members.create(name='Adding people')
beatles.members.set([join, paul, ringo, george])



****** if data is removed 
        all data is removed

>>> beatles.members.clear() 

```

<hr>
 
<br>



<hr>

### In-depth search 


``` 

**** Using filter Search in many to many

>>> Group.objects.filter(members__name__startswith='')
<QuerySet [<Group: Group object>]>



**** Using classes for getting the intersecting table 

>>> Membership.objects.get(group=beatles)
<Membership: Membership object>
>>> 
>>> Membership.objects.get(group=beatles, person= ringo)
<Membership: Membership object>


```

<hr>


### Difference between blank and null 

- Field.null

> If True, Django will store empty values as NULL in the database. Default is False.
Note that empty string values will always get stored as empty strings, not as NULL. Only use null=True for non-string fields such as integers, booleans and dates. For both types of fields, you will also need to set blank=True if you wish to permit empty values in forms, as the null parameter only affects database storage (see blank).
Avoid using null on string-based fields such as CharField and TextField unless you have an excellent reason. If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string. In most cases, it’s redundant to have two possible values for “no data;” Django convention is to use the empty string, not NULL.


- Field.blank

> If True, the field is allowed to be blank. Default is False.
Note that this is different than null. null is purely database-related, whereas blank is validation-related. If a field has blank=True, validation on Django’s admin site will allow entry of an empty value. If a field has blank=False, the field will be required.



<br>


<hr>

### Overriding predefined model methods 

```python

from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.name == 'NOT SAVE'
            return 
        else:
            super(Blog, self).save(*args, **kargs)

```


<hr>


<br>

<hr> 

### Using Raw SQL 

- using Manager.raw() which returns the model instances 

``` 

>>> Person.objects.raw('select id from models_1_person')
<RawQuerySet: select id from models_1_person>

>>> Person.objects.raw('select id from models_1_person')[0]
<Person: Person object>

>>> Person.objects.raw('select id from models_1_person')[0].id

```

- avoid the model layer and execute custom SQL 

``` python

from django.shortcuts import render
from django.db import connection
# Create your views here.


def index(request):
    with connection.cursor() as cursor:

        # Returning the QuerySet with a SET
        cursor.execute('SELECT first_name from models_1_person')
        row = cursor.fetchone()


        # Returning the QuerySet with Dictionaries in List
        row = dictfetchall(cursor)
    return render(request, 'index.html', {'persons' : row})



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [ dict(zip(columns, row)) for row in cursor.fetchall()]

```


<hr>




