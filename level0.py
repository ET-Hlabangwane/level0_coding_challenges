######TASK 0.1
x=0
y=1
print(x)
print(y)
x=x+3
y=y+x
print(x)
print(y)


######TASK 0.2
x=1+1*2
y=(1+1)*2
z=1+(1*2)
a=1+1*2/2
b=(1+1*2)/2
print(x,y,z,a,b)


######TASK 0.3
def hello(word):
    print('Hello',word)

hello('Tshepo')


######TASK 0.4
def even_or_odd(x):
    if x%2==0:
        print('even')
    else:
        print('odd')

even_or_odd(6)


######TASK 0.5
def triangle_area(x,y,z):
    s_p=(x+y+z)*0.5                                #semi-perimeter
    return((s_p*(s_p-x)*(s_p-y)*(s_p-z))**(0.5))

print(triangle_area(3,4,5))


######TASK 0.6
def maximum(*integers):
    number=integers[0]                         #initialise number at the begining of the arguments list
    for i in range(len(integers)):             #iterate over the arguments
        if number<integers[i]:                 #compare to the next item
            number=integers[i]
    return(number)

print(maximum(1,22,3,2))



######TASK 0.7
def celcius_to_fahrenheit(c):
    ftemp=(c*1.8)+32
    return(ftemp)

print(celcius_to_fahrenheit(100),u"\N{DEGREE SIGN}" 'F')

def fahrenheit_to_celcius(f):
    ctemp=(f-32)/1.8
    return(ctemp)
print(fahrenheit_to_celcius(212),u"\N{DEGREE SIGN}" 'C')


######TASK 0.8
def time_convert(x):
    hours=x//60
    var=hours*60
    minu=abs(x-var)
    if hours>1 and minu>1:
        print(str(hours), 'hours', 'and', str(minu), 'minutes')
    elif hours>1 and minu==1:
        print(str(hours), 'hours', 'and', str(minu), 'minute')
    elif hours==1 and minu>1:
        print(str(hours), 'hour', 'and', str(minu), 'minutes')
    elif hours==1 and minu==1:
        print(str(hours), 'hours', 'and', str(minu), 'minutes')
    elif hours==0 and minu==0:
        print(str(hours), 'hours', 'and', str(minu), 'minutes')
    elif hours==0 and minu>1:
        print(str(hours), 'hours', 'and', str(minu), 'minutes')
    elif hours>1 and minu==0:
        print(str(hours), 'hours', 'and', str(minu), 'minutes')
    elif hours==1 and minu==0:
        print(str(hours), 'hour', 'and', str(minu), 'minutes')
    elif hours==0 and minu==1:
        print(str(hours), 'hours', 'and', str(minu), 'minute')

time_convert(121)


######TASK 0.9
def vowel_list(string):
    string_list=list(string.lower())
    v_list=[]
    for i in string_list:
        if i in 'aeiou':
            v_list.append(i)
    vow_list=''.join(v_list)
    print(list(vow_list))

vowel_list('Umuzi')


######TASK 0.10
def common_letter(string1,string2):
    string1_list=list(string1.lower())
    string2_list=list(string2.lower())
    common_l=[]
    for i in string1_list:
        if i in string2_list:
            common_l.append(i)
    common_lett=''.join(common_l)
    print(list(common_lett))

common_letter('hector','Henry')