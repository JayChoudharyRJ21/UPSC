

#----------Libraries----------#
import random 
import os
import subprocess
import linecache

#----------Greeting----------#
class Opening():
    
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
                print(SuggestionList)
        
            RandomSuggestion = random.choice(SuggestionList) 
            
        if str(input1) == 'Y' or str(input1) == 'y':
            UserSuggestion = input('Please write your suggestion here....\n\n')
            with open(file_path, 'a') as file2:
                file2.write(UserSuggestion)
            
        else:
            print(RandomSuggestion)
               

#----------Main_Code----------#
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




#----------Homepage----------#
class HomePage(Fundamentals):
     def __init__(self):
      print('Welcome to HomePage\n\tHere you have three options as follows\n\t\t1.Notes.\n\t\t2.PreviousYearQuestions & Papers.\n\t\t3.Quiz')
      opt = int(input('Please enter the number before your choice....  '))

      # --------------------Notes--------------------#
      if opt == 1:
          print('\n\n\nWelcome to notes')
          opt1 = int(input('Here you have four options\n\t1.NCERT Notes\n\t2.Vision Notes\n\t3.Dhrishti Notes\n\t4.Handwritten Self_Made Notes\n\nPlease Enter the number before your choice: '))
          if opt1 == 1:
              print('Welcome to NCERT Notes')
              self.path = path = "D:/UPSC APP/Raws Notes/NCERT"
              self.list_files_and_directories(path)
              file_no_chosen = int(input('Enter the number before your choice...  '))
              file_chosen = self.Files[file_no_chosen]
              print(file_chosen)
              file_chosen_with_path = f"{path}/{file_chosen}"
              print(file_chosen_with_path)
              self.open_pdf_file(file_chosen_with_path)
              
              
              
          elif opt1 == 2:
              print('Welcome to Vision IAS Notes')
                    
          elif opt1 == 3:
              print('Welcome to Dhrishti IAS Notes')
              
          elif opt == 4:
              print('Welcome to your Handwritten Self_Made Notes' )
              
      #--------------------PYQ&P's--------------------#   
      elif opt == 2:
          print('\n\n\nWelcome to PreviousYearQuestions & Papers' )
          pyp_choice = int(input('Enter the number before your choice.\n\n\t1.Preliminary\n\tMains'))
          if pyp_choice == 1:
              #open Preliminary folder show all the choice available.
              year = int(input('Enter the year .... '))
              # open the file 
   
        
      #--------------------Quiz--------------------#
      elif opt == 3:
            opt = int(input(''''\n\n\n>>_____Welcome to Quiz_____<<\n\n
                Please choose your subject to be taken quiz of,\
                Options:
                     1.History
                     2.Geoography
                     3.Polity
                     4.Science and Tech
                     5.Miscellaneous\n'''))
                            
            
            
          
          
          
      #--------------------ELSE--------------------#   
      else:
          print('Please enter the number before your choice only.')

class UPSC_Quiz(Fundamentals,HomePage):
    file = None
    
    def get_line(self, file, n):
        return linecache.getline(file , n).encode().decode('unicode_escape')
        
    def Questions(self,m,n):
        
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


greeting = Opening
homepage = HomePage()
