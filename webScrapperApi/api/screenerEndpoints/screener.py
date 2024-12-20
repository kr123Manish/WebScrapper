from bs4 import BeautifulSoup as bs
import requests


class Screener:

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
        
    
    def profitLoss(self):
        try:
            profit_loss_data = self.soup.find(id="profit-loss")
            profit_loss_data_th  = profit_loss_data.find_all('th',class_=True)

            year_list = []
            for year in profit_loss_data_th:
                year_list.append(year.get_text(strip=True))


            x = profit_loss_data.find_all('tbody')
            tbody = x[0]  # Or replace with the correct parent containing the <tbody>
            data_dict = {}

            # Find all rows (<tr> elements)
            rows = tbody.find_all('tr')

            # Process each row
            for row in rows:
                # Find the key (first <td> with class="text")
                key_td = row.find('td', class_='text')
                if key_td:
                    key = key_td.get_text(strip=True)  # Extract key as text
                    
                    # Find the other <td> elements for values
                    values = [td.get_text(strip=True) for td in row.find_all('td')[1:]]  # Skip the first <td>
                    
                    # Add key-value pair to dictionary
                    data_dict[key] = values

            return [year_list[1:],data_dict]
        except AttributeError as e:
            return f"Error parsing titles: {e}"