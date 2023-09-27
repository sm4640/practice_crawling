def cls(t_cls):
    clss = ''
    for i in range(len(t_cls)):
        if t_cls[i] == '(':
            j = i + 1
            while t_cls[j] != ')':
                clss += t_cls[j]
                j += 1
            break
    return clss


lst = []
clear_lst = []
f2 = open("crawlCollegeTimetable//major.txt", 'r', encoding='utf-8')
f3 = open("crawlCollegeTimetable//culture.txt", 'r', encoding='utf-8')
while True:
    line = f2.readline()
    first = line.find('(')
    second = line.rfind('(')
    if not line:
        break
    if line == '\n':
        continue
    if first == second:
        lst.append(line.strip('\n'))
    else:
        lst.append(line.strip('\n')[:line.find(')')+1])
        lst.append(line.strip('\n')[line.find(')')+2:])


while True:
    line = f3.readline()
    first = line.find('(')
    second = line.rfind('(')
    if not line:
        break
    if line == '\n':
        continue
    if first == second:
        lst.append(line.strip('\n'))
    else:
        lst.append(line.strip('\n')[:line.find(')')+1])
        lst.append(line.strip('\n')[line.find(')')+2:])

# 객체를 월화수목금토일로 하고 model 요소는 1~12교시이다.
# 각 객체의 1~12에 따른 내용은 빈 강의실 리스트가 들어가 있음.
# 월 1,2,3 을 고르면 월 1,2,3에 빈 강의실 리스트의 교집합을 반환해줌.

# 데베에 위 정보를 넣기 위해 요일과 시간별 빈강의실 리스트 목록을 여기서 뽑는 로직 구현 필요
# 건물별로 구분하는게 좋을듯 -> 먼저 해야될 일: 건물별 전체 강의실 리스트

baek = []  # 백년관 0
a = []  # 어문관 1
gyo = []  # 교양관 2
ja = []  # 자연대 3
iin = []  # 인경관 4
gong = []  # 공대 5
hak = []  # 학생회관 6


buildings = [baek, a, gyo, ja, iin, gong, hak]

days = ['월', '화', '수', '목', '금', '토', '일', '(']

for i in range(len(lst)):
    clss = cls(lst[i])
    if clss[0] == '0':
        if clss in baek:
            continue
        baek.append(clss)
    elif clss[0] == '1':
        if clss in a:
            continue
        a.append(clss)
    elif clss[0] == '2':
        if clss in gyo:
            continue
        gyo.append(clss)
    elif clss[0] == '3':
        if clss in ja:
            continue
        ja.append(clss)
    elif clss[0] == '4':
        if clss in iin:
            continue
        iin.append(clss)
    elif clss[0] == '5':
        if clss in gong:
            continue
        gong.append(clss)
    elif clss[0] == '6':
        if clss in hak:
            continue
        hak.append(clss)
    else:
        continue


# print(lst)
# print(len(lst))

time = input("요일 시간을 입력하세요(ex 월 1 2): ").split()

for i in range(len(lst)):
    if time[0] == '월':
        if '월' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('월')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '화':
        if '화' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('화')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '수':
        if '수' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('수')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '목':
        if '목' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('목')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '금':
        if '금' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('금')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '토':
        if '토' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('토')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    elif time[0] == '일':
        if '일' in lst[i]:
            for j in time[1:]:
                for k in lst[i][lst[i].find('일')+2:]:
                    if k in days:
                        break
                    if j == k:
                        clss = cls(lst[i])
                        if clss in buildings[int(clss[0])]:
                            buildings[int(clss[0])].remove(clss)
                        break
        else:
            continue
    else:
        break

build = int(input("건물 번호를 입력하세요: "))

print(buildings[build])

# 결과로 나온 강의실이 진짜 빈 강의실인지 체크 해본 코드
# for j in range(len(buildings[build])):
#     for i in range(len(lst)):
#         if cls(lst[i]) == buildings[build][j]:
#             print(lst[i])
#             break


f2.close()
f3.close()
