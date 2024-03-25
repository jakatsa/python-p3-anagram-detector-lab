# your code goes here!

# class
# initalize , take in param (word)
# def match to check if the word marches 


class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, array):
        # for loop
        # sort bothr the word and the word in array
        #  if the same in a list
            
        anagram_list = [arr_word for arr_word in array if sorted(self.word)== sorted(arr_word)]
        return anagram_list
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))