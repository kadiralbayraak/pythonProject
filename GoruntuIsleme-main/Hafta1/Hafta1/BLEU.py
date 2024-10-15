import math
import re


r1="the light shines in the darkness and the darkness has not overcome it"
r2="and the light shines in the darkness and the darkness did not comprehend it"
c1="and the light shines in the darkness and the darkness can not comprehend"
c2="the light shines the darkness has not in the darkness and the trials"

arrLambda=[0.5]


def ngrams(text, Combine):
    words = text.split()
    output = []
    for i in range(len(words) - Combine + 1):
        output.append(words[i:i + Combine])
    return output


def maxNgran(r):
    arr=[]
    arrLen=[]
    kk=len(str(r).split(" "))
    for i in range(1,kk):
        arrLen.append(ngrams(r,i))

    return max(arrLen)


def P_Function(r,c):

    arrSum1=0
    for x in range(1,4):
        arrSum1+=min(len(maxNgran(r)),len(ngrams(c,x)))

    arrSum2=0
    for y in range(1,len(c)):
        arrSum2+=len(ngrams(c,y))

    return arrSum1/arrSum2



def BP(r,c):
    if len(c)>=len(c):
        return 1
    else:
        return math.exp(1-len(r)/len(c))

def BLEU(r,c,choose):
    lambdaValue=0
    if choose==0: lambdaValue=arrLambda[0]

    sum=0
    for x in range(1, 4):
        sum+=math.exp(lambdaValue *math.log(P_Function(r, c)))

    return BP(r, c) *sum

print(BLEU(r1,c1,0))



