import collections

dict1 = {'day1': 'Monday', 'day2': 'Tuesday'}
dict2 = {'day3': 'Friday', 'day1': 'Friday'}

result = collections.ChainMap(dict1, dict2)

print(result.maps, '\n')

print('keys = '.format(list(result.keys())))
print('values'.format(list(result.keys())))

print()

print('All the elements form result')

for key, val in result.items():
    print('{} = {} '.format(key, val))
print( 'Find the specific value in result')

print('day1 in result: {}'.format(('day1' in result)))

# Reordering of map items

result1 = collections.ChainMap(dict2, dict2)
print(result1.maps, '\n')

# Upadating the elment of the dictionary

dict2['day3'] = 'Wednesday'

print(result1.maps, '\n')