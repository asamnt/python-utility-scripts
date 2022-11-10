from nturl2path import url2pathname
import requests
import json
from bs4 import BeautifulSoup
import csv
from pathlib import Path
import re



if __name__ == "__main__":
	
	

	with open("udemy.csv", 'a') as f:

		#Wrote the header once and toggle comment

		header = f.write('id' + ',' + 'title' + ',' + 'url' + ',' + 'completion_ratio' + "\n")	
		
		files = Path('data').glob('*.json')
		# files = sorted(files,key=lambda x:int(re.search("([0-9])+",x).group()))
		for file in files:
			print(file)
			d = open(file, 'r', encoding="utf8")
			data = json.load(d)
		
			for i in range(len(data['results'])):

				iden = data['results'][i]['id']
				iden = str(iden)

				url = data['results'][i]['url']
				url = str(url)

				completion_ratio = data['results'][i]['completion_ratio']
				completion_ratio = str(completion_ratio)

				title = data['results'][i]['title']
				title = title.strip().replace(',', '')

				# last_accessed_time = data['results'][i]['last_accessed_time']
			
				f.write(iden + ',' + title + ',' + url + ',' + completion_ratio + "\n")
			d.close()

			









