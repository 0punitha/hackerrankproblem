sentence=input("Enter a sentence:")
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in sentence:
    if i in small:
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")
        
   
        
    
    