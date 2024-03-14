# 6-3

glossary = {
    'string': 'a series of characters',
    'int': 'a variable type which is integer',
    'list': 'a collection of items in a particular order',
    'loop': 'take same action, or set of actions, with every item in a list',
    'dic': 'a collection of key-value pairs, it has dynamic structure',
    }

print(f"String: {glossary['string']}\n")
print(f"Int: {glossary['int']}\n")
print(f"List: {glossary['list']}\n")
print(f"Loop: {glossary['loop']}\n")
print(f"Dictionary: {glossary['dic']}\n")

# 6-4 Glossary 2
glossary['set'] = 'a collection in which each item must be unique'
glossary['float'] = 'a number with decimal fraction'
glossary['boolean'] = 'it contains only True or False'
glossary['machine learning'] = 'supervised learning and unsupervised learning'
glossary['AI'] = 'artificial intelligence'

for term, definition in glossary.items():
    print(f'{term.title()}: {definition}')

