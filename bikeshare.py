#important necessary modules and functions
import pandas as pd
import numpy as np
import time
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#defintion of global variable for month and days
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']

#also a create a global and local variable for easter egg
global easter_egg
easter_egg = ''


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    #ask if the user want to have a little bit fun with an easter egg during that program --> the code of the easter will follow at the end of this function get_filters()
    global easter_egg
    easter_egg = input("Should we go trough this program with some little easter_eggs 'yes' or 'no'?: ").lower()
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        #run the loop until the user has entered one of the 3 predefined cities
        city = input('\nWould you like to choose Chicago, New York City or Washington? Please choose one of these 3 cities by name: ').lower()
        if city in CITY_DATA.keys():
            print('\nAllright we use the Data of {}.'.format(city.title())) # Answer to the user
            break
        else:
            print('\nUps, that wasn\'t one of the three suggested cities. So please type in the name of the citiy.')

    #get user input for month (all, january, february, ... , june)
    while True:
    #run the loop until the user has entered one of the 6 predefined months
        month = input('Please give me a name of one of the first 6 months (e.g. January) or write "all" for no month filter: ').lower()
        if month in months:
            month_nr = months.index(month)+1
            print('\nAllright we use the {}th month of the year, which is called {}.'.format(month_nr, month.title())) # Answer to the user
            break
        if month == 'all':
            print('\nAllright no additional filter were given so you will see the data over all months.')
            break
        else:
             print('\nUps, that wasn\'t one of the inputs I need. So please type in the name of a month or the word "all" for no filter.')

    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        #run the loop until the user has entered one of the 7 predefined days
        day = input('At least please let me know, which day of the week you would like to choose or write "all" for no additional filter: ').lower()
        if day in days:
            print('\nAllright we use the {} of the week.'.format(day.title())) # Answer to the user
            break
        if day  == 'all':
            print('\nAllright no additional filter were given so you will see the data over all days of the week.')
            break
        else:
             print('\nUps, that wasn\'t one of the inputs I need. So please type in the name of the day or the word "all" for no filter.')

    print('-'*40)
    #display a short sum up of the user inputs
    print('\nOk let\'s sum up before we go further on:\n1) Your choosen data is: {}\n2) Your filter for month is: {}\n3) Your filter for day is: {}\n'.format(city.title(), month.title(), day.title()))



    #little easter_egg in get filters function
    """
    Here is a little Easter_Egg hidden in the Function of get_filters.
    It asks the user, if he wants to have a little bit fun with an easter egg during that program or not.
    I hope you will enjoy it :-)

    Returns:
        (str) - global varibale with a yes or no statement to activate or deactive the easter eggs in all other functions
    """

    if easter_egg == 'yes': #there is no else condition because of not grinding on someone else nerves
        print('-'*40)
        print("Ok ok got it. But let me tell you one last thing from my side.\nI really don't know how much does this hole calculation will take to run through with your choosen settings.\nMaybe a few seconds, minutes or even hours?!?\n\nI hope not the last one, because nobody will feed my cat at home.\nAnd later, when I will come home, my cat ,Sir Luis the 3rd, will show me whats he thinks about long calculations here at our office far away from home.\nHe can get really mad when the bowl stays empty for such a long time :-( \n\nSo crossed fingers for us, it hopefully will get fast!")
        while True:
            #run the loop until the user write yes
            egg = input("\nIf you stay here and we should go on write 'yes'.\nIf you would rather get a new cup of coffee or even feed also your pet at home (I hope so), then write 'no': ").lower()
            if egg == 'yes':
                print('\nWe start the calculation in')
                print('3')
                print('2')
                print('1')
                break
            elif egg == 'no':
                print('-'*40)
                print("\nWe both know that you've already got a cup of coffee next to your PC before you start this little program here, but I'm glad to see that you are thinking about your pet.\nWe see us in a few minutes again.\nGreetings to the pet(s)!\n")
            else:
                print("\nThere are only two possible answers: 'Yes' your pet is already fed or 'No' You're on your way to your pet.\n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load the data of the input given city and put it into a datamframe
    df = pd.read_csv(CITY_DATA[city])

    #convert the column of Start Time into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #1) now extract the month of this datetime column
    df['month'] = df['Start Time'].dt.month

    #2) now extract the day_of_week (=dow) of this datetime column
    df['dow'] = df['Start Time'].dt.weekday

    #3) last extract the hour of this datetime column
    df['hour'] = df['Start Time'].dt.hour

    #additional filter options here, if the user input != all
    #1) filter by month if applicable.
    if month != 'all':
        #tranfer the name of the month into an int
        month_nr = months.index(month)+1

        #after filtering create new dataframe
        df = df[df['month'] == month_nr]

    #2) filter by day of week (=dow) if applicable.
    if day != 'all':
        #transfer the dow into an int
        day_nr = days.index(day)

        #after filtering create new dataframe
        df = df[df['dow'] == day_nr]


    return df


def data_head(df):
    """
    Displays the first 5 rows of the choosen data from the cities as a preview and ask you, if you want to see antoher +=5 rows or go further on.

    Args:
        df - Pandas DataFrame containing all data of the choosen city and it's filters
    """

    #new additional function to show the user the first 5 rows and ask them, if the user want's to go on 'yes' or 'no'
    n=5
    show_head = input('\nWould you like to get a short overview like the first 5 rows of your choosen data first? Yes or no? :').lower()
    #loop and ad 5 more rows until the user input is no
    while True:
        if show_head == 'yes':
            print(df.head(n))
            show_head = input('\nWould you like 5 more rows? Yes or no? :').lower()
            n+=5
        elif show_head == 'no':
            break
        else:
            #continue of my little easter egg
            global easter_egg
            if easter_egg == 'yes':
                print("\nDon't worry. I also can't focus at all right now, because now would be just the time to brush my cat at home. Instead we calculate here together and you can't imagine how vindictive my cat can be...")
            show_head = input("\nPlease try again with only 'yes' or 'no', if you would like to see more rows or further on?: ").lower()


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Arg:
        df - andas DataFrame containing all data of the choosen city and it's filters
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #find the most common month
    most_common_month = df['month'].mode()[0]

    #find the most common day of week
    most_common_day = df['dow'].mode()[0]

    #find the most common start hour
    most_common_hour = df['hour'].mode()[0]

    #display all 3 attributes
    print("The most common month is: {}".format(months[most_common_month-1]).title()) #transfer back from number of month to the name of the month. Opposite of above row 48.
    print("The most common day of the week is: {}".format(most_common_day))
    print("The most common hour of a day is: {} o'clock".format(most_common_hour))

    #display how long does it took for calculation
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Arg:
        df - andas DataFrame containing all data of the choosen city and it's filters
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #find the most commonly used start station
    most_commonly_start_station = df['Start Station'].mode()[0]

    #find the most commonly used end station
    most_commonly_end_station = df['End Station'].mode()[0]

    #find the most frequent combination of start station and end station trip
    df['Start_to_End_Trip'] = df['Start Station'] + ' up to ' + df['End Station'] #combination of both columns with ' up to ' in the middle
    most_commonly_start_to_end_trip = df['Start_to_End_Trip'].mode()[0]

    #display all 3 attributes
    print("The most commonly start station is: {}".format(most_commonly_start_station))
    print("The most commonly end station is: {}".format(most_commonly_end_station))
    print("The most commonly trip from a start to an end station is: {}".format(most_commonly_start_to_end_trip))

    #display how long does it took for calculation
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Arg:
        df - Pandas DataFrame containing all data of the choosen city and it's filters
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #calculate the total travel time
    travel_time_total = df['Trip Duration'].sum()


    #calculate the mean travel time
    travel_time_mean = df['Trip Duration'].mean()

    #display all 2 attributes and change it from seconds into usual time. Then display again all 2 attributes
    print("The total travel time in seconds is: {}s".format(travel_time_total))
    print("The mean travel time in seconds is: {}s".format(travel_time_mean))
    print("\nOr we can convert that both answers from seconds into time [h:m:s]\n")
    print("The total travel time is: {}".format(datetime.timedelta(seconds = int(travel_time_total))))
    print("The mean travel time is: {}".format(datetime.timedelta(seconds = int(travel_time_mean))))

    #display how long does it took for calculation
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Displays statistics on bikeshare users.

    Arg:
        df - andas DataFrame containing all data of the choosen city and it's filters
        (str) city - name of the city to analyze
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #counts of user types
    user_type = df['User Type'].value_counts()

    #counts of gender
    gender = 0
    if city.lower() != 'washington': #washington doesn't got any informartion about gender
        gender = df['Gender'].value_counts()
    else:
        print('Sry, there are no data of genders in Washington')

    #display earliest, most recent, and most common year of birth
    if city != 'washington':  #washington doesn't got any informartion about birth year
        year_of_birth_earliest = int(df['Birth Year'].min())
        year_of_birth_most_recent = int(df['Birth Year'].max())
        year_of_birth_most_common = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is: {}".format(year_of_birth_earliest, year_of_birth_most_recent, year_of_birth_most_common))
    else:
        print('Sry, there are no data of birth year in Washington')

    #display all attributes (the display statements of birth year are in the if condition row298. Otherwise the code would crash in case of washington with no birth data)
    print("\nThe counts of the user types are:\n{}".format(user_type))
    print("\nThe counts of the genders are:\n{}".format(gender))

    #display how long does it took for calculation
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    #continue easter_egg here
    if easter_egg == 'yes': #there is no else condition because of not grinding on someone else nerves
        print('\nDamn that was fast! Great Job!!!\nMany thanks for you help to get faster as I thought! Finally I can breathe easy again.\n\nBut could you do me a favour and bring the results to chief Wagner for his presentation please?\nAs you know I got urgent things to do. Cat things you know?!?!')


def main():
    while True:
        #run this loop and ask the user if he would like to restart again at the end. There are also two additional cases when the easter_egg was activate from user.
        city, month, day = get_filters()
        df = load_data(city, month, day)
        data_head(df) #new function for the first 5 rows of the chosen data (head)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() == 'yes' and easter_egg == 'yes': #combined it with my easter_egg
            #continue my little easter_egg and don't let restart the program, because of no time if easter_egg == 'yes'
            print('-'*40)
            print("\nÄhhhhh nope, no, niente, nada! It's over! Now!\nDo you really think I would restart the hole program again and get in trouble with Sir Luis the 3rd?\nHave you looked at your watch yet?\nYou were listening to me before, weren't you?\nGive me back my program and go please, because you don't live under the same roof with him, do you?\nHe will take revenge... believe me.\nBut not during the daytime when you'd expect it.\n\nNo, no, nobody won't see it coming...\n\n(And so the cat nerd grabbed all his stuff and began to run out of the office right the direction to his house. Some witnesses rumored, that he was even faster than Forest Gump back then...)\n\n\nTHE\n END\n\n(Short note for the mentor / reviewer:\nThanks for having a little bit fun with me. I hope you enjoyed it just a little bit.\nFor myself it was also fun to bring in the little codes during the hole projekt.\nAnd I can reassure them, in real life I'm not a cat nerd and that's just a fictional cat name. But I've had to go through such stories with former colleagues haha.\nGreetings go out at this point to the two :-))\n\nHave a nice day!\n\nGreetings Stefan")
            break

        elif restart.lower() == 'no' and easter_egg == 'yes':
            #continue my little easter_egg and don't let restart the program, because of no time if easter_egg == 'yes'
            print('-'*40)
            print("\nAhhh thanks that's really nice from you. You are the only colleague here in our office, who understands the important to get home to the cats as fast as we can.\nGive me a second, I will just record a short speak message and send it home to my house over Alexa teade, so that Sir Luis the 3rd know's that I'm already on my way to him.\nYou have something good with me, so thanks a lot and bye.\n\n(And so the cat nerd grabbed all his stuff and began to run out of the office right the direction to his house. Some witnesses rumored, that he was even faster than Forest Gump back then...)\n\n\nTHE\n END\n\n(Short note for the mentor / reviewer:\nThanks for having a little bit fun with me. I hope you enjoyed it just a little bit.\nFor myself it was also fun to bring in the little codes during the hole projekt.\nAnd I can reassure them, in real life I'm not a cat nerd and that's just a fictional cat name. But I've had to go through such stories with former colleagues haha.\nGreetings go out at this point to the two :-))\n\nHave a nice day!\n\nGreetings Stefan")
            break

        elif restart.lower() != 'yes'  and easter_egg == 'no':
            #orignal code when no easter_egg ist activ
            break


if __name__ == "__main__":
	main()
