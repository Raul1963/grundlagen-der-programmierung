#1
def nr_perf(num):
    sum_div=0
    for i in range(1, num):
        if num %i==0:
            sum_div+=i
        if num==sum_div:
            return True

def test_nr_perf():
    assert nr_perf(6)==True

def suma_col(matrix):

    for i in range(len(matrix)):
        sum=0
        for j in range(len(matrix[i])):
            sum+=matrix[j][i]
        if nr_perf(sum)==True:
            return True

def test_sum_col():
    assert suma_col([[4,3,10],
                     [1,2,10],
                     [1,1,8]
                     ])==True



test_nr_perf()
test_sum_col()

#2
def sum_diag(matrix):
    result=[]
    for i in range(len(matrix)):
        sum_linie=0
        for j in range(len(matrix[i])):
            # target=matrix[i][j]

            if i!=j:
                sum_linie+=matrix[i][j]
        result.append(sum_linie==matrix[i][i])
    return result
            # if sum_linie==matrix[i][j]:
            #     result.append(True)
            # else:
            #     result.append(False)

def test_sum_diag():
    assert sum_diag([[4,3,1],
                    [1,2,1],
                    [0,5,1]
                     ])==[True,True,False]
    assert sum_diag([[1,2,3],
                     [1,2,1],
                     [0,4,0]
                     ])==[False,True,False]

def main():
    pass

test_sum_diag()
main()

#4

def max_line_file(filename):
    f=open(filename,'r')
    result=[]
    for line in f:
        max_length=0
        words=line.split(' ')

        for word in words:
            word=word.strip()
            if len(word)>max_length:
                max_word, max_length= word, len(word)

        result.append(max_length)

    f.close()
    return result

def test_max_line_file():
    assert max_line_file('data.input')==[4,4]

test_max_line_file()

#5

def is_palindrom(word):
    return word==word[::-1]

def find_count(filename,word):
    f=open(filename, 'r')
    count=0
    for line in f:
        words=line.split(' ')
        for w in words:
            if word==w.strip():
                count+=1
    f.close()
    return count

def count_pali(filename):
    f=open(filename, 'r')
    result={}
    for line in f:
        words=line.split(' ')

        for word in words:
            if is_palindrom(word):
                result[word]=find_count(filename,word.strip())

    f.close()
    return result

def test_count_pali():
    assert count_pali('data2.input')=={'anna':2, 'abbcbba':1, 'abba':2}

test_count_pali()