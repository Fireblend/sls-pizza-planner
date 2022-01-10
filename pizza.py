import math
from datetime import timedelta
from collections import defaultdict
from babel.dates import format_date, format_datetime, format_time

DATE_FORMAT = "%A, %b %d "
INGREDIENTS = {"flour" : 90, "semolina" : 9, "salt" : 1.8, "sourdough" : 36, "water" : 58, "olive_oil":3, "yeast":0.15}
ORIG_INGREDIENTS = {"flour" : 83.33, "semolina" : 8.33, "salt" : 1.66, "sourdough" : 33.33, "water" : 54.166, "olive_oil":8.33, "yeast":0.166}
STEPS = ["feed", "dough", "fridge_in", "fridge_out", "shape", "bake"]

def get_ingredients(pizzas, orig, strings): 
    ings = INGREDIENTS  
    if not orig:
        half_sourdough = math.ceil(ings["sourdough"])/2
        ings['water'] = (math.ceil(ings["flour"]+ings["semolina"])+half_sourdough)*0.7-half_sourdough
    return [{"ingredient":strings[i], "amount":math.ceil(a*pizzas)} for i,a in (ings if not orig else ORIG_INGREDIENTS).items()]

def get_schedule(time, sour_time, ferm_time, rest_time, strings):
    times = [sour_time, 0.5, ferm_time, 0.5, rest_time, 0]   
    basic_sched = [{"step":strings[s],"time":(time-timedelta(hours=sum(times[i:])))} for i,s in enumerate(STEPS)]
    
    adv_sche = defaultdict(lambda: list())

    for x in basic_sched:
        time = x["time"]
        date = format_datetime(time, strings["date_format"], locale=strings["date_locale"]).capitalize()
        adv_sche[date].append({"step":x["step"], "time":time.time().strftime("%I:%M %p")})
    
    print(adv_sche)
    return adv_sche

def get_pizza_data(time, strings, pizzas=6, sour_time=8, ferm_time=24, rest_time=2, orig=False):
    ingredients = get_ingredients(pizzas, orig, strings)
    print(ingredients)
    schedule = get_schedule(time, sour_time, ferm_time, rest_time, strings)
    return {"amounts":ingredients, "total_weight":sum([x["amount"] for x in ingredients]), "schedule":schedule}
