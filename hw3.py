class Hw3 :

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        if(self.name == '도라에몽' or self.name == '코난') : 
            print("%s은 %d세이고, %s입니다." %(self.name, self.age, self.gender))
        else:
            print("%s는 %d세이고, %s입니다." %(self.name, self.age, self.gender))


chr1 = Hw3("짱구", 5, "남자")
chr1.introduce()

chr2 = Hw3("도라에몽", 14, "남자")
chr2.introduce()

chr3 = Hw3("코난", 8, "남자")
chr3.introduce()

chr4 = Hw3("쇼콜라", 15, "여자")
chr4.introduce()

chr5 = Hw3("아무", 12, "여자")
chr5.introduce()

chr6 = Hw3("가영", 16, "여자")
chr6.introduce()



