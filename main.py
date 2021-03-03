from bs4 import BeautifulSoup
import requests
import time

print('Mettez des compétences avec lesquelles vous n\'êtes pas familier')
unfamiliar_skill = input(":")
print(f"Filtrer {unfamiliar_skill}")

def find_jobs():
	html_text = requests.get('https://www.portaljob-madagascar.com/search/advanced/res/1/motcle/symfony')
	soup = BeautifulSoup(html_text.text, 'lxml')
	jobs = soup.find_all('article', class_= 'item_annonce')
	
	for index,job in enumerate(jobs):
		job_name = job.find('strong').text.replace(' ', ' ')
		job_company_name = job.find('h4').text.replace(' ', '')
		job_description = job.find('a', class_='description').text
		job_date_lim = job.find('i', class_='date_lim')
		job_more_info = job.h3.a['href']

		#save result in a text file
		if unfamiliar_skill not in job_description:
			with open(f'jobs/{index}.txt', 'w') as f:
				f.write(f"Poste: {job_name.strip()}\n")
				f.write(f"Nom de l'entreprise: {job_company_name.strip()}\n")
				f.write(f"Déscription: {job_description.strip()}\n")
				f.write(f"Date limite: {job_date_lim}\n")
				f.write(f"En savoir plus: {job_more_info}\n")
				f.write("")
			print(f'File saved: {index}' )	
			
if __name__ == '__main__':
	while  True:
		find_jobs()
		time_wait = 10
		print(f'Veuillez attendre {time_wait} minutes...')
		time.sleep(time_wait * 60)	 