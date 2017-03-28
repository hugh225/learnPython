s=[]
b=[0 for x in range(0,10)]
# 发牌
while True:
	player_a=[int(n) for n in input().split(',')]
	player_b=[int(n) for n in input().split(',')]
	if len(player_a)==len(player_b):
		break
	print("cards not equal, please try again!")

# 打牌
def play_card(player, table, book):
	t=player[0]
	if(book[t]==0):
		player.pop(0)
		table.append(t)
		book[t]=1
	else:
		player.pop(0)
		player.append(t)
		while table[-1]!=t:
			x=table.pop()
			player.append(x)
			book[x]=0
		player.append(table.pop())
		book[t]=0

while len(player_a)>0 and len(player_b)>0:
	play_card(player_a, s, b)
	play_card(player_b, s, b)

if len(player_a)==0:
	print("player b wins!")
	print("the cards on player b:")
	print(player_b)
	print("the cards on table:")
	print(s)
elif len(player_b)==0:
	print("player a wins!")
	print("the cards on player a:")
	print(player_a)
	print("the cards on table:")
	print(s)