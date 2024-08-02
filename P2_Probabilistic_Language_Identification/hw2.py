import sys
import math

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X = {
           'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0,
           'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0,
           'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
           'Y': 0, 'Z': 0
    }
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            str_line = list(line)
            for character in str_line:
                # checking the ASCII value is in the range 'A' TO 'Z'
                if 0 <= ord(character.upper()) - ord('A') <= 25:
                    character = character.upper()
                    X[character] = X[character] + 1
    return X

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

# Answer of Q1
shred_dict = shred("letter.txt")

print("Q1")
for x in shred_dict:
    print(x + ' ' + str(shred_dict[x]))

# Answer of Q2

english, spanish = get_parameter_vectors()

print("Q2")
cal = shred_dict['A'] * math.log(english[0])
print(F'{cal:.4f}')
cal = shred_dict['A'] * math.log(spanish[0])
print(F'{cal:.4f}')

# Answer of Q3
p_e = 0.6
p_s = 0.4

print("Q3")

# calculate f(e)
cal_f = 0
for x in range(0,25):
    cal_f += shred_dict[chr(x + ord('A'))] * math.log(english[x])
f_e = cal_f + math.log(0.6)
print(F'{f_e:.4f}')

# calculate f(s)
cal_f = 0
for x in range(0,25):
    cal_f += shred_dict[chr(x+ord('A'))] * math.log(spanish[x])
f_S = cal_f + math.log(0.4)
print(F'{f_S:.4f}')

# Answer of Q4

if f_S-f_e >= 100:
    p_eng_x = 0
elif f_S-f_e <= -100:
    p_eng_x = 1
else:
    p_eng_x = 1 / (1 + math.exp(f_S - f_e))

print("Q4")
print(F'{p_eng_x:.4f}')
