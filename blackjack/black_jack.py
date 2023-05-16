"""The classic card game also known as 21. (This version doesn't have
splitting or insurance.)
Tags: large, game, card game"""

import random
import sys

# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.
BACKSIDE = 'backside'
CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 1,  # Aces can be 1 or 11, but we'll handle that separately.
}


def result_game(player_value, dealer_value, money, bet):
    if dealer_value > 21:
        print(f"Dealer busts! You win ${bet}!")
        money += bet
    elif (player_value > 21) or (player_value < dealer_value):
        print('You lost!')
        money -= bet
    elif player_value > dealer_value:
        print(f"You won ${bet}!")
        money += bet
    elif player_value == dealer_value:
        print('It\'s a tie, the bet is returned to you.')

    input('Press Enter to continue...')
    print('\n\n')
    return money


def get_bet(max_bet):
    """Ask the player how much they want to bet for this round."""
    while True:
        try:
            bet = input(
                f"How much do you bet? (1-{max_bet}, or QUIT) ").upper().strip()
            if bet.upper() == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            if 1 <= int(bet) <= max_bet:
                return int(bet)
        except ValueError:
            pass


def get_deck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """Show the player's and dealer's cards. Hide the dealer's first
    card if showDealerHand is False."""
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])

    # Show the player's cards:
    print()
    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)


def display_cards(cards):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.

    for _, card in enumerate(cards):
        if card == BACKSIDE:
            # Print the back of the cards:
            rows[0] += '┌─────┐ '
            rows[1] += '│░░░░░│ '
            rows[2] += '│░░░░░│ '
            rows[3] += '│░░░░░│ '
            rows[4] += '└─────┘ '
        else:
            # Print the front of the cards:
            rank, suit = card
            rows[0] += '┌─────┐ '
            rows[1] += f"│{rank.ljust(2)}   │ "
            rows[2] += f"│  {suit}  │ "
            rows[3] += f"│   {rank.rjust(2)}│ "
            rows[4] += '└─────┘ '

    # Print each row on the screen:
    for row in rows:
        print(row)


def get_hand_value(hand):
    """Return the value of a hand of cards."""
    # Count the number of aces and total points in the hand:
    values = [CARD_VALUES[card[0]] for card in hand]
    num_aces = values.count(1)
    total = sum(values)
    # If the hand contains an Ace and the total value is low enough,
    # we can count the Ace as 11 instead of 1:
    if num_aces > 0 and total + 10 <= 21:
        total += 10
    return total


def get_move(player_hand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down."""
    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make:
        moves = ['(H)it', '(S)tand']

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards:
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.


def main():
    print('''Blackjack
    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.''')

    money = 5000
    while True:  # Main game loop.
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        print('Money:', money)
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        while True:  # Keep looping until player stands or busts.
            display_hands(player_hand, dealer_hand, False)

            if get_hand_value(player_hand) > 21:
                break

            move = get_move(player_hand, money - bet)

            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet}.")
                print('Bet:', bet)

            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break

                input('Press Enter to continue...')
                print('\n\n')

        display_hands(player_hand, dealer_hand, True)

        money = result_game(player_value=get_hand_value(player_hand),
                            dealer_value=get_hand_value(dealer_hand),
                            money=money,
                            bet=bet)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
