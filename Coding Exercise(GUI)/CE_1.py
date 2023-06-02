            #             Convertor
            # Enter feet: ________________
            # Enter Inches: _________________
            # |Convert|

import PySimpleGUI as GUI

label_feet = GUI.Text("Enter feet:")
input_feet = GUI.InputText(tooltip="Enter feet")
label_Inches = GUI.Text("Enter Inches:")
input_Inches = GUI.InputText(tooltip="Enter Inches")
convert_btn = GUI.Button("Convert")

window = GUI.Window("Convertor", layout=[[label_feet, input_feet], [label_Inches, input_Inches], [convert_btn]])

window.read()
window.close()
