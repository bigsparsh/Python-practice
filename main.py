import PySimpleGUI as gui
from func import compress

# Labels
label1 = gui.Text('Select the source files: ',
                  key='select_file_label',
                  background_color='black')
label2 = gui.Text('Select destination folder: ',
                  key='select_dest_label',
                  background_color='black')
label3 = gui.Text(text_color='green',
                  background_color='black')

# Inputs
input1 = gui.Input(background_color='white')
input2 = gui.Input(background_color='white')

# File Chooser and Folder Chooser buttons
file_btn = gui.FilesBrowse(key='file_btn',
                           button_color='black on white')
dest_btn = gui.FolderBrowse(key='dest_btn',
                            button_color='black on white')

# Compress button
compress_btn = gui.Button('Compress',
                          key='compress_btn',
                          button_color='black on white')

# Window
window = gui.Window('Compressor',
                    layout=[[label1, input1, file_btn],
                            [label2, input2, dest_btn],
                            [compress_btn, label3]],
                    font=('OCR A Extended', 17),
                    background_color='black')

# Window initialization + Event checking
while True:
    event, values = window.read()
    print(event, "\n", values)
    compress(values['file_btn'].split(';'), values['dest_btn'])
    label3.update('Compression Successful')

# Closing the window
window.close()
