from cgitb import text
import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert

def convert_to_pdf():
    input_word_file = filedialog.askopenfilename(title="word",filetypes=[("word files","*.docx")])
    if input_word_file:
        output_pdf_file = filedialog.askopenfilename(title="pdf",filetypes=[("pdf files","*.pdf")])
        if output_pdf_file:
            convert(input_word_file,output_pdf_file)
            status_label.config(text="Convertirovat")

root = tk.Tk()
root.title("Converter word to pdf")

convert_button = tk.Button(root, text="Convert in pdf", command=convert_to_pdf)
convert_button.pack(pady=20)

status_label = tk.Label(root,text="",fg="green")
status_label.pack()

root.mainloop()
