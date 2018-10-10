# Python gnc tutorial

## Introduction

We can launch python in the following ways:

```python
# launches a python script
python script.py

# launches a script in interactive mode, so that we can interact with the
# environment
python -i script.py
```

A useful enhanced python shell is *ipython*, i highly recommend
getting used to it, it has a lot of nice features and may be helpful for testing purposes.

#### Enhanced python shell: ipython

In order to plot stuff with matplotlib we can do:
```python
%pylab
```
or simply import matlab as usual, knowing that plots will be shown only when we
execute the show() function.


### Basic Data Structures

### Loops


### Substituting Shell with Python
Here we will implement in python some of the common things we would do usually with shell
scripting. 

### List Comprehensions

### Functions

```python
def optimize(w, b, X, Y):
    """
    This function optimizes w and b by running a gradient descent algorithm
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    print_cost -- True to print the loss every 100 steps
    
    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.
    """

    ### INSERT CODE HERE ### 

    return params, grads, costs
```


### Script Template


### Organizing Projects

### Testing with pytest
The three major testing frameworks for python are:

* unittest (shipped with the standard library and very minimal)
* nose
* pytest (we will focus on this one)

### Finding out information about a python object
Python has a strong set of introspection features.

Take a look at the following built-in functions:

    type()
    dir()
    id()
    getattr()
    hasattr()
    globals()
    locals()
    callable()

type() and dir() are particularly useful for inspecting the type of an 
object and its set of attributes, respectively.
Another very useful for inspecting things in python is the **inspect** module.


## Python Data Model

### Dunder Methods


## Data Structures


## Decorators and Generators


## Design Patterns


