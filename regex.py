from verbalexpressions import VerEx
verbal_expression = VerEx()
# tester=""
# str1="smtp;250 2.0.0 * Message accepted for delivery"


def generate_regex(s1): 
    list_str=s1.split(' ')
    flag=False
    str_reg="tester=VerEx().start_of_line()"
    str_temp=""

    for i in range(len(list_str)):
        if(list_str[i]=="*"):
            flag=True
            if(len(str_temp)>0):
                str_reg=str_reg+ ".find(\"" + str_temp + "\")"
                str_temp=""
            str_reg=str_reg+ ".anything_but('')"
        else:
            if(flag):
                str_temp=str_temp + list_str[i]
            else:
                if(len(str_temp)>0):
                    str_temp=str_temp+" "
                str_temp=str_temp+list_str[i]
            flag=False

    if(len(str_temp)>0):
        str_reg= str_reg+ ".find(\"" + str_temp + "\")"

    str_reg=str_reg+".end_of_line()"

    exec(str_reg,globals())
    return tester.source()

# generate_regex(str1)