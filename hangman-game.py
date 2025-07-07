import random

def get_word():
    words = ['banana', 'python', 'laptop', 'vibe']
    return random.choice(words)

def play_game():
    word = get_word()
    guessed = []
    lives = 5
    display = ['_' for _ in word]

    while lives > 0 and '_' in display:
        print("\nWord:", ' '.join(display))
        print(f"Lives: {lives}")
        print("Guessed so far:", ', '.join(guessed))
        bhjguess = input("Guess a letter: ").lower()

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
            print("Wrong guess!")

    if '_' not in display:
        print("🎉 You win! The word was:", word)
    else:
        print("💀 You lost! The word was:", word)

if __name__ == '__main__':
    play_game()





