print("hello world")
a, b = 0, 1
if a < b:
	print('a({}) is less than b ({})'.format(a, b))
else:
	print('a({}) is not less than b ({})'.format(a, b))

print('foo' if a < b else 'bar')

wf = open('README.md')
for s in wf.readlines():
	print(s, end='')

