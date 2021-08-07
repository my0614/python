money = int(input())
m_list = [50000,10000,5000,1000,500,100]
m_count = []

for i in m_list:
    m_count.append(int(money/i))
    money = money%i

for i in range(6):
    print(str(m_list[i])+"원은"+str(m_count[i])+"개")
