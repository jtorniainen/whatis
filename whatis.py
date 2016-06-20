#!/usr/bin/env python3

# A diagnostics tool (think of it as a modernized 'inspect' module)
# Finnish Institute of Occupational Health, 2016
# MIT License

# Currently missing: set, type


def whatis_string(variable):
    """ Prints type and length. """
    print('{} [{}]'.format(type(variable), len(variable)))


def whatis_numeric(variable):
    """ Prints type. """
    print(type(variable))


def whatis_sequence(variable):
    """ Prints type, size and types inside the sequence. """
    types = []
    for item in variable:
        types.append(type(item))
    print('{} [{}] {}'.format(type(variable), len(variable), set(types)))


def whatis_object(variable):
    """ Prints type, attributes and methods."""
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
    """ Prints type and first sentence of documentation. """
    if variable.__doc__:
        doc = variable.__doc__.split('.')[0]
    else:
        doc = '<no docstring>'
    print('{}\n{}'.format(type(variable), doc))


def whatis(variable):
    """ Main function """

    # Check if variable belongs to built-in types
    if isinstance(variable, (float, int, complex, bool)):
        whatis_numeric(variable)
    elif isinstance(variable, str):
        whatis_string(variable)
    elif isinstance(variable, (list, dict, tuple)):
        whatis_sequence(variable)
    elif callable(variable):  # Function (or constructor)
        whatis_function(variable)
    else:  # Object
        whatis_object(variable)
