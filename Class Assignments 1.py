#1)
import matplotlib.pyplot as plt  
import numpy as np  
x=np.array([0,50])
y=np.array([0,50])
plt.plot(x,y)  
plt.title('Draw a line')  
plt.show()

#2)
import matplotlib.pyplot as plt  
import numpy as np 
x=np.array([1,2,3])
y=np.array([2,4,0])
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')  
plt.show()


#3)
import matplotlib.pyplot as plt  
import numpy as np 
x=np.array([1,2,3])
y=np.array([2,4,1])
plt.plot(x,y)  
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')  
plt.show()


#4) Write a Python program to draw line charts of the financial data of Alphabet Inc. between October 3, 2016 to October 7, 2016. 
# Sample Financial data (fdata.csv):
'''Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017'''

'''import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()'''

import matplotlib.pyplot as plt
x=['10-03-16','10-04-16','10-05-16','10-06-16','10-07-16']
y1= [774.25, 776.030029, 779.309998, 779, 779.659973]
y2= [776.065002, 778.710022, 782.070007, 780.47998, 779.659973]
y3= [769.5, 772.890015, 775.650024, 775.539978, 770.75]
y4= [772.559998, 776.429993, 776.469971, 776.859985, 775.080017]
plt.xlabel('Date')
plt.ylabel('Data')
plt.title('Financial Data')
plt.plot(x,y1, color='blue', label = 'open')
plt.plot(x,y2, color='orange', label = 'high')
plt.plot(x,y3, color='green', label = 'low')
plt.plot(x,y4, color='red', label = 'close')
plt.legend()
plt.show()


#5) Write a Python program to plot two or more lines on same plot with suitable legends of each line.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
plt.show()


#6) Write a Python program to plot two or more lines with legends, different widths and colors.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
# show a legend on the plot
plt.legend()
plt.show()


#7) Write a Python program to plot two or more lines with different styles.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
#plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
#plt.plot(x2, y2, label = "line 2")

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('plot two or more lines with different styles.')
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted', linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
# show a legend on the plot
plt.legend()
plt.show()