#!/usr/bin/env python3

# A diagnostics tool (a modern 'inspect' module)
# Finnish Institute of Occupational Health, 2016
# MIT License

# Missing: set, type

def whatis_string(variable):
    print('{} [{}]'.format(type(variable), len(variable)))


def whatis_numeric(variable):
    print(type(variable))


def whatis_sequence(variable):
    types = []
    for item in variable:
        types.append(type(item))
    print('{} [{}] {}'.format(type(variable), len(variable), set(types)))


def whatis_object(variable):
    """ Non standard-object. """
    public = [v for v in dir(variable) if not v.startswith('__')]
    attributes = []
    methods = []
    for item in public:
        if callable(variable.__getattribute__(item)):
            methods.append(item)
        else:
            attributes.append(item)

    print(type(variable))
    print('attributes:\n{}\nmethods:\n{}'.format(attributes, methods))


def whatis_function(variable):
    if variable.__doc__:
        doc = variable.__doc__.split('.')[0]
    else:
        doc = '<no docstring>'
    print('{}\n{}'.format(type(variable), doc))


def whatis(variable):
    """ Pretty-print information about the variable. """

    # Check if variable belongs to builtin types
    if isinstance(variable, (float, int, complex, bool)):
        whatis_numeric(variable)
    elif isinstance(variable, str):
        whatis_string(variable)
    elif isinstance(variable, (list, dict, tuple)):
        whatis_sequence(variable)
    elif callable(variable):
        whatis_function(variable)
    else:  # Not a builtin
        whatis_object(variable)
