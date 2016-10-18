#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, re, io

class open_for_lines:
    def __init__ (self, filename, mode):
        if isinstance(filename, io.IOBase):
            self.fhandle = filename
            self.has_opened = False
        else:
            self.fhandle = open(filename, mode)
            self.has_opened = True
        self.unreadlines = []
            
    def __enter__ (self):
        return self

    # Prendiamo la successiva riga del file oppure la prima in unreadlines
    def get_line (self):
        if len(self.unreadlines) > 0:
            return self.unreadlines.pop(0)
        else:
            return self.fhandle.readline()

    # Rimettiamo la riga in coda a quelle ancora da leggere
    def unget_line (self, line, index='end'):
        if index == 'end':
            self.unreadlines.append(line)
        else:
            self.unreadlines.insert(index, line)
        
    # Salta le righe fino a quando non trova una riga che soddisfa
    # l'espressione regolare passata. Restituisce il match.
    def skipuntil (self, regex):
        match = None; line = '\n';
        while line != '' and (match is None):
            line = self.get_line()
            match = re.search(regex, line)
        self.unget_line(line)
        return match
    
    # Salta il numero di righe indicato, rimanendo fermo alla fine del
    # file (cioè non va più avanti). Ritorna l'ultima riga saltata.
    def skiplines (self, number):
        for i in range(0, number):
            line = self.get_line()
        return line

    # Stampa il numero di righe indicato, senza superare la fine del
    # file. Ritorna l'ultima riga.
    def printlines (self, number):
        for i in range(0, number):
            line = self.get_line()
            print(line, end='')
        return line

    # Stampa le righe fino a quando soddisfano l'espressione regolare.
    # Ritorna il match dell'ultima riga
    def printuntil (self, regex):
        match = None; line = '\n';
        while line != '' and (match is None):
            line = self.get_line()
            match = re.search(regex, line)
            if line != '' and (match is None):
                print(line, end='')
        self.unget_line(line, 0)
        return match
            
    def __exit__ (self, typel, value, traceback):
        if self.has_opened:
            self.fhandle.close()

# Use example: print from a file all lines after shopping list:
# with open_for_lines("varie.txt", "r") as f:
#     f.skipuntil('^Shopping list:')
#     f.skiplines(1)
#     f.printuntil('^\n$')

