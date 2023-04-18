def sort_leaderboard(players):
    for i in range(len(players)):
        highest_player = players[i]
        highest_index = i
        for j in range(i + 1, len(players)):
            if players[j][1] > players[j - 1][1]:
                highest_player = players[j]
                highest_index = j
        players[highest_index] = players[i]
        players[i] = highest_player


first_player_info = input().split(" ")
first_player = [first_player_info[0], sum(list(map(int, first_player_info[1:])))]

second_player_info = input().split(" ")
second_player = [second_player_info[0], sum(list(map(int, second_player_info[1:])))]

third_player_info = input().split(" ")
third_player = [third_player_info[0], sum(list(map(int, third_player_info[1:])))]

leaderboard = [first_player, second_player, third_player]
sort_leaderboard(leaderboard)
print(leaderboard)
