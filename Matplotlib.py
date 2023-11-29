import matplotlib.pyplot as plt
import datetime

x = ['Paper one','Paper 2','Paper 3','Paper 4']
y = [85,77,95,100] 

plt.plot(x,y)

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Highschool Math Exam Scores")

plt.grid(True)

plt.savefig("Simple_line_plot.png")

plt.show()

