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
<br>Compare with the dictionary 


``` python

#order does not matter in dictionary 

my_dict = {1:1, 2:2, 3:3}
your_dict = {2:2, 3:3, 1:1}

print(my_dict==your_dict) #true 

```

<br>

### Loop Basics 

basic funciton of loops 

``` python

#creating loop
prices = [2,50, 3.50, 4.5]
total = 0
for price in prices:
	print('prices is ', price)
	total += price
	print('total is', total)

```

<br>
<br>Generating a random letter

``` python

import random

#random number from 0.0 to 1.0 
print(random.random())

#random number from the list
print(random.choice([1,2,3,4,5]))


#random number from the range 
print(random.randint(1,1000))

```

<br>
<br>Creating list for the loop 

``` python

import random 

for i in range(10): 
	ticket = random.randint(1,1000)
	print(ticket)

#start stop step values in range 
#result: 2005, 2007, 2009...
for i in range(2005,2016, 2):
	print(i)

```

<br>

### Creating the Monty Python Restaurant Menu 

 
``` python

slang = ['Knachered', 'Pip pip', 'Squidgy', 'Smashing']
menu = []

# add spams in the menu list 
for word in slang:
	menu.append(word + 'Spam')

print(menu)


# store the menu item with the prices in the dictionary 
price = 0.50
for item in menu:
	menu_prices[item] = price
	price += 1 

print(menu_prices)


# get the data from the dictionary using loop
for name, price in menu_prices.items():
	print(name,' : $', format(price,'.2f') )

```
 







