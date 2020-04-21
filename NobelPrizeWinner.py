import urllib.request, json

def read_data_from_api(input_url):
    with urllib.request.urlopen(input_url) as url:
        data = json.loads(url.read().decode())
        return data

def read_data():
    url_laureates = "https://api.nobelprize.org/2.0/laureates"
    url_nobelPrizes = "https://api.nobelprize.org/2.0/nobelPrizes"
    laureates = read_data_from_api(url_laureates)
    nobelPrizes = read_data_from_api(url_nobelPrizes)
    return laureates, nobelPrizes

def get_laurates_id(year, category, nobelPrizes_data):
    nobelPrizes_list = nobelPrizes_data['nobelPrizes']
    storage_dict = {}
    for nobel_prize in nobelPrizes_list:
        award_year = nobel_prize['awardYear']
        category = nobel_prize['category']['en']
        laureates_id = nobel_prize['laureates'][0]['id']
        storage_dict[award_year + "~" + category] = laureates_id

    laureates_id = storage_dict[str(year)+"~"+str(category)]
    return laureates_id

def get_laureates_details(laureates_data):
    laureates_list = laureates_data['laureates']
    storage_dict = {}
    for laureates in laureates_list:
        name = laureates['fullName']['en']
        place = laureates['birth']['place']['country']['en']
        year = laureates['birth']['date'].split('-')[0]
        npy = str(name)+", "+str(place)+", "+str(year)

        nobelPrizes_list = laureates['nobelPrizes']
        nobel_prize = nobelPrizes_list[0]

        award_year = nobel_prize['awardYear']
        category = nobel_prize['category']['en']
        #laureates_id = nobel_prize['laureates'][0]['id']
        storage_dict[award_year + "~" + category] = npy
    return storage_dict

def search_db(year, category):
    laureates_data, nobelPrizes_data = read_data()
    #laurates_id = get_laurates_id(year, category, nobelPrizes_data)
    storage_dict = get_laureates_details(laureates_data)
    key = str(year)+"~"+str(category)
    return storage_dict.get(key)

laureates_details = search_db(2005, 'Economic Sciences')
print(laureates_details)
print("Successfull")



