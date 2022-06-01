def most_frequent(List):
    return max(set(List), key = List.count)
n=int(input())
a=list(map(int,input().split()))
print(most_frequent(a))
