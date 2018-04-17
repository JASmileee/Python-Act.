
jas ="Water is a vital element in each of our lives. Not only is it essential to our health, but we also use it for numerous household tasks. The country is endowed with rich natural resources, including water, which are essential for the country’s economic development."
print jas



jas = jas.replace("","")
jas = jas.lower()

jas_list = list(jas)

jas_rev = jas_list[::-1]


if jas_rev == jas_list:
    print ("\n\n\n THIS IS A PALINDROME!!")
else:
    print ("\n\n\n OOPS THIS IS NOT A PALINDROME!!")
