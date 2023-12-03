# run through each game
# check if game is possible (FOLD):
# get ID, run through subgames (split by ;)
# for each subgame, 
# sum ID to running tally of possible or store ID to sum over later

file = open("day_2_input")

# part 1
sum_valid_game_ids=0
sum_valid_game_ids_list=[]

# part 2
sum_power_set_games=0

for i_game,game_info in enumerate(file.readlines(),start=1):
    
    is_valid_game=(game_info!="")

    subgames=game_info.strip().split(":")[1]

    # part 2
    max_red=max_green=max_blue=0 

    for subgame in subgames.split(";"):
        n_red=n_green=n_blue=0
        for color in subgame.split(","):
            
            if color.find("red")!=-1:
                n_red=int(color.strip(" red"))
            elif color.find("green")!=-1:
                n_green = int(color.strip(" green"))
            elif color.find("blue")!=-1:
                n_blue = int(color.strip(" blue"))

        # part 1
        if (n_red > 12) or (n_green > 13) or (n_blue > 14):
            is_valid_game=False

        # part 2
        max_red=max(max_red,n_red)
        max_green=max(max_green,n_green)
        max_blue=max(max_blue,n_blue)

    # part 1
    if is_valid_game:
        sum_valid_game_ids+=i_game
        sum_valid_game_ids_list.append(i_game)

    # part 2
    sum_power_set_games+=max_red*max_green*max_blue 

# part 1
print(sum_valid_game_ids_list)
print(sum_valid_game_ids)

# part 2
print(sum_power_set_games)

