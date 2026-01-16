#Program needs to remember changes = use chapter 6 

    

line = '---------------------------------------------------------------------------'
print(line,'\n'+'  Class: 01\n  1.Toh Heng Jui\n  2.Lexiann\n'+line)
print('             Cryptocurrency Portfolio Application Main Menu')
print(line)
print('1. Display Cryptocurrency\n2. Add Cryptocurrency\n3. Amend Cryptocurrency\n4. Remove Crytocurrency\n5. Cryto Porfolio Statement\n6. HJ function\n7. Lexiann function\nE. Exit Main Menu')
print (line)
option = input('Select an option: ')
while (True):
    if option =='1':
        display = []
        filepath = 'cryptocurrency.txt'
        displayr = open(filepath,'r')
        displayc = displayr.readlines()
        cdisplay = [line.strip() for line in displayc]
        for x in range(len(cdisplay)):
            z = cdisplay[x].split(',')
            display.append(z)
        for row in display:
            print ('{:<8} {:<15} {:<15} {:<10} {:<12} {:<12}'.format(*row))
            
        break
    elif option =='2':
        print ('2')
        break
    elif option =='3':
        listforedit = ['Name','Market Cap','Quantity Bought','Buy in Price','Market Price']
        amend = []
        filepath = 'cryptocurrency.txt'
        amendr = open(filepath,'r')
        amend1 = amendr.readlines()
        amend2 = [line.strip() for line in amend1]
        for x in range(len(amend2)):
            a = amend2[x].split(',')
            amend.append(a)
        del amend[0]
        while (True):
            print (line)
            print ("No - Cryptocurrency")
            for x in range(len(amend)):
                print (x+1,'-',amend[x][1])
            print (line)
            print ('Enter 1 to',len(amend),'to edit crytocurrency or E to exit: ',end='')
            s = input( )
            if s.upper() == 'E':
                print ('You have chosen to exit.')
                break
            else:
                 try: 
                     if 0<int(s)<=len(amend):
                        while (True):
                             print (line)
                             print ('Index                 : ',int(s))
                             print ('1.Name                : ',amend[int(s)-1][1])
                             print ('2.Market Cap          : ',amend[int(s)-1][2])
                             print ('3.Quantity Bought     : ',amend[int(s)-1][3])
                             print ('4.Buy in Price        : ',amend[int(s)-1][4])
                             print ('5.Market Price        : ',amend[int(s)-1][5])
                             print ('E to exit')
                             u= input('What do you wish to edit/do : ')
                             if u.upper() == 'E':
                                 print ('You have chosen to exit.')
                                 break
                             else:
                                 try:
                                     if 0<int(u)<=5:
                                         print ('Enter new',listforedit[int(u)-1],'of crypto : ',end='')
                                         new = input(' ')
                                         amend = []
                                         filepath = 'cryptocurrency.txt'
                                         amendr = open(filepath,'r')
                                         amend1 = amendr.readlines()
                                         amend2 = [line.strip() for line in amend1]
                                         for x in range(len(amend2)):
                                             a = amend2[x].split(',')
                                             amend.append(a)
                                         
                                         amend[int(s)].insert(int(u),new)
                                         
                                         del amend[int(s)][int(u)+1]
                                         for a in range(len(amend)):
                                             changes = ','.join(amend[a])
                                             
                                         filepath = 'cryptocurrency.txt'
                                         ac = open(filepath, 'w')
                                         for x in amend:
                                             ac.write(','.join(x) + '\n')
                                

                                         
                                         break
                                     else:
                                         print("Inavlid Input. Please try again.")
                                 except ValueError:
                                     print ('Please enter a valid integer or E.')
                        break
                     else:
                        print ('Your integer was too large. Pleae enter an integer which is an index of a crytocurrency')
                 except ValueError:
                     print ('Please enter a valid integer or E.')
        break
        
    elif option == '4':
        print ('4')
        break
    elif option =='5':
        print ('5')
        break
    elif option == '6':
        print ('6')
        break
    elif option =='7':
        print ('7')
        break
    elif option.upper()== 'E':
        print('You have chosen to exit')
        break

#hj function - find live data last 6 months etc put into a graph and compare 2 different coins