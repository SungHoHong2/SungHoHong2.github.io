---
published: true
title: Learning about Python modules
layout: post
category: programming
permalink: /programming/
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

### Files
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
### Files Sample

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





