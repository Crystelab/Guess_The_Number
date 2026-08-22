import requests

baseUrl= 'http://127.0.0.1:5000/api'

def getGames():
    try:
        response = requests.get(baseUrl + '/game')

        if response.status_code == 200:
            games = response.json()
            printGames(games)
            return games
        else:
            print('Error:', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Error:', e)

def printGames(games):
    if not games:
        print("No games found.")

    for game in games:
        status = "In Progress" if game['Status'] == 1 else "Finished"
        print(f"Game {game['GameId']} - {status}")

def printRounds(rounds):
    last = rounds[len(rounds) - 1]
    print(f"{last['Guess']}")

def getGameStatus(gameId):
    game = requests.get(baseUrl + '/game/' + gameId).json()
    return game['Status']

def playGame(gameNumber):
    print(f"You are now playing Game {gameNumber}. \nEnter a 4 numbers guess in this format: n:n:n:n")
    gameRunning = True
    while(gameRunning):
        validGuess = False
        guess = ''
        while (validGuess != True):
            guess = input()

            if len(guess) == 7 and guess[1] == ':' and guess[3] == ':' and guess[5] == ':' and guess[0].isdigit() and guess[2].isdigit() and guess[4].isdigit() and guess[6].isdigit():
                validGuess = True
            elif guess == 'r':
                initialMenu()
            else:
                print('Invalid input')
        
        requests.post(baseUrl + '/guess', json={"gameId": gameNumber, "guess": guess})
        status = getGameStatus(gameNumber)

        if(status == 1):
            rounds = requests.get(baseUrl + '/rounds/' + gameNumber).json()
            printRounds(rounds)
        if(status == 0):
            gameRunning = False
            print("Congrats!!!! \nPress enter to go back to the home menu.")
            input()
    

def initialMenu():
    print("Enter 'og' to play an old game. \nOr enter 'ng' to play a new game")
    oOrn = input()

    if (oOrn != 'og' and oOrn != 'ng'):
        print('Invalid input')

    if (oOrn == 'og'):
        games = getGames()
        print("Enter the game number you wish to continue.")

        valid = False
        while(valid == False):
            gameNumber = input()

            if gameNumber != 'r' and gameNumber not in [str(game['GameId']) for game in games]:
                print('Invalid input')

            elif(gameNumber == 'r'):
                valid = True
                initialMenu()

            else:
                status = getGameStatus(gameNumber)
                if (status == 1):
                    valid = True
                    playGame(gameNumber)
                else:
                    print(f'The Game {gameNumber} is already finished! Try another one.')

    elif (oOrn == 'ng'):
        game = requests.post(baseUrl + '/begin').json()
        gameId = game['id']
        playGame(str(gameId))
            

while True:
    print("Enter 'r' anytime to return to this menu.")
    initialMenu()