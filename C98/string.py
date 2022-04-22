#simple splitting with space
text="One Two Three"
print(text.split( ))

ingredients='Milk, Bread, Dough, Butter'

#split with comma
print(ingredients.split(', '))
#split with colon
print(ingredients.split(':'))

#splits "maxsplit" number of items

#separate only first 2 items
print(ingredients.split(',',2))

#separate only the first item
print(ingredients.split(',',1))

#separate the first 5 items (only separates first 4 because there is no 5th separator)
print(ingredients.split(',',5))

#separates 0 items and returns 1 whole string
print(ingredients.split(',',0))