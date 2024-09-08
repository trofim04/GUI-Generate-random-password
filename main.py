import customtkinter as ctk

from CTkMessagebox import CTkMessagebox
from random import randint

from os import startfile
from string import ascii_uppercase, ascii_lowercase, digits, punctuation



class App(ctk.CTk):
    def __init__(self, windowWidth, windowHeight):
        """Creating a core widgets on GUI """
        super().__init__()
        self.geometry(f"{windowWidth}x{windowHeight}")
        self.minsize(windowWidth, windowHeight)
        self.maxsize(windowWidth, windowHeight)
        self.title("Main Window")

        self.HelpLabel = ctk.CTkLabel(self, text="Select variables: ").place(x=5, y=0)
        
        self.upperLetterCaseVar = ctk.StringVar(value="on")
        self.upperLetterCase = ctk.CTkCheckBox(self, text="A - Z",  variable=self.upperLetterCaseVar, command=self.passwordGen,
                                            onvalue="on", offvalue="off").place(x=5, y=30)
        
        self.lowerLetterCaseVar = ctk.StringVar(value="off")
        self.lowerLetterCase = ctk.CTkCheckBox(self, text="a - z",  variable=self.lowerLetterCaseVar, command=self.passwordGen,
                                            onvalue="on", offvalue="off").place(x=75, y=30)
        
        self.digitCaseVar = ctk.StringVar(value="off")
        self.digitCase = ctk.CTkCheckBox(self, text="0 - 9",  variable=self.digitCaseVar, command=self.passwordGen,
                                            onvalue="on", offvalue="off").place(x=150, y=30)
        
        self.punctuationCaseVar = ctk.StringVar(value="off")
        self.punctuationCase = ctk.CTkCheckBox(self, text="? - !", variable=self.punctuationCaseVar, command=self.passwordGen,
                                            onvalue="on", offvalue="off").place(x=215, y=30)
        
        self.sliderValue = ctk.CTkLabel(self, text="Length: 0")
        self.sliderValue.place(x=5, y=58)
        self.slider = ctk.CTkSlider(self, from_=4, to=32, command=self.slider_event, number_of_steps=32).place(x=5, y=80)
        
        
        self.passwordEntry = ctk.CTkEntry(self, width=300)
        self.passwordEntry.place(x=5, y=105)
        self.GenButton = ctk.CTkButton(self, text="Generate", command=self.passwordGen).place(x=5, y=140)
        self.saveButton = ctk.CTkButton(self, text="Save on file", command=self.saveOn).place(x=5, y=170)
        self.openFileButton = ctk.CTkButton(self, text="Open file", command=self.openFile).place(x=5, y=200)

    def slider_event(self, value):
        self.value = round(value)
        self.sliderValue.configure(text=f"Length: {self.value}")
        

    def passwordGen(self):
        """Generation password with selected range and selected symbols"""
        self.symbols = ""
        self.newPassword = ""
        if self.punctuationCaseVar.get() == "on":
            self.symbols += punctuation
        if self.digitCaseVar.get() == "on":
            self.symbols += digits
        if self.upperLetterCaseVar.get() == "on":
            self.symbols += ascii_uppercase
        if self.lowerLetterCaseVar.get() == "on":
            self.symbols += ascii_lowercase
        try:
            for i in range(self.value):
                self.newPassword += self.symbols[randint(0, len(self.symbols)-1)]
        except AttributeError:
            pass
            
        self.passwordEntry.delete(0, ctk.END)
        self.passwordEntry.insert(0, self.newPassword)
        
    def saveOn(self):
        """Saving passwords in file named 'passwords.txt'"""
        with open("passwords.txt", "a+") as f:
            data = f.read()
            try:
                if self.newPassword in data:
                    pass
                else:
                    f.write(f"{self.newPassword}\n")
            except AttributeError:
                pass

    def openFile(self):
        try:
            startfile("passwords.txt")
        except FileNotFoundError:
            CTkMessagebox(self, title="Warning", message="You dont generate any password!")


        

if __name__ == "__main__":
    app = App(windowWidth=325, windowHeight=400)
    app.mainloop()
