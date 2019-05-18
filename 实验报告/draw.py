import math
map_log = lambda lst: list(map(math.log, lst))

import matplotlib.pyplot as plt

'''plt.title('Running Time (Using 4 Cores)')
plt.xlabel('Data Scale')
plt.ylabel('Time (s)')
 
plt.plot(log_scale, map_log(y14),'r', label='Seperate By Rows')
# plt.plot(log_scale, map_log(y104),'purple', label='Scatter-Gather')
plt.plot(log_scale, map_log(y24),'g', label='Seperate By Blocks')
plt.plot(log_scale, map_log(y34),'b', label='Cannon')'''

'''plt.title('Running Time Comparison when Applying Master-Slave Mode \n (Using 4 Cores)')
plt.xlabel('Data Scale')
plt.ylabel('Time (s)')
 

plt.plot(log_scale, y314,'g', label='Collaborative Computing')
plt.plot(log_scale, y34,'b', label='Master-Slave')

plt.xticks(log_scale, scale, rotation=0)'''

'''plt.title('Running Memory Comparison\n(R stands for Row Seperation, B stands for Block Seperation)')
# plt.xlabel('')
plt.ylabel('Memory (MB)')
 
plt.bar([i for i in range(len(mem2048))], mem2048, width = 0.25,facecolor = 'r', edgecolor = 'white', label = 'Total')
plt.bar([i + 0.3 for i in range(len(mem2048))], mem2048_main, width = 0.25,facecolor = 'g', edgecolor = 'white', label = 'Master')
plt.bar([i + 0.6 for i in range(len(mem2048))], mem2048_sub, width = 0.25,facecolor = 'b', edgecolor = 'white', label = 'Slave')
x_label = [' ', 'R-Send-Recv', ' ', 'R-Scatter-Gather', ' ', 'B-Send-Recv\nRows & Columns', ' ', 'B-Send-Recv\nCannon']
loc, labels = plt.xticks()
plt.xticks([elem + 0.3 for elem in list(loc)], x_label, rotation=0)'''

'''plt.title('Running Time\n(In Calculating 1024 * 1024 Matrixes, Using 4 Cores)')
plt.xlabel('Number of Processes')
plt.ylabel('Time (s)')

time = [34.4074, 18.9103, 11.4054, 12.4829, 12.9519]
corenum = [1, 2, 4, 8, 16]
 
plt.plot(corenum, time,'r')'''

plt.title('Overview of Speedup and Increasing Memory')
plt.xlabel('Implementations')

y1 = [1, 1.71, 3.24, 5.53]
y2 = [1, 6.38, 12.66, 23.14]
 
plt.bar([i + 1/4 for i in range(len(y1))], y1, width = 0.4,facecolor = 'r', edgecolor = 'white', label = 'Speedup')
plt.bar([i + 3/4 for i in range(len(y1))], y2, width = 0.4,facecolor = 'b', edgecolor = 'white', label = 'Memory Cost')

loc, labels = plt.xticks()
x_label = ['', 'Serial', '', '2-Pipeline', '', '4-Pipeline', '', '8-Pipeline']
plt.xticks([elem + 1/2 for elem in list(loc)], x_label, rotation=0)

# plt.legend(bbox_to_anchor=[0.5, 0.9])
plt.legend()
# plt.grid()
plt.show()