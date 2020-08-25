## Get all methods available for an object

```python
dir(x)
```
we can be more specific and get all the methods which
the developers want us to use (excluding the dunder methods)
with:

```python
[method for method in dir(a) if not method.startswith('_')]
```

## Getting documentation for Python objects and methods

```python
help(a.method)
```

## Get the source code of a function


```python
import inspect
lines = inspect.getsource(foo)
print(lines)
```
