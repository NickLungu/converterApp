from main import convert4tg
import easygui
import tkinter as tk
import pyperclip
import os

class App:
    path = ""
    num_files = ""
    def __init__(self):

        self.root = tk.Tk()

        self.root.title('Image converter')
        self.root.geometry('600x250')
        self.root['background'] = '#DAFFEF'

        # self.back_image = tk.PhotoImage(file="bg.png")
        self.l = tk.Label(self.root, text = "")
        self.l['background'] = '#DAFFEF'
        self.l.bind("<Button-1>", self.printKey)

        self.btn = tk.Button(self.root,
                             font=('calibri', 15),
                             text='load images',
                             command=self.get_file
                             )

        self.btn.pack(expand=1)
        self.l.pack(padx=0, pady=40)

        self.root.mainloop()


    def get_file(self):
        input_file = easygui.fileopenbox(default="*.jpg", filetypes=["*.jpeg", "*.jpg"], multiple=True)
        if not input_file == None:
            self.num_files, self.path = convert4tg(input_file)
            wording = "File is ready" if self.num_files == 1 else "Files are ready"
            self.l.configure(text=wording + ": (click here to open folder): \n\n"+self.path)
            # msg = "files are ready here: \n\n" + path
            # tk.messagebox.showinfo("Information", msg)

    def printKey(self,a=0):
        pyperclip.copy(self.path)
        os.system(r"explorer.exe " + self.path)



if __name__ == '__main__':
    app = App()


