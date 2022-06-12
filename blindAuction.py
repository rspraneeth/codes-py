logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bidders = {}
more_bid = 'y'


def max_bid(bidders_list):
    max_c = 0
    winner = ''
    for name_user in bidders_list:
        if bidders_list[name_user] > max_c:
            max_c = bidders_list[name_user]
            winner = name_user

    print(f"winner is {winner} with bid amount of {max_c}")


while more_bid == 'y':
    name = input("What's the name of user: ")
    bid = int(input("What's the bid amount: $"))
    bidders[name] = bid
    more_bid = input("is there anyone more to bid Y/N: ").lower()
    if more_bid == 'n':
        max_bid(bidders_list=bidders)
