def calc_submult(list, result, subset, index):
    result.append(subset[:])
    for i in range(index, len(list)):
        subset.append(list[i])
        calc_submult(list,result,subset,i+1)
        subset.pop()

def submult(list):
    subset=[]
    result=[]
    index=0
    calc_submult(list,result,subset,index)
    return result
opt=list(input())
print(submult(opt))