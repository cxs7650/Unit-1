import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 5 # Number of sets of bars
w = 0.8 # Width of each bar
school_a_x =  [t*x + w*n for x in range(d)]

plt.bar(school_a_x, middle_school_a)

#1
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 5 # Number of sets of bars
w = 0.8 # Width of each bar
school_b_x =  [t*x + w*n for x in range(d)]

#2 creating width & height
plt.figure(figsize=(10, 8))
# Make your chart here#creating set of axes
ax = plt.subplot()#3
plt.bar(school_a_x, middle_school_a )#4
plt.bar(school_b_x, middle_school_b)

middle_x = [(a + b)/2.0 for a, b in zip(school_a_x, school_b_x)]#5

ax.set_xticks(middle_x)#6
ax.set_xticklabels(unit_topics)#7
plt.legend(['Middle School A', 'Middle School B'])#8
plt.title("Test Averages on Different Units")#9
plt.xlabel("Unit")
plt.ylabel("Test Average")

plt.show()
plt.savefig('my_side_by_side.png')
