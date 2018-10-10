# Python Regex

Python uses the same syntax of Perl for what concerns regular expressions.
With some enhancements.


## Finding Patterns in Text

In order to search for patterns we use `search()`, which will return 
a match object if the pattern is found and None if it is not found.



```python
import re

pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))
```


It is often a good idea to compile our regex, especially if our program
will use it more than once.

```python
import re
# Precompile the patterns.
regexes = [ re.compile(p) for p in ['this', 'that'] ]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))
for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')
    if regex.search(text):
        print('match!')
    else:
        print('no match')
```


## Getting multiple matches

With search we just want to check if our pattern is there or not, but we can do
more, we can search for all occurrences of a specific pattern in a text
by using `findall`:

```python

import re

text = 'ciaociaociao'
pattern = 'ciao'
for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
```

Now what we can do is left to our imagination, since we could count occurrences,
or we could put all the occurrences in a list and so on.


We can also use finditer(), which produces an iterator instead of
a list of strings.

```python
import re
text = 'abbaaabbbbaaaaa'
pattern = 'ab'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(
    text[s:e], s, e))
```

A very useful feature is named groups, we can use them like this:
```python

text = "This is some text -- with punctuation."
patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
]

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print(' ', match.groups())
    print(' ', match.groupdict())
    print()
```



Another example related to Web Log Request Line parsing may be:

```python
request_line_regex = re.compile(r"""
    ^(?P<method>\S+)\s+             # HTTP method used in request
    (?P<path>\S+)\s+                # Path requested
    (?P<http_version>\S+)           # HTTP version used
""", re.VERBOSE)

text = "GET /site/home/naviga-per/studenti/acersat/acersat--- english-version/documento20060.html HTTP/1.1"


match = request_line_regex.search(text)
print(' ', match.groups())              # gets the results in the form of a tuple
print(' ', match.groupdict())           # gets the results in the form of a dictionary
```
