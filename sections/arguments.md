# Command Line Parameters Parsing

From python documentation we can read:
*Parameters starting with - or -- are usually considered optional. 
All other parameters are positional parameters and as such 
required by design (like positional function arguments). 
It is possible to require optional arguments, but this is a bit 
against their design. Since they are still part of the non-positional 
arguments, they will still be listed under the confusing header 
"optional arguments" even if they are required. The missing square 
brackets in the usage part however show that they are indeed required.*

We can sum up this by saying that When we parse parameters on command line 
we generally speak about different things:
* Arguments (which are required)
* Options (which are optional and generally provided with `--` or `-`)

There is an exception, e.g., some people use required named required
arguments, but this is another story.


## Snippets with argparse

### General Workflow

Let's see a very general example of snippet using argparse:
```python

parser = argparse.ArgumentParser(description='Optional app description', prog='myprog', allow_abbrev=False)
# here we give the program description, the program name
# and if we want to enable/disable automatic argument abbreviations

# Required positional argument
parser.add_argument('pos_arg', type=int, help='A required integer positional argument')

# Optional positional argument
parser.add_argument('opt_pos_arg', type=int, nargs='?', help='An optional integer positional argument')
# Optional argument
parser.add_argument('--opt_arg', type=int, help='An optional integer argument')
# Switch
parser.add_argument('--switch', action='store_true', help='A boolean switch')

args = parser.parse_args()


# Check values
if args.pos_arg > 10:
        parser.error("pos_arg cannot be larger than 10")
if args.opt_pos_arg < 3:
        parser.error("opt_pos_arg cannot be less than 3")


# Access values
print(args.pos_arg)
print(args.opt_pos_arg)
print(args.opt_arg)
print(args.switch)
```
Notice that for each argument we may specify if it is optional, or if it takes
more values with `nargs`:
* `nargs='?'`: optional parameter
* `nargs='+'`: accepting multiple values parameter

Let's see other cases where we only use optional parameters:


```python
import argparse

parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument("--inputsurv", help="the input dataset, representing the good judgement yearly survey csv file")
parser.add_argument("--inputquest", help="the input dataset, representing the good judgement yearly survey csv file")
parser.add_argument("--outputf", help="the output dataset, representing a processed file that can be used to feed a general neural network")
args = parser.parse_args()

print(args.inputsurv)
```


Another example with only optional arguments:
```python
import argparse
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument(
    "--input",
    help="input dataset",
    default="ds_short.csv",
    type=str)
parser.add_argument(
    "--epochs",
    help="number of epochs in the training phase",
    default=5,
    type=int)
parser.add_argument(
    "--batch_size",
    help="size of the batch to use in the training phase",
    default=64,
    type=int)

args = parser.parse_args()

# Now we can take the argument value with
print(args.input)
print(args.epochs)
```

### Parsing Arguments within the command

From time to time it happens, I want to implement a simple interpreter within
my command line program (e.g., purp), a way to do this is:

```python
parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('cmd', type=str, help="HELLOOO HELP")
parser.add_argument('--f1', type=int, help='An optional integer argument')
parser.add_argument('--f2', type=int, help='A boolean switch')

# In program parameter checking
args = parser.parse_args("inspect --f2=5 --f1=100".split())

# Check subroutines/conditionals
# ... 

# Access
print(args.cmd)
print(args.f1)
print(args.f2)

# We can also explicitly call the help with:
parser.print_help()
```


### Changing names of the parameter variables

We can make the variable containing the value name and the parameter
name independent by using the `dest` attribute when creating arguments.

So also if our parameter will be `--some-random-name` we can save it in
`args.counter` by setting `dest=counter` in the `add_argument`, let's
see an example:

```python
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('cmd', type=str, help="HELLOOO HELP")
parser.add_argument('--f1',dest='minghie', type=int, help='An optional integer argument')
parser.add_argument('--f2', dest='steekatz', type=int, help='A boolean switch')


# Access
print(args.cmd)
print(args.minghie)
print(args.steekatz)
```


### Dealing with choices and rages

```python
# in this case we constraint an integer value
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=int, choices=range(5, 10))
```


```python
parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
parser.parse_args(['rock'])
```



