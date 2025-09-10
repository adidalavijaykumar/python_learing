#Replace

str = '2025/09/30'
print(str.replace('/', '-'))


# Transformation


price_1= "$1,35642222222.56"
print(price_1.replace("$", "").replace(",", ""))


phone = "+49 (179) 123-4567"
print(phone.replace("+49","0049").replace(" ","").replace("(","").replace(")","").replace("-",""))