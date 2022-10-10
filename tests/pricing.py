from webhook_omni import main

# nightly very short usage(same day)
exemplary_nightly1 = {
    'type':'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-01'
                   },
    'start_time': {'value':'19:30:00'},
    'end_date': {
                'value' : '2022-04-01'
                 },
    'end_time': {'value':'22:30:00'},
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#exact nightly time used
exemplary_nightly2={
    'type':'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                    'value':'2022-04-01'
                   },
    'start_time': {'value':'19:30:00' },
    'end_date': {
                    'value':'2022-04-02'
                 },
    'end_time': {'value': '08:00:00'},
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False

}
#more than nightly time used-->daily
exemplary_nightly3={
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {'value':'2022-04-01'
                   },
    'start_time': {'value':'19:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'08:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False

}

############################################################
############################################################
############################################################

# not we, within time (1.slot), hd
exemplary_hd1 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'12:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False

}

# not we, exact time (1.slot), hd
exemplary_hd2 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False

}

# not we, over time (1.slot), hd
exemplary_hd3 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'14:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, within time(2.slot), hd
exemplary_hd4 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'17:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False

}

# not we, exact time (2.slot), hd
exemplary_hd5 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'19:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, over time (2.slot), hd
exemplary_hd6 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'19:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

############################################################


# we, within time (1.slot), hd
exemplary_hd7 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'12:30:00'
                   },
    'car': 'car1','everytime_storno': False,
'driven_km': 100,
'drive_ecologically': False,
'flex_tariff': False,
'low_co_payment': False,
'tire_glass_protect': False,
'interior_protect': False,
'mobility_service': False
}

# we, exact time (1.slot), hd
exemplary_hd8 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# we, over time (1.slot), hd
exemplary_hd9 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'14:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# we, within time(2.slot), hd
exemplary_hd10 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'17:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# we, exact time (2.slot), hd
exemplary_hd11 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'19:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# we, over time (2.slot), hd
exemplary_hd12 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'19:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

############################################################
############################################################
############################################################





# not we, within time (1.slot), d
exemplary_d1 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'07:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, exact time (1.slot), d
exemplary_d2 ={
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'08:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, over time (1.slot), d
exemplary_d3 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time':{'value':'14:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, within time(2.slot), d
exemplary_d4 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'10:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, exact time (2.slot), d
exemplary_d5 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

# not we, over time (2.slot), d
exemplary_d6 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-03'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'19:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

############################################################


#  we, within time (1.slot), d
exemplary_d7 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'07:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#  we, exact time (1.slot), d
exemplary_d8 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'08:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#  we, over time (1.slot), d
exemplary_d9 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'08:30:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'14:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#  we, within time(2.slot), d
exemplary_d10 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'10:00:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#  we, exact time (2.slot), d
exemplary_d11 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

#  we, over time (2.slot), d
exemplary_d12 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-03'
                   },
    'end_time': {'value':'19:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

############################################################
############################################################
############################################################


exemplary_time_test1 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-01'
                   },
    'end_time': {'value':'19:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}

exemplary_time_test2 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'19:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-02'
                   },
    'end_time': {'value':'14:30:00'
                   },
    'car': 'car1',
    'everytime_storno': False,
    'driven_km': 100,
    'drive_ecologically': False,
    'flex_tariff': False,
    'low_co_payment': False,
    'tire_glass_protect': False,
    'interior_protect': False,
    'mobility_service': False
}
############################################################
############################################################
############################################################
# exact/lower than 6 days, to test maxima's of all options
exemplary_option_test1 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-04'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': True,
    'driven_km': 150,
    'drive_ecologically': True,
    'flex_tariff': True,
    'low_co_payment': True,
    'tire_glass_protect': True,
    'interior_protect': True,
    'mobility_service': True
}

exemplary_option_test2 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-08'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': True,
    'driven_km': 150,
    'drive_ecologically': True,
    'flex_tariff': True,
    'low_co_payment': True,
    'tire_glass_protect': True,
    'interior_protect': True,
    'mobility_service': True
}

# more than 6 days, to test maxima's of all options
exemplary_option_test3 = {
    'type': 'price_calc',
    'departure': 'Stuttgart',
    'destiny': 'Hamburg',
    'start_date': {
                   'value' : '2022-04-02'
                   },
    'start_time': {'value':'14:00:00'
                   },
    'end_date': {
                   'value' : '2022-04-09'
                   },
    'end_time': {'value':'13:30:00'
                   },
    'car': 'car1',
    'everytime_storno': True,
    'driven_km': 150,
    'drive_ecologically': True,
    'flex_tariff': True,
    'low_co_payment': True,
    'tire_glass_protect': True,
    'interior_protect': True,
    'mobility_service': True
}

from datetime import datetime, timedelta
start_dt=datetime(day=1, year=2022, month=1, hour=13, minute=30)
# a=start_dt.time()>=time(hour=19, minute=30)
# b=start_dt.time()<time(hour=8, minute=0)
#print(time(hour=8, minute=30) <= start_dt.time() < time(hour=13, minute=30))



#nightly
print('we: nightly very short usage(same day):' + str(main(exemplary_nightly1)['body']['price']))
print('we: exact nightly time used: ' + str(main(exemplary_nightly2)['body']['price']))
print('we: more than nightly time used-->daily:' + str(main(exemplary_nightly3)['body']['price']))
# print()
# print()



#####################################

# hd, not we
print('not we, within time (1.slot), hd' + str(main(exemplary_hd1)['body']['price']))
print('not we, exact time (1.slot), hd' + str(main(exemplary_hd2)['body']['price']))
print('not we, over time (1.slot), hd' + str(main(exemplary_hd3)['body']['price']))
print('not we, within time(2.slot), hd' + str(main(exemplary_hd4)['body']['price']))
print('not we, exact time (2.slot), hd' + str(main(exemplary_hd5)['body']['price']))
print('not we, over time (2.slot), hd' + str(main(exemplary_hd6)['body']['price']))
print()
print()

#hd,  we
print('we, within time (1.slot), hd' + str(main(exemplary_hd7)['body']['price']))
print('we, exact time (1.slot), hd' + str(main(exemplary_hd8)['body']['price']))
print('we, over time (1.slot), hd' + str(main(exemplary_hd9)['body']['price']))
print('we, within time(2.slot), hd' + str(main(exemplary_hd10)['body']['price']))
print('we, exact time (2.slot), hd' + str(main(exemplary_hd11)['body']['price']))
print('we, over time (2.slot), hd' + str(main(exemplary_hd12)['body']['price']))
print()
print()


######################################

#d, not we
print('not we, within time (1.slot), d' + str(main(exemplary_d1)['body']['price']))
print('not we, exact time (1.slot), d' + str(main(exemplary_d2)['body']['price']))
print('not we, over time (1.slot), d' + str(main(exemplary_d3)['body']['price']))
print('not we, within time(2.slot), d' + str(main(exemplary_d4)['body']['price']))
print('not we, exact time (2.slot), d' + str(main(exemplary_d5)['body']['price']))
print('not we, over time (2.slot), d' + str(main(exemplary_d6)['body']['price']))
print()
print()

#d,  we
print('we, within time (1.slot), d' + str(main(exemplary_d7)['body']['price']))
print('we, exact time (1.slot), d' + str(main(exemplary_d8)['body']['price']))
print('we, over time (1.slot), d' + str(main(exemplary_d9)['body']['price']))
print('we, within time(2.slot), d' + str(main(exemplary_d10)['body']['price']))
print('we, exact time (2.slot), d' + str(main(exemplary_d11)['body']['price']))
print('we, over time (2.slot), d' + str(main(exemplary_d12)['body']['price']))
print()
print()

# test time exceptions: start > end
print('start>end' + str(main(exemplary_time_test1)['body']['price']))
print('start>end' + str(main(exemplary_time_test2)['body']['price']))
print()
print()

# test options

print('option testing (2 days)' + str(main(exemplary_option_test1)['body']['price']))
print()
print('option testing (6 days)' + str(main(exemplary_option_test2)['body']['price']))
print()
print('option testing (7 days)' + str(main(exemplary_option_test3)['body']['price']))

