def transposition(text,key):
    ciphertext1=['']*key
    for column in range(key):
        pointer=column
        while pointer<len(text):
            ciphertext1[column] += text[pointer]
            #print(ciphertext1)
            pointer+=key
    for i in range(len(ciphertext1)-1):
        if len(ciphertext1[i])!=len(ciphertext1[i+1]):
            ciphertext1[i+1]+=  "_"
    print(ciphertext1)   
    output=''.join(ciphertext1)
    print("Encrypted text: "+output)
    f=open("text1.txt","w+")
    f.write('Encrypted message:'+output+'\n')
    f.close()
    
    return output

def encrypt(key):
    msg = input('Enter the Message you want to ENCRYPT : \n').lower().replace(" ","")
    f=open("text1.txt","w+")
    f.write(msg+'\n')
    f.close()
    result = "" 
    # traverse text 
    for character in msg:
        char = character 
        result += chr((ord(char) + key - 97) % 26 + 97) 
    print ("Cipher text: " +result)
    return result
    
#-------------------DECRYPTION-----------------------------------------
def decrypt_transposition(output, key):
    empty=""
    d=int(len(output)/key)
    for i in range(d):
        e=0
        e=e+i
        empty+=output[e]
        e=e+d
        while(e<len(output)):
            empty+=output[e]
            e=e+d
    print("Decipher text: "+empty)
    return empty

def decrypt(temp2,key):
    msg = temp2
    result=""
    # traverse text 
    for character in msg:
        if(character !="_"):
            char = character 
            result += chr(((ord(char) + 26 - 97) - key ) % 26 + 97) 
    print ("Decrypted text: " +result)
    f=open("text1.txt","a")
    f.write('Decrypted message:'+result)
    f.close()

key = int(input('Enter the Key for the Encryption: '))
print(f'KEY IS {key}')
temp=encrypt(key)
temp1=transposition(temp,key)
temp2=transposition(temp1,key)
temp3=decrypt_transposition(temp2,key)
temp4=decrypt_transposition(temp3,key)
decrypt(temp4,key)
