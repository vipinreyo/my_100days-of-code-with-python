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


def init():
    filename = os.path.join(os.path.dirname(__file__), 'data', 'thanksgiving-2015-poll-data.csv')

    with open(filename, 'r') as fin:
        reader = csv.DictReader(fin)

        for row in reader:
            parse(row)


CELEBRATE_TG = 'Do you celebrate Thanksgiving?'
MAINS_1 = 'What is typically the main dish at your Thanksgiving dinner?'
MAINS_2 = 'What is typically the main dish at your Thanksgiving dinner? - Other (please specify)'
MAINS_STYLE1 = 'How is the main dish typically cooked?'
MAINS_STYLE2 = 'How is the main dish typically cooked? - Other (please specify)'
STUFFINGS_1 = 'What kind of stuffing/dressing do you typically have?'
STUFFINGS_2 = 'What kind of stuffing/dressing do you typically have? - Other (please specify)'


def parse(row):
    resp_id = row['RespondentID']
    celebrates_tg = row[CELEBRATE_TG]

    mains = list()
    mains.append(row[MAINS_1])
    mains.append(row[MAINS_2])

    mains_style = list()
    mains_style.append(row[MAINS_STYLE1])
    mains_style.append(row[MAINS_STYLE2])

    stuffings = list()
    stuffings.append(row[STUFFINGS_1])
    stuffings.append(row[STUFFINGS_2])

    cranbery_saucedo = list()
    cranbery_saucedo.append(row['What type of cranberry saucedo you typically have?'])
    cranbery_saucedo.append(row['What type of cranberry saucedo you typically have? - Other (please specify)'])
    gravy = row['Do you typically have gravy?']
    side_dishes = list()
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Brussel sprouts'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Carrots'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Cauliflower'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Corn'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Cornbread'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner?'
                           ' Please select all that apply. - Fruit salad'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Green beans/green bean casserole'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Macaroni and cheese'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Mashed potatoes'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner?'
                           ' Please select all that apply. - Rolls/biscuits'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Squash'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Vegetable salad'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner? '
                           'Please select all that apply. - Yams/sweet potato casserole'])
    side_dishes.append(row['Which of these side dishes aretypically served at your Thanksgiving dinner?'
                           ' Please select all that apply. - Other (please specify)'])
    pie = list()
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Apple'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - Buttermilk'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Cherry'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - Chocolate'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Coconut cream'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - Key lime'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - Peach'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Pecan'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Pumpkin'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - Sweet Potato'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner?'
                    ' Please select all that apply. - None'])
    pie.append(row['Which type of pie is typically served at your Thanksgiving dinner? '
                    'Please select all that apply. - Other (please specify)'])
    desserts = list()
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Apple cobbler'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Apple cobbler'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Blondies'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Brownies'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Carrot cake'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Cheesecake'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Cookies'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Fudge'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Ice cream'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Peach cobbler'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - None'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner? '
                        'Please select all that apply.   - Other (please specify)'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Other (please specify)'])
    desserts.append(row['Which of these desserts do you typically have at Thanksgiving dinner?'
                        ' Please select all that apply.   - Other (please specify)'])
    prays = row['Do you typically pray before or after the Thanksgiving meal?']
    travels = row['How far will you travel for Thanksgiving?']
    programs = row['Will you watch any of the following programs on Thanksgiving?' \
                   ' Please select all that apply. - Macy\'s Parade']
    cutoff_age = row['What\'s the age cutoff at your \"kids\' table\" at Thanksgiving?']
    meets = row['Have you ever tried to meet up with hometown friends on Thanksgiving night?']
    friends_giving = row['Have you ever attended a \"Friendsgiving?\"']
    shop_bf = row['Will you shop any Black Friday sales on Thanksgiving Day?']
    works = row['Do you work in retail?']
    works_bf = row['Will you employer make you work on Black Friday?']
    lives = row['How would you describe where you live?']
    age = row['Age']
    gender = row['What is your gender?']
    income = row['How much total combined money did all members of your HOUSEHOLD earn last year?']
    region = row['US Region']

    record = Record(respondent_id=resp_id, celebrates_thanksgiving=celebrates_tg, mains=mains,
                    mains_cooking_style=mains_style, stuffings=stuffings, cranberry_saucedos=cranbery_saucedo,
                    have_gravy=gravy, side_dishes=side_dishes, pies=pie, desserts=desserts, prays_before_meal=prays,
                    travels=travels, watching_programs=programs, age_cutoff_kids=cutoff_age,
                    meets_with_hometown_friends=meets, attended_friends_giving=friends_giving,
                    shops_black_friday_sales=shop_bf, works_in_retail=works, works_on_black_friday=works_bf,
                    type_of_living=lives, age=age, gender=gender, household_income=income, region=region)
    data.append(record)
    print(record)
