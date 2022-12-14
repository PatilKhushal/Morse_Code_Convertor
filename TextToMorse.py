from tkinter import *


def textToMorse(data, result, root2):
    dictValidating = {'1' : '. --- --- --- ---   ', '2' : '. . --- --- ---   ', '3' : '. . . --- ---   ', '4' : '. . . . ---   ', '5' : '. . . . .   ', '6' : '--- . . . .   ', '7' : '--- --- . . .   ', '8' : '--- --- --- . .   ', '9' : '--- --- --- --- .   ', '0' : '--- --- --- --- ---   ', ' ' : '    ', 'a' : '. ---   ', 'b' : '--- . . .   ', 'c' : '--- . --- .   ', 'd' : '--- . .   ', 'e' : '.   ', 'f' : '. . --- .   ', 'g' : '--- --- .   ', 'h' : '. . . .   ', 'j' : '. --- --- ---   ', 'i' : '. .   ', 'k' : '--- . ---   ', 'l' : '. --- . .   ', 'm' : '--- ---   ', 'n' : '--- .   ', 'o' : '--- --- ---   ', 'p' : '. --- --- .   ', 'q' : '--- --- . ---   ', 'r' : '. --- .   ', 's' : '. . .   ', 't' : '---   ', 'u' : '. . ---   ', 'v' : '. . . ---   ', 'w' : '. --- ---   ', 'x' : '--- . . ---   ', 'y' : '--- . --- ---   ', 'z' : '--- --- . .   '}

    cipher = ""

    for x in data:
        cipher += dictValidating[x]

    result['text'] = ""
    
    #result['bg'] = 'green'
    for i,x in enumerate(cipher):
        if i % 80 == 0:
            result['text'] += "\n"
        result['text'] += x

    root2.clipboard_clear()
    root2.clipboard_append(result.cget('text').replace('\n','').strip())
    

def tTM(data, result, root2):
    dictValidating = {'1' : '. --- --- --- ---   ', '2' : '. . --- --- ---   ', '3' : '. . . --- ---   ', '4' : '. . . . ---   ', '5' : '. . . . .   ', '6' : '--- . . . .   ', '7' : '--- --- . . .   ', '8' : '--- --- --- . .   ', '9' : '--- --- --- --- .   ', '0' : '--- --- --- --- ---   ', ' ' : '    ', 'a' : '. ---   ', 'b' : '--- . . .   ', 'c' : '--- . --- .   ', 'd' : '--- . .   ', 'e' : '.   ', 'f' : '. . --- .   ', 'g' : '--- --- .   ', 'h' : '. . . .   ', 'j' : '. --- --- ---   ', 'i' : '. .   ', 'k' : '--- . ---   ', 'l' : '. --- . .   ', 'm' : '--- ---   ', 'n' : '--- .   ', 'o' : '--- --- ---   ', 'p' : '. --- --- .   ', 'q' : '--- --- . ---   ', 'r' : '. --- .   ', 's' : '. . .   ', 't' : '---   ', 'u' : '. . ---   ', 'v' : '. . . ---   ', 'w' : '. --- ---   ', 'x' : '--- . . ---   ', 'y' : '--- . --- ---   ', 'z' : '--- --- . .   '}

    cipher = ""

    for x in data:
        cipher += dictValidating[x]

    result['text'] = ""
    
    #result['bg'] = 'green'
    for i,x in enumerate(cipher):
        if i % 80 == 0:
            result['text'] += "\n"
        result['text'] += x

    root2.clipboard_clear()
    root2.clipboard_append(result.cget('text').replace('\n','').strip())




def morseToText(event, data, validateTextLabel, result):
    dictValidating = {'. --- --- --- ---' : '1', '. . --- --- ---' : '2', '. . . --- ---' : '3', '. . . . ---' : '4', '. . . . .' : '5', '--- . . . .' : '6', '--- --- . . .' : '7', '--- --- --- . .' : '8', '--- --- --- --- .' : '9', '--- --- --- --- ---' : '0', '    ' : ' ' , '. ---' : 'a' , '--- . . .' : 'b' , '--- . --- .' : 'c' , '--- . .' : 'd' , '.' : 'e' , '. . --- .' : 'f' , '--- --- .' : 'g' , '. . . .' : 'h' , '. --- --- ---' : 'j' , '. .' : 'i' , '--- . ---' : 'k' , '. --- . .' : 'l' , '--- ---' : 'm' , '--- .' : 'n' , '--- --- ---' : 'o' , '. --- --- .' : 'p' , '--- --- . ---' : 'q' , '. --- .' : 'r' , '. . .' : 's' , '---' : 't' , '. . ---' : 'u' , '. . . ---' : 'v' , '. --- ---' : 'w' , '--- . . ---' : 'x' , '--- . --- ---' : 'y' , '--- --- . .' : 'z' }

    cipher = ""

    i = True
    for x in data.split('       '):
        if not(i) :
            break
        for y in x.split('   '):
            if y.strip() not in dictValidating :
                validateTextLabel['text'] = 'Invalid Morse Code'
                i = False
                break
            validateTextLabel['text'] = ''
            cipher += dictValidating[y.strip()]
        cipher += " "
    
    result['text'] = ""
    
    #result['bg'] = 'green'
    for i,x in enumerate(cipher):
        if i % 80 == 0:
            result['text'] += "\n"
        result['text'] += x

    result['text'] = result['text'].strip()
    
    if len(data) == 0:
        validateTextLabel['text'] = ''

def on_Closing(anyroot):

    anyroot.destroy()
    root.deiconify()

def validateText(event, text, validateTextLabel, result, root2):
    if len(text) == 0 :
        validateTextLabel['text'] = ""
    flag = False
    for x in text:
        if not(x.isalpha() or x.isdigit() or x.isspace()):
            validateTextLabel['text'] = "Text must be a digit or alphabet"
            flag = False
            break

        else:
            flag = True
            validateTextLabel['text'] = ""
    
    if flag:
        textToMorse(text, result, root2)

def validateB(event, text, validateTextLabel, result, root2):
    if len(result.cget('text')) > 0 and len(validateTextLabel.cget('text')) == 0:
        tTM(text[0 :(len(text) - 1)], result, root2)


def newRoot1():
    
    root.withdraw()

    root2 = Tk()
    w = root2.winfo_screenwidth()
    h = root2.winfo_screenheight()

    root2.geometry("%dx%d" %(w, h))
    root2.title("Text 2 Morse-Code Module")
    root2['bg'] = 'black'

    root2.grid_rowconfigure(0, weight = 1)
    
    root2.grid_rowconfigure(3, weight = 1)
    root2.grid_rowconfigure(4, weight = 1)
    root2.grid_rowconfigure(5, weight = 1)

    root2.grid_columnconfigure(0, weight = 1)
    root2.grid_columnconfigure(1, weight = 2)
    root2.grid_columnconfigure(2, weight = 1)

    Label0 = Label(root2, text = "Text 2 Morse-Code Module", bg = 'black', fg = 'blue', font=("Times New Roman bold", 50))
    Label0.grid(row = 0, column = 0, columnspan = 3)

    validateTextLabel = Label(root2, text = "", bg = 'black', fg = 'red', font=("Times New Roman bold", 15))
    validateTextLabel.grid(row = 2, column = 1)

    Label2 = Label(root2, text = "Equivalent Morse Code", bg = 'black', fg = 'green', font=("Times New Roman bold", 20))
    Label2.grid(row = 3, column = 0, sticky = E)

    result = Label(root2, text = "", bg = 'black', width = 42, fg = 'red', font=("Times New Roman bold", 15))
    result.grid(row = 3, column = 1)

    Label1 = Label(root2, text = "Enter Text", bg = 'black', fg = 'green', font=("Times New Roman bold", 20)).grid(row = 1, column = 0, sticky = E)
    text = Entry(root2, font=("Times New Roman bold", 15))
    text.bind("<KeyRelease>", lambda event, arg = (text.get(), validateTextLabel, result, root2) : validateText(event, text.get().lower(), validateTextLabel, result, root2))
    text.bind("<BackSpace>", lambda event, arg = (text.get(), validateTextLabel, result, root2) : validateB(event, text.get().lower(), validateTextLabel, result, root2))
    text.grid(row = 1, column = 1, ipadx = 150)


    root2.protocol("WM_DELETE_WINDOW", lambda arg = root2 : on_Closing(root2))
    root2.mainloop()

def newRoot2():
    
    root.withdraw()

    root2 = Tk()
    w = root2.winfo_screenwidth()
    h = root2.winfo_screenheight()

    root2.geometry("%dx%d" %(w, h))
    root2.title("Morse-Code 2 Text Module")
    root2['bg'] = 'black'

    root2.grid_rowconfigure(0, weight = 1)
    
    root2.grid_rowconfigure(3, weight = 1)
    root2.grid_rowconfigure(4, weight = 1)
    root2.grid_rowconfigure(5, weight = 1)

    root2.grid_columnconfigure(0, weight = 1)
    root2.grid_columnconfigure(1, weight = 2)
    root2.grid_columnconfigure(2, weight = 1)

    Label0 = Label(root2, text = "Morse-Code 2 Text Module", bg = 'black', fg = 'blue', font=("Times New Roman bold", 50))
    Label0.grid(row = 0, column = 0, columnspan = 3)

    validateTextLabel = Label(root2, text = "", bg = 'black', fg = 'red', font=("Times New Roman bold", 15))
    validateTextLabel.grid(row = 2, column = 1)

    Label2 = Label(root2, text = "Equivalent Text", bg = 'black', fg = 'green', font=("Times New Roman bold", 20))
    Label2.grid(row = 3, column = 0, sticky = E)

    result = Label(root2, text = "", bg = 'black', width = 42, fg = 'red', font=("Times New Roman bold", 15))
    result.grid(row = 3, column = 1)

    Label1 = Label(root2, text = "Enter Morse Code", bg = 'black', fg = 'green', font=("Times New Roman bold", 20)).grid(row = 1, column = 0, sticky = E)
    text = Entry(root2, font=("Times New Roman bold", 15))
    text.bind("<KeyRelease>", lambda event, arg = (text.get(), validateTextLabel, result) : morseToText(event, text.get().lower(), validateTextLabel, result))
    text.grid(row = 1, column = 1, ipadx = 150)


    root2.protocol("WM_DELETE_WINDOW", lambda arg = root2 : on_Closing(root2))
    root2.mainloop()
    
root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry("%dx%d" %(w, h))
root.title("Morse-Code Translator")
root['bg'] = 'black'

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)
root.grid_columnconfigure(2, weight = 1)

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)

Label(root, text = "Morse-Code Translator", bg = 'black', fg = 'blue', font=("Times New Roman bold", 50)).grid(row = 0, column = 0, columnspan = 3)
Button(root, bg = 'purple', fg = 'black', command = newRoot1, font=("Times New Roman bold", 20), text = "Text 2 Morse-Code").grid(row = 1, column = 0, sticky = E, ipadx = 50)
Button(root, bg = 'purple', fg = 'black', command = newRoot2, font=("Times New Roman bold", 20), text = "Morse-Code 2 Text").grid(row = 1, column = 1, sticky = E, ipadx = 50)

root.mainloop()
