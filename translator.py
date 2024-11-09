#IDEAS
# map words to emoji so create input and split up that input(sentence into the words 
#of the sentence)
#make the words equal to something? so we can compare that word to values in a 
#dictionary: consisting of emojis matched up with words

#STEP 3: create a dictionary of emojis, key = word, value = emoji
emoji_dict = {
    "love": "❤️",
    "cookie": "🍪",
    "eat": "🍽️"
}

#getting user input(WORKS)
print("Enter a sentence:")
inp = input()
#print(inp)

#process of splitting up the sentence into a list of words(WORKS)
sentence = inp.split()
#print ("split up: " + str(sentence))

#find out how to access each part of the split list and then compare that to a 
#dictionary of emojis

answer = ""

for item in sentence:
    #print(item)
    for key in emoji_dict:
        if(item==key):
            answer = emoji_dict.get(key)
        else:
            answer += item

print (answer)
#  for key in emoji_dict:
#     print(emoji_dict.get(key))

#print(emoji_dict.values())



