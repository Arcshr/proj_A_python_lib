#In the following example, a sentence is split up into a list of words, 
#then a list is created that contains the length of each word.

sentence = 'It is raining cats and dogs'
words = sentence.split()
print words
#['It', 'is', 'raining', 'cats', 'and', 'dogs']


lengths = map(lambda word: len(word), words)
print lengths
#[2, 2, 7, 4, 3, 4]