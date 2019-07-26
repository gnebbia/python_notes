# Strings


The string module contains a number of constants relate to ASCII and numerical
character sets.

Let's see how to explore these:

```python
import inspect
import string


def is_str(value):
    return isinstance(value, str)
for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))
```

Notice that special characters in string are interpreted, for example:
```python
print("ciao\n example string\b")
```
Will print on screen:
```output
ciao
example strin
```
so in order to not interpret them as special character we have two options:
```python
# Solution 1: Escape
print("ciao\\n example string\\b")
# Solution 2: Use the 'r' modifier
print(r"ciao\n example string\b")
```

The 'r' modifier is particularly useful when we use regexes, it is always a good
idea to insert the 'r' modifier before a regex expression.

When describing string it is a good idea to put placeholders in this manner:
```python
var1 = 'ciao'
var2 = 'arrivederci'
'my string {} and {}'.format(var1, var2)
```
