import sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()
print("conned to database")
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
print("creatde table")

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    #print(line)
    org = re.findall("^From.*@([^ ]*) .+", line)
    if len(org) == 0 : continue
    #print("org b =", org, line)
    org = org[0]
    #print("org = ", org)
    # if not line.startswith('From: '): continue
    # pieces = line.split()
    # email = pieces[1]
    #print("checking for email ", email)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
