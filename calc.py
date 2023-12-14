import PySimpleGUI as sg

def create_layout():
    return [
        [sg.Input(size=(20, 1), key='-DISPLAY-', justification='right')],
        [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
        [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
        [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('*')],
        [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/')]
    ]

def main():
    layout = create_layout()
    window = sg.Window('Simple Calculator', layout, return_keyboard_events=True)

    current_input = ''

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break

        if event == 'C':
            current_input = ''
        elif event == '=':
            try:
                result = eval(current_input)
                current_input = str(result)
            except Exception as e:
                current_input = 'Error'

        elif event in '1234567890':
            current_input += event
        elif event in ['+', '-', '*', '/']:
            current_input += event

        window['-DISPLAY-'].update(current_input)

    window.close()

if __name__ == '__main__':
    main()
