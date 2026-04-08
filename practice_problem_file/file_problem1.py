
from functools import reduce

with open("text.txt","r") as file:
    # lines= file.read()
    strings= file.readlines()
    total_Lines=len(strings)

     
    
    words = list(map(str.strip,strings))
    filter_words= list(filter(lambda x: len(x)>=1,words))

    num_of_words= list(map(lambda x :len(x.split(" ")),filter_words))

    total_words= reduce(lambda x,y: x+y, num_of_words)

    reduce_space = list(map(lambda x :x.replace(" ",""),filter_words)) 

    index_lengths= list(map(lambda x :len(x),reduce_space))
    total_char= reduce(lambda x,y: x+y, index_lengths)

    # print(lines)
    print(f'Total Line : {total_Lines}')
    print(f'Total words :  {total_words}')
    print(f'Total Character : {total_char}')






