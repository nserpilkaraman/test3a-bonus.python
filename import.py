import ogretmen
import ogrenci

student_list = list()
teacher_list = list()

student2 = ogrenci.Student("Ayça", "Güven", 21, "Yazılım Kalite ve Test")
student_list.append(student2)
ogrenci.Student.printdetails(student2)

student3 = ogrenci.Student("Hilal", "Cebel", 21, "Yazılım Kalite ve Test")
student_list.append(student3)
ogrenci.Student.printdetails(student3)

student4 = ogrenci.Student("Nisanur", "Baş", 21, "Yazılım Kalite ve Test")
student_list.append(student4)
ogrenci.Student.printdetails(student4)

student5 = ogrenci.Student("Eray", "Koç", 21, "Yazılım Kalite ve Test")
student_list.append(student5)
ogrenci.Student.printdetails(student5)

student6 = ogrenci.Student("Serpil Nur","Karaman", 21, "Yazılım Kalite ve Test")
student_list.append(student6)
ogrenci.Student.printdetails(student6)

teacher = ogretmen.Teacher("İrem", "Balcı", 25, "Yazılım Kalite ve Test")
teacher_list.append(teacher)
ogretmen.Teacher.printdetails(teacher)




