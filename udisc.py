players = []
players.append(["Ezra Aderhold"])
players.append(["James Conrad"])
players.append(["Paul McBeth"])
players.append(["Ricky Wysocki"])
players.append(["Eagle McMahon"])
players.append(["Calvin Heimburg"])
players.append(["Simon Lizotte"])
players.append(["Garrett Gurthie"])


players.append(["fakeplayer"])

def SG_tournament(players, filename):
    tournament = open(filename, "r")
    lines=tournament.readlines()
    player_not_here = []
    
    for i in range(len(players)):
        try:
            player_index=lines.index(players[i][0] + "\n")
            player_index_min = player_index
            while True:
                player_index += 1
                if len(lines[player_index]) >6 and lines[player_index] != "Birdie\n":
                    player_index_max = player_index-2
                    
                    players[i].append(int(lines[player_index_min-1].strip().replace("T", "")))
                    players[i].append(int(lines[player_index_min+1].strip()))
                    players[i].append(float(lines[player_index_max-4].strip()))
                    players[i].append(float(lines[player_index_max-2].strip()))
                    players[i].append(float(lines[player_index_max-1].strip()))
                    players[i].append(-int(lines[player_index_max].strip()))
                    players[i].append(sum(players[i][1:]))
                    break
        except:
            print("Error: {:^30} did not play this event".format(players[i][0]))
            player_not_here.append(i)
        
    for index in reversed(player_not_here):
        del players[index]
    players.sort(key=lambda x: x[1])
    print("\n --------------------------- {:^30} ---------------------------".format(filename))
    print(" --------------------------- {:^30} ---------------------------".format("Raw stats from uDisc live"))
    print("\n{:>20}   {:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format("0) Player name:", "1) Place:", "2) Score:","3) T->G:","4) C1x:","5) C2:","6) OB:"))
    for player in players:
        print("{:>20.20}   {:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format(player[0], player[1], player[2], player[3], player[4], player[5], player[5]))

    SG_avr = []
    
    # for i in range(1,len(players[0]))
        #calculate average
    # print(players[:][1])
    # return players_SG

SG_tournament(players, "udisc_las_vegas.txt")
