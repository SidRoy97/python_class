print(list(map(lambda x : x % 2, range(5))))
print(list(filter(lambda x : x % 2, range(5))))

a = [ 'kalidasa', 'kuvempu', 'bendre', 'karanta', 'maasti' ]
# convert all strings to uppercase and pick those having more than 6 char

# terrible
print(list(filter(lambda s : len(s) > 6 , map(str.upper, a))))

print(list(map(str.upper, filter(lambda s : len(s) > 6, a))))

