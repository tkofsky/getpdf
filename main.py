import requests
import csv
import time
import datetime
import os
import fitz
countx=0
from pathlib import Path
cnt=0
zerosize =0
toggle=1
#12356
exetime=0
starttime =0
with open('xml apps.dat', encoding='latin-1') as f:  #in
#
#

    sreader=csv.reader(f, delimiter=' ', quotechar='"')
    for row in sreader:
        countx+=1

        #time.sleep(5.1) #5.1 #15.1 5/3 = 1.7 and 15/3 = 5.1 time.sleep(1.7-exetime)
        #print ("exe time:",exetime)
        if exetime > 5.1:
            exetime = 5.1
        #print("real:", exetime)
        #print ("waiting for",5.1-exetime)
        ###############time.sleep(5.1-exetime)
        time.sleep(7.1)

        starttime = time.time()

        sn=str(row[1])
        dte=str(row[2])
        dte = dte[0:4] + "-" + dte[4:6] + "-" + dte[6:8]
        weekdate = "January-02-2023" # case where no date in the xmlapps.dat line
        dtemadrid=str(row[3])   #dtemadrid=str(row[2]) ####2 for pub########################################
        if dtemadrid.isnumeric():
            #dtemadrid = dtemadrid[0:4] + "-" + dtemadrid[4:6] + "-" + dtemadrid[6:8]
            datetime_object = datetime.datetime.strptime(dtemadrid[4:6], "%m")
            full_month_name = datetime_object.strftime("%B")
            madriddate = full_month_name+"-"+dtemadrid[6:8]+"-"+dtemadrid[0:4]


        if toggle==1:
           # print ("toggle1")
            url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn="+sn+"&date="+dte+"&USPTO-API-KEY=p0U59nBx9u2WE0tFzednzmHXv9NbkThe"
        #url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90815289&date=20220326&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"
        #url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90813837&date=2022-03-24&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"

            payload = {}
            headers = {
            'USPTO-API-KEY': 'p0U59nBx9u2WE0tFzednzmHXv9NbkThe',
            'Cookie': 'TS01b2ceaa=01874167c7092c3ccdc9e0fb4fbc51a8fb587127a556b024f727d3c426d9a4333cbb86fd42ea9318b6b10a86c145f4164d0f7f8b30'
        }
            toggle=2
        elif toggle==2:
            #print("toggle0")
            url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8"
            payload = {}
            headers = {
                'USPTO-API-KEY': 'hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8',
                'Cookie': 'TS01b2ceaa=01874167c753dbf5751b58b7ffef05b2c7318a59da9beefbc678177cdad1e398c7629f0de3478f52406d8daa510e06accc0e58063c'
            }
            toggle=3
        elif toggle==3:
            #print("toggle0")
            url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz"
            payload = {}
            headers = {
                'USPTO-API-KEY': 'b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz',
                'Cookie': 'TS01b2ceaa=01874167c70e2f905e3fe4234528f7fd901d5003245e754aece424261f01187dae529bfb3429199e59dc4760b5041caf9b76559a67'
            }
            toggle=1


        response = requests.request("GET", url, headers=headers, data=payload)
        print (response)
        print (sn)
        if response.status_code == 429:
            print("429***************")
            time.sleep(15.1)
            #####################################################################
            if toggle == 1:
                # print ("toggle1")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=p0U59nBx9u2WE0tFzednzmHXv9NbkThe"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90815289&date=20220326&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90813837&date=2022-03-24&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"

                payload = {}
                headers = {
                    'USPTO-API-KEY': 'p0U59nBx9u2WE0tFzednzmHXv9NbkThe',
                    'Cookie': 'TS01b2ceaa=01874167c7092c3ccdc9e0fb4fbc51a8fb587127a556b024f727d3c426d9a4333cbb86fd42ea9318b6b10a86c145f4164d0f7f8b30'
                }
                toggle = 2
            elif toggle == 2:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8',
                    'Cookie': 'TS01b2ceaa=01874167c753dbf5751b58b7ffef05b2c7318a59da9beefbc678177cdad1e398c7629f0de3478f52406d8daa510e06accc0e58063c'
                }
                toggle = 3
            elif toggle == 3:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz',
                    'Cookie': 'TS01b2ceaa=01874167c70e2f905e3fe4234528f7fd901d5003245e754aece424261f01187dae529bfb3429199e59dc4760b5041caf9b76559a67'
                }
                toggle = 1
                ##############################################################
            #quit()
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response)
            print(sn)

        if response.status_code == 429:
            print("429***************")
            time.sleep(15.1)
            #####################################################################
            if toggle == 1:
                # print ("toggle1")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=p0U59nBx9u2WE0tFzednzmHXv9NbkThe"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90815289&date=20220326&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90813837&date=2022-03-24&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"

                payload = {}
                headers = {
                    'USPTO-API-KEY': 'p0U59nBx9u2WE0tFzednzmHXv9NbkThe',
                    'Cookie': 'TS01b2ceaa=01874167c7092c3ccdc9e0fb4fbc51a8fb587127a556b024f727d3c426d9a4333cbb86fd42ea9318b6b10a86c145f4164d0f7f8b30'
                }
                toggle = 2
            elif toggle == 2:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8',
                    'Cookie': 'TS01b2ceaa=01874167c753dbf5751b58b7ffef05b2c7318a59da9beefbc678177cdad1e398c7629f0de3478f52406d8daa510e06accc0e58063c'
                }
                toggle = 3
            elif toggle == 3:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz',
                    'Cookie': 'TS01b2ceaa=01874167c70e2f905e3fe4234528f7fd901d5003245e754aece424261f01187dae529bfb3429199e59dc4760b5041caf9b76559a67'
                }
                toggle = 1
                ##############################################################
            # quit()
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response)
            print(sn)

        if response.status_code == 429:
            print("429***************")
            time.sleep(15.1)
            #####################################################################
            if toggle == 1:
                # print ("toggle1")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=p0U59nBx9u2WE0tFzednzmHXv9NbkThe"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90815289&date=20220326&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"
                # url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=90813837&date=2022-03-24&USPTO-API-KEY=1csin1EnVbBiVYlYqhxPZLThC9s4LjwW"

                payload = {}
                headers = {
                    'USPTO-API-KEY': 'p0U59nBx9u2WE0tFzednzmHXv9NbkThe',
                    'Cookie': 'TS01b2ceaa=01874167c7092c3ccdc9e0fb4fbc51a8fb587127a556b024f727d3c426d9a4333cbb86fd42ea9318b6b10a86c145f4164d0f7f8b30'
                }
                toggle = 2
            elif toggle == 2:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'hMtewl5gpVnSU5oCjGhffQJRPzzbuQa8',
                    'Cookie': 'TS01b2ceaa=01874167c753dbf5751b58b7ffef05b2c7318a59da9beefbc678177cdad1e398c7629f0de3478f52406d8daa510e06accc0e58063c'
                }
                toggle = 3
            elif toggle == 3:
                # print("toggle0")
                url = "https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=" + sn + "&date=" + dte + "&USPTO-API-KEY=b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz"
                payload = {}
                headers = {
                    'USPTO-API-KEY': 'b5gQljPDz10SXyQljqvk2Tz0FDRMH3uz',
                    'Cookie': 'TS01b2ceaa=01874167c70e2f905e3fe4234528f7fd901d5003245e754aece424261f01187dae529bfb3429199e59dc4760b5041caf9b76559a67'
                }
                toggle = 1
                ##############################################################
            # quit()
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response)
            print(sn)




        if response.status_code!=404:
            filename = sn+".pdf"
            htmldir=Path("files/")

            pdffiletouse = htmldir / filename
            with open(pdffiletouse, "wb") as f:
                f.write(response.content)### write pdf to file

            filename = sn + ".pdf"
            htmldir = Path("files/")
            pdffiletouse = htmldir / filename
            file=Path(pdffiletouse)
            if file.exists() and file.stat().st_size > 13000: #1: # check if size is > 200000 bytes and it downloaded correctly
                with fitz.open(pdffiletouse) as doc: ## open PDF
                    text = ""
                    for page in doc:
                        text += page.getText().strip()
                    #print (text)
                    filename = sn + ".txt"
                    htmldir = Path("files/")
                    txtfiletouse = htmldir / filename
                    with open(txtfiletouse,"w", encoding="utf-8") as f:## write as TXT file
                        if sn[:2]=='79':
                            f.write(madriddate+"***"+ text)
                        else:
                            f.write(text)

            else: # save to look at later
                zerosize+=1
                htmldir = Path("files/")
                filetouse = Path(htmldir / 'snerror.txt')
                dte = dte.replace("-", "")
                text = "OOA " + sn + " " + dte+" not complete"
                with open(filetouse, "a", encoding="utf-8") as f:  ## write as TXT file
                    f.write(text)
                    f.write("\n")
        else:  ### if 404 then write to file for later
            cnt+=1
            print (response.status_code)
            htmldir = Path("files/")
            filetouse = Path(htmldir/'snerror.txt')
            dte = dte.replace("-","")
            text = "OOA "+sn+" "+dte
            with open(filetouse, "a", encoding="utf-8") as f:  ## write as TXT file
                f.write(text)
                f.write("\n")
        exetime = time.time() - starttime
        print ("exe time was",exetime)



print ("***************")
print (cnt)
print (zerosize)