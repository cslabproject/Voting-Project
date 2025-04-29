from logic import *

def main():
    '''
    Function to run GUI program
    '''
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()

'''
Note: If, after running, the text isn't bold:

'font.setWeight(75)' must be removed or commented out for every time text is bolded in 'gui.py' 
For whatever reason, it breaks how bold text works, but PyQt6 puts it in anyway.
This must be repeated every time the gui.py file is updated with a gui.ui file.
'''