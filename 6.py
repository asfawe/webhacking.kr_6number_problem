import base64
 
id= 'admin'.encode()
pw = 'nimda'.encode()
 
for j in range(20):
    pw = base64.b64encode(pw)
    id = base64.b64encode(id)
 
print(id)
print('\n\n')
print(pw)