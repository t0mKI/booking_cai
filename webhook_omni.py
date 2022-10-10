from datetime import datetime, timedelta, time
from copy import deepcopy
import smtplib

def main(query):
    if 'type' not in query:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': {'err': "Ungültige Anfrage", "query": query}
        }
    elif query['type'] == "price_calc":
        return calc_price(query)
    elif query['type'] == "mail":
        return mail(query)

    return {
        'statusCode': 404,
        'headers': {'Content-Type': 'application/json'},
        'body': {'err': "Keine Anfrage"}
    }

sending_addr = 'testingMail@gmail.com'
mail_pwd='AAAABBBBCCCCDDDD'
recv_addr = ['testingMail@proton.me']

def mail(query):
    msg = ("From: %s\r\nTo: %s\r\nSubject: Support request\r\n\r\n%s"
           % (sending_addr, ", ".join(recv_addr), query['message']))
    try:
        # connecting to mail server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.set_debuglevel(1)
        server.starttls()
        server.login(sending_addr, mail_pwd)

        # sending e-mail
        sending_failed = server.sendmail(sending_addr, recv_addr, msg)

        # sending e-mail failed
        if len(sending_failed) > 0:
            return {
                'statusCode': 500,
                'body': "Das Versenden der E-Mail hat leider nicht geklappt."
            }

        server.quit()
        return {
            'statusCode': 200
        }

    except smtplib.SMTPException as e:
        return {
            'statusCode': 500,
            'body': f"Das Versenden der E-Mail hat leider nicht geklappt: {e}"
        }

# renting information
# 8:30, 14:00, 19:30 rental beginning times

# 19:30-8:00 rental time overnight
# half day rental:
    # 08:30-13:30 == 5h
    # 14:00-19:00 == 5h
# else daily
#plus optionss

car1_cfg = {
    'hd_extra_charge_we': 10.0,  # additional weekend half day price
    'd_extra_charge_we': 15.0,  # additional weekend daily price
    'hd_charge': 29.0,  # half day price
    'd_charge': 49.0,  # daily price
    'n_charge': 29.0,  # nightly price
    'traylorCoupling': 10.0,
}
car2_cfg = {
    'hd_extra_charge_we': None,  # additional weekend half day price
    'd_extra_charge_we': 15.0,  # additional weekend daily price
    'hd_charge': None,  # half day price
    'd_charge': 59.0,  # daily price
    'n_charge': 29.0,  # nightly price
    'traylorCoupling': 10.0,
}
car3_cfg = {
    'hd_extra_charge_we': 20.0,  # additional weekend half day price
    'd_extra_charge_we': 30.0,  # additional weekend daily price
    'hd_charge': 49.0,  # half day price
    'd_charge': 69.0,  # daily price
    'n_charge': 29.0,  # nightly price
    'traylorCoupling': None,
}
options = {
    'low_co_payment': 15.0,  # lower own payment per damage event: x euro/day
    'everytime_storno': 1.0,  # everytime storno: x euro/day
    'drive_ecologically': 0.01,  # drive ecologically: x euro/driven km
    'flex_tariff': 10.0,  # flexible tariff: x euro/rental
    'tire_glass_protect': 4.0,  # tire and glass protection: x euro/day
    'interior_protect': 2.0,  # interior space protection: x euro/day
    'mobility_service': 3.0,  # mobility service while having car trouble: x euro/day
    'extra_km': 0.15  # additional km: x euro/km
}

# all maxima refer to the overall rental and constrain the price correspondingly
option_max = {
    'low_co_payment': (90.0, '"geringere Selbstbeteiligung (300\u20ac)"'),
    'tire_glass_protect': (24.0, '"Reifen- und Glasschutz"'),
    'interior_protect': (12.0, '"Innenraumschutz"'),
    'mobility_service': (18.0, '"Mobilitätsservice"')
}

drive_eco_min = 1.0             #minimum for driving ecologically
max_nightly_usage_min = 750.0   # max nightly usage: 12.5h converted to min
max_hd_usage_min = 300.0        # max half day usage: 5 h converted to min
we_days = [4, 5]           # weekend days

day_out_str = '''
Auto: {0}
Gesamtpreis: {1} \u20ac
{2} Tage Miete {3} \u20ac = {4} \u20ac
{5} Tage Wochenendzuschlag {6} \u20ac = {7} \u20ac
'''

night_out_str = '''
Auto: {0}
Gesamtpreis (Nachtfahrt): {1} \u20ac
'''

def calc_price(input):
    price = float(0.0)
    price_explain = ''
    d_ctr = 0.0                 #day counter
    we_d_ctr = 0.0              #weekend day counter

    if input['car'] == 'car1':
        car_cfg = car1_cfg
    elif input['car'] == 'car2':
        car_cfg = car2_cfg
    elif input['car'] == 'car3':
        car_cfg = car3_cfg

    # extract time, date values and their delta from input
    start_time = datetime.strptime(
        input["start_time"]["value"], '%H:%M:%S')
    end_time = datetime.strptime(
        input["end_time"]["value"], '%H:%M:%S')

    start_dt = datetime.fromisoformat(input["start_date"]["value"])
    start_dt = start_dt.replace(
        hour=start_time.hour, minute=start_time.minute)

    end_dt = datetime.fromisoformat(input["end_date"]["value"])
    end_dt = end_dt.replace(hour=end_time.hour, minute=end_time.minute)

    delta_date = end_dt - start_dt
    delta_min = delta_date.total_seconds() / 60

    if start_dt > end_dt:
        return {
            'statusCode': 400,
            'headers': {'Content-Type': 'application/json'},
            'body': {
                'price': 'Preis konnte nicht berechnet werden, da Start der Miete > Ende der Miete'}
        }

    # if start_dt<datetime.today():
    #     return {'price': "%.2f €" % -1.0,
    #             'explanation': 'Preis konnte nicht berechnet werden, da Start der Miete < aktueller Zeitpunkt'}

    # nightly usage?
    # is time between 19:30-8:00 and short enough for nightly usage
    if (delta_min <= max_nightly_usage_min) and \
            (start_dt.time() >= time(hour=19, minute=30) or start_dt.time() <= time(hour=8, minute=0)) and \
            (end_dt.time() >= time(hour=19, minute=30) or end_dt.time() <= time(hour=8, minute=0)):
        price += car_cfg['n_charge']

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': {'price': night_out_str.format(input['car'], price)}
        }

    # half day renting
    # 08:30-13:30 == 5h
    # 14:00-19:00 == 5h
    elif (delta_min <= max_hd_usage_min and \
         ((time(hour=8, minute=30) <= start_dt.time() <= time(hour=13, minute=30)) and \
          (time(hour=8, minute=30) <= end_dt.time() <= time(hour=13, minute=30)) ) or \
                                                                                      \
          ((time(hour=14, minute=0) <= start_dt.time() <= time(hour=19, minute=0))) and \
           (time(hour=14, minute=0) <= end_dt.time() <= time(hour=19, minute=0)) ):

        if input['car'] == 'car2':
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': {'price': 'Preis konnte nicht berechnet werden, da für das Fahrzeug keine Halbtagesmiete verfügbar ist'}
            }
        price += car_cfg['hd_charge']
        d_ctr = 0.5

        if start_dt.weekday() in we_days:
            we_d_ctr = 0.5
            price += car_cfg['hd_extra_charge_we']

    # daily renting
    else:
        tmp_date = deepcopy(start_dt)
        #remain_min = -30  # make second condition false for first time
        remain_min = (end_dt - tmp_date).total_seconds() / 60

        # calc daily price, including overlapping ones and weekend days
        while tmp_date.day < end_dt.day or remain_min > -30:
            price += car_cfg['d_charge']
            d_ctr += 1

            # is weekend day (sa,su)?-->extra charge
            if tmp_date.weekday() in we_days:
                price += car_cfg['d_extra_charge_we']
                we_d_ctr += 1

            tmp_date += timedelta(days=1)
            remain_min = (end_dt - tmp_date).total_seconds() / 60


    # day counter for options
    opt_d_ctr = max(d_ctr, 1)
    opt_we_ctr = max(we_d_ctr, 1)

    # include different options charges for both: half day, daily rental
    if input['everytime_storno']:
        charge = options['everytime_storno'] * opt_d_ctr
        price += charge
        price_explain += ('{0} Tage "Jederzeit kostenfrei stornieren": {1} \u20ac').format(d_ctr, charge)

    if input['driven_km']>0:

        # calculate extra km ecologically
        if input['drive_ecologically']:
            charge = max(options['drive_ecologically'] * input['driven_km'],
                         drive_eco_min)
            price += charge
            price_explain += ('\n{0} km "Klimaneutral fahren" (min '
                              + str(drive_eco_min)
                              + '\u20ac): {1} \u20ac').format(
                input['driven_km'], charge)

        # only calculate extra km, that are not included in the basic tariff
        else:
            additional_km = input['driven_km'] - 100 if input['driven_km'] - 100 > 0 else 0

            # add price only, if the additional km>0
            if additional_km > 0:
                charge = options['extra_km'] * additional_km
                price += charge
                price_explain += ('\n{0} "Zusatzkilometer" (min ): {1} \u20ac').format(
                    additional_km, charge)

    if input['flex_tariff']:
        price += options['flex_tariff']
        price_explain += '\n"Flextarif": {0} \u20ac'.format(options['flex_tariff'])

    # calc price for: low co-payment, tire-glass-protection, interior protection, mobility service
    for key, val_tuple in option_max.items():
        # if option is set, account it
        if input[key]:
            charge = min(options[key] * opt_d_ctr,  # overall charge for all days
                         val_tuple[0])  # maximum charge of rental option
            price += charge
            price_explain += ('\n{0} Tage ' +
                              val_tuple[1] +  # description of option
                              ' (max ' + str(val_tuple[0])  # maximum value of option
                              + '\u20ac): {1} \u20ac').format(d_ctr, charge)

    # explain basic renting price depending on days rented
    if d_ctr==0.5:
        charge_idx, we_charge_idx = 'hd_charge', 'hd_extra_charge_we'
    else:
        charge_idx, we_charge_idx = 'd_charge', 'd_extra_charge_we'

    price_explain = day_out_str.format(input['car'], price,
                                       d_ctr if d_ctr==0.5 else int(d_ctr), car_cfg[charge_idx], opt_d_ctr*car_cfg[charge_idx] if d_ctr > 0.0 else 0.0,
                                       we_d_ctr if we_d_ctr==0.5 else int(we_d_ctr), car_cfg[we_charge_idx], opt_we_ctr*car_cfg[we_charge_idx] if we_d_ctr > 0.0 else 0.0) \
                    + price_explain

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {'price': price_explain}
    }