import utils 
import read_csv
import chars

def run():
    path = "./data.csv"
    '''
    data = read_csv.read_csv(path)
    data_filtered = data[0: 5]
    country, ranks, continent = utils.get_population_average(data_filtered)
    chars.generate_rank_barh_chart(keys, values, ranks, continent)
    '''

    '''
    country = input('Enter a country: ')
    print(f'{country} population by year')
    new_data = utils.get_country(data, country)
    print(new_data)

    if len(new_data) < 0:
        print('Country not found')
        return
    
    keys, values = utils.get_population_by_year(new_data[0])
    chars.generate_bar_chart(keys, values)

    keys, values = utils.get_world_population_percentage(data)
    chars.generate_pie_chart(keys, values)
    '''

    df = read_csv.read_csv_pandas(path)
    df = df[df['Continent'] == 'South America']
    countries = df['Country/Territory'].values
    percentage = df['World Population Percentage'].values
    continent = df['Continent'].values[0]

    chars.generate_pie_chart(countries, percentage, continent)

if __name__ == '__main__':
    run()


