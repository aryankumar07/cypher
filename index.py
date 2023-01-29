cont=True
while cont:
    do=input("type 'encode' to encrypt and 'decode' to decrypt :\n")
    msg=input("type your message :\n")
    shift=int(input("type the shift number :\n"))

    ans=[]

    def encrypt(msg):
        for i in range(len(msg)):
            j=ord(msg[i])
            j=j+shift
            if(j>122):
                j=96+(j-ord(msg[i]))
            k=chr(j)
            ans.append(k)
        return ans


    def decrypt(msg):
        for i in range(len(msg)):
            j=ord(msg[i])
            j=j-shift
            if(j<97):
                j=123-(ord(msg[i])-j)
            k=chr(j)
            ans.append(k)
        return ans


    if(do=='encode'):
        ans=encrypt(msg)
    elif(do=='decode'):
        ans=decrypt(msg)
    else:
        print("entered type is not correct")


    ans=''.join(map(str,ans))
    print(ans)


    k=input("type 'yes' to continue and 'no' to stop : \n")

    if(k=='yes'):
        cont=True
    elif(k=='no'):
        cont=False


