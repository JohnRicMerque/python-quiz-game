#  anime quiz game python program 

# initializes game
def newGame():
    qNum = 0
    correct = 0

    for question in questionAns:
        print('-----------------------------------------------------------------------------')
        print(f'{qNum+1}. {question}')
        for item in choices[qNum]:
            print(item)
        qNum += 1

        userAns = input('Enter Answer: ')
        userAns = userAns.lower()

        correct += check(questionAns.get(question),userAns)
        print(f'Score: {correct} / {qNum}')
    print('-----------------------------------------------------------------------------')
    playAgain()

# checks answer
def check(answer, guess):
    if answer == guess:
        print('Correct')
        return 1
    else:
        print('Wrong')
        return 0

# asks user to play again
def playAgain():
    tryAgain = input('\nDo you want to try again? y/n: ')
    tryAgain = tryAgain.lower() 
    if tryAgain == 'y':
        newGame()
    else:
        print('Goodbye Player!')

# dictionary for question and answers
questionAns = {
'In the anime series “Full Metal Alchemist”, what do Alchemists consider as the greatest taboo?':'a', #Human Transmutation
"In Death Note, what was Light's allias?":'b',#Kira
'In “Hunter x Hunter”, what are members in Killua’s family known for being?':'b',#Assasins
"Who is humanity's strongest soldier in Attack on Titan?":'a',#Levi
"What name do Naruto address Jiraiya?":'c', #Pervy Sage
"What is Dororo's biological sex?":'b', #Female
"What was Lelouch vi Britannia's Geass?":'b' #Absolute Obedience
}

# list of lists for choices
choices = [
['a. Human Transmutation', 'b. Mass Murder', 'c. Human Alteration'],
['a. L', 'b. Kira', 'c. Ryuk'],
['a. Wizards','b. Assasins','c. Cannibals'],
['a. Levi', 'b. Mikasa', 'c. Erwin'],
['a. Master Raya', 'b. Jira-senpai', 'c. Pervy Sage'],
['a. Male', 'b. Female'],
['a. One for All', 'b. Absolute Obedience', 'c. Amaterasu']]

# main
newGame()