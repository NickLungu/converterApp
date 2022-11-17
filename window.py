from main import convert4tg
import easygui
import tkinter as tk



class App:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title('Конвертер изображений')
        self.root.geometry('500x400')
        self.btn = tk.Button(self.root, text='Загрузить изображение', command=self.get_file)
        self.btn.pack(expand=True)

        self.root.mainloop()

    def get_file(self):
        input_file = easygui.fileopenbox(filetypes=["*.img"])
        convert4tg(input_file)


if __name__ == '__main__':
    app = App()


