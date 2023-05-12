import utils 
import read_csv
import chars


def run():
    # keys, values = utils.get_population()
    # print(keys, values)

    path = "./data.csv"
    data = read_csv.read_csv(path)

    data_filtered = data[0: 10]
    print(data_filtered)
    
    # country = input('Enter a country: ')
    # print(f'{country} population by year')
    # new_data = utils.get_country(data, country)
    # print(new_data)

    # if len(new_data) < 0:
    #     print('Country not found')
    #     return
    
    # keys, values = utils.get_population_by_year(new_data[0])
    # print(keys, values)

    keys, values = utils.get_world_population_percentage(data)

    # keys, values = utils.get_country_ranking_by_population(data_filtered)

    chars.generate_pie_chart(keys, values)




if __name__ == '__main__':
    run()


