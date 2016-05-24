abc = ['nhao', "sjoggd", '我好啊']
print(abc)
print(len(abc))
print(abc[0])
print(abc[1])
print(abc[len(abc) - 1])
abc.append('admin')
print(abc)
abc.insert(1, 'xiaolong')
print(abc)
abc.pop()
print(abc)
abc[1] = 'hello world'
abc.pop(0)
print(abc)
one = ['apple', 'banana', 12345, True]
print(one)
jack = ['pan', one, 789, 'google']
print(jack)
work = ('a', 'b', 'c')
print(work)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][3])