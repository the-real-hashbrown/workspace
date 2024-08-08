#kap={'usa':'DC','UK':'London','canada':';ottava'}
#print(kap['canada'



heroes={'abb':'spiderman','bbb':'flash','aaa':'superman','aba':'iron man','bab' :'hulk' , 'bba':'batman' , 'aab':'hawkeye', 'bba': 'wonderwoman'}
print ("welcome to your superhero destiny!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print ("what colour do you like best??") 
print ("A).blue B).red")
q1= input ()
print ("what game is better?")
print ("A).minecraft B).fortnight")
q2= input ()
print ("which sport?") 
print("A).tennis B).basketball")
q3= input ()
key=q3+q1+q2
m=input ("do you want to know your superhero destiny!!!! (wrtite y or n)")
if m=="y":
    print("you are "+ heroes[key])
else:
    print ("goodbye!!!")