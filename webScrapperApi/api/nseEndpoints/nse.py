import requests
import brotli

class NSE:

    def __init__(self, cpname):
        self.companyName = cpname
        self.base_url = f"https://www.nseindia.com/api/quote-equity?symbol={self.companyName}"
        self.status_code = None
        self.response = None  
        self._fetch_page()

    def _fetch_page(self):
        try:
            headers = {
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "cookie": (
                    "_ga=GA1.1.1981718691.1705769225; nsit=-RcldLvM4XIdqUe0-HOiSR8q; "
                    "AKA_A2=A; _abck=4E5BDC6A1259E6C323EE4252950F2054~0~YAAQFv7UF0hReLaTAQAAQp7quw0buSz0diRX+/dPdG2tYfqjN+VjuOWxdj8QxRPGqaMqtupljJMxpeJF5JDGfTakC+TkSZpSt63hs4noUMQafKD+62sq2ZsnIidYxekwL3eZBH6Osa5jp1/RFoyq1pPrETFGIyZvXl6oqUhlGhBcSXnpARhTzErSfow5p2M4Ru0L/eflIKxSbmwYtniys3MOn1MKMBtaGCoyn3FlRqhzRj8dhMboP//3hQ8ArMvhLUMYLE/jpWVxfze8MVuUdlRrQRfOywBa04zf50sMsFD2rfyndTjeZ25++TKsJq0cuHLIwfbUmJ9sE2HiNCoh4JhLxgUuiqA1DeFTuWGcY9n5ihx1TctHDY5/pfH00NcldKtKNPQcGxMIwsefH0cLzi95tgbgJy1vCb7tt8q00RvTrM1HwyPaTcu7ukARFjTyggeTATvMgWNLNokPr+UvmQVdLXuYAYfHlBxI62QMbjdnHw==~-1~-1~-1; "
                    "defaultLang=en; ak_bmsc=35360F57517456B4D3D8FAEC0C42C3D4~000000000000000000000000000000~YAAQFv7UF2tReLaTAQAAWaLquxr4wVtxUF5wR7+La3lb0qFrM8gDcSbwAiZxFmvqdkZiOSNmISjdmNkEw6ho55jMY3AXKM9nPQfPHJPf3AOtbAAxaCy7S6hdSSxxAJfFljwtrRF4vD+3QE2ssB5iGhqRGGBhNjhseX9gvxof/L9VHOtEHoCYi2+mEBt5MKYkNG3/QrJ+6EAgoa4bhoOxtrbEV3rTgXNfwihl+0xswPjnyttaxtsEpJ4cyPxho8vNJAXPxPWHrGvTkd+ODTAwxivhKf+eYgsiXBSxO36asHKnxrtns4SSmkNXaMTXGjg0PramsbDs6dUE1YyJpcQ4yF7JSyHByIlpJSW4hV42T3asY9dAYBRyiBRc5geHQ3PsWeHIQp6Q3gZjZv7Bru7QvTC6OI3adXwlB4cQLze9tKZ+Gphp2j7pFisaFD8cdTDfmCyHHeXZIofksysQRVw=; "
                    "nseQuoteSymbols=[{\"symbol\":\"INFY\",\"identifier\":\"\",\"type\":\"equity\"},{\"symbol\":\"RELIANCE\",\"identifier\":\"\",\"type\":\"equity\"}]; "
                    "nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTczNDAyNDgyOSwiZXhwIjoxNzM0MDMyMDI5fQ.z-5H9kw10mN4kv-bIHohBnVIswOfcW9iQXxjPhd5I3I; "
                    "bm_sz=A67C80EA33E3C53F5F41B3CB035301E9~YAAQFv7UF4STeLaTAQAA5B3vuxrSZ+MjAiZToH6TOK2VA7znaiL13wCJ1fSgmpjvnuK3vvqzTYvu6e6v+nUheMd0+uH2juBVe2CbT+S53K90bicOYRCfPoA1PBXcTRleub7OzxDmDYWhSJNUx8yQeHaWRtewore1uYJTJD8nPoR3ioDdx2vQHIjvL/zioRyFq0owuCqkqfG7EM7PZX9PzZnmGXyBb+Z02LcuC+CF2wqkplIuz5rd0cbWus4F8vBbff46N5lYBcgKO6tYKQd5aYPh+sNEnaZzZJP2AfaT7uzHR2zcB5oEF6isgs0MEyVr6GJahUx84vhw5CPr8HELMdnsFE4tS7B8G98lYCyrdy7q6uIof55F9YyipGbJwDryA6SGY0yloXyJXLWaKkfIFqCg5R1hedyxf7eLmmWxfr/a1skfOgxmy4mWfefLQN2y0c4=~4535607~4469828; "
                    "_ga_87M7PJ3R97=GS1.1.1734024534.8.1.1734024829.11.0.0; _ga_WM2NSQKJEK=GS1.1.1734024534.4.1.1734024829.0.0.0; "
                    'RT="z=1&dm=nseindia.com&si=33bf9af4-c1d7-4e2b-b0d5-330ef7eb2e09&ss=m4llfoen&sl=7&se=8c&tt=8th&bcn=%2F%2F684d0d41.akstat.io%2F"; '
                    "bm_sv=2829C37C3F9DD25654B55979EBF167BF~YAAQFv7UF6WTeLaTAQAAmiHvuxotk56pMYZS1uK+0br4tSD+4vfRqxA8NdZgwejC25lYIfeqDSw1gEwhSrEQMkyAEzrmql1rPVkZC3yfctzsmbnd0Gm1Wp9l7vI7PeBP/2AQAyoNie95DolpnaRBzWlMXA3As6fdggANkcA0+NkConLCsz/69P36p6wAd5Qb44WLmXFrILVG81zSuFqkSFxYRH/cH6XM5Seg9FxVYSigRC4iGP0mmhw0nkYaeq0Kj81H~1"
                ),
                "priority": "u=1, i",
                "referer": "https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE",
                "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"
                ),
            }
            
            self.response = requests.get(url=self.base_url,headers=headers)
            self.response.raise_for_status()  
            self.status_code = self.response.status_code
        except requests.exceptions.RequestException as e:
            return self.status_code

    def getStatus(self):
        return self.status_code
    

    def getData(self):
        try:
            decompressed_data = brotli.decompress(self.response.content)
            data = decompressed_data.decode('utf-8')
            jsonData = json.loads(data)
            return "jsonData"
        except AttributeError as e:
            return f"Error parsing titles: {e}" 
