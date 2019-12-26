

class Word:
    def __init__(self, word):
        self.word = word
    
    def __repr__(self):
        return self.word
    
    def __add__(self, other_word):
        return Word('%s %s' % (self.word, other_word))
    
    # Add an alias from method __add__ to the method concat
    concat = __add__



if __name__ == "__main__":
    first_name = Word('Max')
    last_name = Word('Smith')

    print(first_name + last_name)

    print(first_name.concat(last_name))

    print(Word.__add__ == Word.concat)


