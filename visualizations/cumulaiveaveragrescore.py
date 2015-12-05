import glob
import csv

filecounter=0
for f in glob.glob("/path/to/tsv-files"):
	with open(f) as csvfile:
		total=0
		filecounter+=1
		counter=0
		reader=csv.reader(csvfile,delimiter="\t")
		headerrow=1
		with open("./data"+str(filecounter)+".tsv","wb") as csvwriter:
			writer=csv.writer(csvwriter,delimiter="\t")
			for row in reader:
				if headerrow==1:
					writer.writerow([row[0],row[1]])
					headerrow=0
				else:
					counter+=1
					total+=float(row[1])
					score=float(total)/counter
					writer.writerow([row[0],score])

