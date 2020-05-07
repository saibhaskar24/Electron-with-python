from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


raw_html = simple_get('https://www.cricbuzz.com/cricket-match/live-scores')

html = BeautifulSoup(raw_html, 'html.parser')


div = html.findAll('div',class_="cb-col cb-col-100 cb-lv-main")

for i in div:
    name = i.find('h2',class_="cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr")
    mname = i.find('a',class_="text-hvr-underline text-bold")
    series = i.find('span',class_="text-gray")
    venue = i.find('div',class_="cb-col-100 cb-col cb-schdl")
    score = i.find('div',class_="cb-lv-scrs-col text-black")
    result = i.find('div',class_="cb-lv-scrs-col cb-text-complete")
    if name != None:
        print("Tourney :" , name.text)
    print("Name :" ,mname.text)
    print("Venue Status : ",venue.text)
    print("Series :" ,series.text)
    if score != None:
        print("Score :",score.text)
        if result != None:
            print("Result: ", result.text)
    else:
        print("Result: Match is yet to start")
    print()

# if(gimme=="flipkart"):
#     raw_html = simple_get('https://www.flipkart.com/search?q=tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_2_na_na_na&as-pos=0&as-type=RECENT&suggestionId=tv%7CTVs&requestId=87b94593-0f2c-494f-b28a-5694a95be986&as-backfill=on')

#     html = BeautifulSoup(raw_html, 'html.parser')

#     div = html.findAll('div',class_="_3O0U0u")

#     for i in div:
#         name=i.find('div',"_3wU53n")
#         price=i.find('div',"_1vC4OE _2rQ-NK")
#         rating=i.find('div',"hGSR34")
#         features=i.find('ul',"vFw0gD")
#         off=i.find('div',"VGWI6T")
#         if(name!=None):
#             print("Name:",name.text)
#             mrp=price.text
#             print("Price:Rs",mrp[1:])
#             '''print("Features:")
#             if(features!=None):
#                 feature=features.findAll('li',"tVe95H")
#                 for j in feature:
#                     print(j.text)'''
#             if(rating!=None):
#                 print("Rating:",rating.text)
#             else:
#                 print("Rating: Not yet rated")
#             if(off!=None):
#                 print("Offer:",off.text)
#         else:
#             print("None")

