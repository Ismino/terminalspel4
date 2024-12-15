import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['Sten','Sax','Påse']

    def start_game(self):
        print("Välkommen till sten sax påse!")
        while True:
            player_choice = self.get_player_choiche()
            if player_choice == 'Avsluta':
                print("Tack för att du spelade")
                break
            computer_choice = random.choice(self.choices)
            self.determine_winner(player_choice, computer_choice)

    def get_player_choiche(self):
        while True:
            print("\nVälj:")
            for i, choice in enumerate(self.choices, start=1):
                print(f"{i}. {choice}")
            print("4.Avsluta")

            try:
                selection = int(input("Ange ditt val:"))
                if 1 <= selection<= 3:
                    return self.choices[selection - 1]
                elif selection == 4:
                    return 'Avsluta'
                else:
                    print("Fel: Ogiltigt val försök igen.")

            except ValueError:
                print("Fel: Vänligen ange ett heltal")

    def determine_winner(self,player, computer):
        print(f"\nDu valde: {player}")
        print(f"Datorn valde: {computer}")

        if player == computer:
            print("det är oavgjort")
        elif (player == 'Sten' and computer == 'Sax') or \
             (player == 'Sax' and computer == 'Påse') or \
             (player == 'Påse' and computer == 'Sten'):
             print("grattis du vann")
        else:
            print("datorn vann")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.start_game()