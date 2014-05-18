bread_slices=4
jars_peanutbutter=1
jars_jelly=10

if bread_slices>=2 and jars_peanutbutter>=1 and jars_jelly>=1:
	print "I'm hungry, let's make a sandwich! We can make {0} sandwiches to share or {1} open faced sandwiches.".format(bread_slices/2, bread_slices)
elif bread_slices<2 or jars_peanutbutter<1 or jars_jelly<1:
	print "No sandwiches for you."
if bread_slices<1:
	print "You really need to go to the grocery, you don't have enough bread make sandwiches."
elif jars_peanutbutter<1 
	print "You really need to go to the grocery, you don't have enough peanut butter make sandwiches."
elif jars_jelly<1:
	print "You really need to go to the grocery, you don't have enough jelly make sandwiches."
if bread_slices>=2 and jars_peanutbutter>0 and jars_jelly == 0:
	print "I guess you could have a peanut butter sandwich, but you don't have jelly, and really, what is life worth if it ain't got any jelly in it?"
