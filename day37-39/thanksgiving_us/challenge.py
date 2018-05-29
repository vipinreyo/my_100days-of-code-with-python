import research


def main():
    research.init()

    print('\n\n Regions:\n')
    regions = research.get_regions()
    for k, v in regions.items():
        print(f'({k}).{v}')
    region = regions.get(int(input('Please select the region: ')))

    print('\n\nIncomes\n')
    incomes = research.get_income_ranges()
    for k, v in incomes.items():
        print(f'({k}).{v}')
    income = incomes.get(int(input('Please select the income range: ')))

    research.output_region_appropriate_menu_of_five_items(region, income)


if __name__ == '__main__':
    main()
