

files1 = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\kaiqi.txt')
#files_num = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\2th.txt','a')

def to_2th (num):                  #将数字转化为二进制
    num_2th = '{:04b}'.format(num)
    return num_2th

def Newfiles(i):
	files_num = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\kaiqi\\2th' +str(i)+'.txt','a')
	return files_num

def to_gery(thous, hunrds, tens, units):#二进制转格雷码
    thous = int(thous , 2)
    thous_g = bin(thous ^ ( thous >> 1 ) ) [2:].zfill(4)
    hunrds = int(hunrds , 2)
    hunrds_g = bin(hunrds ^ ( hunrds >> 1 ) ) [2:].zfill(4)
    tens = int(tens , 2)
    tens_g = bin(tens ^ ( tens >> 1 ) ) [2:].zfill(4)
    units = int(units , 2)
    units_g = bin(units ^ ( units >> 1 ) ) [2:].zfill(4)
    return (thous_g, hunrds_g, tens_g, units_g)

def split_num(line):              #将数字各位分离
    #numbers = float(line) * 1000  # 3.588*1000=3588
    numbers = str(line).replace(".","")
    lists   = list(str(numbers))  # lists=[3,5,8,8]
    units   = to_2th( int(lists[3]) )
    tens    = to_2th( int(lists[2]) )
    hunrds  = to_2th( int(lists[1]) )
    thous   = to_2th( int(lists[0]) )
    return (thous, hunrds, tens, units)

def add_space(thous_g, hunrds_g, tens_g, units_g):#添加空格和回车
    temp1   = str(thous_g)
    thous_G = temp1[0] + ' '+ temp1[1] + ' ' +temp1[2] + ' ' + temp1[3] + '\n'
    temp2   = str(hunrds_g)
    hunrds_G = temp2[0] + ' '+ temp2[1] + ' ' +temp2[2] + ' ' + temp2[3] + '\n'
    temp3   = str(tens_g)
    tens_G = temp3[0] + ' '+ temp3[1] + ' ' +temp3[2] + ' ' + temp3[3] + '\n'
    temp4   = str(units_g)
    units_G = temp4[0] + ' '+ temp4[1] + ' ' +temp4[2] + ' ' + temp4[3] + '\n'
    return(thous_G, hunrds_G, tens_G, units_G)

i = 1
for line in files1:
    (thous, hunrds, tens, units)         = split_num(line)
    (thous_g, hunrds_g, tens_g, units_g) = to_gery(thous, hunrds, tens, units)
    (thous_G, hunrds_G, tens_G, units_G) = add_space(thous_g, hunrds_g, tens_g, units_g)

    strings = str(thous_G) + str(hunrds_G) + str(tens_G) + str(units_G)

    files_num = Newfiles(i)
    files_num.write(strings)
    i = i + 1
    files_num.close()