def newGame ():
    qNum = 0
    for question in questionAns:
        print(f'{qNum+1}. {question}')
        print (choices[qNum])
        qNum += 1

# dictionary for question and answers
questionAns = {
'In the anime series “Full Metal Alchemist”, what do Alchemists consider the greatest taboo?':'a', #Human Transmutation
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
['a. One for All', 'b.Absolute Obedience', 'c.Amaterasu']]

newGame()