import PySimpleGUI as Gui
import zipfile
import pathlib

print('Hello bro')

label1 = Gui.Text("Source Address: ",
                  background_color='black')
label2 = Gui.Text("Destination Address: ",
                  background_color='black')

source_field = Gui.Input(background_color='white')
destination_field = Gui.Input(background_color='white')

choose_source_btn = Gui.FileBrowse(button_color='black on white', key='source')
choose_destination_btn = Gui.FolderBrowse(button_color='black on white', key='destination')

compress_btn = Gui.Button('Compress', button_color='black on white')

window = Gui.Window("Compressor",
                    layout=[[label1, source_field, choose_source_btn],
                            [label2, destination_field, choose_destination_btn],
                            [compress_btn]],
                    font=('OCR A Extended', 17),
                    background_color='black')

event, values = window.read()
while True:
    print(event, values)
    match event:
        case 'Compress':

window.close()
