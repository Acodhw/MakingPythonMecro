a = "3213126312587421621537215362185365216352173671735126358214734128753612738421538621438" # value

print("first = ", a)

i = -1
k = a.find('3') # first find  = -1 check

while not k == -1: # loop until not finded 3
    i = k + i + 1 # sum and get cut index
    print("cut index = ", i, " : ", end="") # print index
    a = a[k+1:len(a)] # cut after '3'
    print(a) # print cut string
    k = a.find('3') # find next '3' index

    
