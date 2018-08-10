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
parser = argparse.ArgumentParser(description='Optional app description')

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

