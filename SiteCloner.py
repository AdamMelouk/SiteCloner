import os
import pywebcopy



class SiteCloner:
	def __init__(self):
		self.urlToClone  = None
		self.saveToPath  = None
		self.projectName = None



	def clone_site(self):
		pywebcopy.save_webpage(
			url = self.urlToClone,
			project_folder = self.saveToPath,
			project_name = self.projectName 
		)



def main():
	if os.name == "nt":
		pathDivider = "\\"
	else:
		pathDivider = "/"

	urlToClone  = input("https://sh1mmer.com: ")
	projectName = input("sh1mmer_clone: ")
	saveToPath  = os.getcwd() + pathDivider + projectName

	siteCloner = SiteCloner()
	siteCloner.urlToClone  = urlToClone
	siteCloner.saveToPath  = saveToPath
	siteCloner.projectName = projectName

	siteCloner.clone_site() 



if __name__ == "__main__":
	main()
