"""This program uses the request library to request data from the website OpenWeatherMap using an API. This program
allows the user to specify whether they would like to search weather conditions by zip code or city and state. It then
also asks them how they would like their temperature results formatted (Celsius Fahrenheit, or Kelvin) and finally
presents the user with a pleasingly formatted output. The function temp_units() carries out the necessary temperature
selection work, as well as keeping track of what was selected so that the final output will have the appropriate
temperature unit presented alongside the numerical temperature read. The city_finder() function collects the user's
city-name input for later use, and the state_finder() function assesses whether a valid state code has been input and
then saves the input for later use; both of these functions outputs are then used in the weather lookup part of the
program. The zipcode_finder() function uses the zip code input by the user to acquire the latitude and longitude of the
corresponding region and then passes that information to the final portion of the program. Finally, the main() function
performs an API lookup to find the weather for the indicated region either by city and state or by latitude and
longitude. The pretty_print_custom() function presents the received weather information in a pleasing format."""

import requests

# Here is the variable where you input your private api code. Insert it over the comment section to the right of the
# variable below for the program to function (be sure to input your code as a string).
appid = # Input the string version of your personal api code here.


def temp_units():
    # Prompts user to select format for temperature readout.
    while True:  # Used to keep program in loop until a proper input is received.
        degrees = input('How would you like your temperature presented: Kelvin, Fahrenheit, or Celsius?\n'
                        '(K, F, or C) >>>  ').upper()
        if degrees == 'K':
            temp = 'K'  # The temp variable will later be presented alongside the numerical temperature output.
            units = 'standard'
            break
        elif degrees == 'C':
            temp = 'C'
            units = 'metric'
            break
        elif degrees == 'F':
            temp = 'F'
            units = 'imperial'
            break
        else:
            print("I'm sorry your temperature selection was invalid. Please try again.")
    return units, temp


def city_finder():
    # Receives manual input of city-name for later use by main function in the geocode API lookup
    while True:
        city_name = input("Please input the name of the city you would like the weather for:\n"
                          ">>>  ")
        if city_name == '':  # Catches blank inputs. Further error catching of invalid city-names occurs later.
            print("I'm sorry, you entered a blank value for the city name. Please try again.")
            continue
        else:
            break
    return city_name


def pretty_print_custom(data, temp):
    # Receives the JSON dictionary response from the geocode API lookup call to OpenWeatherMap and presents it
    # in a pleasing format. Also takes the cloud coverage percent and sets a user readable assessment of the cloud
    # coverage percent. The 'description' portion of the response data covers the standard 'Okta' nomenclature.
    cloud_cover = data.get('clouds', 'Unavailable').get('all', 'Unavailable')
    if cloud_cover == 100:
        cloud_cover = 'Total'
    elif cloud_cover >= 56.25:
        cloud_cover = 'Substantial'
    elif cloud_cover >= 31.25:
        cloud_cover = 'Moderate'
    elif cloud_cover > 0:
        cloud_cover = 'Minimal'
    elif cloud_cover == 0:
        cloud_cover = 'None'
    else:
        cloud_cover = 'Unavailable'
    print(f"The present weather conditions in {data.get('name', 'Name Unavailable')} are:\n"
          f"Current Temp: {data.get('main', 'Unavailable').get('temp', 'Unavailable')} {temp}\n"
          f"High Temp: {data.get('main', 'Unavailable').get('temp_max')} {temp}\n"
          f"Low Temp: {data.get('main', 'Unavailable').get('temp_min')} {temp}\n"
          f"Pressure: {data.get('main', 'Unavailable').get('pressure')} hPa\n"
          f"Humidity: {data.get('main', 'Unavailable').get('humidity')}%\n"
          f"Cloud Coverage: {cloud_cover} ({data.get('clouds', 'Unavailable').get('all', 'Unavailable')}%)\n"
          f"Description: {data.get('weather', 'Unavailable')[0].get('description', 'Unavailable').title()}.\n")


def state_finder():
    # Verifies that the user input state code is a valid one by comparing it to the states dictionary.
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
              'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH,', 'NJ', 'NM', 'NY', 'NC',
              'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    while True:  # Keeps a loop in place until a valid state code has been input.
        state_code = input('Please input the state the city is in ("Only two letter codes: i.e. CA)\n'
                           '>>>  ').upper()
        if state_code not in states:
            print("I'm sorry, the state code you entered is not recognized. Please try again.")
            continue
        else:
            break
    return state_code


def zipcode_finder():
    # This function uses a user provided zip code to look up the corresponding latitude and longitude for later use in
    # the OpenWeatherMap weather lookup API

    global appid
    appid = appid
    api_error_message = "I'm sorry, while you were able to connect to OpenWeatherMap successfully,\n" \
                        "there's been a problem collecting your data."
    connection_error_message = "I'm sorry, you were unable to connect with OpenWeatherMap.\n" \
                               "They may be experiencing technical problems, or your internet\n" \
                               "connection or settings may be the issue. Please check\n" \
                               "your connection and settings and try again later.\n" \
                               "This program will now close."
    while True:
        zipcode = input("Please input the zip code:\n"
                        ">>>  ")
        try:  # API uses the zip code provided to find the latitude and longitude of that city.
            weather = requests.get(
                f"https://api.openweathermap.org/geo/1.0/zip?zip={zipcode},US&limit=1"
                f"&appid={appid}")
            weather.raise_for_status()
        except requests.ConnectionError:  # Error handling to check for proper connection to OpenWeatherMap.
            print(connection_error_message)
            exit()
        except (requests.HTTPError, requests.RequestException):
            if weather.status_code == 400 or 404:  # Error handling to catch improper zip code entries.
                print(f"I'm sorry, the zip code you entered seems to be invalid.\n"
                      f"(Error code: {weather.status_code})")
                # Allows for user to back out of program if they don't have a zip code they want to enter
                # after first failed attempt.
                while True:
                    answer = input("Would you like to try inputting a zip code again? ('Y' or 'N')\n"
                                   ">>>  ").lower()
                    if answer == 'n':
                        print("You have chosen not to try again. The program will now close.")
                        exit()
                    elif answer == 'y':
                        break
                    else:
                        print("I'm sorry, your answer wasn't one of the available options.")
                        continue
                continue
            else:
                print(f"{api_error_message}:\n"
                      f"{weather.text}\n"
                      f"The program will now close.")
                exit()
        if weather.status_code == 200:  # Checks to see if API lookup call to OpenWeatherMap was successful.
            data = weather.json()
            lat = data['lat']
            lon = data['lon']
            break
        else:
            print(f"{api_error_message}"
                  f"Error Code: {weather.status_code}\n"
                  f"The program will now close.")
            exit()
    return lat, lon


def main():
    # Standard main() function. Brings together the different functions of the program to ultimately perform a weather
    # lookup from the website OpenWeatherMap, and presents the output in a pleasing format.

    appid = "05d75964f8a72a182587b1ef51ca4b84"
    error_message = "I'm sorry, your input was not one of the options given"
    api_error_message = "I'm sorry, there's been an error"
    connection_error_message = "I'm sorry, you were unable to connect with OpenWeatherMap.\n" \
                               "They may be experiencing technical problems, or your internet\n" \
                               "connection or settings may be the issue. Please check\n" \
                               "your connection and settings and try again later.\n" \
                               "This program will now close"
    print("Hello and welcome to my weather program!\n"
          "(Weather data courtesy of OpenWeatherMap)")
    answer = ''
    # These questions allow for natural conversational progression through multiple attempts.
    question1 = 'Would you like to know the weather in a U.S. city?'
    question2 = 'Would you like to know the weather in another U.S. city?'
    count = 0
    data_dict = {}
    while answer != 'n':  # Overarching loop that allows program to be run multiple times, as needed.
        if count == 0:
            query = question1
        else:
            query = question2
        answer = input(f"{query}\n"
                       "('Y' or 'N')>>> ")
        if answer.lower() == 'n':
            print("This program will now close. Have a nice day!")
            exit()
        if answer.lower() == 'y':
            while True:
                location_method = input("Would you like to look up the weather by city or zip code?\n"
                                        "('C' or 'Z') >>>  ").upper()
                #  The functions below provide their outputs to the data_dict dictionary for later use in the final
                #  weather retrieval API attempt.
                if location_method == 'C':  # For use if the lookup method was to be by city.
                    data_dict['city_name'] = city_finder()
                    data_dict['state_code'] = state_finder()
                    data_dict['units'], data_dict['temp'] = temp_units()
                    lookup_method = 1
                elif location_method == 'Z':  # For use if the lookup method was to be by zip code.
                    data_dict['lat'], data_dict['lon'] = zipcode_finder()
                    data_dict['units'], data_dict['temp'] = temp_units()
                    lookup_method = 2
                else:
                    print(f"{error_message}")
                    print("(Please select either 'C' or 'Z')")
                    continue
                if lookup_method == 1:  # API lookup by city and state
                    try:
                        api = requests.get(
                            f"https://api.openweathermap.org/data/2.5/weather?q={data_dict['city_name']},"
                            f"{data_dict['state_code']}, US&units={data_dict['units']}&limit="
                            f"1&appid={appid}")
                    except requests.ConnectionError:  # Catches connection errors to OpenWeatherMap.
                        print(connection_error_message)
                        exit()
                    except (requests.HTTPError, requests.RequestException):
                        if 'city not found' in weather.text:  # Error handling to catch improper city-names.
                            print("I'm sorry, your connection to the weather program was successful but the city\n"
                                  "you've entered was not found. Please try again.")
                            continue
                        else:  # General error handling.
                            print(f"{api_error_message}:\n"
                                  f"{weather.text}\n"
                                  f"The program will now close.")
                            exit()
                else:  # API lookup by zip code
                    api = requests.get(
                        f"https://api.openweathermap.org/data/2.5/weather?lat={data_dict['lat']}&lon="
                        f"{data_dict['lon']}&units={data_dict['units']}&limit="
                        f"1&appid={appid}")
                weather = api  # Weather lookup attempt.
                break
            if weather.status_code == 200:  # Checks if weather data lookup was successful.
                data = weather.json()
                print("Your connection to OpenWeatherMap was successful!\n"
                      "The weather for your requested region was found:")
                pretty_print_custom(data, data_dict['temp'])
            else:
                print("I'm sorry, although you were able to connect to OpenWeatherMap\n"
                      "the attempt to retrieve your requested data\n"
                      "was not successful in an unanticipated way.\n"
                      "Please try again.")
            count += 1  # Used for the natural conversational progression of prompts through multiple attempts.
        else:
            print(f"{error_message}\n"
                  "(Please answer 'Y' or 'N')")
            continue


if __name__ == '__main__':  # Standard call to main() function.
    main()
