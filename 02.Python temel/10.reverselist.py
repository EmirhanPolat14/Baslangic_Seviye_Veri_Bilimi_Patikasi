"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
"""

liste = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(liste):
    a = len(liste) // 2  
    while a > 0:
            liste[a - 1], liste[-a] = liste[-a], liste[a-1]      
            a -= 1      
    for i in liste:
        if type(i) == list:                     
            reverse(i)                                          

reverse(liste)
print(liste)