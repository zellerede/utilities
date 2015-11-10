'''
   utility stuff: 
    - lists: 
        ShiftedList and CycleList
    - baseObject: 
        @buildOnObject decorator
    - wp:
        @withoutParenthesis decorator for cmd line usage of a function without parenthesis
    - pr2:
        PrintTo context
    - ujson
        oneliners for json Read/Write
    - symbols
        function Symbols to define symbols into preset namespace

'''

import lists
import baseObject
import wp
import pr2
import ujson

import symbols
symbols.addSymbolsTo(globals())  # Symbols created at util pkg level


