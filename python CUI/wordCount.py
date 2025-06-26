#ask the user to write the paragraph
text = input("Enter the paragraph:\n")

#split the paragraph 
words = text.split()

#show the entered text just for now:-
# print("\nYoun entered:\n", words)

#create an empty dictornary to hold the words
word_count = {}

#loop through each word in the list
for word in words:
    word = word.lower()#convert the lowercase to avoid the duplicate
    if word in word_count:
        word_count[word] += 1 #if already there add 1
    else:
        word_count[word] = 1 #if not there add value 1

print("\nWord Frequency:\n")
for word,count in word_count.items():
    print(f"{word} : {count}")
