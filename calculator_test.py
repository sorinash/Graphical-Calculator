# -*- coding: utf-8 -*-
"""
First attempt at using tkinter with python
Also a test of a basic calculator

Can add, subtract, multiply, and divide, as well as handle decimals and avoid
divide-by-zero errors
"""
from tkinter import *

class calc():
    def __init__(self): 
        self.firstnum = 0
        self.sign = ''
        self.secondnummem = 0
        self.secondnumstr = ''
        self.did_i_start = False
        self.using_decimal = False
        self.decimalplace = 10
        self.secondnumstart = False
        self.is_this_negative = False
        self.which_number = 0
        self.error_thrown = False
        self.decimalstart = False
        self.totalstr = str(self.firstnum) + self.sign + self.secondnumstr
        self.mem_number = None
    
    def after_calc(self):
        self.firstnum = 0
        self.sign = ''
        self.secondnummem = 0
        self.secondnumstr = ''
        self.did_i_start = False
        self.using_decimal = False
        self.decimalplace = 10
        self.secondnumstart = False
        self.is_this_negative = False
        self.which_number = 2
        self.error_thrown = False
        self.decimalstart = False
        self.totalstr = str(self.firstnum) + self.sign + self.secondnumstr
    
    def remake(self):
        if self.which_number == 0 and self.using_decimal and not self.decimalstart:
            firststr = str(self.firstnum) + '.'
        else: 
            firststr = str(self.firstnum)
        
        if not self.secondnumstart: 
            secondstr = ''
        elif self.which_number == 1 and self.using_decimal and not self.decimalstart:
            secondstr = str(self.secondnummem) + '.'
        else: 
            secondstr = str(self.secondnummem)
            
        self.totalstr = firststr + self.sign + secondstr
    
    def updatenumber(self,innum):
        if self.error_thrown:
            return
        if self.which_number == 2: 
            if self.decimalstart:
                self.firstnum = innum/10
            else:
                self.firstnum = innum
            self.did_i_start = True
            self.which_number = 0
        elif self.which_number == 3: 
            if self.decimalstart:
                self.secondnummem = innum/10
            else:
                self.secondnummem = innum
            self.secondnumstart = True
            self.which_number = 1
        elif self.which_number == 0: 
            if not self.did_i_start and innum == 0: 
                return
            elif not self.did_i_start:
                self.firstnum = innum
                self.did_i_start = True
            elif self.using_decimal: 
                self.firstnum += innum/self.decimalplace
                self.decimalplace = self.decimalplace * 10
                self.decimalstart = True
            else: 
                self.firstnum = self.firstnum * 10
                self.firstnum += innum
        else: 
            if not self.secondnumstart: # if starting second number, create initial value
                self.secondnummem = innum
                self.secondnumstart = True
            elif self.using_decimal: 
                self.secondnummem += innum/self.decimalplace
                self.decimalplace = self.decimalplace * 10 #remember to reset between numbers
                self.decimalstart = True
            elif self.secondnummem == 0:
                self.secondnummem = innum
            else:
                self.secondnummem = self.secondnummem * 10
                self.secondnummem += innum
        self.remake()
        
    def includesign(self,signstr):
        if self.which_number == 1 or self.error_thrown: 
            return
        self.sign = signstr
        self.decimalplace = 10
        self.which_number = 1
        self.using_decimal = False
        self.decimalstart = False
        self.remake()
    
    def make_a_decimal(self):
        if self.using_decimal:
            return
        self.using_decimal = True
        if self.which_number in [0,2]:
            self.did_i_start = True
            print('yes')
        else: 
            self.secondnumstart = True
            
        if self.which_number == 2: 
            self.firstnum = 0
            self.which_number = 0
        elif self.which_number == 3: 
            self.secondnummem = 0
            self.which_number = 1
        self.remake()
        return
    
    def make_negative(self):
        if self.error_thrown:
            return
        if self.which_number in [0,2]: 
            self.firstnum = self.firstnum * -1
        elif self.which_number in [1,3]:
            self.secondnummem = self.secondnummem * -1
        self.remake()
    
    def clearall(self):
        memnum = self.mem_number
        self.__init__()
        self.mem_number = memnum
    
    def add_to_memory(self): 
        if self.which_number == 2:
            self.mem_number = self.firstnum
    
    def clear_memory(self):
        self.mem_number = None 
    
    def recall_memory(self):
        if self.mem_number == None:
            print('whoopsy')
            return
        
        if self.which_number != 1:
            self.firstnum = self.mem_number
            self.remake()
            self.which_number = 2
        else: 
            self.secondnummem = self.mem_number
            self.secondnumstart = True
            self.remake()
            self.which_number = 3
    
    def do_calculation(self):
        if self.error_thrown: 
            return
        if self.which_number in [0,2]:
            outnum = float(self.firstnum)
        elif self.sign == '+':
            outnum = self.firstnum + self.secondnummem
        elif self.sign == '-':
            outnum = self.firstnum - self.secondnummem
        elif self.sign == '*':
            outnum = self.firstnum * self.secondnummem
        elif self.sign == '/' and self.secondnummem == 0:
            outnum = 'ERROR: Cannot divide by 0'
            self.error_thrown = True
        elif self.sign == '/':
            outnum = self.firstnum / self.secondnummem
        elif self.sign == '^':
            outnum = self.firstnum ** self.secondnummem
        self.after_calc()
        self.firstnum = outnum
        self.remake()
    
        
        
    
mycalc = calc() # create a calculator object
root = Tk() # create Tk object
root.geometry("200x150")
frame = Frame(root)
frame.pack() #make frame

leftframe = Frame(root)
leftframe.pack(side=LEFT)

#creates a label
label = Label(frame, text = mycalc.totalstr)
label.pack()


# creates functions for each button
# by and large self-explanatory, but after running the function from the 
# Calc class, updates the label to display the redone number
def upone(): 
    mycalc.updatenumber(1)
    label.configure(text = mycalc.totalstr)
def uptwo(): 
    mycalc.updatenumber(2)
    label.configure(text = mycalc.totalstr)
def upthree(): 
    mycalc.updatenumber(3)
    label.configure(text = mycalc.totalstr)
def upfour(): 
    mycalc.updatenumber(4)
    label.configure(text = mycalc.totalstr)
def upfive(): 
    mycalc.updatenumber(5)
    label.configure(text = mycalc.totalstr)
def upsix(): 
    mycalc.updatenumber(6)
    label.configure(text = mycalc.totalstr)
def upseven(): 
    mycalc.updatenumber(7)
    label.configure(text = mycalc.totalstr)
def upeight():
    mycalc.updatenumber(8)
    label.configure(text = mycalc.totalstr)
def upnine():
    mycalc.updatenumber(9)
    label.configure(text = mycalc.totalstr)
def upzero():
    mycalc.updatenumber(0)
    label.configure(text = mycalc.totalstr)
def upplus():
    mycalc.includesign('+')
    label.configure(text = mycalc.totalstr)
def upmin():
    mycalc.includesign('-')
    label.configure(text = mycalc.totalstr)
def uptim():
    mycalc.includesign('*')
    label.configure(text = mycalc.totalstr)
def updiv(): 
    mycalc.includesign('/')
    label.configure(text = mycalc.totalstr)
def upexp(): 
    mycalc.includesign('^')
    label.configure(text = mycalc.totalstr)
def clearall(): 
    mycalc.clearall()
    label.configure(text = mycalc.totalstr)
def decimalmake():
    mycalc.make_a_decimal()
    label.configure(text = mycalc.totalstr)
def docalc():
    mycalc.do_calculation()
    label.configure(text = mycalc.totalstr)
def memplus():
    mycalc.add_to_memory()
def memclear():
    mycalc.clear_memory()
def memrec():
    mycalc.recall_memory()
    label.configure(text = mycalc.totalstr)
def posneg():
    mycalc.make_negative()
    label.configure(text = mycalc.totalstr)

# number buttons
button1= Button(leftframe,text = "1", command = upone)
button1.grid(row=0, column = 0)
button2 = Button(leftframe, text = "2", command = uptwo)
button2.grid(row=0, column = 1)
button3 = Button(leftframe, text = "3",  command = upthree)
button3.grid(row=0, column = 2)
button4 = Button(leftframe, text = "4", command = upfour)
button4.grid(row=1,column=0)
button5 = Button(leftframe, text = "5", command = upfive)
button5.grid(row=1, column = 1)
button6 = Button(leftframe, text = "6", command = upsix)
button6.grid(row=1, column = 2)
button7 = Button(leftframe, text = "7", command = upseven)
button7.grid(row=2, column = 0)
button8 = Button(leftframe, text = "8", command = upeight)
button8.grid(row=2, column = 1)
button9 = Button(leftframe, text = "9", command = upnine)
button9.grid(row=2, column = 2)
button0= Button(leftframe,text = "0", command = upzero)
button0.grid(row=3,column=1)

#decimal button
buttondot = Button(leftframe, text = '.', command = decimalmake)
buttondot.grid(row=3, column=0)

buttoneq = Button(leftframe, text = '=', command = docalc)
buttoneq.grid(row=3, column = 5)

buttonclear = Button(leftframe, text = 'CE', command = clearall)
buttonclear.grid(row=3, column = 6)

buttonplus = Button(leftframe, text = "+", command = upplus)
buttonplus.grid(row=0, column = 5)
buttonminus = Button(leftframe, text = "-", command = upmin)
buttonminus.grid(row=0, column = 6)
buttontimes = Button(leftframe, text = "*", command = uptim)
buttontimes.grid(row=1, column = 5)
buttondiv = Button(leftframe, text = "/", command = updiv)
buttondiv.grid(row=1, column = 6)
buttonexp =  Button(leftframe, text = "^", command = upexp)
buttonexp.grid(row = 2, column = 5)

button_memplus = Button(leftframe, text = "M+", command = memplus)
button_memclear = Button(leftframe, text = "MC", command = memclear)
button_memrec = Button(leftframe, text = "MR", command = memrec)

button_memplus.grid(row=0,column = 7)
button_memclear.grid(row=1, column = 7)
button_memrec.grid(row=2, column = 7)

button_neg = Button(leftframe, text = "±", command = posneg)
button_neg.grid(row=3, column = 2)

label.pack(padx=5,pady=5)

root.title("Test")
root.mainloop()