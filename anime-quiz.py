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
    percent = (correct/qNum)*100   
  
    print('-----------------------------------------------------------------------------')
    print(f" Score Percentage: {percent:.2f}%")
    print('-----------------------------------------------------------------------------')
    label(percent)
    playAgain()

# checks answer
def check(answer, guess):
    if answer == guess:
        print('\033[34;1mCORRECT\033[m')
        return 1
    else:
        print('\033[31;1mWRONG\033[m')
        return 0

# asks user to play again
def playAgain():
    tryAgain = input('\nDo you want to try again? y/n: ')
    tryAgain = tryAgain.lower() 
    if tryAgain == 'y':
        newGame()
    else:
        print('\nGoodbye Player!')

# introduction
def intro():
    print ('\n\033[32mHello Player! Welcome to the Anime Quiz Game!\033[m\n')

# rating message after results
def label(percent):
    if int(percent) <= 33:
        print("Rating: \033[31;1mNovice\033[m, vWatch more young one!")
    elif int(percent) > 33 and int(percent) <= 66:
        print("Rating: \033[33;1mIntermediate\033[m, Nice... GRAPE!")
    else:
        print('Rating: \033[34;1mExcellent\033[m, All heil player! Long Live!')


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
intro()
newGame()