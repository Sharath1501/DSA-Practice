class fourthsem:
    def __init__(self,rollnums,test1_marks,test2_marks,test3_marks):
        self.Test1_marks = test1_marks
        self.Test2_marks = test2_marks
        self.Test3_marks = test3_marks
        self.Rollnums = rollnums
    def calculate_averages(self):
        avg1= sum(self.Test1_marks)/len(self.Test1_marks)
        avg2  = sum(self.Test2_marks)/len(self.Test2_marks)
        avg3 = sum(self.Test3_marks)/len(self.Test3_marks)
        return avg1,avg2,avg3
    def student_averages(self):
        stu_avg = []
        for i in range(len(self.Rollnums)):
            avg = (self.Test1_marks[i]+self.Test2_marks[i]+self.Test3_marks[i])/3
            stu_avg.append(avg)
        return stu_avg
    def last5_top5(self,testscores):
        sorti = sorted(testscores)
        last5 = sorti[:5]
        first5 = sorti[-5:]
        return last5,first5
    def all_info(self):
        avg1,avg2,avg3 = self.calculate_averages()
        print(f"Class average for test1 :{avg1}")
        print(f"Class average for test1 :{avg2}")
        print(f"Class average for test1 :{avg3}")

        student_averages = self.student_averages()
        for i in range(len(self.Rollnums)):
            print(f"Student {self.Rollnums[i]} , Average {student_averages[i]}")
        

        top15,last15 = self.last5_top5(self.Test1_marks)
        top25,last25 = self.last5_top5(self.Test2_marks)
        top35,last35 = self.last5_top5(self.Test3_marks)

        print(f"Top 5 scores for Test 1: {top15}")
        print(f"Last 5 scores for Test 1: {last15}")
        print(f"Top 5 scores for Test 2: {top25}")
        print(f"Last 5 scores for Test 2: {last25}")
        print(f"Top 5 scores for Test 3: {top35}")
        print(f"Last 5 scores for Test 3: {last35}")

roolnums = [i for i in range(1,21)]
test1 = [20,30,40,50,50,20,40,20,10,50,45,45,67,76,54,34,32,56,34,56]
test2 = [20,30,40,50,50,20,40,20,10,50,45,45,67,76,54,34,32,56,34,56]
test3 = [20,30,40,50,50,20,40,20,10,50,45,45,67,76,54,34,32,56,34,56]

fourths = fourthsem(roolnums,test1,test2,test3)
fourths.all_info()

