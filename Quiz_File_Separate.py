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
    
    def Add_Question(self):
        with open('Added Questions.txt','w') as f:
            question = input("Enter the question..\n")
            option1 = input ('Enter option (a)  ')
            option2 = input ('Enter option (b)  ')
            option3 = input ('Enter option (c) ')
            option4 = input ('Enter option (d)  ')
            right_answer = input('Enter the corrext answer a b c or d ..')
            explanation = input('Give the Explanation of your answer  ')
            f.write('Q ' +question+'\n(a)'+option1+'\n(b)'+option2+'\n(c)'+option3+'\n(d))'+option4)
            f.write('\nThe correct answer is' + right_answer)
            f.write('\nExplanation: ' +explanation)
        with open('Added Questions.txt','r') as f:
             f.read()
Upsc = UPSC_Quiz()
Upsc.Questions(1, 5)
#Upsc.Add_Question()
with open('Added Questions.txt','r') as f:
    print( f.read())
     