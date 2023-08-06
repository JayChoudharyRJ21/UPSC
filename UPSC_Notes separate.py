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





class Notes(Fundamentals):
    opt1 = 0
    
    def __init__(self):
        print('\n\n>>___________Welcome_To_Notes___________<<')
    
    def Run(self):
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
                    Notes.NCERT_Notes()
                elif self.opt1 == 2:
                    Notes.Vision_Notes()
                elif self.opt1 == 3:
                    Notes.Dhrishti_Notes()
                elif self.opt1 == 4:
                    Notes.Handwritten_Notes()
                elif self.opt1 == 5:
                    pass
                elif self.opt1 == 6:
                    quit()
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
        Notes.Run(self)
                
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
            Notes.Run(self)
                  
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
            Notes.Run(self)
            
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
            Notes.Run(self)
            
nts = Notes()
nts.Run()
    