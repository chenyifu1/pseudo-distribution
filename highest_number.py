import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

#Map phase, we process each record and return a tuple of airport and passenger count.
def map_phase(row):
    id = row[0]
    return (id, 1)

#the Reduce phase, we sum up all counts for each airport
def reduce_phase(mapped_data):
    counts = Counter()

    for id, count in mapped_data:
        counts[id] += count

    return counts

# 读取乘客数据文件
passenger_data = []
with open('AComp_Passenger_data_no_error.csv', 'r') as file:
    reader = csv.reader(file)
    passenger_data = list(reader)

# 定义并行执行的线程数，这里就是定义一个线程数量
numOfthreads = 4

# 并行执行Map阶段，多线程，这样就类似于map阶段了
with ThreadPoolExecutor(max_workers=numOfthreads) as executor:
    data = list(executor.map(map_phase, passenger_data))

# 执行Reduce阶段，将多线程执行得到的结果进行总数统计
total = reduce_phase(data)

# 找出飞行次数最多的乘客
highest_flight_passenger = total.most_common(1)[0]
id = highest_flight_passenger[0]
flight_count = highest_flight_passenger[1]

print("The passenger with the highest number of flights is",id,"with ",flight_count,"flights.")

