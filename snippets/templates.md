# String Templates

we need an import string

Let's see 3 different ways to build
templates:
```python
import string
values = {'var': 'foo'}
t = string.Template("""
Variable : $var
Escape : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))
s = """
Variable : %(var)s
Escape : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)
s = """
Variable : {var}
Escape : {{}}
Variable in text: {var}iable
"""
print('FORMAT:', s.format(**values))
```


