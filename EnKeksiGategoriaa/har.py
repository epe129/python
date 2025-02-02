# def nelio(sana, luku):
#     a = sana
#     laskuri = 0
#     c = True
#     while c:
#         for i in sana:
#             a += i
#             ekakirjain = i
#             if luku >= 5 and luku <= 9:
#                 if len(a) >= luku:
#                     print(a[:luku])
#                     laskuri += 1
#                     if ekakirjain == a[0]:
#                         laskuri += 1
#                         print(a[:luku])
#                     a = a[2:luku]
#                 if laskuri == luku:
#                     c = False
#                     break
#             elif luku <= 4:
#                 if len(a) >= luku:
#                     print(a[:luku])
#                     laskuri += 1
#                     if ekakirjain == a[0]:
#                         laskuri += 1
#                         print(a[1:luku] + a[1])
#                 if laskuri == luku:
#                     c = False
#                     break
            # elif luku >= 10:
            #     if len(a) >= luku:
            #         print(a[:luku])
            #         laskuri += 1
            #         if ekakirjain == a[0]:
            #             print(a[:luku])
            #             laskuri += 1
            #         a = a[3:luku]
            #     if laskuri == luku:
            #         c = False
            #         break
                
# if __name__ == "__main__":
#     # nelio("aba", 3)
#     nelio("abc", 7)
#     # nelio("python", 15)


# def nelio(sana,luku):
#     laskuri = 0
#     a = sana
#     c = True
#     while c:
#         for i in sana:
#             a += i
#             ekakirjain = i
#             if luku > 4:
#                 if len(a) >= luku:
#                     print(a[:luku])
#                     laskuri += 1
#                     if ekakirjain == a[0]:
#                         laskuri += 1
#                         print(a[1:luku])
#                     a = a[2:luku]
#                 if laskuri == luku:
#                     c = False
#                     break
#             else:
#                 if len(a) >= luku:
#                     print(a[:luku])
#                     laskuri += 1
#                     if ekakirjain == a[0]:
#                         laskuri += 1
#                         print(a[1:luku] + a[1])
#                     if laskuri == luku:
#                         c = False
#                         break

# if __name__ == "__main__":
#     nelio("aba", 3)
#     # nelio("abc", 5)
#     # nelio("python", 15)


# def nelio(sana, luku):
#     pituus = len(sana)
#     kopio = sana
#     for i in range(luku):
#         if pituus < luku:
#             kopio = kopio * luku
#         print(kopio[0:luku])
#         kopio = (kopio[luku:] + kopio)[:pituus] 

# if __name__ == "__main__":
#     # nelio("aba", 3)
#     # nelio("abc", 5)
#     # nelio("python", 15)
#     # nelio("aybabtu", 5)

# def tee_jotain(a: int):
#    b = 2 * a           
#    return b            
   
# x = tee_jotain(23)  

# def palindromi(sana):
#     a = sana[::-1]
#     if sana == a:
#         print(f"{sana} on palindromi!")
#     else:
#         print("ei ollut palindromi")

# while True:
#     kysy = input("Anna sana: ")
#     palindromi(kysy)
#     a = kysy[::-1]
#     if kysy == a:
#         break
    
# def summa(lista1, lista2):
#     new_list = []
#     luku = 0
#     for i in lista1:
#         print(i)

#     for x in lista2:
#         print(x)
        
#         if luku in new_list:
#             luku = 0
#         else:
#             luku = x + i
#             print(luku)    
#             new_list.append(luku)
#             luku = 0

    
#     print(new_list)
# if __name__ == "__main__":
#     lista1 = [1, 2, 3]
#     lista2 = [7, 8, 9]
#     summa(lista1, lista2)
# n = 7
# luku = 2
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i - 1)
#     elif i % 1 == 0:
#         if i == luku:
#             print(i)
#         else:
#             print(i + 1)
#     i += 1

def ilman_vokaaleja(lause):
    vokaalit = ["a","e","i","o","u","y","ä","ö"]
    sanat = lause.split()
    ilman = ""
    for x in sanat:
       pass
    # print(x)
    for _ in range(len(sanat)):
        for i in vokaalit:
            if i in x:
                m = x.replace(i, "")
                ilman = ilman + m
                ilman += " "

    print(ilman)

if __name__=="__main__":
    mjono = "testisana"
    ilman_vokaaleja(mjono)
