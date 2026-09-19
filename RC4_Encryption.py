S = [101, 124, 172, 10, 166, 26, 46, 91, 2, 137, 39, 243, 253, 25, 3, 30, 47, 238,
196, 38, 94, 149, 15, 32, 248, 51, 158, 150, 106, 183, 67, 219, 95, 177, 138,
152, 13, 188, 118, 108, 207, 151, 41, 142, 236, 103, 55, 72, 20, 244, 216,
14, 168, 90, 4, 42, 153, 64, 250, 129, 97, 225, 87, 199, 204, 100, 16, 249,
191, 82, 43, 131, 24, 169, 69, 54, 96, 77, 255, 84, 1, 143, 242, 123, 21, 93,
61, 102, 224, 107, 109, 79, 80, 23, 229, 6, 156, 181, 105, 159, 33, 141, 18,
104, 9, 56, 233, 178, 127, 111, 135, 206, 202, 128, 31, 71, 211, 222, 45, 66,
163, 189, 167, 201, 232, 17, 251, 198, 170, 155, 115, 57, 228, 98, 190, 76,
59, 239, 37, 147, 180, 240, 197, 200, 19, 0, 213, 99, 125, 44, 195, 164, 176,
121, 220, 212 ,
86, 186, 34, 214, 230, 254, 40, 203, 194, 231, 162, 226, 187, 116, 208, 22,
68, 88, 192, 140, 205, 234, 119, 83, 136, 63, 12, 112, 217, 154, 184, 81, 70,
35, 174, 78, 241, 179, 210, 215, 49, 144, 130, 48, 133, 7, 209, 92, 73, 193,
28, 75, 117, 223, 50, 113, 114, 148, 173, 29, 53, 160, 8, 139, 246, 65, 252,
161, 221, 185, 27, 36, 11, 110, 237, 165, 5, 182, 145, 171, 120, 157, 134,
175, 122, 58, 235, 52, 62, 126, 85, 60, 132, 74, 245, 227, 218, 89, 247, 146]
"""key = []
#key is for generating an output and can [0x88, 0x33, 0x31, 0x56, ...] whatever you want
for i in range(256):
    S.append(i)
j=0
for i in range(256):
    j=(j+S[i]+key[i%key_size])%256
    temp = S[i]
    S[i] = S[j]
    S[j] = temp"""
def bin_to_int(bin_msg):
    enc_msg = []
    bin_str = ""
    for i, c in enumerate(bin_msg):
        if c == ' ':
            enc_msg.append(int(bin_str, 2))
            bin_str = ""
        elif (i == len(bin_msg)-1):
            bin_str += c
            enc_msg.append(int(bin_str, 2))
        else:
            bin_str += c
    return enc_msg
def str_to_bin(msg):
    bin_msg = ""
    for i, c in enumerate(msg):
        binary_val = f"{ord(c):08b}"
        if len(msg)-1 == i:
            bin_msg += binary_val
        else:
            bin_msg += binary_val + ' '
    return bin_msg
def int_array_to_bin(key):
    bin_msg = ""
    for i, c in enumerate(key):
        binary_val = f"{c:08b}"
        if len(key) - 1 == i:
            bin_msg += binary_val
        else:
            bin_msg += binary_val + ' '
    return bin_msg
def encode(bin_msg, key):
    enc_msg = ""
    for i, c in enumerate(bin_msg):   
        if c == ' ':
            enc_msg += " "
        elif c == key[i]:
            enc_msg += "0"
        else:
            enc_msg += "1"
    return enc_msg

def pusdo_rand(msg_len, S=[]):
    i=0
    j=0
    x=0
    K_list=[]
    while x < msg_len:
        i = (i+1)%256
        j = (j+S[i])%256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        K=S[(S[i]+S[j])%256]
        K_list.append(K)
        x+=1
    return K_list

choice = input("Please enter what you want: \n1. char_input\n2. array_input\n3. Test\nEnter Number Choice: ")
if(choice == "1"):
    msg = input("Please enter your msg: ")
    K_list = pusdo_rand(len(msg),S)
    bin_msg = str_to_bin(msg)
    key = int_array_to_bin(K_list)
    new = encode(bin_msg, key)
    enc_msg = bin_to_int(new)
    print(new)
    print(K_list)
    print(enc_msg)   
elif(choice == "2"):
    array_msg = input("Copy and paste array here: ")
    msg = []
    msg_str = ""
    for c in array_msg:
        if c == ' ':
            msg.append(int(msg_str))
            msg_str = ""
        elif (c == '[') | (c == ','):
            continue
        elif c == ']':
            msg.append(int(msg_str))
            break
        else:
            msg_str += c
    K_list = pusdo_rand(len(msg),S)
    bin_msg = int_array_to_bin(msg)
    key = int_array_to_bin(K_list)
    new = encode(bin_msg, key)
    enc_msg = bin_to_int(new)
    print(new)
    print(K_list)
    print(enc_msg)
else:
    msg = input("Please enter your msg: ")
    K_list = pusdo_rand(len(msg),S)
    bin_msg = str_to_bin(msg)
    array_msg = bin_to_int(bin_msg)
    key = int_array_to_bin(K_list)
    new = encode(bin_msg, key)
    enc_msg = bin_to_int(new)
    bin_enc_msg = int_array_to_bin(enc_msg)
    dec_enc = encode(bin_enc_msg, key)
    dec_msg = bin_to_int(dec_enc)
    print(f"msg in binary: {bin_msg}")
    print(f"Puesdo Random Key: {K_list}")
    print(f"Puesdo Random Key in Binary: {key}")
    print(f"Msg in array: {array_msg}")
    print(f"enc_msg: {enc_msg}")
    print(f"dec_msg: {dec_msg}")
