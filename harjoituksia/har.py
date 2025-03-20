# # tee ratkaisu tänne

# def lisaa_opiskelija(opiskelijat: dict, nimi: str):
#     opiskelijat[nimi] = []

# def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
#     suoritukset = []
#     suoritukset.append(suoritus)
#     for i in suoritukset:
#         aine, numero = i
#         if numero == 0:
#             del i
#         else:
#             opiskelijat[nimi].append(i)
        
# def tulosta(opiskelijat: dict, nimi: str):
#     if nimi not in opiskelijat:
#         print(f"ei löytynyt ketään nimellä {nimi}") 
#     for avain, arvot in opiskelijat.items():
#         if avain == nimi:
#             print(f"{avain}:")
#             if arvot == "":
#                 print(" ei suorituksia")
#             else:
#                 nähdytArvot = {}
#                 keskiarvo = 0
#                 lukuja = 0
                
#                 for avain2,arvot2 in arvot:
#                     keskiarvo += arvot2
#                     lukuja += 1
#                     nähdytArvot[avain2] = arvot2
#                 suoritukset = len(nähdytArvot)
                
#                 if suoritukset == 0:
#                     print(" ei suorituksia")
#                 else:
#                     print(f" suorituksia {suoritukset} kurssilta:") 
                
#                 for a,s in nähdytArvot.items():
#                     print(f"  {a} {s}")
                
#                 if keskiarvo == 0:
#                     pass
#                 else:
#                     print(f" keskiarvo {keskiarvo/lukuja}")
                
   

# def kooste(opiskelijat: dict):
#     print(f"opiskelijoita {len(opiskelijat)}")
#     edellinen = 0
#     keskiarvot = {}
#     summa = 0
#     e = 0
#     for avaint,arvot in opiskelijat.items():
#         if len(arvot) > edellinen:
#             edellinen = len(arvot)
#         for nimi,numero in arvot:
#             summa += numero
#         keskiarvot[avaint] = summa
#         summa = 0
#     for w,i in keskiarvot.items():
#         if i > e:
#             e = i
#     print(f"eniten suorituksia",len(arvot),avaint)
#     print("paras keskiarvo",i/len(arvot) ,w)
        

# if __name__=="__main__":
#     opiskelijat = {}
#     lisaa_opiskelija(opiskelijat, "emilia")
#     lisaa_opiskelija(opiskelijat, "pekka")
#     lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
#     lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
#     lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
#     lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
#     lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
#     lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
#     tulosta(opiskelijat, "emilia")
#     tulosta(opiskelijat, "pekka")
#     print(opiskelijat)

# def sudoku_oikein(sudoku: list):
  
#     paikat = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

#     riviNähty = [] 
#     for i in range(9):
#         for rivi in sudoku[i]:
#             # print(rivi)
#             if rivi in riviNähty:
#                 return False
#             else:
#                 if rivi == 0:
#                     continue
#                 else:
#                     riviNähty.append(rivi)
#         riviNähty.clear()
        
#     sarakeNähty = []
#     for c in range(9):
#         for x in range(9):
#             sarake = sudoku[x][c]
#             # print(sarake)
#             if sarake in sarakeNähty:
#                 return False
#             else:
#                 if sarake == 0:
#                     continue
#                 else:
#                     sarakeNähty.append(sarake)
#         sarakeNähty.clear()

#     return True




# if __name__=="__main__":
#     sudoku = [
#         [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
#         [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
#         [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
#         [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
#         [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
#         [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
#         [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
#         [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
#         [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
#     ]
#     print(sudoku_oikein(sudoku))
        
    
# rv = 0
# sk = 0
    
  
 # for z in paikat:
    #     laskuri = 0
    #     nelio = []
    #     nähty = []
    #     rv,sk = z
    #     # print(rv, sk)       
    #     if sk == 0:
    #         pituus = 3
    #     else:
    #         pituus = sk
    #     for rivi1 in range(len(sudoku)):
    #         if rivi1 == rv:
    #             for x in range(len(sudoku[rivi1])):
    #                 nelio.append(sudoku[rivi1][x])
    #                 while pituus <= sk*2 - 1:
    #                     pituus += 1
    #             # print(nelio[sk:pituus])
    #             for numerot in nelio[sk:pituus]:
    #                     if numerot in nähty:
    #                         return False
    #                     else: 
    #                         if numerot == 0:
    #                             continue
    #                         else:
    #                             nähty.append(numerot)
    #             nelio.clear()
    #             nähty.clear()
    #             rv += 1
    #             laskuri += 1
    #             if laskuri == 3:
    #                 break


# suoritukset = [('ohpe', 4),('ohpe', 5),('tira', 3),('lama', 0),('tira', 2),('jtkt', 1)]
# nähäty = {}
# for i in suoritukset:
#     aine, numero = i
#     if aine not in nähäty and numero > 0:
#         nähäty[aine] = numero
#     if aine in nähäty:
#         edlli=numero
#         e = aine
#         for avain,numero in nähäty.items():
#             if numero > edlli and avain == e:
#                 nähäty[aine] = numero
#             if numero < edlli and avain == e:
#                 nähäty[aine] = edlli                
#     else:
#         pass

# print(nähäty)
# if suoritus[1] == 0:
#         return 0 

# def lisaa_opiskelija(opiskelijat: dict, nimi: str):
#     opiskelijat[nimi] = list()

# def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):          
#     if suoritus[1] == 0:
#         return 0 
#     opiskelijat[nimi].append(suoritus)
    
    
        
# def tulosta(opiskelijat: dict, nimi: str):
#     if nimi not in opiskelijat:
#         print(f"ei löytynyt ketään nimellä {nimi}") 
#     for avain, arvot in opiskelijat.items():
#         if avain == nimi:
#             print(f"{avain}:")
#             if arvot == "":
#                 print(" ei suorituksia")
#             else:
#                 nähdytArvot = {}
#                 keskiarvo = 0
#                 lukuja = 0
                
#                 for avain2,arvot2 in arvot:
#                     nähdytArvot[avain2] = arvot2
#                 suoritukset = len(nähdytArvot)
#                 for a,s in nähdytArvot.items():
#                     keskiarvo += s
#                     lukuja += 1

#                 if suoritukset == 0:
#                     print(" ei suorituksia")
#                 else:
#                     print(f" suorituksia {suoritukset} kurssilta:") 
                
#                 for a,s in nähdytArvot.items():
#                     print(f"  {a} {s}")
                
#                 if keskiarvo == 0:
#                     pass
#                 else:
#                     print(f" keskiarvo {keskiarvo/lukuja}")
                
   

# def kooste(opiskelijat: dict):
#     print(f"opiskelijoita {len(opiskelijat)}")
#     edellinen = 0
#     keskiarvot = {}
#     summa = 0
#     e = 0
#     for avaint,arvot in opiskelijat.items():
#         if len(arvot) > edellinen:
#             edellinen = len(arvot)
#         for nimi,numero in arvot:
#             summa += numero
#         keskiarvot[avaint] = summa
#         summa = 0
#     for w,i in keskiarvot.items():
#         if i > e:
#             e = i
#     print(f"eniten suorituksia",len(arvot),avaint)
#     print("paras keskiarvo",i/len(arvot) ,w)
        

# if __name__=="__main__":
#     opiskelijat = {}
#     lisaa_opiskelija(opiskelijat, "pekka")
#     lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 5))
#     lisaa_suoritus(opiskelijat, "pekka", ("ohpe", 1))
#     tulosta(opiskelijat, "pekka")
#     # print(opiskelijat)

# def add_student(students, name):
#     students[name] = set()


# def print_student(students, name):
#     if name not in students:
#         print(f"{name}: no such person in the database")
#     else:
#         print(f"{name}:")
#         print(f"{len(students[name])}  completed courses:")
#         for course in students[name]:
#             print(f" {course[0]} {course[1]}")
#         av_grade = 0
#         for course in students[name]:
#             course[1] += av_grade
#             print(f"average grade {av_grade / len(students[name])}")

          
# def add_course(students,name,course: tuple):
#     if course[1] == 0:
#         return 0
#     students[name].add(course)

# def summary(students):
#     print(f"students {len(students)}")
#     most_courses = 0
#     student_most_courses = None
#     for student, courses in students.items():
#         if len(courses) > most_courses:
#             student_most_courses = student
#             most_courses = len(courses)
    
#     print(f"most courses completed {most_courses} {student_most_courses}")
         
          



# if __name__ == "__main__":
#     students = {}
#     add_student(students, "Peter")
#     add_student(students, "Eliza")
#     # print_student(students, "Peter")
#     # print_student(students, "Eliza")
#     # print_student(students, "Jack")
#     add_course(students, "Peter", ("Data Structures and Algorithms", 1))
#     add_course(students, "Peter", ("Introduction to Programming", 1))
#     add_course(students, "Peter", ("Advanced Course in Programming", 1))
#     add_course(students, "Eliza", ("Introduction to Programming", 5))
#     add_course(students, "Eliza", ("Introduction to Computer Science", 4))
#     summary(students)



def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    opiskelijat[nimi].append(suoritus)
    nähty = {}
    for c,x in opiskelijat.items():
        for a in x:
            q,w = a
            if q not in nähty and w > 0:
                nähty[q] = w
        if q in nähty:
            edlli=w
            e = q
            for avain,w in nähty.items():
                if w > edlli and avain == e:
                    nähty[q] = w
                if w < edlli and avain == e:
                    nähty[q] = edlli                
        else:
            pass



def tulosta(opiskelijat: dict, nimi: str):
    if nimi not in opiskelijat:
        print(f"ei löytynyt ketään nimellä {nimi}") 
    for avain, arvot in opiskelijat.items():
        if avain == nimi:
            print(f"{avain}:")
            if arvot == "":
                print(" ei suorituksia")
            else:
                nähdytArvot = {}
                keskiarvo = 0
              
                
                for avain2,arvot2 in arvot:
                    nähdytArvot[avain2] = arvot2
                suoritukset = len(nähdytArvot)
                
                for a,s in nähdytArvot.items():
                    keskiarvo += s
              
                if suoritukset == 0:
                    print(" ei suorituksia")
                else:
                    print(f" suorituksia {suoritukset} kurssilta:") 
                
                for a,s in nähdytArvot.items():
                    print(f"  {a} {s}")
                
                if keskiarvo == 0:
                    pass
                else:
                    print(f" keskiarvo {keskiarvo/len(nähdytArvot)}")
                
   

def kooste(opiskelijat: dict):
    print(f"opiskelijoita {len(opiskelijat)}")
    edellinen = 0
    keskiarvot = {}
    summa = 0
    e = 0
    for avaint,arvot in opiskelijat.items():
        if len(arvot) > edellinen:
            edellinen = len(arvot)
        for nimi,numero in arvot:
            summa += numero
        keskiarvot[avaint] = summa
        summa = 0
    for w,i in keskiarvot.items():
        if i > e:
            e = i
    print(f"eniten suorituksia",len(arvot),avaint)
    print("paras keskiarvo",i/len(arvot) ,w)
        

if __name__=="__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
    kooste(opiskelijat)
    print(opiskelijat)
