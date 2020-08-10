# Command Line Parameters Parsing

From python documentation we can read:
- Parameters starting with - or -- are usually considered optional. 
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
import argparse 


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

### Types of arguments

```python
parser.add_argument('-i', type=int)
parser.add_argument('-f', type=float)
parser.add_argument('--file', type=file)
```
We can have also more complicated things for files, such as:
```python
parser.add_argument('-i', metavar='in-file',  type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file', type=argparse.FileType('wt'))
# Note that metavar is just the name of the argument/option in the help message
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


### Types of parameters

We can have different types of parameters and options we may want for our
program, let's see some examples.

#### Boolean Options

We may want boolean options, so options which are either set or not set, and
this can be done in this way:

```python
# in this case we insert two boolean options
parser.add_argument(
    "-v","--verbose",
    dest='is_verbose',
    action='store_true',
    help="Enables verbose mode",
    default=False,
    )

parser.add_argument(
    "-s","--strict",
    dest='is_strict',
    action='store_true',
    help="Enables strict mode, where only proper (and not also related)\
    subdomains will be saved",
    default=False,
    )
```

### Lists

Here we show how to add an argument which can get multiple values:

```python
parser.add_argument(
    "websites",
    help="Specify a website",
    default=[],
    type=str,
    nargs='+',
    )
```

So from the command line we can specify something like:
```sh
python myprogram.py website1.com website2.com website3.com 
```

In the last case we specified an argument which could get multiple values, the
following example will instead show an example where we have an option which can
be specified multiple times:
```python
parser.add_argument(
    "-w", "--wordlist",
    action='append',
    help="input wordlist used for fuzzing",
    default=[],
    type=str,
    nargs='+',
    )
```
in this way we can specify from the command line something like this:
```sh
python myprogram.py --wordlist value1 --wordlist value2 --wordlist value3
```

### Files

Let's see how to specify a file as an option:
```python
parser.add_argument(
    "-o","--output",
    dest='outputfile',
    help="Save results to standard output",
    default=None,
    nargs='?',
    type=argparse.FileType('w'),
    )
```

In this case the file is optional as can be seen in `nargs=?`, we can write to
the file later in the program by doing:
```python
if args.outputfile is not None:
    args.outputfile.write('\n'.join(subdomains))
```

#### Ranges and Choices


In this case we have a constraint on the integer parameter:
```python
parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=int, choices=range(5, 10))
```


In this case we have a constraint on a string parameter:
```python
parser = argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
parser.parse_args(['rock'])
```

## Complex Parsers

By complex parsers I mean, parsers which accept subcommands with their
own flags.

For example we may build programs which as a first argument get a command
and their following arguments are indications for that command.
An example program may be:

    mycmd add --option1 flag1 --option2 blabla
    mycmd update --option1 flag1 --option2 blabla
    mycmd delete --option1 flag1 --option2 blabla

To implement such programs we may build parsers as explicited here:

```python
import argparse

def parse_args(args):
    """
    This function parses the arguments which have been passed from the command
    line, these can be easily retrieved for example by using "sys.argv[1:]".
    It returns a parser object as with argparse.

    Arguments:
    args -- the list of arguments passed from the command line as the sys.argv
            format

    Returns: a parser with the provided arguments, which can be used in a
            simpler format
    """
    parser = argparse.ArgumentParser(prog='exampleap',
                                     description='INSERT TAGLINE HERE.™')

    
    subparsers = parser.add_subparsers(help='commands', dest="command")

    # ACTIONS
    # tool add    ...
    # tool edit ...
    # tool delete ...
    list_parser   = subparsers.add_parser('list',   help='List artifacts')
    delete_parser = subparsers.add_parser('delete', help='Delete an artifact')
    add_parser    = subparsers.add_parser('add',    help='Add an artifact')
    edit_parser   = subparsers.add_parser('edit',   help='Edit an artifact')

    # List parser options/args
    list_parser.add_argument(
        "query",
        help="the query to execute",
        type=int,
        )

    # Edit parser options/args
    edit_parser.add_argument(
        "id",
        help="ID of the article",
        type=int,
        )
    edit_parser.add_argument(
        "-t", "--tags",
        help="Tags to update in the form \"tag1;tag2;...;tagN\"",
        default="",
        type=str,
        )
    edit_parser.add_argument(
        "-c", "--category",
        help="Category to update",
        default=None,
        type=str,
        )
    edit_parser.add_argument(
        "-n", "--name",
        help="Name to update",
        default=None,
        type=str,
        )
    edit_parser.add_argument(
        "-a", "--author",
        help="Author to update",
        default=None,
        type=str,
        )
    edit_parser.add_argument(
        "-s", "--status",
        help="Status to update",
        type=str,
        )

    # Add parser options/args
    add_parser.add_argument(
        "id",
        help="ID of the article",
        type=int,
        )
    add_parser.add_argument(
        "-t", "--tags",
        help="Tags to update in the form \"tag1;tag2;...;tagN\"",
        default="",
        type=str,
        )
    add_parser.add_argument(
        "-c", "--category",
        help="Category to update",
        default=None,
        type=str,
        )
    add_parser.add_argument(
        "-n", "--name",
        help="Name to update",
        default=None,
        type=str,
        )
    add_parser.add_argument(
        "-a", "--author",
        help="Author to update",
        default=None,
        type=str,
        )
    add_parser.add_argument(
        "-s", "--status",
        help="Status to update",
        type=str,
        )

    add_parser.add_argument(
        "-s", "--concurrency",
        help="number of concurrent http requests",
        default=20,
        type=int,
        )
    add_parser.add_argument(
        "-d", "--data",
        help="data passed in the body, when set, the request will be a POSt",
        action='append',
        default=[],
        type=str,
        nargs='+',
        )

    # Delete parser options/args
    delete_parser.add_argument(
        "-H", "--header",
        help="A header that will be passed within the requests",
        action='append',
        default=[],
        type=str,
        nargs='+',
        )
    edit_parser.add_argument(
        "-H", "--header",
        help="A header that will be passed within the requests",
        action='append',
        default=[],
        type=str,
        nargs='+',
        )


    return parser.parse_args(args)
```


### Creating mutually exclusive groups of options


```python
import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument('-a', action='store_true')
group.add_argument('-b', action='store_true')

print parser.parse_args()
```

## References

https://pymotw.com/2/argparse/
