import re
sentence = []
words = []
count_words = all_words = count_lines = 0
upper_char=0
lower_char=0
digit_char=0
space_char=0
with open('text.txt','r') as infile:
    for line in infile:
        sentence.append(line.rstrip('\n'))
        count_lines+=1
        for i in range(len(sentence)):
            #words.append(sentence[i].split(" "))
            count_words = len(re.findall('(\w+)',sentence[i]))
        all_words += count_words
        
        for i in range(len(sentence)):
            for j in sentence[i]:
                if j.isupper():
                    upper_char += 1
                elif j.islower():
                    lower_char += 1
                elif j.isdigit():
                    digit_char += 1
                elif j.isspace():
                    space_char += 1
                
    print('averaged words per sentence: ',all_words/count_lines)
    print('total upper character:',upper_char)
    print('total lower character:',lower_char)
    print('total digit character:',digit_char)
    print('total space character:',space_char)
    
infile.close()
'''
upper_char=0
lower_char=0
digit_char=0
space_char=0
    
def count_char():
def main():
    
    
        
        

    infile.close()


    
    


main()
'''