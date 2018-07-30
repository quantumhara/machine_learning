from sklearn import svm

xor_data=[
    # input1, input2, resutl
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0],
]


data=[]
label=[]
for row in xor_data:
    #print(row)
    #print(xor_data)
    #input("pause")
    p=row[0]
    q=row[1]
    r=row[2]

    data.append([p,q])
    label.append(r)

    #print(data)
    #print(label)
    #input("pause")

clf=svm.SVC()
clf.fit(data, label)

pre=clf.predict(data)
print("prediction", pre)
ok=0; total=0

for idx, answer in enumerate(label):
    print(label)
    print(enumerate(label))
    print(idx, answer)
    p=pre[idx]
    if p==answer: ok+=1
    total+=1
    #input("pause")

print("right percentage:", ok, "/", total, "=", ok/total)
