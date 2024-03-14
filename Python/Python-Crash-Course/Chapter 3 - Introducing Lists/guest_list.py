# exercise 3-4 Invitation for dinner
guest_list = ['Bruce Lee', 'Lewis Jones', 'Bin Wang', 'Hao Wang']

# convert a list to a string
# method 1
s = ' '
print(s.join(guest_list))

# method 2
converted = ', '.join([str(elem) for elem in guest_list])
print(converted)

#method 3
mapped = ', '.join(map(str,guest_list))
print(mapped)

print(f"I'd like to invite {converted} for dinner")
# exercise 3-9 dinner guest
print(f'{len(guest_list)} people was/were invited for dinner')

# exercise 3-5 modify guest list
print(f"{guest_list[-1]} cannot come to my dinner")
guest_list[-1] = 'my younger brother'
converted =  ', '.join([str(elem) for elem in guest_list])
print(f"After consideration, I'd like to invite {converted} for dinner")

# exercise 3-6 append guest
print('A bigger dinning table found')
guest_list.insert(0, 'Jingcheng Huang')
guest_list.insert(2, 'Pro. Zhao')
guest_list.append('Zhizhuo Wang')
print(guest_list)
converted = ', '.join([str(elem) for elem in guest_list])
print(f"Since we have a bigger dinning table, I'd very much like to invite {converted} for dinner")

# exercise 3-7 shorten list
print('Unfortunately, due to the big table cannot be delivered on time, I can only invite two guys')
for i in range(len(guest_list)-2):
    print(f"I'm sorry that I cannot invite {guest_list.pop()} for dinner today")
print(f"Real call, I will invite {guest_list[0]} and {guest_list[1]} for dinner")
del guest_list[1]
del guest_list[0]
print(guest_list)

