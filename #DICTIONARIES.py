#DICTIONARIES

my_dictionary = {}

my_dictionary["apina"] = "Monkey"
my_dictionary["banaani"] = "Banana"
my_dictionary["cemalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])

word = input("please type in a word: ")
if word in my_dictionary:
    print("Translation: " + my_dictionary[word])
else:
    print("Word not found in the dictionary.")

    results = {}
    results["mary"] = 4
    results["Alice"] = 5
    results["Tiana"] = 2

    print(results)

    lists = {}
    lists[5] = [1,2,3]
    lists[42] = [5,4,5,4,5]
    lists[100] = [5,2,3]
    print(lists)

    my_dictionary["suuri"] = "big"
    my_dictionary["suuri"] = "large"
    print(my_dictionary["suuri"])

    word_lists = ["banana", "milk", "beer", "cheese", "juice", "pot roast", "carrots", "tuna", "salmon", "butter", "margarine", "chocolate", "beer", "cheese","gummy worms"]

    def counts(my_list):
        words = {}
        for my in words:
            #if the word is not already in the dictionary, initialize the value to zero
            if word not in words:
                words[word] = 0
                #increment the value
                words[word] += 1
                return words

            print(counts(word_lists))
    