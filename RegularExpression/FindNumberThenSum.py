import re

def sumAll(fileName):
    # accepts file name as string and returns the sum of all numbers present in file
    handle = open(fileName)
    text = handle.read()
    nums = list(map(int,re.findall('[0-9]+', text)))
    return sum(nums)

if __name__ == "__main__":
    print(sumAll("regex_sum_25051.txt"))
