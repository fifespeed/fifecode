#takes input, opens & reads file, extracts info,
#displays info in terminal and writes out file

#to see how this works, enter "2022-pubs.txt" when prompted for a file.




print('')

print('')
    
print('Extracting Journal Titles from Publication Citations')
print('---------------------------------------')

import re

pubfile = input('Enter Txt File: ')


if len(pubfile) < 1 : pubfile = ('pubs.txt')
pubs = open(pubfile)

count = 0
counts = dict()

print('File in review: ', pubfile)
print('')

for pub in pubs:
    pub = pub.rstrip()
    j = re.findall('[.?] ([A-zA-z\s]+)[.] 2022', pub)
    count = count + 1
    if len(j) > 0 :
        k = j[0]
        for k in j:
            counts[k] = counts.get(k, 0) + 1
            

print('')


jextract = open('journal_counts.txt', 'w')

lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

#if we want to see all journals display in terminal
#then uncomment out lines 54 & 58


#print('ALL JOURNAL COUNTS')

lst = sorted(lst, reverse=True)
for val,key in lst:
    #print(key,val)
    jextract.write(f'{key,val}\n')
jextract.close()
print()


print()


lst = sorted(lst, reverse=True)
print('-----------------------------')
print('TOP 25 JOURNAL COUNTS')
print('-----------------------------')
for val,key in lst[:25]:
    print(key,val)



print()
print('______________________________')
print('Total Pubs Reviewed: ', count)
print('______________________________')
print()
print('For full list of extracted journals \n'
      'see journal_counts.txt file written out to the folder.')
print()

