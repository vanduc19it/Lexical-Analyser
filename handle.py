import re
import nltk

f = open('input.txt', 'r')
input = f.read()
input_tokens = nltk.wordpunct_tokenize(input);

print(input_tokens);


keywords = "while|if|else|return|break|continue|int|float|void" 
indentifier = "^[a-zA-z_]+[a-zA-Z0-9_]*"
nums = "([0-9][0-9]*)|(([0-9][0-9]*).('.').([0-9][0-9]*))|(([0-9][0-9]*).('.').'E'([0-9][0-9]*))|(([0-9][0-9]*).('.').([0-9][0-9]*)'E'('+'|'-')[0-9][0-9]*)"
operators_1 = ['+','-'] # addop
operators_2 = ['*','/'] #mulop
operators_3 = ['<','>','<=','>=','==','!='] #relop
operators_4 = ['&&'] #and
operators_5 = ['||'] #or
operators_6 = ['!']  #not
operators_7 = ['='] #=
# operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
# specials = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
special_1 = ['(']
special_2 = [')']
special_3 = ['{']
special_4 = ['}']
special_5 = ['[']
special_6 = [']']
special_7 = [';']
special_8 = ['()']


for token in input_tokens:
    if(re.findall(keywords,token)):
        print("keyword : " + token)
    elif(re.findall(indentifier,token)):
        print("indentifier : " + token)
    elif(re.findall(nums,token)):
        print("num : " + token)
    elif token in operators_1:
        print("addop : " + token)
    elif token in operators_2:
        print("mulop : " + token)
    elif token in operators_3:
        print("relop : " + token)
    elif token in operators_4:
        print("and : " + token)
    elif token in operators_5:
        print("or : " + token)
    elif token in operators_6:
        print("not : " + token)
    elif token in operators_7:
        print("= : " + token)
    elif token in special_1:
        print("( : " + token)
    elif token in special_2:
        print(") : " + token)
    elif token in special_3:
        print("{ : " + token)
    elif token in special_4:
        print("} : " + token)
    elif token in special_5:
        print("[ : " + token)
    elif token in special_6:
        print("] : " + token)
    elif token in special_7:
        print("; : " + token)
    elif token in special_8:
        print("( : (" )
        print(") : )" )
    # elif(re.findall(")",token)):
    #     print("): " + token)
    # elif(re.findall("{",token)):
    #     print("{: " + token)
    # elif(re.findall("}",token)):
    #     print("}: " + token)
    # elif(re.findall("[",token)):
    #     print("[: " + token)
    # elif(re.findall("]",token)):
    #     print("]: " + token)
    # elif(re.findall(operators,token)):
    #     print("operator:" + token)
    # elif(re.findall(specicals,token)):
    #     print("specicals: " + token)
    else:
        print("Error : " + token)