from TravelAgent import TravelAgent
def main():
    # print('Main function is executing')
    travel_agent = TravelAgent('Go Bro')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','04/01/2000')
    print('aircraft',trip_info1[0])
    print('price',trip_info1[1])

if __name__ == '__main__':
    main()