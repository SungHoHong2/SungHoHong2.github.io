---
published: true
title: Learning about Python basics
layout: post
category: languages
permalink: /languages/
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






