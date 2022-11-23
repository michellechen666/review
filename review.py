#讀取Amazon留言的檔案 (檔名是reviews.txt)
#將他們加入data清單裡
#印出所有資料的長度、第1~2的內容
data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data . append(line) #將每一行的資料加入到data清單裡
        count += 1 #count = count + 1
        if count % 1000 == 0: #如果count的餘數除以1000是0
            print(len(data)) #印出data
print(len(data))
print('------------------')
print(data[0])
print('------------------')
print(data[1])

#<<挑戰>> 算出留言的平均長度
sum_len = 0
for d in data: #每一筆留言資料叫d
    sum_len += len(d) #sum_len = sum_len + len(d)
print('留言平均長度為',sum_len/len(data))