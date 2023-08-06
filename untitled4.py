#----------------------------
import linecache


#----------------------------

file_path = "C:\\Users\Jugal\Desktop\TEST.txt"

line1 = linecache.getline(file_path,1).encode().decode('unicode_escape')
line2 = linecache.getline(file_path,4)
line3 = linecache.getline(file_path,5)

line = 'Hello brother \n\t How are you??\n\t\tWhats Going on ?'
print( line)
print(line1) 

# =============================================================================w 
# with open(file_path, 'r') as file:
#     text_content = file.read().encode().decode('unicode_escape')
#     print(text_content)
# =============================================================================
