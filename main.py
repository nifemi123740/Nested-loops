word=input("Enter the word: ")
char=input("Enter the character to check:")
i=0
count=0

while(i<len(word)):
    if(word[i]==char):
        count+=1
    i+=1

print(f"The occurance of the letter {char} is {count}")