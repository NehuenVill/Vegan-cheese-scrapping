from h11 import Data
import requests
import pandas as pd

url = "https://www.vegangrocerystore.com.au/collections/vegan-cheese"

querystring = {"view":"elspw-json"}

payload = ""
headers = {
    "cookie": "secure_customer_sig=; localization=AU; cart_currency=AUD; _orig_referrer=https^%^3A^%^2F^%^2Fwww.google.com^%^2F; _landing_page=^%^2F; _y=761b8cb6-d84c-4b9f-93d5-63f015056c07; _s=0a44512a-48b7-41c8-b0d8-f88f8d30d9a5; _shopify_y=761b8cb6-d84c-4b9f-93d5-63f015056c07; _shopify_s=0a44512a-48b7-41c8-b0d8-f88f8d30d9a5; _shopify_sa_p=; _fbp=fb.2.1650239868780.1336763426; _sp_ses.b920=*; _sp_id.b920=e70afbcc24fa03c6.1650239870.1.1650239960.1650239870; _shopify_sa_t=2022-04-17T23^%^3A59^%^3A24.526Z",
    "authority": "www.vegangrocerystore.com.au",
    "accept": "*/*",
    "accept-language": "en-AU,en;q=0.9,es-419;q=0.8,es;q=0.7",
    "referer": "https://www.vegangrocerystore.com.au/collections/vegan-cheese?page=2",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def GetData():

    OutPut = []

    Response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    Jresponse = Response.json()

    for i in Jresponse:

        TitleDescription = i['title']

        Tags = i['tags']

        TagsInLine = ""

        for Tag in Tags:

            TagsInLine += ', ' + str(Tag)


        Data = {
            'Title and description': TitleDescription,
                             'Tags': TagsInLine,
        }

        print(Data)

        OutPut.append(Data)

    return OutPut

def SaveData(Data):

    df = pd.DataFrame(Data, columns=['Title and description', 'Tags'])
    df.to_excel('Vegan cheese products.xls', index=False, columns=['Title and description', 'Tags'])


SaveData(GetData())