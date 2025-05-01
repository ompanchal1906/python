#3.	Create a dictionary with dept(department) no, employee roll no. and salary.
#Find out department wise min and maximum of salary.
a={1:{101:10000,102:20000,103:30000,104:40000,105:50000},2:{106:60000,107:70000,108:80000,109:90000,110:100000},
   3:{111:110000,112:120000,113:130000,114:140000,115:150000}}
m=int(input("enter the department number:"))
print("Department number:",m)
print("Minimum salary:",min(a[m].values()))
print("Maximum salary:",max(a[m].values()))








#a={1:{101:10000},2:{102:20000},3:{103:30000},4:{104:40000},5:{105:50000}}
#m=int(input("enter the department number:"))
#for i in a:
 #   print("Department number:",m)
  #  print("Minimum salary:",min(a[m].values()))
   # print("Maximum salary:",max(a[m].values()))
