#A9Q2

f1=open('iter.txt','r')
word_count=0
vowels_count=0
vowels='aeiouAEIOU'
for line in f1:
    words=line.split(' ')
    word_count=word_count+len(words)
    
    for ch in line:
        if ch in vowels:
            vowels_count=vowels_count+1

print('The number of words = ',word_count)
print('The number of vowels = ',vowels_count)
f1.close()
