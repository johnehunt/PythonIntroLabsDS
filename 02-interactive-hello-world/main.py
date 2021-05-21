print('Hello World')
name = input('Please enter your name: ')
print('Welcome', name)

input1 = int(input('Please enter a number: '))
input2 = int(input('Please enter another number: '))

value = input1 + input2
print(f'The result of {input1} + {input2} is', value)
print('The type of the value is', type(value))

input_string1 = input('Please enter a string: ')
input_string2 = input('Please enter another string: ')
value = input_string1 + input_string2
print('The new value is', value)
print('The type of the value is now', type(value))

title = 'Data Processing App Version' + str(1.0)
print(f'The title of this app is {title}')

user = None
print('user:', user)
print('user is None:', user is None)
print('user is not None:', user is not None)
print('The type of the user', type(user))
