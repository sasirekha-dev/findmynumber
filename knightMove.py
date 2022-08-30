'''
PROBLEM:
Knight Sequences
We want to find all 10-key sequences that can be keyed into the keypad in 
the following manner:
The initial keypress can be any of the keys.
Each subsequent keypress must be a knight move from the previous keypress.
There can be at most 2 vowels in the sequence.
A knight move is made in one of the following ways:
1. Move two steps horizontally and one step vertically.
2. Move two steps vertically and one step horizontally.

'''
import unittest
# possible knight moves with each keypress
knight = {
'1':['F','H','N'],
'2':['G','I','K','O'],
'3':['H','J','L'],
'A':['L','H'],
'B':['K','M','I'],
'C':['L','N','F','J'],
'D':['O','M','G'],
'E':['N','H'],
'F':['C','M','1'],
'G':['D','N','2'],
'H':['A','K','1','3','E','O'],
'I':['B','L','2'],
'J':['C','M','3'],
'K':['H','2','B'],
'L':['A','C','I','3'],
'M':['J','F','B','D'],
'N':['C','E','G','1'],
'O':['2','D','H'],
}

# Map 1,2,3 .....M,N,0 TO  0,1,2....15,16,17 
mapped_index = {k: ((ord(k)-ord('A')+3) if ord(k) in range(ord('A'),ord('P'))else int(k)-1) for k in knight.keys() }

# Identify keys which are vowel based on index 
isVowel = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1] 

''' 
Function gives number of knight moves possible 

Inputs:
vertex : starting keypress
length: number of knight moves or Max number of keypress in a sequence
vowelsRemaining: count of vowels remaining

output:
count of key sequence with given length
'''
def generateSequence( vertex,length, vowelsRemaining):
# Recursively returns the number of knight sequence    
    sequence =0    
    if length>0:
        length-=1
        # Each possible key press possible with each key and
        # check if vowel count max 2 in each combination
        for keyindex in vertex:
            
            value = 0
            if (vowelsRemaining or (not isVowel[mapped_index[keyindex]])):
                if length:
                    # traverse tree further to find more combinations...
                    value = generateSequence(knight[keyindex],length,\
                        vowelsRemaining-isVowel[mapped_index[keyindex]])
                else:
                    value = 1
            sequence = sequence+value
            
    return sequence

if __name__ == '__main__':
    
    count = 0
    sequenceLength = int(input('Enter the length of sequence:'))
    
    if sequenceLength == 0:
        print('please enter any number greater than 0.....')
    
    else:
        output = 0
        for keypress in knight.keys():
            numVowelsAllowed = 2
            
            output += generateSequence(keypress,sequenceLength,numVowelsAllowed)
        print(f'Knight moves with {len(knight.keys())} keys and {sequenceLength} length each sequence can have {output} combinations')

