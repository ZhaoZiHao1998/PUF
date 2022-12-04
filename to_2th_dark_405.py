for i in range(1,82):
    files_dark     = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\gery_dark\\2th' + str(i) + '.txt')
    files_405      = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\gery_405\\2th' + str(i) + '.txt')
    files_dark_405 = open('D:\\实验\\实验数据\\iv\\2022-04-13\\iv_data\\python\\gery_dark_405\\2th' + str(i) + '.txt','a')
    for (th1, th2) in zip(files_dark , files_405):
        files_dark_405.write(th1.strip('\n'))
        files_dark_405.write(' ')
        files_dark_405.write(th2)
#将两个数据矩阵拼接