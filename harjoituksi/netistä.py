# eri laisia algorytmejä netistä
# Ota käyttöön seuraavat lajittelualgoritmit:
#  Valintalajittelu, Lisäyslajittelu, Yhdistä lajittelu, 
# Pikalajittelu, Stooge Lajittelu. 
# Tarkista Wikipedian kuvaukset.
# python program for implementation of selection
# sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [45,67,23,45,23,45]
selection_sort(arr)
print(arr)