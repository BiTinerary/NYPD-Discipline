#NYPD Sucks

import requests, csv, os

def createDir(directory):
	if not os.path.exists(directory):
	    os.makedirs(directory)

def dlFile(url, offFolder):
    lfile = 'Officers-Reports/%s/%s' % (offFolder, url.split('/')[-1])
    print lfile
    
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(lfile, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    return lfile

with open('nypd-discipline.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader)
	dada = [r for r in reader]

for each in dada:
	offName = each[1].split('/')
	directPDF = each[3].replace('www', 'assets').replace('html', 'pdf').replace('-nypd', '/nypd')
	
	print directPDF
	offFolder = '%s-%s' % (offName[0], offName[1])

	createDir('Officers-Reports/%s' % offFolder)
	dlFile(directPDF, offFolder)
