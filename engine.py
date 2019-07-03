import PageTemplate.MainWindow_support as window


def pprint():
    window.w.Label.configure(text='Waiting')
    a = window.w.InputField.get('0.0', 'end')
    print(a.strip())
