import os ,subprocess

class Fundamentals():
    Files = {}
    
    def list_files_and_directories(self,folder_path):
        # Iterate over all items in the given folder
        for root, dirs, files in os.walk(folder_path):
            # Print the current directory
            print(f"Directory: {root}")
            i = 0
            
            # Print all files in the current directory
            
                #print(Files)
            
            # Print all subdirectories in the current directory
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                print(f"Directory: {dir_path}")
            
    def open_pdf_file(file_path):
        try:
            subprocess.Popen([file_path], shell=True)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except OSError:
            print(f"Error: Unable to open '{file_path}'.")      
    
# =============================================================================

class Funda(Fundamentals):
    def __init__(self):
       fundu = Fundamentals()
       self.Files = fundu.Files  # Here we derived Files dictionary from the class Fundamentals to Funda class
       
    def list_files_and_directories2(self):
          
          self.path = path = "D:/UPSC APP/Raws Notes/NCERT"
          self.list_files_and_directories(path)
          file_no_chosen = int(input('Enter the number before your choice...  '))
          file_chosen = self.Files[file_no_chosen]
          print(file_chosen)
          
NCERT = Funda()
files = NCERT.list_files_and_directories2()

