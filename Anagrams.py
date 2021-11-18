def anagrams():  
#here i am defining the function that my code will run in
    O_word1=input("Enter the first word here: ")
    O_word2=input("Enter the second word here: ")
    
    word1=O_word1.lower()
    word1=word1.replace(" ","")
    word2=O_word2.lower()
    word2=word2.replace(" ","")
    
    print("The first word is:",O_word1)
    print("The second word is:",O_word2)
#here is some unsolicited error correctionfor the user inputted variables. basically if they input somthing they arent supposed to then the code that asks for the user's input loops until they input somthing correct
    if sorted(word1)==sorted(word2):
        print(O_word1,"is in fact an anagram of",O_word2)
#this sorts both words into alphabetical order and then checks if they are comprised of the same letters. if they are then the code returns that they are anagrams
    else:
        print(O_word1,"is not an anagram of",O_word2)
#if anything else happens then the code prints that it is not an anagram

    O_phrase=input("Enter a phrase here: ")
    
    phrase=O_phrase.lower()
    phrase=phrase.replace(" ","")
    
    if sorted(phrase)==sorted(word1):
        print(O_word1,"is in fact an anagram of",O_phrase)
    elif sorted(phrase)!=sorted(word1):
        print(O_word1,"is not an anagram of",O_phrase)
        
    if sorted(phrase)==sorted(word2):
        print(O_word2,"is in fact an anagram of",O_phrase)
    elif sorted(phrase)!=sorted(word2):
        print(O_word2,"is not an anagram of",O_phrase)
anagrams()
#this prints what my code has returned. this will either be: (This is not an Anagram) or (This is in fact an Anagram)