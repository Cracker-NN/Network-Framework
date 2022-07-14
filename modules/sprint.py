import sys
import time

def sprint(string):
    list = []
    fer = ['-', "\\", "|", '/']
    for char in string:
        list.append( char )
    timer = 0
    pointer = 0
    fer_pointer = 0
    while timer < 20:
        list[pointer] = list[pointer].upper()
        print( "\r" + ("".join( str( x ) for x in list ) + " " + fer[fer_pointer]), end="" )
        list[pointer] = list[pointer].lower()
        max_fer = len( fer ) - 1
        if fer_pointer == max_fer:
            fer_pointer = -1
        max = len( list ) - 1
        if pointer == max:
            pointer = -1
        pointer += 1
        fer_pointer += 1
        timer += 1
        time.sleep( 0.1 )
        if timer == 20:
            print( "\r" + string + "\n", end="" )
            return