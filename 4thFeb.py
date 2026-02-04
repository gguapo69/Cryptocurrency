
#Program needs to remember changes = use chapter 6 

    

line = '---------------------------------------------------------------------------'
print(line,'\n'+'  Class: 01\n  1.Toh Heng Jui\n  2.Lexiann\n'+line)
print('             Cryptocurrency Portfolio Application Main Menu')
print(line)
print('1. Display Cryptocurrency\n2. Add Cryptocurrency\n3. Amend Cryptocurrency\n4. Remove Crytocurrency\n5. Cryto Porfolio Statement\n6. HJ function(Notification)\n7. Lexiann function\nE. Exit Main Menu')
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
        filename = "cryptocurrency.txt"

        with open(filename, "r") as file:
         lines = file.readlines()

        last_line = lines[-1].strip().split(",")
        next_number = int(last_line[0]) + 1

        name = input("Enter Cryptocurrency name: ")

        while True:
         marketcap = input("Enter Market Cap of Crypto (High, Mid, Low): ").capitalize()
         if marketcap in ["High", "Mid", "Low"]:
             break
        else:
            print("Invalid input")
        

        while True:
            try:
                quantity= float(input("Enter the Quantity of Crypto Bought: "))
                if quantity > 0:
                    break
                print("Invalid input")
            except:
                print("Invalid input")

        while True:
            try:
                bp=float(input("Enter Buy in Price of Crypto: "))
                if bp > 0:
                    break
                print("Price must be greater than zero")
            except:
                print("Invalid input")
        while True:
            cp=float(input("Enter Current Price of Crypto: "))
            if cp > 0:
                break
            print("Invalid input")
        
        new_line = f"{next_number},{name},{marketcap},{quantity},{bp},{cp}\n"

        with open(filename, "a") as file:
            file.write(new_line)

        print("New cryptocurrency record added successfully.")
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
                                         print("Edit Complete")
                                

                                         
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
        filepath = 'cryptocurrency.txt'
        f = open(filepath, 'r')
        lines = f.readlines()
        f.close()

        records = []
        for line1 in lines:
            records.append(line1.strip().split(','))

        header = records[0]
        data = records[1:]

        while True:
            print(line)
            print("No - Cryptocurrency")
            for i in range(len(data)):
                print(i+1, '-', data[i][1])
            print(line)
            choice = input('Enter number to delete or E to exit: ')

            if choice.upper() == 'E':
                print('You have chosen to exit.')
                break
            else:
                try:
                    num = int(choice)
                    if 1 <= num <= len(data):
                        del data[num-1]

                        f = open(filepath, 'w')
                        f.write(','.join(header) + '\n')
                        for i in range(len(data)):
                            data[i][0] = str(i+1)  # re-number
                            f.write(','.join(data[i]) + '\n')
                        f.close()

                        print("Cryptocurrency deleted successfully.")
                        break
                    else:
                        print("Invalid number.")
                except:
                    print("Please enter a number or E.")
        break
    elif option =='5':
        fp = 'cryptocurrency.txt'
        fp1 = open(fp,'r')
        fp2 = fp1.readlines()
        
        fp3 = [q.strip() for q in fp2]
        fp4 = []
        for w in range(len(fp3)):
            e = fp3[w].split(',')
            fp4.append(e) 
        fp4[0].append('Total Invested')
        fp4[0].append('Invested Portfolio Size')
        fp4[0].append('Total Current Value')
        fp4[0].append('Profit/Loss')
        fp4[0].append('Current Portfolio Size')
        sumofti = []
        for r in range (len(fp4)-1):
            ti = float(fp4[r+1][4])*float(fp4[r+1][3])
            fp4[r+1].append(ti)
            sumofti.append(ti)
        soti = sum(sumofti)
        for t in range (len(fp4)-1):
            ips = (fp4[t+1][6]/soti)*100
            ips1 = round(ips,2)
            fp4[t+1].append(str(ips1)+('%'))
        totcurval=[]
        for u in range(len(fp4)-1):
            tcv = float(fp4[u+1][3])*float(fp4[u+1][5])
            fp4[u+1].append(tcv)
            totcurval.append(tcv)
        profloss = []
        for i in range(len(fp4)-1):
            pl = fp4[i+1][8]-fp4[i+1][6]
            fp4[i+1].append(pl)
            profloss.append(pl)
        for o in range(len(fp4)-1):
            cps = (fp4[o+1][8]/sum(totcurval))*100
            cps1= round(cps,2)
            fp4[o+1].append(str(cps1)+'%')
        for p in range(len(fp4)):
            del fp4[p][2]
        fp5 = []
        for x in range (len(fp4)):
            fp5.append(fp4[x])
        fp6 = []
        for y in range(len(fp5)):
            a= fp5[y].pop(6)
            b= fp5[y].pop(6)
            c= fp5[y].pop(6)
            d= fp5[y].pop(6)
            fp6.append([a,b,c,d])
        for row in fp5:
            print('{:<8}{:<14}{:<11}{:<13}{:<14}{:<16}'.format(*row))
        g = ' '
        print ("Sum: ",g*53,soti)
        for row in fp6:
            print('{:<25}{:<21}{:<13}{:<22}'.format(*row))
        gh = ['Sum: ',sum(totcurval),sum(profloss),' ']
        
        print('{:<25}{:<21}{:<13}{:<22}'.format(*gh))
        

        break
    elif option == '6':
        import pywhatkit as pwk
        import time 
        import pyautogui
        import requests
        ph = input('Enter phone number you want to send notifications to? (Include country code, no spaces in phone nummber): ')
        crypto = input('Which cryptocurrency do you wish to track?: ')
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {'ids':crypto,'vs_currencies':'SGD'}
        headers = { 'x-cg-demo-api-key': 'CG-ex47ksXbGSG5ZFUKnZVN57QM' }
        response = requests.get(url,params = params)
        if response.status_code == 200:
            pricehis = [ ]
            data = response.json()
            crypto_price = data[crypto]["sgd"]
            print (crypto_price)
            pricehis.append(crypto_price)
            while(True):
                response = requests.get(url, params = params)
                data = response.json()
                crypto_price = data[crypto]["sgd"]
                time.sleep(30)
                print (crypto_price)
                if crypto_price >= pricehis[0]*1.00005:
                    break
                else:
                    continue
        else:
            print('Failed')
        try:
            pwk.sendwhatmsg_instantly(ph,crypto+'price has increased by 5 percent from'+pricehis[0]+'to'+crypto_price)
            time.sleep(5)
            pyautogui.press("enter")
            print (0)
        except:
            print (1)
        break
    elif option =='7':
        print ('7')
        break
    elif option.upper()== 'E':
        print('You have chosen to exit')
        break





