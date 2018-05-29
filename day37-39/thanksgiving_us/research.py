import os
import csv
import collections

data = list()

Record = collections.namedtuple('Record', 'respondent_id, celebrates_thanksgiving, mains, mains_cooking_style,'
                                'stuffings, cranberry_saucedos, have_gravy, side_dishes,'
                                'pies, desserts, prays_before_meal, travels, watching_programs,'
                                'age_cutoff_kids, meets_with_hometown_friends, attended_friends_giving,'
                                'shops_black_friday_sales, works_in_retail, works_on_black_friday,'
                                'type_of_living, age, gender, household_income, region')

YES = 'Yes'
CELEBRATE_TG = 'Do you celebrate Thanksgiving?'

MAINS_1 = 'What is typically the main dish at your Thanksgiving dinner?'
MAINS_2 = 'What is typically the main dish at your Thanksgiving dinner? - Other (please specify)'

MAINS_STYLE1 = 'How is the main dish typically cooked?'
MAINS_STYLE2 = 'How is the main dish typically cooked? - Other (please specify)'

STUFFINGS_1 = 'What kind of stuffing/dressing do you typically have?'
STUFFINGS_2 = 'What kind of stuffing/dressing do you typically have? - Other (please specify)'

CRANBERRY_SAUCEDO1 = 'What type of cranberry saucedo you typically have?'
CRANBERRY_SAUCEDO2 = 'What type of cranberry saucedo you typically have? - Other (please specify)'

GRAVY = 'Do you typically have gravy?'

SIDE_DISH1 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Brussel sprouts'
SIDE_DISH2 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Carrots'
SIDE_DISH3 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cauliflower'
SIDE_DISH4 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Corn'
SIDE_DISH5 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Cornbread'
SIDE_DISH6 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Fruit salad'
SIDE_DISH7 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Green beans/green bean casserole'
SIDE_DISH8 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Macaroni and cheese'
SIDE_DISH9 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Mashed potatoes'
SIDE_DISH10 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Rolls/biscuits'
SIDE_DISH11 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Squash'
SIDE_DISH12 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Vegetable salad'
SIDE_DISH13 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Yams/sweet potato casserole'
SIDE_DISH14 = 'Which of these side dishes aretypically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)'

PIE1 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'
PIE2 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Buttermilk'
PIE3 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Cherry'
PIE4 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Chocolate'
PIE5 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Coconut cream'
PIE6 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Key lime'
PIE7 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Peach'
PIE8 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'
PIE9 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'
PIE10 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Sweet Potato'
PIE11 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - None'
PIE12 = 'Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Other (please specify)'

DESSERTS1 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Apple cobbler'
DESSERTS2 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Blondies'
DESSERTS3 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Brownies'
DESSERTS4 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Carrot cake'
DESSERTS5 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cheesecake'
DESSERTS6 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Cookies'
DESSERTS7 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Fudge'
DESSERTS8 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Ice cream'
DESSERTS9 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Peach cobbler'
DESSERTS10 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - None'
DESSERTS11 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)'
DESSERTS12 = 'Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.   - Other (please specify)'

PRAYS = 'Do you typically pray before or after the Thanksgiving meal?'
TRAVELS = 'How far will you travel for Thanksgiving?'
PROGRAM = 'Will you watch any of the following programs on Thanksgiving? Please select all that apply. - Macy\'s Parade'
CUTOFF_AGE = 'What\'s the age cutoff at your \"kids\' table\" at Thanksgiving?'
MEETS = 'Have you ever tried to meet up with hometown friends on Thanksgiving night?'
ATTENDS = 'Have you ever attended a \"Friendsgiving?\"'

SHOPS_BF = 'Will you shop any Black Friday sales on Thanksgiving Day?'
WORKS_IN_R = 'Do you work in retail?'
WORKS_BF = 'Will you employer make you work on Black Friday?'
LIVES = 'How would you describe where you live?'
AGE = 'Age'
GENDER = 'What is your gender?'
INCOME = 'How much total combined money did all members of your HOUSEHOLD earn last year?'
REGION = 'US Region'


def init():
    filename = os.path.join(os.path.dirname(__file__), 'data', 'thanksgiving-2015-poll-data.csv')

    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            parse(row)


def cleanup_list(list_data):
    return [i for i in list_data if i]


def parse(row):
    if row[CELEBRATE_TG] == YES:
        resp_id = row['RespondentID']
        celebrates_tg = row[CELEBRATE_TG]

        mains = list()
        mains.append(row[MAINS_1])
        mains.append(row[MAINS_2])
        mains = cleanup_list(mains)

        mains_style = list()
        mains_style.append(row[MAINS_STYLE1])
        mains_style.append(row[MAINS_STYLE2])
        mains_style = cleanup_list(mains_style)

        stuffings = list()
        stuffings.append(row[STUFFINGS_1])
        stuffings.append(row[STUFFINGS_2])
        stuffings = cleanup_list(stuffings)

        cranbery_saucedo = list()
        cranbery_saucedo.append(row[CRANBERRY_SAUCEDO1])
        cranbery_saucedo.append(row[CRANBERRY_SAUCEDO2])
        cranbery_saucedo = cleanup_list(cranbery_saucedo)

        gravy = row[GRAVY]

        side_dishes = list()
        side_dishes.append(row[SIDE_DISH1])
        side_dishes.append(row[SIDE_DISH2])
        side_dishes.append(row[SIDE_DISH3])
        side_dishes.append(row[SIDE_DISH4])
        side_dishes.append(row[SIDE_DISH5])
        side_dishes.append(row[SIDE_DISH6])
        side_dishes.append(row[SIDE_DISH7])
        side_dishes.append(row[SIDE_DISH8])
        side_dishes.append(row[SIDE_DISH9])
        side_dishes.append(row[SIDE_DISH10])
        side_dishes.append(row[SIDE_DISH11])
        side_dishes.append(row[SIDE_DISH12])
        side_dishes.append(row[SIDE_DISH13])
        side_dishes.append(row[SIDE_DISH14])
        side_dishes = cleanup_list(side_dishes)
        
        pies = list()
        pies.append(row[PIE1])
        pies.append(row[PIE2])
        pies.append(row[PIE3])
        pies.append(row[PIE4])
        pies.append(row[PIE5])
        pies.append(row[PIE6])
        pies.append(row[PIE7])
        pies.append(row[PIE8])
        pies.append(row[PIE9])
        pies.append(row[PIE10])
        pies.append(row[PIE11])
        pies.append(row[PIE12])
        pies = cleanup_list(pies)

        desserts = list()
        desserts.append(row[DESSERTS1])
        desserts.append(row[DESSERTS2])
        desserts.append(row[DESSERTS3])
        desserts.append(row[DESSERTS4])
        desserts.append(row[DESSERTS5])
        desserts.append(row[DESSERTS6])
        desserts.append(row[DESSERTS7])
        desserts.append(row[DESSERTS8])
        desserts.append(row[DESSERTS9])
        desserts.append(row[DESSERTS10])
        desserts.append(row[DESSERTS11])
        desserts.append(row[DESSERTS12])
        desserts = cleanup_list(desserts)

        prays = row[PRAYS]
        travels = row[TRAVELS]
        programs = row[PROGRAM]
        cutoff_age = row[CUTOFF_AGE]
        meets = row[MEETS]
        friends_giving = row[ATTENDS]
        shop_bf = row[SHOPS_BF]
        works = row[WORKS_IN_R]
        works_bf = row[WORKS_BF]
        lives = row[LIVES]
        age = row[AGE]
        gender = row[GENDER]
        income = row[INCOME]
        region = row[REGION]

        record = Record(respondent_id=resp_id, celebrates_thanksgiving=celebrates_tg, mains=mains,
                        mains_cooking_style=mains_style, stuffings=stuffings, cranberry_saucedos=cranbery_saucedo,
                        have_gravy=gravy, side_dishes=side_dishes, pies=pies, desserts=desserts, prays_before_meal=prays,
                        travels=travels, watching_programs=programs, age_cutoff_kids=cutoff_age,
                        meets_with_hometown_friends=meets, attended_friends_giving=friends_giving,
                        shops_black_friday_sales=shop_bf, works_in_retail=works, works_on_black_friday=works_bf,
                        type_of_living=lives, age=age, gender=gender, household_income=income, region=region)
        data.append(record)
    else:
        print('{} does not celebrate thanks giving day. Skipping....'.format(row['RespondentID']))


def get_regions():
    return dict([(i, reg) for i, reg in enumerate(set([r.region for r in data if r.region]), start=1)])


def get_income_ranges():
    return dict([(i, inc) for i, inc in enumerate(set([r.household_income for r in data if r.household_income]), start=1)])


def output_region_appropriate_menu_of_five_items(region, income):
    record = [r for r in data if r.region == region and r.household_income == income][0]
    menu = [f'\n------------------',
            f'       MENU       ',
            f'------------------',
            f'Mains: {record.mains[0]}',
            f'Stuffing: {record.stuffings[0]}',
            f'Pie: {record.pies[0]}',
            f'Side dish: {record.side_dishes[0]}',
            f'Dessert: {record.desserts[0]}']
    print('\n'.join(menu))
