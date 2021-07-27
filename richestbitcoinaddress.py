from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import xlsxwriter
import time
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)
browser.get("https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html")
adres=[]
wallet=[]
adet=[]
firstin=[]
firstout=[]
lastin=[]
lastout=[]
for i in range(19):
    adress = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[2]/a') # adres
    adres.append(adress.text)
    try: # wallet
        cuzdan = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[2]/small/a')
        wallet.append(cuzdan.text)
    except:
        wallet.append('')
    try: # BTC adet
        balance = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[3]')
        z=balance.text.split('BTC ',1)
        adet.append(z[0])
    except:  
        adet.append('')
    fin = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[5]')
    firstin.append(fin.text)
    lin = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[6]')
    lastin.append(lin.text)
    fout = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[8]')
    firstout.append(fout.text)
    lout = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[9]')
    lastout.append(lout.text)
for j in range(81):
    adress = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[2]/a') # adres
    adres.append(adress.text)
    try: # wallet
        cuzdan = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[2]/small/a')
        wallet.append(cuzdan.text)
    except:
        wallet.append('')
    try: # BTC adet
        balance = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[3]')
        z=balance.text.split('BTC ',1)
        adet.append(z[0])
    except:  
        adet.append('')
    fin = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[5]')
    firstin.append(fin.text)
    lin = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[6]')
    lastin.append(lin.text)
    fout = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[8]')
    firstout.append(fout.text)
    lout = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[9]')
    lastout.append(lout.text)

for k in range(99):
    browser.get("https://bitinfocharts.com/top-100-richest-bitcoin-addresses-"+str(k+2)+".html")
    for i in range(19):
        adress = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[2]/a') # adres
        adres.append(adress.text)
        try: # wallet
            cuzdan = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[2]/small/a')
            wallet.append(cuzdan.text)
        except:
            wallet.append('')
        try: # BTC adet
            balance = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[3]')
            z=balance.text.split('BTC ',1)
            adet.append(z[0])
        except:  
            adet.append('')
        fin = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[5]')
        firstin.append(fin.text)
        lin = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[6]')
        lastin.append(lin.text)
        fout = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[8]')
        firstout.append(fout.text)
        lout = browser.find_element_by_xpath('//*[@id="tblOne"]/tbody/tr['+str(i+1)+']/td[9]')
        lastout.append(lout.text)
    for j in range(81):
        adress = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[2]/a') # adres
        adres.append(adress.text)
        try: # wallet
            cuzdan = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[2]/small/a')
            wallet.append(cuzdan.text)
        except:
            wallet.append('')
        try: # BTC adet
            balance = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[3]')
            z=balance.text.split('BTC ',1)
            adet.append(z[0])
        except:  
            adet.append('')
        fin = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[5]')
        firstin.append(fin.text)
        lin = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[6]')
        lastin.append(lin.text)
        fout = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[8]')
        firstout.append(fout.text)
        lout = browser.find_element_by_xpath('//*[@id="tblOne2"]/tbody/tr['+str(j+1)+']/td[9]')
        lastout.append(lout.text)
for i in range(10000):
    print(adres[i] +" "+ wallet[i]+" "+adet[i]+" "+firstin[i]+" "+firstout[i]+" "+lastin[i]+" "+lastout[i])
workbook=xlsxwriter.Workbook('btcaccount.xlsx')
worksheet=workbook.add_worksheet()
for q in range(10000):
    worksheet.write('A'+str(q+1),adres[q])
    worksheet.write('B'+str(q+1),wallet[q])
    worksheet.write('C'+str(q+1),adet[q])
    worksheet.write('D'+str(q+1),firstin[q])
    worksheet.write('E'+str(q+1),firstout[q])
    worksheet.write('F'+str(q+1),lastin[q])
    worksheet.write('G'+str(q+1),lastout[q])
workbook.close()
