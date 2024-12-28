# Euler #93 - Arithmetic Expressions
import itertools

maxn = 15

most = 0

for n1 in range(1,maxn):
    for n2 in range(n1+1,maxn):
        for n3 in range(n2+1,maxn):
            for n4 in range(n3+1,maxn):
                e = str(n1)
                f = str(n2)
                g = str(n3)
                h = str(n4)

                permutations = list(itertools.permutations([e,f,g,h]))

                # Will generate all possible expressions. Insert a random operation between each. 
                # Then insert each possible bracket in each case. 

                # All (?) possible bracket configurations: 
                # abcd
                # (ab)cd
                # (abc)d
                # a(bc)d
                # a(bcd)
                # ab(cd)
                # (ab)(cd)
                # ((ab)c)d
                # (a(bc))d
                # a((bc)d)
                # a(b(cd))

                operations = ["+", "-", "*", "/"]

                results = []
                for [a,b,c,d] in permutations:
                    for op1 in operations:
                        for op2 in operations:
                            for op3 in operations:
                                explist = []
                                explist.append(a+op1+b+op2+c+op3+d) # abcd
                                explist.append("("+a+op1+b+")"+op2+c+op3+d) # (ab)cd
                                explist.append("("+a+op1+b+op2+c+")"+op3+d) # (abc)d
                                explist.append(a+op1+"("+b+op2+c+")"+op3+d) # a(bc)d
                                explist.append(a+op1+"("+b+op2+c+op3+d+")") # a(bcd)
                                explist.append(a+op1+b+op2+"("+c+op3+d+")") # ab(cd)
                                explist.append("("+a+op1+b+")"+op2+"("+c+op3+d+")") # (ab)(cd)
                                explist.append("(("+a+op1+b+")"+op2+c+")"+op3+d) # ((ab)c)d
                                explist.append("("+a+op1+"("+b+op2+c+"))"+op3+d) # (a(bc))d
                                explist.append(a+op1+"(("+b+op2+c+")"+op3+d+")") # a((bc)d)
                                explist.append(a+op1+"("+b+op2+"("+c+op3+d+"))") # a(b(cd))



                                for exp in explist:
                                    try:
                                        result = eval(exp)
                                    except:
                                        #print("Impossile calc.")
                                        pass
                                    if result%1 == 0:
                                        #print(exp,result)
                                        results.append(result)

                values = sorted(list(set(results)))

                values = [x for x in values if x >0]

                i = 0
                while len(values) > i and values[i] == i+1:
                    i+=1

                if i > most: 
                    print(n1, n2, n3, n4, i)
                    most = i

