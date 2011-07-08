"""
Copyright (c) 2011 Martin Prout
 
This module is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

csgrammar.py module
Supports the parsing of 1-L lsystem rules with ignore
axiom/rules are evaluated by the produce function, the repeat function 
is used to repeatedly iterate the rules in a recursive fashion.

Example Rules:

Non-Context-Sensitive = { "A": "A+F", "G": "GG", "X" :"G-G"}

Context-Sensitive = { "A<F": "G"}
"""

# string walk constants
LEFT = -1
RIGHT = 1

def __context(a):
    """
    Private helper function returns a tuple of value, index and context from key 'a'
    Valid direction setters are '>' or '<' else no direction is set
    """
    index = 0
    before =  a[1] == '<' if len(a) == 3 else False # python ternary operator
    after =  a[1] == '>' if len(a) == 3 else False # python ternary operator
    cont = a[0] if (before or after) else None
    if (before): 
        index += LEFT
    if (after): 
        index += RIGHT
    value = a[2] if len(a) == 3 else a[0]    
    return (value, index, cont)

def __getContext(path, index, direction, ignore):
    """
    Private helper returns context character from path[index + direction], 
    skipping any ignore characters
    """
    skip = 0
    while path[direction + index + skip] in ignore:
        skip += direction
    return path[direction + index + skip] 
    
        
def hasContext(a, b, index, ignore):
    """
    from a given key, axiom/production string and index returns
    has context boolean (ignoring characters in IGNORED)
    """
    cont = False
    if __context(a)[0] == b[index] and __context(a)[1] != 0:
        if __context(a)[1] == LEFT and index > 0:     # guard negative index
            cont = __context(a)[2] == __getContext(b, index, LEFT, ignore)
        elif __context(a)[1] == RIGHT and index < len(b) - 1: # guard out of range index
            cont = __context(a)[2] == __getContext(b, index, RIGHT, ignore)  
    return cont

def produce(ax, rules, ignore):
    """
    generate production from axiom and rules
    """
    str_buf = []   # initialize string buffer
    csrule = {}    # initialize context sensitive dict
    for key in rules.keys():
        if len(key) == 3:
            csrule[key[2]] = key
    for i, a in enumerate(ax):
        r = csrule.get(a, a)
        if (r == a):  # handle as a cf rule
            str_buf.append(rules.get(a, a))
        else:         # handle as a cs rule
            if hasContext(r, ax, i, ignore):
                str_buf.append(rules.get(r))
            else:
                str_buf.append(r[2])
    return ''.join(str_buf) # join str_buf list as a single string
    

def repeat(rpx, axiom, rules, ignore):
    """
    Repeat rule substitution in a recursive fashion rpx times
    """ 
    production = axiom
    from itertools import repeat
    for _ in repeat(None, rpx):
        production = produce(production, rules, ignore)
    return production
    
       
