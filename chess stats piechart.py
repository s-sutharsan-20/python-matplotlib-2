import matplotlib.pyplot as pyplot
print("Data")
print("Total games played=2374")
print("Won=1200 \n Lost=1149 \n Draw=25")

labels=("Won","Lost","Draw")
sizes=[1200,1149,25]
pyplot.pie(sizes,labels=labels,autopct='%1.f%%',counterclock=False,startangle=105)
pyplot.show()


