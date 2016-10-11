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











