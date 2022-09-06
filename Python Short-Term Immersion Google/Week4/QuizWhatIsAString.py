# Modify the double_word function to repeat the same word twice and return the length of the newly added word after it. For example, double_word ("hello") should return hellohello10.

def double_word(word):
    word = (word + word)
    word += str(len(word))
    return word


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
