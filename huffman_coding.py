import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

#string = 'ALGORITAM SHANNON-FANOVOG KODIRANJA JE JEDNOSTAVAN ZA IMPLEMENTIRATI.'
#string = 'DA BI STUDENT MOGAO IMPLEMENTIRATI ALGORITAM POTREBNO JE DA PROCITA PREDAVANJA IZ PREDMETA MMS.'
#string = 'ZA SVAKU OD OVIH RECENICA POTREBNO JE IZRACUNATI STEPEN KOMPRESIJE AKO SE ZA NEKOMPRIMIRANI TEKST KORISTI BITNA REPREZENTACIJA ASCII VRIJEDNOSTI SIMBOLA.'
string='EACAEAABAAEDAEA'
frequency=defaultdict(int)
for simbol in string:
    frequency[simbol]+=1

huffmanCode = encode(frequency)
noBitsCompressed=0
print("Slovo|Frekventnost|Huffmanov kod|")
for coded in huffmanCode:
    print(coded[0]+"     |     "+str(frequency[coded[0]])+"    |     "+coded[1])
    noBitsCompressed+= len(coded[1])

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
# Main Function 
dict_obj = my_dictionary() 
for i in huffmanCode:
    dict_obj.add(i[0],i[1])
print("Coded message:")
ispis=""
for i in string:
    ispis+=dict_obj[i]
print(ispis)
print("Degree of compression: "+str(8*len(string)/len(ispis)))