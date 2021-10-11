import requests
from bs4 import BeautifulSoup
from random import shuffle

score = 0
# For common words in sentences
dictionary = []
with open('sentences.dat', 'r', encoding = 'UTF+8') as f:
    for line in f:
        li = line.find('**')
        if len(line[li+2:line.find('**', li+1)]) > 2:
            dictionary.append(line)

shuffle(dictionary)
dictionary = dictionary[0:20]

for i in dictionary:
    ii = i.find('**')
    j = i[ii+2:i.find('**', ii+1)]
    print('\n'+str(dictionary.index(i)+1)+'.'+i[i.find(' ')+1:ii]+str(j[0] + '___' + j[-1])+i[i.find('**', ii+1)+2:-1]+i[-1], end='')
    
    for k in range(4):
        if k <= 2:
            ans = input('Your Answer(h for hint):')
        else:
            ans = input('Your Final Answer:')
        if ans.lower() == j.lower():
            print('Answer Correct!\n')
            input('Press enter to continue...')            
            score += 4-k
            break
        elif ans == 'h':
            if k == 0:
                print('Hint:'+str(len(j))+' letters')
            elif k == 1:
                html = requests.get('https://en.oxforddictionaries.com/definition/'+j)
                sp = BeautifulSoup(html.text, 'html.parser')
                print('Next hint:')
                try:
                    goal = str(sp.select(".ind")[0])
                    print(goal[goal.find('>')+1:-7])
                except:
                    print("error")
            elif k == 2:
                print('Next hint:(no more hints)')
                try:
                    goal = str(sp.select(".ind")[1])
                    print(goal[goal.find('>')+1:-7])
                except:
                    print("error")
            else:
                print('Answer Incorrect!\n')
                print('The sentence is:\n', i[i.find(' ')+1:-1]+i[-1])
                input('Press enter to continue...')            
            continue
        else:
            print('Answer Incorrect!\n')
            print('The sentence is:\n', i[i.find(' ')+1:-1]+i[-1])
            input('Press enter to continue...')
            break

print('You Score', str(score), 'points')
input()
