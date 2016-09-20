---
published: true
title: Learning about Python modules
layout: post
categories: programming
permalink: /programming/python_module
---

### Functions
functions are useful when developers are repeating the 
<br> same type of algorithms over and over again 
<br>_functions are mini programs that perform a specific task_

1. Name of the function
2. Arguments of the function
3. Returns of the function 

``` python 

def average(prices):
	total = 0
	for num in prices:
		total += num
	avg = total / len(numbers)	
	return avg

numbers = [1,2,3,4,5]
my_average = average(numbers)
print(my_average)

```
 
### Function Example

``` python

menu = {'knackered Spam' :0.59
       ,'Pip pip Spam'	 :1.50 }

def print_menu(menu):
	for name, price in menu.items():
		print(name, ': $', format(price, '.2f'), sep='')		

def get_order(menu):
	orders=[]
	order = input('What would you like to order? (Q to quit)')

	while (order.upper()  != 'Q'):
		found = menu.get(order)
		if found:
			orders.append(order)
		else:
			print('Menu does not exists')

	order = input('Anything else? (Q to quit)')	
	return orders

def bill_total(orders, menu):
	total = 0
	for order in orders:
		total += menu[order]
	return total

def main():
	print_menu(menu)
	orders = get_order(menu)
	print('You ordered:', bill_total(orders, menu))

main()

```

### File Write 
One way of using the sub-memory type data
<br> steps to write a file 

``` python

# w: write
# r: read
# a: append

#open a file
sales_log = open('spam_orders.txt', 'w')

#write a file
sales_log.write('The Spam Van')

#write a file with adding new lines 
sales_log.write('Sales Log\n')

#close file
sales_log.close()

```


<br>

### Files Writing Sample

``` python

def write_sales_log(order):
	#open the file
	#append in order to prevent initializing the file during the second attempt
	file = open('sales.txt', 'a')
	
	total = 0 
	for item, price in order.items():
		file.write(item + '  '+ format(price, '.2f') + '\n')
		total += price	
	
	file.write('total = '+ format(total, '.2f') + '\n')
	file.close()

def main():
	order = { 'Cheeky spam' : 1.0
        	  'Yonks Spam'  : 4.0 } 	
	write_sales_log(order)

main()

```

### File Read

``` python

dollar_spam = open('dollar_menu.txt', 'r')

# read the entire file 
print(dollar_spam.read())

# read one line at a time 
print(dollar_spam.readline())
print(dollar_spam.readline())

# using for loop while reading file 
dollar_menu = []
for line in dollar_spam:
	# remove the (\n) in the line 
	line.strip()
	dollar_menu.append(line)
print(dollar_menu) 

dollar_spam.close()

```

<br>

### Exceptions

``` python

try:
	file = open('gogo.txt')
except:
	print('file does not exists')

```

<br>

### Using JSON to format and share data 

JSON is a standard way to format and share data 
<br> Using the Request Module will help receive HTTP requests

``` python

import requests
my_request = requests.get('http://go.codeschool.com/spamvanmenu')
menu_list = my_request.json()
print(menu_list)

print('Today's Menu')
for item in menu_list:
	print(item['name'], item['desc'], item['price'])

```

<br>

### Seperating Modules

orders.py

``` python

def print_menu(menu):
	...

def get_order(menu):
	...

def total_bill(orders, menu):
	...

```

<br>
spam_van.py

``` python

import orders

def main():
	menu = {'Cheerio Spam': 0.50 ...}
	orders.print_menu(menu)
	orders = orders.get_order(menu)
	total = orders.bill_total(orders, menu)
	print('You ordered:', order, 'Total:', total)

main()

```






