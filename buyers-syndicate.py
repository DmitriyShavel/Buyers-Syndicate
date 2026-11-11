import random,time,json
class Car:
    def __init__(self,brand,model,year,current_price,condition,type):
        self.brand = brand
        self.model = model
        self.year = year
        self.current_price = current_price
        self.condition = condition
        self.type = type
class YourProperty:
    def __init__(self,balance):
        self.balance = balance
        self.cars_list = []
    def add_garage(self,car_obj):
        self.cars_list.append(car_obj)
    def buy_car(self,car):
        self.cars_list.append(car)
        self.balance -= car.current_price
class CarShop:
    def __init__(self):
        self.available_cars = [
            {'brand' : 'Mercedes', "model" : 'W201', 'year' : 2000, 'current_price' : 10000, 'condition' : 100,'type' : 'regular'},
            {'brand' : 'Ford', "model" : 'Mondeo', 'year' : 2001, 'current_price' : 12000, 'condition' : 100,'type' : 'regular'},
            {'brand' : 'Mazda', "model" : 'Z350', 'year' : 2010, 'current_price' : 20000, 'condition' : 100,'type' : 'sport'},
            {'brand' : 'Wolkswagen', "model" : 'X40', 'year' : 2007, 'current_price' : 16000, 'condition' : 100,'type' : 'regular'}
        ]
random_events = ['CAR RACING','SPONSORS']
car_shop = CarShop()
garage = YourProperty(10000000)
default_car = Car('BMW','E36',2000,5000,90,'regular')
garage.add_garage(default_car)
try:
    with open('data.json','r',encoding='utf-8') as data_out:
        all_data = json.load(data_out)
        for i in all_data['garage_data']:
            if i['model'] != 'E36':
                garage.cars_list.append(Car(**i))
            else:
                garage.cars_list[0] = Car(**i)
        garage.balance = all_data['balance']
        car_shop.available_cars = all_data['car_shop_data']
except FileNotFoundError:
    print("Looks like you re new here and you dont have a load file.")
def check_my_garage(garage):
    print("==========YOUR GARAGE===========")
    if len(garage.cars_list) == 0:
        print("YOUR GARAGE IS EMPTY")
        return
    else:
        print(f'BALANCE: {garage.balance}')
        for num,car in enumerate(garage.cars_list,start = 1):
            print(f'{num}. Brand: {car.brand} Model: {car.model} Year: {car.year} Current price: {car.current_price} Condition: {car.condition} Type: {car.type}')
def buy_car_function(garage,car_shop):
    if len(car_shop.available_cars) >=1:
        while True:
            print(f"Your balance: {garage.balance} Print any letter to quit. ")
            for num,car in enumerate(car_shop.available_cars,start = 1):
                print(f'{num}.Brand: {car['brand']} Model: {car['model']} Year: {car['year']} Price: {car['current_price']} Condition: {car['condition']} Type: {car['type']}')
            try:
                user_input = int(input('Enter number of car that you wanna buy:'))
            except ValueError:
                print("You chase quit to main menu.")
                break
            buy_choice = user_input - 1
            if 0 <= buy_choice < len(car_shop.available_cars):
                if garage.balance >= car_shop.available_cars[buy_choice]['current_price']:
                    print(f"YOU BOUGHT A CAR! {car_shop.available_cars[buy_choice]['model']} ")
                    garage.buy_car(Car(**car_shop.available_cars[buy_choice]))
                    del car_shop.available_cars[buy_choice]
                else:
                    print('Looks like you dont have so much money to buy this car! You should go for random events to get some!')
            else:
                print("THERE IS NO CAR WITH THIS NUMBER")
    else:
        print('WTF, you bought all cars? Winner!')
def sell_car_function(garage,car_shop):
    while True:
        print(f'Your balance: {garage.balance}')
        for num,car in enumerate(garage.cars_list,start = 1):
            print(f'{num}. Brand: {car.brand} Model: {car.model} Year: {car.year} Current price: {car.current_price} Condition: {car.condition} Type: {car.type}')
        try:
            user_input = int(input('Enter number of car that you wanna sell:'))
        except ValueError:
            print("You chase quit to main menu.")
            break
        sell_choice = user_input - 1 
        if 0 <= sell_choice < len(garage.cars_list):
                print(f"Are you sure that you want to sell {garage.cars_list[sell_choice].brand} {garage.cars_list[sell_choice].model}")
                yes_no = input("Enter YES or NO: ").lower()
                if yes_no == 'yes' and garage.cars_list[sell_choice] == garage.cars_list[0]:
                    print("YOU CANT SELL YOUR FIRST DEFAULT CAR!")
                elif yes_no == 'yes':
                    print(f'You sold your car: {garage.cars_list[sell_choice].brand} {garage.cars_list[sell_choice].model} and get {garage.cars_list[sell_choice].current_price}')
                    garage.balance += garage.cars_list[sell_choice].current_price
                    sold_car = {
                                'model' : garage.cars_list[sell_choice].model,
                                'brand' : garage.cars_list[sell_choice].brand,
                                'year' : garage.cars_list[sell_choice].year,
                                "current_price" : garage.cars_list[sell_choice].current_price,
                                'condition' : garage.cars_list[sell_choice].condition,
                                'type' : garage.cars_list[sell_choice].type
                                }
                    car_shop.available_cars.append(sold_car)
                    del garage.cars_list[sell_choice]
                    break
                elif yes_no == 'no':
                    continue
                else:
                    print("Type YES or NO!")
def tune_car_function(garage):
    while True:
        print("==========TUNE CAR MENU==========")
        print(f'Your balance: {garage.balance} (type any letter or press enter to quit to main menu)')
        for num, car in enumerate(garage.cars_list,start = 1):
            print(f'{num}.Brand: {car.brand} Model: {car.model} Year: {car.year} Current price: {car.current_price} Condition: {car.condition} Type: {car.type}')
        try:
            tune_car_choice = int(input('Enter number of car that you want to tune: '))
        except ValueError:
            print("you chase quit to main menu!")
            break
        tune_car = tune_car_choice - 1
        if 0 <= tune_car < len(garage.cars_list):
            print(f'You chase {garage.cars_list[tune_car].brand} {garage.cars_list[tune_car].model}. ')
            print(f"==========TUNE LIST==========\n1.Repair car. (this car condition: {garage.cars_list[tune_car].condition} %)")
            tune_choice = input('Enter an option:')
            match tune_choice:
                case '1':
                    repair_car_function(garage,tune_car)
        else:
            print('There is no car with this number')
def repair_car_function(garage,tune_car):
    while True:
        repair_price = (garage.cars_list[tune_car].current_price * 10) / 100
        print(f'Are you sure that you want to repair your car to 100%? Price: {repair_price} $ Your balance: {garage.balance} $ YES/NO')
        yes_no = input("Enter:").lower()
        if yes_no == 'yes':
            if garage.balance >= repair_price:
                if garage.cars_list[tune_car].condition == 100:
                    print("You car is 100 condition! Nothing to repair!")
                    break
                else:
                    print("Successfully repaired your car!")
                    garage.cars_list[tune_car].condition = 100
                    garage.balance -= repair_price
                    print('Press enter to back.')
                    enter = input()
                    break
            else:
                print(f'You dont have enough money! Go for random events to get some!')
                enter = input('Press enter to continue')
                break
        elif yes_no == 'no':
            print("Returning you to tune menu...")
            break
def sponsors_events(garage):
    random_money = random.randint(1,4500) 
    garage.balance += random_money
    print(f'YOU GOT {random_money} from SPONSORS!')
def car_racing_events(garage):
    while True:
        print('WELCOME TO GRAND RACE! Choose your car to race!')
        for num,car in enumerate(garage.cars_list,start = 1):
            print(f'{num}.Brand: {car.brand} Model: {car.model} Year: {car.year} Current price: {car.current_price} Condition: {car.condition} Type: {car.type}')
        try:
            car_choice = int(input('Enter number of car that you want to race: (or enter letters to back)'))
        except ValueError:
            print('Returning you back...')
            break
        car_race = car_choice - 1
        if 0 <= car_race < len(garage.cars_list):
            if garage.cars_list[car_race].condition <= 5:
                print(f'YOU HAVE TO REPAIR YOUR CAR! YOUR CAR CONDITION IS {garage.cars_list[car_race].condition}')
                break
            else:
                print(f'YOU CHASE {garage.cars_list[car_race].brand} {garage.cars_list[car_race].model}')
                random_prize = random.randint(5000,50000)
                print(f'Event: RACE. Amount of racers: 10 Prize: {random_prize}$ for 1 place!')
                enter = input('PRESS ENTER TO START RACE!')
                print("RACING.")
                time.sleep(1)
                print('RACING..')
                time.sleep(1)
                print("RACING...")
                time.sleep(1)
                random_place = random.randint(1,10)
                random_prize = random_prize // random_place
                garage.cars_list[car_race].condition = garage.cars_list[car_race].condition - random.randint(5,15)
                garage.balance += random_prize
                print(f'YOUR PLACE IS {random_place} CONGRATULATIONS! Your prize: {random_prize} Your car condition: {garage.cars_list[car_race].condition} %')
                break
        else:
            print("There is no car with this number!")
                
def random_event_function(garage):
    while True:
        print("==========RANDOM EVENTS==========\nAre you sure that you want to start new event? YES/NO")
        yes_no = input('Enter:').lower()
        if yes_no == 'no':
            print('Returning you to main menu...')
            break
        elif yes_no == 'yes':
            event = random.choice(random_events)
            match event:
                case 'SPONSORS':
                    sponsors_events(garage)
                case 'CAR RACING':
                    car_racing_events(garage)
def save_function(garage,car_shop):
        garage_data = []
        car_shop_data = []
        garage_balance = garage.balance
        diction = {}
        for i in garage.cars_list:
            diction = {
                'model' : i.model,
                'brand' : i.brand,
                'year' : i.year,
                'current_price' : i.current_price,
                'condition' : i.condition,
                'type' : i.type
            }
            garage_data.append(diction)
        for i in car_shop.available_cars:
            diction = {}
            for key,value in i.items():
                diction[key] = value
            car_shop_data.append(diction)
        all_data = {
            'garage_data' : garage_data,
            'balance' : garage_balance,
            'car_shop_data' : car_shop_data
        }
        with open('data.json','w',encoding='utf-8') as data_in:
            json.dump(all_data, data_in, ensure_ascii=False, indent=4)
        exit()
print("==============================\nBuyer syndicate\n==============================")
while True:
    print('==========MAIN MENU==========\n1.Check my garage\n2.Buy new car\n3.Sell car\n4.Tune car\n5.Random event\n6.Leave')
    choice = input("Enter option:")
    match choice:
        case '1' | 'check':
            check_my_garage(garage)
        case '2' | 'buy':
            buy_car_function(garage,car_shop)
        case '3' | 'sell':
            sell_car_function(garage,car_shop)
        case '4' | 'tune':
            tune_car_function(garage)
        case '5' | 'event':
            random_event_function(garage)
        case '6' | 'leave':
            yes_no = input("Are you sure you want to quit? :(").lower()
            match yes_no:
                case 'no':
                    print("Glad to see you want to play more!")
                    continue
                case 'yes':
                    save_function(garage,car_shop)