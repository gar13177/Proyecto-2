#!/usr/bin/python
# -*- coding: utf-8 -*-

from antlr4 import *
from BayesInput.BayesGrammarLexer import BayesGrammarLexer
from BayesInput.BayesGrammarParser import BayesGrammarParser
from MyCode import BayesListener
from BayesianNetwork import BayesianNetwork

from BayesUser.BayesGrammarUserLexer import BayesGrammarUserLexer
from BayesUser.BayesGrammarUserParser import BayesGrammarUserParser
from MyCode2 import BayesUserListener


from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, Button, StringVar, OptionMenu, Scale, HORIZONTAL,Entry, Text, LEFT, Y, Scrollbar, END, DISABLED, NORMAL
from tkFileDialog import askopenfilename
from ttk import Frame, Style
from ScrolledText import ScrolledText
import tkMessageBox

import networkx as nx
import matplotlib.pyplot as plt

class Example(Frame):
    

    def __init__(self, parent):
        Frame.__init__(self, parent)  
        self.parent = parent
        #self.textFrame = Frame(parent)
        self.initUI()

        
    def initUI(self):
        self.bn = None
        
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        self.errors = False
        #b.pack(padx=10, pady=10)
        Style().configure("TFrame", background="#333")

        b = Button(self, text="Nueva Gramatica", width=14, height=1, command=self.openFile)
        b.place(x= 10, y=10)

        d = Button(self, text="Ver Red Bayesiana", width=14, height=1, command=self.viewGraph)
        d.place(x= 150, y=10)

        self.text = ScrolledText(self, undo = True, width = 70, height = 10)
        self.text.place(x=10, y = 70)
        self.text.config(state= DISABLED)               

        self.consulta = StringVar()
        self.consulta.set("")
        
        self.entry = Entry(self, textvariable=self.consulta, width = 80)
        self.entry.place(x=10, y = 250)

        self.grammarPath = StringVar()
        self.grammarPath.set("descripcion1.txt")

        c = Button(self, text="Ingresar consulta", width=12, height=1, command=self.doWork)
        c.place(x=498, y=250)

        self.parent.bind("<Return>",self.onClick)

    def viewGraph(self):
        if self.bn == None:
            self.text.config(state=NORMAL)
            self.text.insert(END, ">> Ingrese una descripcion primero\n")
            self.text.config(state=DISABLED)
            return
        edge, path = self.bn.getDigraph()
        G = nx.DiGraph()
        for node in edge:
            G.add_node(node)

        G.add_edges_from(path)
        graph_pos = nx.shell_layout(G)
        nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
        # we can now added edge thickness and edge color
        nx.draw_networkx_edges(G, graph_pos, width=2, alpha=0.3, edge_color='green')
        nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

        # show graph
        plt.show()

        
        
              
    def openFile(self):
        self.grammarPath.set(askopenfilename())
        self.updateGrammar()
    
    def updateGrammar(self):
        nFile = open(self.grammarPath.get(),'r')
        data=nFile.read()
        nFile.close()
        lexer = BayesGrammarLexer(InputStream(data))
        stream = CommonTokenStream(lexer)
        parser = BayesGrammarParser(stream)
        tree = parser.program()
        printer = BayesListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        self.bn = BayesianNetwork(printer.probabilities, printer.variables)
        if self.bn.hasError:
            self.text.config(state=NORMAL)
            self.text.insert(END, ">> "+self.bn.error+"\n")
            self.text.config(state=DISABLED)
            self.errors = True
        else:
            self.text.config(state=NORMAL)
            self.text.insert(END, ">> Red correcta\n")
            self.text.config(state=DISABLED)
            self.errors = False
            self.bn.printFactores()
    
    def doWork(self):
        
        if self.errors:
            self.text.config(state=NORMAL)
            self.text.insert(END, ">> La descripcion tiene errores\n")
            self.text.config(state=DISABLED)
            return
        elif self.bn == None:
            self.text.config(state=NORMAL)
            self.text.insert(END, ">> Ingrese una descripcion primero\n")
            self.text.config(state=DISABLED)
            return
        else:
            try:
                string = self.consulta.get()
                lexer = BayesGrammarUserLexer(InputStream(string))
                stream = CommonTokenStream(lexer)
                parser = BayesGrammarUserParser(stream)
                tree = parser.program()
                printer = BayesUserListener()
                walker = ParseTreeWalker()
                walker.walk(printer, tree)
                self.text.config(state=NORMAL)
                self.text.insert(END, ">> "+ self.consulta.get()+"\n")
                self.text.config(state=DISABLED)
                self.text.config(state=NORMAL)
                self.text.insert(END, ">> "+ self.bn.enumeration(printer.probability, printer.variables)+"\n")
                self.text.config(state=DISABLED)
            except ValueError:
                self.text.config(state=NORMAL)
                self.text.insert(END, ">> "+str(ValueError)+"\n")
                self.text.config(state=DISABLED)

    def onClick(self, event = None):
        if event!= None:
            self.doWork()
            

def main():
  
    root = Tk()
    root.geometry("600x300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
