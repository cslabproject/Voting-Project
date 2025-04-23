from PyQt6.QtWidgets import *
from gui import Ui_MainWindow
import csv

class Logic(QMainWindow, Ui_MainWindow):
    '''
    A class controlling the logic for the GUI application.
    '''
    def __init__(self) -> None:
        '''
        Method to initialize a Logic class and connect GUI buttons to functions.
        '''
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(lambda:self.submit())


    def clear_text(self) -> None:
        '''
        Method to clear the vote result text by setting all of the widths to 0, making them invisible.
        '''
        self.voteprompt_label.resize(0,80)
        self.votefail_label.resize(0,40)
        self.votefail_repeat_label.resize(0,80)
        self.votefail_candidiate_label.resize(0,40)
        self.votefail_empty_label.resize(0,40)
        self.votefail_number_label.resize(0,40)
        self.votesuccess_label.resize(0,40)
        

    def data_writing(self, voter_id:int) -> None:
        '''
        Method to write vote data into a .csv file.
        :param voter_id: The unique voter ID integer entered by the user
        '''
        if self.candidate_one_radiobutton.isChecked():
            choice = 'Candidate 1'
        elif self.candidate_two_radiobutton.isChecked():            # Evaluates user choice
            choice = 'Candidate 2'
        elif self.candidate_three_radiobutton.isChecked():
            choice = 'Candidate 3'
        else:
            raise AttributeError
        
        with open('vote_data.csv','a+', newline='') as my_csv:
            csv_writer = csv.writer(my_csv)
            
            my_csv.seek(0)
            lines = my_csv.readlines()
            temp_list = []
            for line in lines:                          # Verifies ID has not voted before
                temp_list = line.split(',')
                if str(voter_id) in temp_list[0]:
                    raise IndexError
                temp_list = []
            
            if len(lines) == 0:
                csv_writer.writerow(['Voter ID','Choice','Candidate 1 Votes', 'Candidate 2 Votes', 'Candidate 3 Votes', 'Total Votes'])
                total_votes = 0
                candidate_one_votes = 0                     # Sets template for .csv
                candidate_two_votes = 0
                candidate_three_votes = 0
            else:                                           
                final_line = lines[-1]
                final_line = final_line.split(',')
                total_votes = int(final_line[5])
                candidate_one_votes = int(final_line[2])    # Retrieves values of previous line in .csv to update later    
                candidate_two_votes = int(final_line[3])
                candidate_three_votes = int(final_line[4])

            my_csv.seek(0,2)
            if choice == 'Candidate 1':
                candidate_one_votes += 1
                total_votes +=1
            elif choice == 'Candidate 2':
                candidate_two_votes += 1
                total_votes +=1                     # Writes data to .csv
            elif choice == 'Candidate 3':
                candidate_three_votes += 1
                total_votes += 1
            csv_writer.writerow([voter_id,choice,candidate_one_votes, candidate_two_votes, candidate_three_votes, total_votes])


    def submit(self) -> None:
        '''
        Method to submit vote and provide GUI feedback.
        '''
        voter_id = self.ID_input.text()
        self.clear_text() # Necessary to prevent text overlapping             

        try:
            if voter_id == '':
                raise TypeError
            else:
                voter_id = int(voter_id)
        except ValueError:
            self.votefail_label.resize(120,40)
            self.votefail_number_label.resize(300,40)     
            return                                          # Evaluates blank/non-integer ID errors
        except TypeError:
            self.votefail_label.resize(120,40)
            self.votefail_empty_label.resize(180,40)
            return
        
        try:
            self.data_writing(voter_id)
        except IndexError:
            self.votefail_label.resize(120,40)
            self.votefail_repeat_label.setText(f'ID {voter_id} has already voted')    #Handles repeat voter errors  
            self.votefail_repeat_label.resize(350,80)
            return
        except AttributeError:
            self.votefail_label.resize(120,40)
            self.votefail_candidiate_label.resize(260,40)           #Handles missing candidate errors
            return
        
        self.votesuccess_label.resize(240,40)
        self.ID_input.clear()
        self.ID_input.setFocus()