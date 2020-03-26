import copy

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

def LZW(input_string,dictionary):
    coded_message=[]
    print("Coded message: ")
    #initial symbol
    S = input_string[0]
    #initial code symbol
    code = len(dictionary)+1
    for i in range(1,len(input_string)):
        #next symbol
        C = input_string[i]
        #if combined string is in dictionary:
        if dictionary.get(S+C) is not None:
            if i==len(input_string)-1:
                coded_message.append(dictionary.get(S+C))
            S = S+C
        else:
            coded_message.append(dictionary.get(S))
            print(dictionary.get(S),end=" ")
            dictionary.add(S+C,code)
            code += 1
            S = C
    print(" ")
    max_el = dictionary.popitem()
    dictionary.add(max_el[0],max_el[1])
    padding = len(str(bin(max_el[1])[2:]))-1
    for i in dictionary:
        print("   Letter:     "+str(i)+"       Decimal code:    "+str(dictionary.get(i))+"   Binary code:    "+str(bin(dictionary.get(i))[2:]).zfill(padding))
    return coded_message



def LZWDecode(coded_message, decoding_dictionary):
    decoded_message = ""
    for i in coded_message:
        decoded_message += str(decoding_dictionary[i])
    return decoded_message



string = "BABAABBACABABB"

encoding_dictionary = my_dictionary()
code = 1
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    encoding_dictionary.add(i,code)
    code+=1

coded_message = LZW(string,encoding_dictionary)
enc_dict_temp = copy.deepcopy(encoding_dictionary)

decoding_dictionary = my_dictionary()
while len(enc_dict_temp)>0:
    temp = enc_dict_temp.popitem()
    decoding_dictionary.add(temp[1],temp[0])

decoded_message = LZWDecode(coded_message,decoding_dictionary)
print("\nDecoded message is: ")
print(decoded_message)