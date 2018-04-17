#Structure

jas = ['j','a','s','m','i','l','e','j','a','s','m','i','l','e','o','r','d','a','l','a','c','s','o','n']


from collections import Counter
jas_counts = Counter(jas)
repeat = jas_counts.most_common(5)
print ("letters repeated")
print(repeat)
