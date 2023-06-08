            #             Convertor
            # Enter feet: ________________
            # Enter Inches: _________________
            # |Convert|

import PySimpleGUI as GUI

label_feet = GUI.Text("Enter feet:")
input_feet = GUI.InputText(tooltip="Enter feet", key='feet')
label_Inches = GUI.Text("Enter Inches:")
input_Inches = GUI.InputText(tooltip="Enter Inches", key='inches')
output = GUI.Text(text_color='black', key='output')
convert_btn = GUI.Button("Convert")

window = GUI.Window("Convertor",
                    layout=[[label_feet, input_feet], [label_Inches, input_Inches], [convert_btn, output]],
                    font=('OCR A Extended', 20))

while True:
    event, values = window.read()
    feet = values['feet']
    inches = values['inches']
    meters = float(feet) * 0.3048 + float(inches) * 0.0254
    print(feet, '\n', inches)
    window['output'].update(f'There are {meters} meters in {feet} feet and {inches} inches.')
    # output.update('Hellow')
window.close()
