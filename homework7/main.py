#Zadacha 10
#a = {"John": "Develop", "Mike": "desighner"}
#del a["John"]
#print(a)

#Zadacha 11
#a = {"banana": 5, "apple": 6, "orange": 1, "lichi": 4}
#alist = sorted(a.items(), key=lambda x:x[1])
#print(alist)

#Dop zadacha 1
#def set_diff(set1, set2):
 #   return [item for item in set1 if item not in set2]
#set1 = input("Введите элементы 1-го мно-ва через запятую: ")
#set2 = input("Введите элементы 2-го мно-ва через запятую: ")

#set1 = [item.strip() for item in set1]
#set2 = [item.strip() for item in set2]

#diff = set_diff(set1, set2)
#print("Разность множеств: ", diff)

#Dop zadacha 2
#def find_ocenki(puple1, puple2, puple3):
 #   all_ocenki = set(range(1, 11))
  #  ocenki = all_ocenki - set(puple1) - set(puple2) - set(puple3)
   # return  ocenki

#puple1 = list(map(int, input("Введите оценки 1-го ученика: ").split()))
#puple2 = list(map(int, input("Введите оценки 2-го ученика: ").split()))
#puple3 = list(map(int, input("Введите оценки 3-го ученика: ").split()))

#ocenki = find_ocenki(puple1, puple2, puple3)
#print("Оценки, не встечающиеся ни у одного из 3-х учеников: ", ocenki)