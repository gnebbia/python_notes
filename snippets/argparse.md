# Python Snippets

In this repository I will put all the python snippets of code I found useful.


* [Basics](basics)
* [Globs](globs)
* [Regex](regex)

## Files

Select all the files with extension .py recursively,
but exclude a set of directories:

```python
exclude_dirs = ['./env/','./docs/']
    exclude = re.compile('(%s)' % '|'.join(map(re.escape, exclude_dirs)))


for filename in glob.iglob('./**/*.py', recursive=True):
        if not exclude.match(filename):
                    print(filename)
```
