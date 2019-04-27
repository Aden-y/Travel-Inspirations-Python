"""

"""

__author__ = ""
__date__ = ""


from destinations import Destinations
def match_children(des,pref):
    if (des==True and pref=="yes") or (des==False and pref=="no") or(des==True and pref=="no"):
        return True
    else:
        return  False
def cost_int(string):
    if string == "$":
        return 1
    elif string == "$$":
        return 2
    else:
        return 3
def crimeRate(crime):
    if crime == "low":
        return 1
    elif crime == "avarage":
        return 2
    else:
        return 3
def main():

    # Task 1: Ask questions here
    print("Welcome to Travel Inspiration!")
    name = input("What is your name?")
    print ("Hi, ", name)

    # paste from here
    invalid=True
    continent=""
    money=""
    crime=""
    chidren=""
    season=""
    climate=""
    #Likes
    sports=nature=dining=historical=adventure=beach=wildlife=-6

    while continent=="":
        travel_to = input("Which continent would you like to travel to?"
                          "\n1)  Asia"
                          "\n2)  Africa"
                          "\n3)  North America"
                          "\n4)  South America"
                          "\n5)  Europe"
                          "\n6)  Oceania"
                          "\n7)  Antarctica\n")
        travel_to=int(travel_to)

        if travel_to == 1:
            continent = "asia"
        elif travel_to == 2:
            continent == "africa"
        elif travel_to == 3:
            continent == "north america"
        elif travel_to == 4:
            continent = "south america"
        elif travel_to == 5:
            continent = "europe"
        elif travel_to == 6:
            continent = "oceania"
        elif travel_to == 7:
            continent = "antarctica"
        else:
            print ("Please reply with a valid option")
            continent = ""


    while money=="":
        money_to_you = input("What is money to you?"
                             "\n$$$)  No object"
                             "\n$$)  Spendable, so long as I get value from doing so"
                             "\n$)  Extremely important; I want to spend as little as possible\n")

        if money_to_you == "$$$":
            money = "$$$"
        elif money_to_you == "$$":
            money = "$$"
        elif money_to_you == "$":
            money = "$"
        else:
            print ("Please reply with a valid option")
            money = ""




    while crime=="":
        crime_acceptable = input("How much crime is acceptable when you travel?"
                                 "\n1)  Low"
                                 "\n2)  Avarage"
                                 "\n3)  High\n")
        crime_acceptable=int(crime_acceptable)
        if crime_acceptable == 1:
            crime = "low"
        elif crime_acceptable == 2:
            crime == "avarage"
        elif crime_acceptable == 3:
            crime = "high"
        else:
            print ("Please reply with a valid option")
            crime = ""

    while chidren=="":
        traveling_with_children = input("Will you be travelling with children?"
                                        "\n1)  Yes"
                                        "\n2)  No\n")
        traveling_with_children=int(traveling_with_children)
        if traveling_with_children == 1:
            chidren = "yes"
        elif traveling_with_children == 2:
            chidren = "no"
        else:
            print ("Please reply with a valid option")
            chidren = ""


    while season=="":
        season_of_travel = input("Which season do you plan to travel in?"
                                 "\n1) Spring"
                                 "\n2) Summer"
                                 "\n3) Autumn"
                                 "\n4) Winter\n")
        season_of_travel=int(season_of_travel)

        if season_of_travel == 1:
            season = "spring"
        elif season_of_travel == 2:
            season = "summer"
        elif season_of_travel == 3:
            season = "autumn"
        elif season_of_travel == 4:
            season = "winter"
        else:
            print ("Please reply with a valid option")
            season = ""
    while climate=="":
        prefered_climate = input("What climate do you prefer?"
                                 "\n1) Cold"
                                 "\n2) Cool"
                                 "\n3) Moderate"
                                 "\n4) Warm"
                                 "\n5) Hot\n")
        prefered_climate=int(prefered_climate)
        if prefered_climate == 1:
            climate = "cold"
        elif prefered_climate == 2:
            climate = "cool"
        elif prefered_climate == 3:
            climate = "moderate"
        elif prefered_climate == 4:
            climate = "warm"
        elif prefered_climate == 5:
            climate = "hot"
        else:
            print ("Please reply with a valid option")
            climate = ""


    print (
        "Now we would like to ask you some questions about your interests, on a scale of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, and 0 indicates indifference.")

    while sports==-6:
        like_sports = input("How much do you like wildlife? (-5 to 5)\n")
        like_sports = int(like_sports)
        if like_sports > -6 and like_sports < 6:
            sports = like_sports
        else:
            print ("Please reply with a valid response(-5 to 5)")
            sports = -6

    while wildlife==-6:
        like_wild_life = input("How much do you like nature? (-5 to 5)\n")
        like_wild_life = int(like_wild_life)
        if like_wild_life > -6 and like_wild_life < 6:
            wildlife = like_wild_life
        else:
            print ("Please reply with a valid response(-5 to 5)")
            wildlife = -6

    while nature==-6:
        like_nature = input("How much do you like nature? (-5 to 5)\n")
        like_nature = int(like_nature)
        if like_nature > -6 and like_nature < 6:
            nature = like_nature
        else:
            print ("Please reply with a valid response(-5 to 5)")
            nature = -6

    while historical==-6:
        like_historical_sites = input("How much do you like historical sites? (-5 to 5)\n");
        like_historical_sites = int(like_historical_sites)
        if like_historical_sites > -6 and like_historical_sites < 6:
            historical = like_historical_sites
        else:
            print ("Please reply with a valid response(-5 to 5)")
            historical = -6


    while dining==-6:
        like_fine_dining = input("How much do you like fine dining? (-5 to 5)\n")
        like_fine_dining = int(like_fine_dining)
        if like_fine_dining > -6 and like_fine_dining < 6:
            dining = like_fine_dining
        else:
            print ("Please reply with a valid response(-5 to 5)")
            dining = -6



    while adventure==-6:
        like_adventure = input("How much do you like adventure activities? (-5 to 5)\n")
        like_adventure = int(like_adventure)
        if like_adventure > - 6 and like_adventure < 6:
            adventure = like_adventure
        else:
            print ("Please reply with a valid response(-5 to 5)")
            adventure = -6



    while beach==-6:
        like_beach = input("How much do you like the beach? (-5 to 5)\n")
        like_beach = int(like_beach)
        if like_beach > - 6 and like_beach < 6:
            beach = like_beach
        else:
            print ("Please reply with a valid response(-5 to 5)")
            beach = -6

    print ("Thank you for answering all our questions. Your next travel destination is:")

    found=False;
    season_score =0.0
    dest_name=""
    score=""


    print ("Continent" ,continent)
    print ("Money" , money)
    print ("Crime" , crime)
    print ("Continent" , continent)
    print ("Children" , chidren)
    print ("Season" , season)
    print ("Climate" , climate)
    print ("Wildlife", wildlife)
    print ("Nature", nature)
    print ("Hisorical", historical)
    print ("Dining", dining)
    print ("Adventure", adventure)
    print ("Beach", beach)
    for destination in Destinations().get_all():
        # Task 2+: Add comparison logic here

        if destination.get_continent()==continent:#and match_children(destination.is_kid_friendly(),"no" and cost_int(destination.get_cost())<= cost_int("$$$") and  crimeRate(destination.get_crime())<= crimeRate("high")):

            if match_children(destination.is_kid_friendly(),chidren):
                if cost_int(destination.get_cost()) <= cost_int(money):
                    if crimeRate(destination.get_crime) <= crimeRate(crime):
                        if destination.get_climate() == climate:

                            if destination.get_season_factor(season) >= season_score:
                                season_score=destination.get_season_factor(season)

                                interest_score=sports* destination.get_interest_score("sports") + wildlife*destination.get_interest_score("wildlife") + nature*destination.get_interest_score("nature") + historical*destination.get_interest_score("historical") + dining*destination.get_interest_score("cuisine") + adventure*destination.get_interest_score("adventure") + beach*destination.get_interest_score("beach")
                                temp_score=season_score*interest_score
                                if score=="":
                                    score=int(temp_score)
                                if temp_score >= score:
                                    found=True
                                    dest_name=destination.get_name()


    if found==False:
        print("None")
    else:
        print (dest_name)
        # Task 1: The following code is example code, and
        #         should be deleted once you implement task 2.


    # Task 2+: Output final answer here


if __name__ == "__main__":
    main()
