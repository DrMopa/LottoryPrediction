import requests
import csv

def Pull_Data(CSV_URL, CSV_File_Name):

    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        with open(CSV_File_Name, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    escapechar=' ', quoting=csv.QUOTE_NONE)
            for row in my_list:
                date = row[0]
                individual = row[1].split()
                #individual = individual.translate({ord(i): None for i in '[}'})
                newlist = []
                for cell in individual:
                    if cell == "winning_numbers":
                        continue
                    cell = int(cell)
                    newlist.append(cell)
                #print(newlist)
                spamwriter.writerow([newlist])