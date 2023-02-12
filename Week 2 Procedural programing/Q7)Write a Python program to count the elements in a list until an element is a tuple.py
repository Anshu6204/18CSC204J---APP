List = [10,20,30,(40,50),60]
count = 0
for i in List:
    if isinstance(i, tuple):
        break
    count=count + 1
print(count)