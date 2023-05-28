def get_population():
    keys = ['ec', 'es']
    values = [100, 200]
    return keys, values

def get_population_by_year(data):
    new_dict = {
        '2022': data['2022 Population'],
        '2020': data['2020 Population'],
        '2015': data['2015 Population'],
        '2010': data['2010 Population'],
        '2000': data['2000 Population'],
        '1990': data['1990 Population'],
        '1980': data['1980 Population'],
        '1970': data['1970 Population'],
    }

    keys = new_dict.keys()
    values = new_dict.values()
    return keys, values

def get_country(data, country):
    new_data = list(filter(lambda item: item['Country/Territory'] == country, data))
    return new_data

def get_world_population_percentage(data):
    new_dict = {item['Country/Territory']: float(item['World Population Percentage']) for item in data}    
    keys = new_dict.keys()
    values = new_dict.values()
    return keys, values

def get_population_average(data):
    new_dict_poblation = {}
    ranks = [item['Rank'] for item in data]
    continent = data[0]['Continent']
    
    for item in data:
        data_population = [int(item['2022 Population']), int(item['2020 Population']), int(item['2015 Population']), int(item['2010 Population']), int(item['2000 Population']), int(item['1990 Population']), int(item['1980 Population']), int(item['1970 Population'])]
        new_dict_poblation[item['Country/Territory']] = sum(data_population) / len(data_population)  

    keys = list(new_dict_poblation.keys())
    values = list(new_dict_poblation.values())
    return keys, values, ranks, continent


def get_population_average_pandas(data):
    ranks = data['Rank'].values
    country = data['Country/Territory'].values
    continent = data['Continent'].values[0]

    return country, ranks, continent


def get_country_ranking_by_population(data):
    new_dict = {f"Rank {item['Rank']}": int(item['Rank']) for item in data}    
    keys = new_dict.keys()
    values = new_dict.values()
    return keys, values