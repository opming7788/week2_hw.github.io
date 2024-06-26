print("=============Task1==============")

def find_and_print(messages, current_station):
    #Xiaobitan放在greenLine最後一個元素變成greenLineModified
    greenLineModified=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan", 
               "Beimen","Ximen","Xiaonanmen","Chiang Kai-shek Memorial Hall","Guting","Taipower Building",
                "Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian","Xiaobitan"]
    Frdlocation={} #將message中朋友的訊息解構出來放入Frdlocation字典中key:"朋友名"，value:"朋友所在的站名"
    for friend,stationText in messages.items():
        friendstation=[str for str in greenLineModified if str in stationText]
        Frdlocation[friend]=friendstation[0]
        # 讓Frdlocation變成{朋友:所在地點}此種字典=>Frdlocation={"Leslie":"Xiaobitan","Bob":"Ximen","Mary":"Jingmei",\
    #              "Copper":"Taipei Arena","Vivian":"Xindian"}
    friendToStationsDistanceSet={}#計算每個朋友距離每個車站的距離並蒐集成{朋友:[3,2,1,0,1,2,3.....]}的字典，此字典例子=>朋友在Nanjing Fuxing
    for friend,location in Frdlocation.items():#將朋友與該朋友所在車站名稱拿出來遍歷
        if location!="Xiaobitan":#如果該朋友所在車站不是"Xiaobitan"，將該朋友距離每個車站的距離蒐集成list並將該擴充後的list成為朋友名字所對應的鍵值
            friendToStationsDistanceSet[friend]=[abs(greenLineModified[:-1].index(itm)-greenLineModified[:-1].index(location)) for itm in greenLineModified[:-1]]
            #由於"Xiaobitan"距離其他車站距離="Qizhang"距離其他車站距離+1站
            #以下特別加入"Xiaobitan"距離朋友的距離加入該list，並將該擴充後的list成為朋友名字所對應的鍵值
            friendToStationsDistanceSet[friend].append(abs(greenLineModified[:-1].index(location)-greenLineModified[:-1].index("Qizhang"))+1)
        elif location=="Xiaobitan":#如果該朋友所在車站剛好是"Xiaobitan"
            location="Qizhang"#將朋友所在車站換成"Qizhang"站去計算，最後統一加上1
            friendToStationsDistanceSet[friend]=[abs(greenLineModified[:-1].index(itm)-greenLineModified[:-1].index(location))+1 for itm in greenLineModified[:-1]]
            #手動加入朋友距離"Xiaobitan"距離進入list鍵值
            friendToStationsDistanceSet[friend].append(abs(greenLineModified[:-1].index(location)-greenLineModified[:-1].index("Qizhang")))

    myindex=greenLineModified.index(current_station)#current_station目前所在位置

    dis_of_friends={}#計算所有朋友與current_station的距離放入dis_of_friends字典中
    for friend,distSet in friendToStationsDistanceSet.items():
        dis_of_friends[friend]=distSet[myindex]
    # print(dis_of_friends)
    #找出最近距離的朋友們的名字
    min_dist_of_friends = min(dis_of_friends.values())#蒐集距離最近的朋友們的距離
    nearest_friends = [key for key, value in dis_of_friends.items() if value == min_dist_of_friends]
    for frd in nearest_friends:
        print(frd,end=" ")#印出最近距離的朋友們的名字
    print("")
        

# your code here
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

print("=============Task2==============")

schedule=[]
def book(consultants, hour, duration, criteria):
    if len(schedule)==0:
        for consultant in consultants:
            name = consultant.pop("name")  # 移除並取得 "name" 鍵的值
            schedule.append({name: [], **consultant})  # 創建新的字典，將 "name" 鍵替換為新的鍵值對，例如下方schedule
    # schedule=[{"John":[15,16,17], "rate":4.5, "price":1000},
    #           {"Bob":[3,4,5], "rate":3, "price":1200},
    #           {"Jenny":[12,13,14,15], "rate":3.8, "price":800}]
    duration_Time=[] #輸入book(consultants, 14, 3, "price")=>duration_Time=[14,15,16]
    for i in range(1,duration+1):
        duration_Time.append(hour)
        hour+=1
    is_available=[]
    for consultant in schedule:#遍歷schedule取出其中的元素如=>{"xxxx":[被占用時間], "rate":..., "price":...}
        #consultant中的"xxxx":[被占用時間]是否跟duration_Time中的時間衝突，沒衝突代表此人可以預約時間(加入is_vaailable)
        if all(time not in consultant.get(list(consultant.keys())[0], []) for time in duration_Time):
            is_available.append(consultant)        
    if is_available==[]:#如果所有人的時間都被占滿，回傳"No Service"
        print("No Service")
        return
    if criteria=="price":#只考慮價格低的狀況
        min_price_consultant = min(is_available, key=lambda x: x["price"]) #is_available中選出價格最低的
    if criteria=="rate":#只考慮評價最高的狀況
        min_price_consultant = max(is_available, key=lambda x: x["rate"]) 
    first_key = list(min_price_consultant.keys())[0]#取出該價格最低人的名字{"xxxx":[占用時間],"rate":..., "price":...}
    print(first_key)#印出(價格/評價)最低人的名字
    # /////////////////
    #將duration_Time加入該人的占用時間字典元素中{"xxxx":[占用時間],"rate":..., "price":...}
    bob_consultant = next((consultant for consultant in schedule if first_key in consultant), None)
    if bob_consultant:
        bob_consultant[first_key].extend(duration_Time)
        
# your code here
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
] 
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

print("=============Task3==============")

def func(*data):
    mydic={}
    for mytext in data:
        index=len(mytext)//2
        mydic[mytext]=mytext[index]
    # print(mydic)
    unique_values = {}
    for key, value in mydic.items():
    # 如果值不在unique_values的鍵中，將該值添加到unique_values並將其對應的鍵設為當前值
        if value not in unique_values:
            unique_values[value] = key
        # 如果值已經在unique_values的鍵中，將其值設為None表示重複
        else:
            unique_values[value] = None
    # print(unique_values)
    unique_keys = [key for key, value in unique_values.items() if value is not None]

    # print(unique_keys)
    if len(unique_keys)==0:
        print("沒有")
    else:
        # 如果有多筆單獨名字的需要回傳
        for value in unique_keys:
            print(unique_values[value])
        
# your code here
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

print("=============Task4==============")

def get_number(index):
    n=(index+1)//3
    n+=1
    mycolle=[0]
    start=0
    # print(start)
    for i in range(n):
        for a in range(2): 
            start+=4
            mycolle.append(start)
            # print(start)    
        start-=1
        mycolle.append(start)
        # print(start)
    # return mycolle[index]
    print(mycolle[index])

    # your code here

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

print("=============Task5==============")

def find(spaces, stat, n):
    availableSeats_Dist_between_n=[x*y for x,y in zip(spaces,stat)] #將spaces和stat做內積
                                                        #例如:[4, 6, 5, 8]*[0, 1, 1, 1]=[0,6,5,8]
    candidateSeats=[]#蒐集可供搭乘的列車車廂候選
    for itm in availableSeats_Dist_between_n:#遍歷availableSeats_Dist_between_n
        if itm!=0 and itm>=n:#尋找有座位的車廂且該車廂座位數大於需要搭乘的人數n
            candidateSeats.append(itm)#蒐集可供搭乘的列車車廂候選
    if len(candidateSeats)!=0:#若發現有可供搭乘的列車車廂
        print(availableSeats_Dist_between_n.index(min(candidateSeats)))#印出該可供搭乘的列車車廂編號
    else:#找不到可供搭乘的列車車廂回傳-1
        print(-1)

# your code here
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2
