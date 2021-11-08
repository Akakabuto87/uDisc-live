from statistics import mean

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
                    players[i].append(sum(players[i][2:]))
                    break
        except:
            print("Error: {:^30} did not play this event. Did you spell their name right?".format(players[i][0]))
            player_not_here.append(i)
        
    for index in reversed(player_not_here):
        del players[index]
    players.sort(key=lambda x: x[1])
    print("\n --------------------------- {:^35} ---------------------------".format(filename))
    print(" --------------------------- {:^35} ---------------------------".format("Raw stats from uDisc live"))
    print("\n{:>20}   {:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format("0) Player name:", "1) Place:", "2) Score:","3) T->G:","4) C1x:","5) C2:","6) OB:"))
    for player in players:
        print("{:>20.20}   {:^12}{:^12}{:^12}{:^12}{:^12}{:^12}".format(player[0], player[1], player[2], player[3], player[4], player[5], player[6]))

    SG_total = [[] for i in range(len(players[0]))]

    for player in players:
        for i in range(len(player)):
            SG_total[i].append(player[i])
            
    # score_avr, t_to_g_avr, c1x_avr, c2_avr, ob_avr = mean(SG_total[2]), mean(SG_total[3]), mean(SG_total[4]), mean(SG_total[5]), mean(SG_total[6])
    avr = [None, None, mean(SG_total[2]), mean(SG_total[3]), mean(SG_total[4]), mean(SG_total[5]), mean(SG_total[6]), mean(SG_total[7])]
    players_SG = []
    for i in range(len(players)):
        players_SG.append([players[i][0]])
        for j in range(2,len(players[0])):
            players_SG[i].append(players[i][j]-avr[j])
        if abs(players_SG[i][6]) > 0.5:
            print("Error:   {}s SG stats does not fit his score ...".format(players_SG[i][0]))
    

    print("\n --------------------------- {:^35} ---------------------------".format("SG compared to the limited field"))
    print("\n{:>20}   {:^12}{:^12}{:^12}{:^12}{:^12}".format("0) Player name:", "1) Score:","2) T->G:","3) C1x:","4) C2:","5) OB:"))
    for player in players_SG:
        print("{:>20.20}   {:^12}{:^12}{:^12}{:^12}{:^12}"
        .format(player[0], round(player[1],2), round(player[2],2), round(player[3],2), round(player[4],2), round(player[5],2)))
    
    return players_SG

SG_tournament(players, "udisc_las_vegas.txt")
