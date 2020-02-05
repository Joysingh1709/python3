s="iShIKa"
up=0
lw=0
for i in range(len(s)):
    st=s[i]
    if st.isupper()==True:
        up+=1
    if st.islower()==True:
        lw+=1

print(lw)
print(up)
    
