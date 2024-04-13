import re
email=str(input("Enter your Emailid:"))
match=re.search(r"@gmail",email)
if match:
    print("your Email is correct")
else:
    print("did not match")