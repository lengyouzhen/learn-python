#-*-coding:utf-8-*-
print '欢迎使用校验身份证号码真伪系统' 
print '------------------------------' 
print ' 1.测试身份证真伪 ' 
print ' 2.随机生成身份证号码并校验'
print ' 3.从文件读取至少10个身份证号码并校验'
print ' 4.退出'
print '------------------------------' 
a=input('请输入想要进行的操作:')
if a==1:
    a=input('请输入第一位数字：')
    b=input('请输入第二位数字：')
    c=input('请输入第三位数字：')
    d=input('请输入第四位数字：')
    e=input('请输入第五位数字：')
    f=input('请输入第六位数字：')
    g=input('请输入第七位数字：')
    h=input('请输入第八位数字：')
    i=input('请输入第九位数字：')
    j=input('请输入第十位数字：')
    k=input('请输入第十一位数字：')
    l=input('请输入第十二位数字：')
    m=input('请输入第十三位数字：')
    n=input('请输入第十四位数字：')
    o=input('请输入第十五位数字：')
    p=input('请输入第十六位数字：')
    q=input('请输入第十七位数字：')
    sum=7*a+9*b+10*c+5*d+8*e+4*f+2*g+1*h+6*i+3*j+7*k+9*l+10*m+5*n+8*o+4*p+2*q#定义公式，计算各位数字乘以系数之和
    #求余数
    y = sum%11
    #根据余数求其校验码
    ARR=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2) 
    if y==1:
        z=0
    elif y==2:
        z='x'
    elif y==3:
        z=9
    elif y==4:
        z=8
    elif y==5:
        z=7
    elif y==6:
        z=6
    elif y==7:
        z=5
    elif y==8:
        z=4
    elif y==9:
        z=3
    elif y==10:
        z=2
    else:
        z=1
    print '校验码为',ARR[z] 
elif a==2:
    import time,random
    ARR=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2) 
    LAST=('1','0','X','9','8','7','6','5','4','3','2')
    #u'''随机生成新的18位身份证号码'''
    t=time.localtime()[0]
    x='%02d%02d%02d%04d%02d%02d%03d'%(random.randint(10,99),random.randint(01,99),random.randint(01,99),random.randint(t - 80, t - 18),random.randint(1,12),random.randint(1,28),random.randint(1,999))
    print x
    y = 0
    for i in range(17):
      y += int(x[i]) * ARR[i]
    print '效验码为', LAST[y % 11]
elif a==3:
    ARR=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2) 
    LAST=('1','0','X','9','8','7','6','5','4','3','2')
    file=open("C:\Users\Administrator\Desktop\id_number.txt")
    print file
    for i in  range(22):
        print file.readline(i)
       # print y
        '''for n in range(17):
            y += int(y[n]) * ARR[n]
    print '效验码为', LAST[y%11]
else:
    print '您选择了退出程序！'''