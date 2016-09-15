---
published: true
title: Learning about Python basics
layout: post
category: programming
permalink: /programming/
---

### List and Dictionaries
Lists will contain every type of data
<br>This is due to the usage of link-array rather than simple array 
<br>Interpret Languages such as javascript and Python use list as a linked array

``` python
# an empty list
empty=[]

# list of numbers
nums = [10, 20, 30, 40.5]

# list of strings
words ] ['cheerio', 'cheers', 'wacha', 'hiya']

# list of mixed items
anything = [10, 'hello', 'ahoy', 123.5]
```
<br>
<br>the list items are **ordered** starting with index

``` python
greetings = ['cheers', 'cheerio', 'watcha', 'hiya'] 

#cheers
greetings[0]

#hiya
greetings[3]

#cheerio, watcha
greetings[1:3]

```

<br>
<br> Create a list and add items 
<br> Removing items 

``` python
slang = ['cheerio', 'pip pip', 'smashing']
print(slang)

slang.append('cheecky')
print(slang)

#ways for removing cheecky
slang.remove('cheecky')
del slang[3]

```

<br>
 
### Dictionary
The data has a key and value

``` python
slang = {'cheerio' : 'goodbye'
	, 'knackered' : 'tired'
 	, 'yonks': 'ages'
	}
print(slang['cheerio'])

#creating dicitionary and adding values
#same goes for the updates
slang = {}
slang['knachered'] = 'tired'
slang['smashing'] = 'terrific'
print(slang)

#removing the values
del slang['cheerio']

#get the value
result = slang.get('bloody')

#print the value which exits
if result:
	print(result)
else:
	print('key does not exists')

```

<br>
### Comparing List
<br>Checking whether the lists are equal or not 
``` python
my_list = [1,2,3,4]
your_list = [1,2,3,4]

print(my_list==your_list) #true 

```
<br>
<br> compare with the dictionary 
``` python
#order does not matter in dictionary 

my_dict = {1:1, 2:2, 3:3}
your_dict = {2:2, 3:3, 1:1}

print(my_dict==your_dict) #true 

```



 







