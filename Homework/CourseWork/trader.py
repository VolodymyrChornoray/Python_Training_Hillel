from argparse import ArgumentParser
import json
import random


def read_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
        return config


def read_exchange_list(exchange_list):
    with open(exchange_list, 'r') as file:
        exchange = json.load(file)
        return exchange


def change_course(exchange_list):
    with open(exchange_list, 'r') as file:
        data = json.load(file)
        course = data["course"]
        delta = data["delta"]
        new_course = round(random.uniform(course - delta, course + delta), 2)
        data["course"] = new_course
    with open(exchange_list, 'w') as file:
        json.dump(data, file, indent=2)


def buy_sell(exchange_list, args):
    with open(exchange_list, 'r') as file:
        data = json.load(file)
        course = data["course"]
        delta = data["delta"]
        new_course = round(random.uniform(course - delta, course + delta), 2)
        data["course"] = new_course
    with open(exchange_list, 'w') as file:
        json.dump(data, file, indent=2)


pass


def restart_exchange(config_file, exchange_list):
    with open(config_file, 'r') as file:
        config = json.load(file)
    with open(exchange_list, 'w') as file:
        json.dump(config, file, indent=2)


args = ArgumentParser()
args.add_argument("operation", type=str, nargs='?', default='')
args.add_argument("value", type=float, nargs='?', default='0')
args = vars(args.parse_args())
config_file = '../config.json'
exchange_list = '../CourseWork/history_operation.json'
real_course = read_exchange_list(exchange_list)["course"]
uah_acc = read_exchange_list(exchange_list)["uah_acc"]
usd_acc = read_exchange_list(exchange_list)["usd_acc"]
if args["operation"] == 'RATE':
    print(f'Курс:{real_course}')
elif args["operation"] == 'AVAILABLE':
    print(f'UAH:{uah_acc}')
    print(f'USD:{usd_acc}')
elif args["operation"] == 'BUY' and args["value"] > 0:
    usd_acc = args["value"] * real_course
    print(usd_acc)
elif args["operation"] == 'NEXT':
    change_course(exchange_list)
elif args["operation"] == 'RESTART':
    restart_exchange(config_file, exchange_list)
else:
    pass