# exercise 3-10 Try to use all kinds of function for list

games = ['World of Warcraft', 'The Elder Scroll', 'League of Legend', 'Boxing']

# 3.1.1 Visit an element in a list
print(games[0])

# 3.1.1 Index starts from 0, and -1 for quick visiting the last element
print(games[-1])

# 3.1.3 Use an element in a list
print(f'The first computer game I played is {games[0]}')

# 3.2.1 Modify an element in a list
print(games)
games[0] = 'WOW'
print(games)

# 3.2.2 Add an element in the end of a list
games.append('Grand Theft Auto')
print(games)

games.insert(0, 'Need for Speed')
print(games)

# 3.2.3 Delete an element from a list
# Use del statement
del games[1]
print(games)
# Use method: pop()
popped_game = games.pop()
print(popped_game)
print(games)
# Pop an element in a specific position
first_played = games.pop(0)
print(f'The first driving game that I played is {first_played}')
# Remove an element according to its value
now_playing = 'League of Legend'
games.remove(now_playing)
print(games)

# 3.3.2 Temporarily sorted()
games.insert(1,'World of Warcraft')
print(sorted(games))
print(games)

print(sorted(games, reverse=True))

# 3.3.1 Truly sorted .sort()
games.sort()
print(games)
games.sort(reverse=True)
print(games)

# 3.3.3 Reverse a list
games.reverse()
print(games)
games.reverse()
print(games)

# Check the length of a list
print(len(games))

