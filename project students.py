'''
student:
-create student (name)->welcome
-add mark
-get avg

'''


class Student:
    def __init__(self,name):
        print(f'Welcome {name}')
        self.marks = []
     
        
    def add_mark(self,mark):
        self.marks.append(mark)
        print(f'{self.marks}')

    def get_avg(self):
        avg=sum(self.marks)/len(self.marks)
        print(avg)

       

s1 = Student('ahmed')

s1.add_mark(50)
s1.add_mark(40)
s1.add_mark(30)

s1.get_avg()
