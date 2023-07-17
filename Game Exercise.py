'''
Game:
 -start:welcome, options
 -options to exit
 -enter game number
 -play again

'''
class Game:
    def __init__(self):
        while True:
            print('''
    Welcome To Our Game
       1 : Names With Length
       2 : filter starts with
       3 : From To Multiplication Table
       4 : to exit
    ''')
            user_choice = int(input('Enter Game Number : '))
            if user_choice==1:
                names=input('Enter Names Seperated by , :')
                names_list=names.split(',')
                self.name_with_length(names_list)
            elif user_choice==2:
                names=input('Enter Names Seperated by , :')
                char=input('Enter Char : ')
                names_list = names.split(',')
                self.filter_starts_with(names_list,char)
                
            elif user_choice==3:
                start=int(input('Enter Start Number : '))
                end=int(input('Enter End Number : '))
                self.from_to_multiplication_table(start,end)
                
            elif user_choice==4:
                return
            
            play_again = input('press any char to play again , n to exi ')
            if play_again=='n':
                break
    
    def name_with_length(self,names):
        new_names=[]
        for n in names:
            new_names.append(len(n))
        print(new_names)
        
    def filter_starts_with(self,names,char):
        new_names=[]
        for n in names:
            if n.startswith(char):
                new_names.append(n)
        print(new_names)
        
    def from_to_multiplication_table(self,start,end):
        for x in range(start,end+1):
            for y in range(1,11):
                print(f"{x} x {y} ={x*y}")
            print('==============================')
   

g = Game()



































