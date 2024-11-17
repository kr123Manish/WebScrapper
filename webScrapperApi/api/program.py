from bs4 import BeautifulSoup as bs
import requests


class WebScrapper:

    def __init__(self, cpname):
        self.companyName = cpname
        self.base_url = f"https://www.screener.in/company/{self.companyName}/consolidated/"
        self.soup = None  
        self.status_code = None  
        self._fetch_page()

    def _fetch_page(self):
        try:
            res = requests.get(self.base_url)
            res.raise_for_status()  
            self.status_code = res.status_code  
            self.soup = bs(res.content, "html.parser")
        except requests.exceptions.RequestException as e:
            return self.status_code

    def getStatus(self):
        return self.status_code

    
    def getTitles(self):
        try:
            titles = self.soup.find_all(class_="title")
            return [title.get_text(strip=True) for title in titles]
        except AttributeError as e:
            return f"Error parsing titles: {e}"


    def aboutSection(self):
        try:
            companyProfile = self.soup.find_all(class_="company-profile")
            about_section = companyProfile[0].find(class_="sub show-more-box about")
            about_text = about_section.get_text(strip=True)
            return about_text
        except AttributeError as e:
            return f"Error parsing titles: {e}"
    
    def topRatios(self):
        try:
            top_ratios = self.soup.find(id="top-ratios")
            list_items = top_ratios.find_all("li")
            dict_top_ratios={}
            for i in list_items:
                keyName = i.find(class_="name").get_text(strip=True)
                keyValue = i.find(class_="number").get_text(strip=True)
                dict_top_ratios[keyName]= keyValue

            return dict_top_ratios
        except AttributeError as e:
            return f"Error parsing titles: {e}"
    
    
    def analysis(self):
        try:
            analysis = self.soup.find(id="analysis")

            pros = analysis.find_all(class_="pros")
            pros = pros[0].find_all("li")
            pros_list=[]
            for i in pros:
                pros_list.append(i.get_text(strip=True))


            cons = analysis.find_all(class_="cons")
            cons = cons[0].find_all("li")
            cons_list=[]
            for i in cons:
                cons_list.append(i.get_text(strip=True))
            return [ pros_list , cons_list]

        except AttributeError as e:
            return f"Error parsing titles: {e}"