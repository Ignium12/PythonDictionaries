sample_text = "Python is a very powerful language"

vowels = frozenset("aeiou")
#  vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sample_text).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)