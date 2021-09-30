# Swap Binary substring
# Using translate()
  
# initializing string
test_str = "siddharthlaldeo"
  
# printing original string
print("The original string is : " + test_str)
  
# Swap Binary substring
# Using translate()
temp = str.maketrans("sidd", "abcd")
test_str = test_str.translate(temp)
  
# printing result 
print("The string after swap : " + str(test_str)) 
