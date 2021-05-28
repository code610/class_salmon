# import re
# import os
# import subprocess
# import sys
#os.system("pip install numpy")
#path = C:\Users\aznkr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages
#import numpy as np

# for p in sys.path:
#     print(p)



filename = "contacts_list_working.csv"
open_file = open(filename)

# encoding: utf-8
# module _csv
# from (built-in)
# by generator 1.147
"""
CSV parsing and writing.

This module provides classes that assist in the reading and writing
of Comma Separated Value (CSV) files, and implements the interface
described by PEP 305.  Although many CSV files are simple to parse,
the format is not formally defined by a stable specification and
is subtle enough that parsing lines of a CSV file with something
like line.split(",") is bound to fail.  The module supports three
basic APIs: reading, writing, and registration of dialects.


DIALECT REGISTRATION:

Readers and writers support a dialect argument, which is a convenient
handle on a group of settings.  When the dialect argument is a string,
it identifies one of the dialects previously registered with the module.
If it is a class or instance, the attributes of the argument are used as
the settings for the reader or writer:

    class excel:
        delimiter = ','
        quotechar = '"'
        escapechar = None
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = QUOTE_MINIMAL

SETTINGS:

    * quotechar - specifies a one-character string to use as the
        quoting character.  It defaults to '"'.
    * delimiter - specifies a one-character string to use as the
        field separator.  It defaults to ','.
    * skipinitialspace - specifies how to interpret whitespace which
        immediately follows a delimiter.  It defaults to False, which
        means that whitespace immediately following a delimiter is part
        of the following field.
    * lineterminator -  specifies the character sequence which should
        terminate rows.
    * quoting - controls when quotes should be generated by the writer.
        It can take on any of the following module constants:

        csv.QUOTE_MINIMAL means only when required, for example, when a
            field contains either the quotechar or the delimiter
        csv.QUOTE_ALL means that quotes are always placed around fields.
        csv.QUOTE_NONNUMERIC means that quotes are always placed around
            fields which do not parse as integers or floating point
            numbers.
        csv.QUOTE_NONE means that quotes are never placed around fields.
    * escapechar - specifies a one-character string used to escape
        the delimiter when quoting is set to QUOTE_NONE.
    * doublequote - controls the handling of quotes inside fields.  When
        True, two consecutive quotes are interpreted as one during read,
        and when writing, each quote character embedded in the data is
        written as two quotes
"""
# no imports

# Variables with simple values

QUOTE_ALL = 1
QUOTE_MINIMAL = 0
QUOTE_NONE = 3
QUOTE_NONNUMERIC = 2

__version__ = '1.0'

# functions

def field_size_limit(limit=None): # real signature unknown; restored from __doc__
    """
    Sets an upper limit on parsed fields.
        csv.field_size_limit([limit])
    
    Returns old limit. If limit is not given, no new limit is set and
    the old limit is returned
    """
    pass

def get_dialect(name): # real signature unknown; restored from __doc__
    """
    Return the dialect instance associated with name.
        dialect = csv.get_dialect(name)
    """
    pass

def list_dialects(): # real signature unknown; restored from __doc__
    """
    Return a list of all know dialect names.
        names = csv.list_dialects()
    """
    pass

def reader(iterable, dialect='excel', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    csv_reader = reader(iterable [, dialect='excel']
                            [optional keyword args])
        for row in csv_reader:
            process(row)
    
    The "iterable" argument can be any object that returns a line
    of input for each iteration, such as a file object or a list.  The
    optional "dialect" parameter is discussed below.  The function
    also accepts optional keyword arguments which override settings
    provided by the dialect.
    
    The returned object is an iterator.  Each iteration returns a row
    of the CSV file (which can span multiple input lines).
    """
    pass

def register_dialect(name, dialect=None): # real signature unknown; restored from __doc__
    """
    Create a mapping from a string name to a dialect class.
        dialect = csv.register_dialect(name[, dialect[, **fmtparams]])
    """
    pass

def unregister_dialect(name): # real signature unknown; restored from __doc__
    """
    Delete the name/dialect mapping associated with a string name.
        csv.unregister_dialect(name)
    """
    pass

def writer(fileobj, dialect='excel', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    csv_writer = csv.writer(fileobj [, dialect='excel']
                                [optional keyword args])
        for row in sequence:
            csv_writer.writerow(row)
    
        [or]
    
        csv_writer = csv.writer(fileobj [, dialect='excel']
                                [optional keyword args])
        csv_writer.writerows(rows)
    
    The "fileobj" argument can be any object that supports the file API.
    """
    pass

# classes

class Dialect(object):
    """
    CSV dialect
    
    The Dialect type records CSV parsing and generation options.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    doublequote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    escapechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lineterminator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quotechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quoting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipinitialspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod object at 0x000001525ABD6460>, 'find_spec': <classmethod object at 0x000001525ABD6490>, 'find_module': <classmethod object at 0x000001525ABD64C0>, 'create_module': <classmethod object at 0x000001525ABD64F0>, 'exec_module': <classmethod object at 0x000001525ABD6520>, 'get_code': <classmethod object at 0x000001525ABD65B0>, 'get_source': <classmethod object at 0x000001525ABD6640>, 'is_package': <classmethod object at 0x000001525ABD66D0>, 'load_module': <classmethod object at 0x000001525ABD6700>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

_dialects = {}

__spec__ = None # (!) real value is "ModuleSpec(name='_csv', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

contacts_list = []

def menu(selection):
    #contacts_list[name(name)]
    #fav_food = str(input("Enter a favorite food: "))
    #fav_color = str(input("Enter a favorite color: "))
    switch_menu = {
        1: create_record(gather_input()),
        2: retrieve_record(),
        3: update_record(),
        4: delete_record(),
    }

    # key = N
    # print(switch_menu.get(1, "Invalid Choice"))
    return switch_menu.get(selection, "Invalid Choice")

def gather_input():
    name = input("Enter a name: ")
    fav_food = input("Enter a food: ")
    fav_color = input("Enter a color: ")
    return {"name": name}

def create_record(gather):
    #print(gather)
    #print(contacts_list)
    #for item in range(len(contacts_list)):
    #    print(contacts_list[item][gather])
    return

def retrieve_record():
    return

def update_record():
    return

def delete_record():
    return


# with open(filename) as file_obj:
#     #print(type(file_obj))
    
#     clean_lines = re.split("\n|,", file_obj.read())
#     #print(type(lines))
#     #print(lines)
#     #print(x for x in clean_lines)

#     for c in clean_lines:
#         print(c)
# file_obj.close()

with open(filename) as file_obj:
    #print(re.split(",|\n", file_obj.read()))
    # Count the # of items for header
    lines = file_obj.read().strip().split("\n")
    #print(len(lines[0].split(",")))


# with open(filename) as file_obj:
#     find_header_count = len(lines[0].split(","))

#     column_1 = []
#     for c in clean_lines[::3]:
#         column_1.append(c)
    
#     print(column_1)
# file_obj.close()


    #print(lines[0])
    # Separate items in the list
    #clean_for_headers = lines[0].split(",")

    #for l in re.split(",", file_obj.read().strip()):
        #print(l)
        #diction = {i: lines[i] for i in range(0, find_header_count)}

    #print(diction)
    #print(clean_for_headers[0])

    #header_list = []
    #header_value = []
    # Remove the headers
    headers = lines.pop(0)
    
    #for l in lines:
    #    print(l)

    #print(clean_lines)
    #for c in clean_lines:
       # print(c)
    # results = []
    # for line in file_obj:
    #     word = line.split(",")
    #     word = word[0].split(",")
    #     results.append((word))

    # print(results)
    print(f"Headers: {headers}")

    header_items = headers.split(",")

    # print(header_items)
    
    # for h in header_items:
    #     print(h, "line 29")

    #     for l in lines:
    #         print(l, "line 32")

    #         l_items = l.split(",")
    #         print(l_items, "line 35")

    #         for each in l_items:
    #             print(each, "line 38")
    #             break

    #header_list.append(headers)
    #print(lines,"line 16")

    #print(lines[0].split(",")[0])

    #for l in lines:
    #    l_value = str(l).split(",").pop(0)
    #    header_value.append(l_value)

    #dict_entry = {header_list + header_value}
    #print(dict_entry)

    #print(header_list)
    #print(header_value)

    #contact_dict = dict(zip(header_list,header_value))
    #print(contact_dict)

    #for v in header_value:
    #    contact_list = {{header_value}: v}

    #print(contact_list)
    #contact_dict =(hl: hv for hl,hv in zip(header_list, header_value))

#my_dict = [{header: lines[0].split(",")[0] for header,line in zip (headers, lines[0].split(","))}]
#print(my_dict)
for l in lines:
    #print(l.split(","), "line 19")
    line_list = l.split(",")
    contacts = dict(zip(header_items,line_list)) 
    contacts_list.append(contacts)

    #contacts = [contacts]
#print(contacts_list)

#print(contacts_list[])
    #data = lines[1:]
    #print(data)
    #print(lines.split(","))

    #print(lines[0].split(",", 1))

    # For each remaining line. Create a dict and append to list
    #contact_list = [{key: l.split(",", 1)} for key in headers for l in lines]
    #print(contact_list)


# for line in open_file:
#     print(range(len(line)))
#     line_index = line.split(',')
#     list(line_index)
#     print(type(line))
#     print(line_index)
#     contacts_list = dict.fromkeys(line_index)
#     break
#     for i in range(len(line_index)):
#         print(i, line_index[i])
#         contacts_list = dict.fromkeys(i)

#         contacts_list.insert({i}, {line_index[i]})

# print(contacts_list)

# output
# <class 'str'>
# ['name', 'favorite food', 'favorite color\n']
# {'name': None, 'favorite food': None, 'favorite color\n': None}

# switch_menu = {
# 1: create_record(),

# 2: retrieve_record(),1

# 3: update_record(),

# 4: delete_record(),
# ::
# n: n,
# }

# key = N
# value = switch_menu.get(key, "default")

print(menu(int(input(f"""
Make a selection
1) Create Record
2) Retrieve Record
3) Update Record
4) Delete Record
Choice: """))))