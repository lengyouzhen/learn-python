#-*-coding:utf-8-*-
print '��ӭʹ��У�����֤������αϵͳ' 
print '------------------------------' 
print ' 1.�������֤��α ' 
print ' 2.����������֤���벢У��'
print ' 3.���ļ���ȡ����10�����֤���벢У��'
print ' 4.�˳�'
print '------------------------------' 
a=input('��������Ҫ���еĲ���:')
if a==1:
    a=input('�������һλ���֣�')
    b=input('������ڶ�λ���֣�')
    c=input('���������λ���֣�')
    d=input('���������λ���֣�')
    e=input('���������λ���֣�')
    f=input('���������λ���֣�')
    g=input('���������λ���֣�')
    h=input('������ڰ�λ���֣�')
    i=input('������ھ�λ���֣�')
    j=input('�������ʮλ���֣�')
    k=input('�������ʮһλ���֣�')
    l=input('�������ʮ��λ���֣�')
    m=input('�������ʮ��λ���֣�')
    n=input('�������ʮ��λ���֣�')
    o=input('�������ʮ��λ���֣�')
    p=input('�������ʮ��λ���֣�')
    q=input('�������ʮ��λ���֣�')
    sum=7*a+9*b+10*c+5*d+8*e+4*f+2*g+1*h+6*i+3*j+7*k+9*l+10*m+5*n+8*o+4*p+2*q#���幫ʽ�������λ���ֳ���ϵ��֮��
    #������
    y = sum%11
    #������������У����
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
    print 'У����Ϊ',ARR[z] 
elif a==2:
    import time,random
    ARR=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2) 
    LAST=('1','0','X','9','8','7','6','5','4','3','2')
    #u'''��������µ�18λ���֤����'''
    t=time.localtime()[0]
    x='%02d%02d%02d%04d%02d%02d%03d'%(random.randint(10,99),random.randint(01,99),random.randint(01,99),random.randint(t - 80, t - 18),random.randint(1,12),random.randint(1,28),random.randint(1,999))
    print x
    y = 0
    for i in range(17):
      y += int(x[i]) * ARR[i]
    print 'Ч����Ϊ', LAST[y % 11]
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
    print 'Ч����Ϊ', LAST[y%11]
else:
    print '��ѡ�����˳�����'''