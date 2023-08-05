keywords = ['if', 'else', 'for', 'while', 'int', 'bool']
words = ['if', 'hello', 'else']


print("Keywords: ")
def check_keywords(word):
    found=False
    for i in keywords:
        if (i == word) :
            found=True
            print(" ", word)
            break
    # if (found) :
    #     print(word, "is keyword")
    # else:
    #     print(word, "is not keyword")


for j in words:
    check_keywords(j)