#!/usr/bin/env python

# Defined a Riley class
class Person(object):
    
    def __init__(self, isMadAtYoutube):
        self.isMadAtYoutube = isMadAtYoutube
        
    def uMad(self):
        if self.isMadAtYoutube:
            print "He's mad."
        else:
            print "He's still mad."
        
Riley = Person(True)

bool_four = Riley.uMad()

# Prompt user for input
s = raw_input('-->')

print s

# First added commit
