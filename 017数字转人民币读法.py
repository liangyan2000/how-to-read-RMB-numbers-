digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
han_dict = {'0':'零', '1':'壹', '2':'贰', '3':'叁', '4':'肆', '5':'伍', '6':'陆', '7':'柒', '8':'捌', '9':'玖'}
unit_list = ['拾', '佰', '仟', '万', '亿']

def verify_num(num): #判断是否是浮点数
    res = True
    for i in num:
        if i not in digits and i !='.':
            print ("只能输入数字和小数点")
            res= False
            break
    return res

def verify_length(num): #判断整数部分是否超过12位
    res = True
    if len(num) >12:
        print("数字太大，无法转换")
        res = False
    return res

def make_fraction_str(num): # 把小数部分的数字形如“9978”变成两位数的字符串，且四舍五入。但995以上的仍然写作99
    res = ""
    if num <= 99:
        res = str(num)
    else:
        num_str = str(num) [:3] # 注意这才能包括三个数
        digit_one_two = int(num_str[:2])
        digit_three = int(num_str[2])
        if digit_one_two !=99 and digit_three > 4:
            digit_one_two +=1
        res += str(digit_one_two)
    return res    

def digit_to_han(digit_str): # 把数字字符串变成汉字数字字符串，如“123”变为“壹贰叁”
    result = ""
    for i in digit_str:
        result += han_dict[i]
    return result

def divide_integer_four(integer_str):# 把汉字数字字符串按照四位一段分好，并加上“亿、万”
    ans = ""
    str_len = len(integer_str)
    if str_len > 8:
        ans += (within_four(integer_str[:-8]) + "亿")
        integer_str  = integer_str [-8:]
    if str_len >4:
        ans += (within_four(integer_str[:-4]) + "万")
        integer_str = integer_str [-4:]
    ans += (within_four(integer_str) + "元")
    ans = cut_zero(ans)
    return ans

def within_four(num_str): #在不多于四位数字的字符串里，根据需要加入仟、百、拾
    result = ""
    num_len = len(num_str)
    for i in range (num_len):
        result += num_str[i]
        '''如果不是最后一位数字，而且数字不是零，则需要添加单位（千-百-十对应下标2-1-0，即4位的是4-2-0,4-2-1,4-2-2
        三位的是3-2-0,3-2-1，两位的是2-2-0）'''
        if i != num_len-1 and num_str[i] != "零":
            result += unit_list [num_len-2-i]
    return result

def cut_zero(ans): #处理字符串中连续的零以及亿万、零万等问题
    ans = ans.replace("零零零", "零")
    ans = ans.replace("零零", "零")
    ans = ans.replace("零元", "元")
    ans = ans.replace("亿万", "亿")
    for i in unit_list: #把“零万”改为“万”等等
        bug = "零" + i
        ans = ans.replace(bug, i)  
    return ans


def fraction_read(fraction_str): #将小数部分的汉字数字字符串加上“角、分”
    ans = ""
    if fraction_str [0] != "零":
        ans += (fraction_str[0] + "角")
    if fraction_str [1] != "零":
        ans += (fraction_str[1] + "分")
    return ans


num = input ("请输入一个整数部分在12位以下的浮点数作为钱数：") # 要求用户输入一个浮点数

if verify_num(num) and verify_length(num):
    if num.find('.') == -1: # 注意这里要写出=-1，相反肯定的情况数字不定
        integer_str = digit_to_han(num)
        print("以上钱数读作:" + cut_zero(divide_integer_four(integer_str))+ "整") #没有小数的情况
    else:
        num_divide = num.split('.') #有小数的情况，拆分两个部分
        integer_str = digit_to_han(num_divide[0])
        fraction_part = int(num_divide[1])
        fraction_str = digit_to_han(make_fraction_str(fraction_part))
        print("以上钱数读作:"+ cut_zero(divide_integer_four(integer_str))+ fraction_read(fraction_str))
    