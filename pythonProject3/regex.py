import re
text="he is lazy boy so he uses razor to shave"
texture=r'\b\w*z\w*\b'
match=re.findall(texture,text)
print(match)
