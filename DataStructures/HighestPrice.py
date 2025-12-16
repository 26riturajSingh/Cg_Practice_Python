priceList = {"A":1, "D":4, "B":2, "C":3}
print(priceList)
maxVal = -1
maxKey = "1"
for key in priceList:
    if priceList[key] > maxVal:
        maxVal = priceList[key]
        maxKey = key
print(maxKey, maxVal, sep=":")