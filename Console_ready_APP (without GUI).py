#----------Libraries----------#
import random 
import os
import subprocess
import linecache

#----------Classes----------#
class Fundamentals():
      Files = {}
      
      def list_files_and_directories(self,folder_path):
          # Iterate over all items in the given folder
          for root, dirs, files in os.walk(folder_path):
              # Print the current directory
              print(f"Directory: {root}")
              i = 0
              # Print all files in the current directory
              for file in files:
                  file_path = os.path.join(root, file)
                  i+=1
                  self.Files[i] = file
                  print(f"  {i}.{file}")

              # Print all subdirectories in the current directory
              for directory in dirs:
                  dir_path = os.path.join(root, directory)
                  print(f"Directory: {dir_path}")
                  
      def open_pdf_file(self,file_name):
          try:
              subprocess.Popen([file_name], shell=True)
          except FileNotFoundError:
              print(f"Error: File '{file_name}' not found.")
          except OSError:
              print(f"Error: Unable to open '{file_name}'.")



      # Specify the PDF file name
      # Code ====> file_name = "path/to/file.pdf"

      # Call the function to open the PDF file
      # Code ====> open_pdf_file(file_name)

class Opening():
    
    def __init__(self):
        Opening.Greet()
        Opening.Suggestion()
    
    def Greet():
        print('Hello Jay, \n\tGood Morning,Welcome back to your favourite environment\n\t\tThe Best ever Application for your preparation ')

    def Suggestion():
        file_path = "D:\\UPSC APP\Python Files\Text files\Suggestions_Raw.txt"
        input1 = input('If you want to give a suggestion, PLease press Y...Else N   ')
        
        SuggestionList = []
        with open(file_path,'r') as file:
            lines = 0 
            
            for line in file:
                lines +=1
                SuggestionList.append(line)
                
        
        RandomSuggestion = random.choice(SuggestionList) 
            
        if str(input1) == 'Y' or str(input1) == 'y':
            UserSuggestion = input('Please write your suggestion here....\n\n')
            with open(file_path, 'a') as file2:
                file2.write(UserSuggestion)
            
        else:
            print(RandomSuggestion)
               



class Notes(Fundamentals):
    opt1 = 0
    
    def __init__(self):
        print('\n\n>>___________Welcome_To_Notes___________<<')
        
        
        def run_notes(self):
             self.opt1 = int(input('''Here you have four options
        1.NCERT Notes
        2.Vision Notes
        3.Dhrishti Notes
        4.Handwritten Self_Made Notes
        
        5.Return Back to Homepage
        6.To exit Program
        
    Please Enter the number before your choice: '''))
       
        def options_notes(self):
                if self.opt1 == 1:
                    Notes.NCERT_Notes(self)
                elif self.opt1 == 2:
                    Notes.Vision_Notes(self)
                elif self.opt1 == 3:
                    Notes.Dhrishti_Notes(self)
                elif self.opt1 == 4:
                    Notes.Handwritten_Notes(self)
                elif self.opt1 == 5:
                    pass
                elif self.opt1 == 6:
                    quit(self)
                else:
                    print("Please chose the option before your choice ")

        run_notes(self)
        options_notes(self)
       
        
        
    def NCERT_Notes(self):

        print('\n\n>>___________Welcome to NCERT Notes___________<<')
        self.path = path = "D:/UPSC APP/Raws Notes/NCERT"
        self.list_files_and_directories(path)
        file_no_chosen = int(input('These are files that are contained in the NCERT Folder.\nHere you will see a list of files precedding with a number.\nYou can select only one file at a time.\nTo open the file of your choice, enter the number before your choice...  '))
        
        file_chosen = self.Files[file_no_chosen]
        print(file_chosen)
        file_chosen_with_path = f"{path}/{file_chosen}"
        print(file_chosen_with_path)
        self.open_pdf_file(file_chosen_with_path)
        
                
    def Vision_Notes(self):
        
            print('\n\n>>___________Vision IAS Notes___________<<')
            self.path = path = "D:/UPSC APP\Raws Notes\VISION_IAS"
            self.list_files_and_directories(path)
            file_no_chosen = int(input('Enter the number before your choice...  '))
            file_chosen = self.Files[file_no_chosen]
            print(file_chosen)
            file_chosen_with_path = f"{path}/{file_chosen}"
            print(file_chosen_with_path)
            self.open_pdf_file(file_chosen_with_path)
            
                  
    def Dhrishti_Notes(self):
        
            print('\n\n>>___________Dhrishti IAS Notes___________<<')
            #print('Currently these notes are unavailable.These will be uploaded soon')
            self.path = path = "D://UPSC APP/PDF Files Outlook/Notes/DHRISHTI_IAS"
            self.list_files_and_directories(path)
            file_no_chosen = int(input('Enter the number before your choice...  '))
            file_chosen = self.Files[file_no_chosen]
            print(file_chosen)
            file_chosen_with_path = f"{path}/{file_chosen}"
            print(file_chosen_with_path)
            self.open_pdf_file(file_chosen_with_path)
            
            
    def Handwritten_Notes(self):
        
            print('\n\n>>___________Handwritten Self_Made Notes___________<<' )
            #print('Currently these notes are unavailable.These will be uploaded soon')
            self.path = path = "D://UPSC APP/PDF Files Outlook/Notes/HAND_WRITTEN_SELF_MADE"
            self.list_files_and_directories(path)
            file_no_chosen = int(input('Enter the number before your choice...  '))
            file_chosen = self.Files[file_no_chosen]
            print(file_chosen)
            file_chosen_with_path = f"{path}/{file_chosen}"
            print(file_chosen_with_path)
            self.open_pdf_file(file_chosen_with_path)
               
    
class PrevYrQstns(Fundamentals):
    
    def __init__(self):
        print('\n\n\nWelcome to PreviousYearQuestions & Papers' )
        #pyp_choice = int(input('Enter the number before your choice.\n\n\t1. Preliminary\n\t2. Mains'))
        self.path = path = "D:/UPSC APP/DERIVATIVE Follder/Notes/PYQs"
        self.list_files_and_directories(self.path)
        file_no_chosen = int(input('These are files that are contained in the PYQ Folder.\nHere you will see a list of files precedding with a number.\nYou can select only one file at a time.\nTo open the file of your choice, enter the number before your choice...  '))
        file_chosen = self.Files[file_no_chosen]
        print(file_chosen)
        file_chosen_with_path = f"{path}/{file_chosen}"
        print(file_chosen_with_path)
        self.open_pdf_file(file_chosen_with_path)
          
class UPSC_Quiz(Fundamentals):
    file = None
    
    def get_line(self, file, n):
        return linecache.getline(file , n).encode().decode('unicode_escape')
        
    def Questions(self,m,n):
       self.file_path = "D:\\test_file.txt"
        
       while m <= n:   
        i = 8*m-7
        self.i = i
        file = self.file_path
        question = self.get_line(file,self.i)
        print(question,end='')
        opt1 = self.get_line(file,self.i+1)
        opt2 = self.get_line(file,self.i+2)
        opt3 = self.get_line(file,self.i+3)
        opt4 = self.get_line(file,self.i+4)
        options = f'{opt1}{opt2}{opt3}{opt4}'
        print(options,end='')
        U_ans = str(input('Enter your choice : '))
        answer = self.get_line(file,self.i+5)
        explanation = self.get_line(file,self.i+6)
        if U_ans.lower() == answer.strip():
            print('You answer is correct\n')
            print('The explanation is :\n',explanation)
        else:
            print(f'You answer is incorrect. The correct answer is {answer}')
            print('The explanation is :\n'+explanation)
        m+=1
    
# =============================================================================
# class Essentials(Notes,PrevYrQstns):
#     def __init__(self):
#         Notes = self.Notes()
#         Pyq = self.PrevYrQstns()
# 
# =============================================================================
class main(Opening,Notes,PrevYrQstns,UPSC_Quiz):
    opt = 0
    def __init__(self):
        opening = Opening()
        main.Greeting(self)
        
    
    
    def Greeting(self):
      print('\n\n>>___________Welcome_To_Homepage___________<<\n\n \tHere you have three options as follows\n\t\t1.Notes.\n\t\t2.PreviousYearQuestions & Papers.\n\t\t3.Quiz')
      x = int(input('Please enter the number before your choice....  '))
      self.opt =  x
      self.Run()
      
      
    def Run(self):
        self.opt = self.opt
        
        if self.opt == 1 :
            nts = Notes()
            self.Greeting()
       
        elif self.opt == 2:
            PYQ = PrevYrQstns()
            self.Greeting()
            
        elif self.opt ==3:
            qz = UPSC_Quiz()
            self.m = int(input(('Enter the number where you want to start from ')))
            self.n = int(input(('Enter the number where you want to end the questions  ')))
            qz.Questions(self.m,self.n)
            self.Greeting()
            
        else:
            print('Choose the number before your choice only ')
            self.Greeting()
        
        

main = main()


    