import subprocess
path = "D:/UPSC APP/Raws Notes/NCERT"
file_name = 'NCERT-Class-7-Environment.pdf'

file = f"{path}/{file_name}"
print(file)


def open_pdf_file(file_path):
        try:
            subprocess.Popen([file_path], shell=True)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except OSError:
            print(f"Error: Unable to open '{file_path}'.") 
            
open_pdf_file(file)        
                                                          

            
            
            
    
    
    
    
    
    