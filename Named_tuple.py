import collections

User = collections.namedtuple('User', 'name age gender')
shubham = User(name='Shubham', age=23, gender='M')
print(shubham)

print('Name of User: {0}'.format(shubham.name))