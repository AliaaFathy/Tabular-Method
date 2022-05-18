import itertools
def deleteEmpty(lst):
    if isinstance(lst, list):
        return [deleteEmpty(sublist) for sublist in lst if sublist != []]
    return lst


def hyphen(a):
    count = 0
    a = list(a)
    for i in a:
        if i == '-':
            count += 1
    return count


def coverdMinterms(a):
    coverM = [];
    count = 0;
    n = []
    x = list(a)
    for j in range(len(minterms)):
        z = list(minterms[j])
        count = 0
        for i in range(n_v):
            if x[i] != z[i]:
                count += 1
        if count == hyphen(a):
            coverM.append("".join(z))
            count = 0
    for i in range(len(coverM)):
        n.append(int(coverM[i], 2))
    return n


def binary(i, width):
    s = bin(i)
    return s[2:].zfill(width)


def is_grouped(a, b):
    if isinstance(a, int):
        a = list(binary(a, n_v))
        b = list(binary(b, n_v))
    else:
        a = list(str(a))
        b = list(str(b))
    z = 0
    for i in range(n_v):
        if a[i] != b[i]:
            z += 1
            x = i
    if z == 1:
        a[x] = '-'
        result = "".join(a)
        return result
    else:
        return False


def removeAll(value, list):
    i=0
    while i in range(len(list)):
        if list[i]==value:
            del list[i]
            i=0
        else:
            i+=1
    return list


def converArrtoBin(arr):
    for i in range(len(arr)):
        if isinstance(arr[i], int):
            arr[i] = binary(arr[i], n_v)
    return arr


def tables_grouping(group1, not_grouped):
    group2 = [[] for i in range(len(group1) - 1)]
    checked = []
    c = 0
    all_elements = []
    for i in group1:
        all_elements = all_elements + i
    for i in range(len(group1) - 1):
        for j in group1[i]:
            for k in group1[i + 1]:
                if is_grouped(j, k):
                    group2[c].append(is_grouped(j, k))
                    checked.append(j)
                    checked.append(k)
        c += 1
    for i in all_elements:
        if i not in checked:
            not_grouped.append(i)
    return group2, not_grouped


def numOfOnes(a):
    a = list(binary(a, n_v))
    result = 0
    for i in range(len(a)):
        if a[i] == '1':
            result += 1
    return result


def print_array(arr):
    arr = [[]]
    for a in arr:
        for elem in a:
            print("{}".format(elem).rjust(3), end="\n")
        print(end="")



def convert(s):
    out = ''
    n = 0
    letters= list(["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    for i in range (len(s)) :
            if s[i] == '1':
              out = out + letters[n]
              n=n+1
            elif s[i] == '0':
              out = out +  letters[n]+ '\''
              n=n+1
            elif s[i] == '-':
              n=n+1
    return out


def delete_repetition(a):
    i = 0
    while i < len(a):
        if a.count(a[i]) > 1:
            del a[i]
            i = 0
        else:
            i += 1
    return a


def cost(a):
    a = list(a)
    cost = 0
    for i in range(len(a)):
        if a[i] != '-':
            cost += 1
    if len(a) == 1:
        return cost
    else:
        return cost + 1


def row_colDominance(a, b):
    c = a + b
    i=0
    while i < len(c):
        if c.count(c[i])>1:
            removeAll(c[i],c)
            i=0
        else: i+=1
    list_difference = [item for item in a if item not in b]
    if len(a) == len(b):
        flag = True
    else:
        flag = False
    if c == list_difference and len(a)>=len(b):
        return True, flag
    else:
        return False, flag


def table(decmin, primeIm,s):
    sz = len(str(primeIm[-1]))  # The number of digits of the largest minterm
    chart = {}
    print('\n\n\n' +str(s)+ '\n\nPrime Implicant         |%s\n%s' % ( ' '.join((' ' * (sz - len(str(i)))) + str(i) for i in decmin),
        '=' * (len(decmin) * (sz + 1) + len(decmin) + 17)))
    for i in range(len(primeIm)):
        paired_minterms, v = primeIm[i], 0
        print("%-23s |" % ''.join((paired_minterms)), end='')
        for j in (coverdMinterms(primeIm[i])):
            if j in decmin:
                x = (decmin.index(j)) * (sz + 1)  # The position where we should put 'X'
                print(' ' * abs(x - v) + ' ' * (sz - 1) + 'X', end='')
                v = x + sz
            try:
                chart[j].append(i) if i not in chart[j] else None  # Add minterm in chart
            except KeyError:
                chart[j] = [i]
        print('\n' + '-' * (len(decmin) * (sz + 1) + (len(decmin) + 17)))


n_v = int(input("enter number of variable: "))
numOfMint = int(input("enter number of minterms: "))
minterms = []
for i in range(numOfMint):
    if numOfMint >= pow(2, n_v):
        print("please enter a vaild number of minterms ")
        exit()
    y = int(input("please enter the minterms:"))
    if (pow(2, n_v) - 1) >= y >= 0 and y not in minterms:
        minterms.append(y)
    else:
        print("Please Enter a valid number without repeating minterms ")
        exit()

group = [[] for i in range(n_v + 1)]
for j in minterms:
    group[numOfOnes(j)].append(j)
group = deleteEmpty(group)

print("miterms according to number of ones")
for i in range(len(group)):
    print("Number of ones: " + str(list(binary(group[i][0], n_v)).count('1')) + "  Minterms: ")
    for j in group[i]:
        print(str(binary(j, n_v)) + "  " + "(" + str(j) + ")", sep='\n')
print("-----------")
not_grouped = []
checked = []
group2 = [[] for i in range(len(group) - 1)]
fin_group = group
c = 0
for i in range(len(group) - 1):
    print("_________\n Table" + str(i) + ":")
    group2, not_grouped = tables_grouping(fin_group, not_grouped)
    flag = False
    for j in group2:
        if j != []:
            flag = True
    if flag:
        fin_group = deleteEmpty(group2)
    else:
        break
    for j in range(len(fin_group)):
        print("__________")
        for n in fin_group[j]:
            print(n)
if(len(group))==1: not_grouped=group[0]
not_grouped = delete_repetition(not_grouped)

not_grouped = converArrtoBin(not_grouped)

minterms = converArrtoBin(minterms)

for i in range(len(fin_group)):
    fin_group[i] = converArrtoBin(fin_group[i])
print("__________")
print("Unchecked terms:")
print("__________")
for i in not_grouped:
    print(i)
# _______________________________________
# pairing,Not grouped,nom of ones are done
# _______________________________________
primeIm_dict = {}
primeIm = []

for i in range(len(fin_group)):
    for j in fin_group[i]:
        primeIm.append(j)
for i in not_grouped:
    primeIm.append(i)
primeIm = delete_repetition(primeIm)
for i in range(len(primeIm)):
    i = "".join(primeIm[i])
    z = coverdMinterms(i)
    primeIm_dict[i] = [eval('z'), cost(i)]
print("________________________________________")
print("Prime implicants and minterms they cover")
print("________________________________________")
print("Number of Prime Implicants: ",len(primeIm_dict))
print("---------------------------------")
for i in primeIm_dict:
    print("Prime implicant: ", i, "  ", convert(i), '  Minterms & Cost: ', primeIm_dict[i])


# _______________________________________
# prime implicants are done
# _______________________________________

essPI = []
decmin = []
for k in range(len(minterms)):
    decmin.append(int(minterms[k], 2))
for i in decmin:
    z = 0
    for j in range(len(primeIm_dict)):
        if i in primeIm_dict[primeIm[j]][0]:
            z += 1
            x = j
            if z > 1:
                z = 0
                break
    if z == 1:
        essPI.append(primeIm[x])

i = 0
essPI = delete_repetition(essPI)
essPI_dict = {}

for i in essPI:
    w = ""
    w = w + (convert(i))
    essPI_dict[i] = eval('w')
# _______________________________________
# esspI in arr esspI and in dictionary are done
# _______________________________________
s="Prime implicants Chart"
print(table(decmin,primeIm,s))

for i in essPI:
    for j in primeIm:
        for n in range(len(primeIm_dict[i][0])):
            if primeIm_dict[i][0][n] in decmin:
                    removeAll(primeIm_dict[i][0][n],decmin)
            if primeIm_dict[i][0][n] in primeIm_dict[j][0] and j != i:
                removeAll(primeIm_dict[i][0][n], primeIm_dict[j][0])




i=0
while i < len(primeIm):
    if primeIm[i] in essPI:
        del primeIm_dict[primeIm[i]]
        del primeIm[i]
        i = 0
    else:
        i += 1
# delete all minterms of essentals from p IMP
if primeIm:
    s="Prime implicants after removing Essentials"
    print(table(decmin,primeIm,s))
if not primeIm:
    print("All prime implicants are essential")
    print("Final answer:")
    print("F = ", end=" ")
    for i in essPI_dict:
        if i == list(essPI_dict.keys())[-1]:
            print(essPI_dict[i], end=" ")
        else:
            print(essPI_dict[i], "+", end=" ")
    exit()


sum_dict = {}
for i in decmin:
    sum = []
    for j in primeIm:
        if i in primeIm_dict[j][0]:
            sum.append(j)
            sum_dict[i] = eval('sum')
if not sum_dict:
    print("All minterms are covered by Essential prime implicants")
    print("Final answer:")
    print("F = ", end=" ")
    for i in essPI_dict:
        if i == list(essPI_dict.keys())[-1]:
            print(essPI_dict[i], end=" ")
        else:
            print(essPI_dict[i], "+", end=" ")
    exit()
# Row and Column dominance:
# 1 Row dominance:
before1=sum_dict.copy(); before2=primeIm_dict.copy()
notdominated=0
while notdominated ==0 :
    y = list(primeIm_dict.keys())
    i = 0
    j = 0
    q=sum_dict.copy()
    w=primeIm.copy()
    e=decmin.copy()
    r=primeIm_dict.copy()
    removed = []
    while i < len(y):
        j = 0
        while j < len(y):
            a, flag = row_colDominance(primeIm_dict[y[i]][0], primeIm_dict[y[j]][0])
            if a and i != j:
                if not flag and cost(y[i]) > cost(y[j]):
                    j += 1
                    continue
                elif not flag and cost(y[i]) <= cost(y[j]) or flag and cost(y[i]) <= cost(y[j]):
                    del primeIm_dict[y[j]]
                    del y[j]
                    removed.append(primeIm[j])
                    del primeIm[j]
                    i = -1
                    break
                elif flag and cost(y[i]) > cost(y[j]):
                    del primeIm_dict[y[i]]
                    del y[i]
                    removed.append(primeIm[i])
                    del primeIm[i]
                    i = -1
                    break
            j += 1
        i += 1

    j = 0
    i = 0
    x = list(sum_dict.keys())
    for i in removed:
        while j < len(sum_dict):
            if i in sum_dict[x[j]]:
                removeAll(i, sum_dict[x[j]])
                j = 0
            else:
                j += 1
    removed = []
    i = 0
    j = 0
    y = list(sum_dict.keys())
    while i in range(len(y)):
        j = 0
        while j in range(len(y)):
            a, flag = row_colDominance(sum_dict[y[i]], sum_dict[y[j]])
            if a and i != j:
                removed.append(y[i])
                if y[i] in decmin: decmin.remove(y[i])
                del sum_dict[y[i]]
                del [y[i]]
                i = -1;
                break

            j += 1
        i += 1
    x = list(primeIm_dict.keys())
    j = 0
    for i in removed:
        while j < len(primeIm_dict):
            if i in primeIm_dict[x[j]][0]:
                removeAll(i, primeIm_dict[x[j]][0])
                if i in decmin:
                    removeAll(i, decmin)
                j = 0
            else:
                j += 1
    if sum_dict==q and primeIm == w and decmin==e and primeIm_dict==r:
      notdominated=1
    else: notdominated=0


if before1==sum_dict and before2==primeIm_dict: flag = True
s= "After applying Row and Column dominance:"
print(table(decmin,primeIm,s))

final_answer = []
minimum = 52
y = list(sum_dict.values())
combination = []
combination = list(itertools.product(*y))
combination = [list(x) for x in combination]
i = 0
while i < len(combination):
    j = 0
    while j in range(len(combination[i])):
        if combination[i].count(combination[i][j]) > 1:
            del (combination[i][j])
            j = 0
        else:
            j += 1
    i += 1

sum = []
for i in combination:
    summation = 0
    for j in i:
        summation = summation + cost(j)
    sum.append(summation)
minimum = min(sum)
for i in range(len(sum)):
    if sum[i] == minimum:
        final_answer.append(combination[i])
for i in final_answer:
    for j in essPI_dict:
        i.append(j)
print("______________________________")
print("Number of Essential Prime Implicants: ",len(essPI_dict))
print("--------------------------")
print("the essentials = ")
for i in essPI_dict:
    print (essPI_dict[i],' Binary representation: ',i)
if len(essPI_dict) == 0:
    print("none")
print("______________________________")


print("Final solution:")
print("F = ", end=" ")
for j in range(len(final_answer[0])):
        if j == len(final_answer[0]) - 1:
            print(convert(final_answer[0][j]), end=" ")
        else:
            print(convert(final_answer[0][j]), '+', end=" ")
print("\n")

