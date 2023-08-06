import linecache

class Fundamentals:
    
        file_path = "D:\\test_file.txt"


class UPSC_Quiz(Fundamentals):
     
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
            
Upsc = UPSC_Quiz()
Upsc.Questions(1,5)

   
     