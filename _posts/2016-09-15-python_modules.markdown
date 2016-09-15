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




