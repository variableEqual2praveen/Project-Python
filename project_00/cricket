###a simple cricket game 

import random

def for_single () :

    com_for_single = ['Good cricket all round','That seems to be missing leg...and its single',
    'Thats a Proper Cricket Shot.','Excellent batting conditions','Good cricket all round',]
    print(random.choice(com_for_single))

def for_boundary() :
    commentry_for_boundary = ['Good cricket all round','When He Hits It, It Stays Hit.',
    'hats placed in the gaps/vacant region',
    'Thats a screamer','Excellent batting conditions',
    'Straight down the ground','What a lovely shot!...its six',
    'Only he can play that shot']
    print(random.choice(commentry_for_boundary))


def for_six():

    com_for_six = ['Good cricket all round',
    'Just over the fielder',
    'Thats a hugeeeee hit!',
    'That’s a screamer',
    'Excellent batting conditions',
    'That’s massive and out of the ground',
    'Maxxxxximumm',
    'What a lovely shot!...its six',
    'Only he can play that shot',
    'Thats huge ',
    'Thats a maximum']
    print(random.choice(com_for_six))

def for_wickt() :

    com_for_wick = ['In the airrr…and taken','Good cricket all round','Excellent line and length',
    'Thats some good short stuff','Straight Down the Fielder Throat.',
    'Right Up in the Blockhole.','……..And he makes no mistake.','Edged and taken.',
    'That’s a screamer',
    'n the air..... fielder coming underneath and taken',
    'Batsman tried a fancy stroke and threw his wicket',
    'The break cost him his wicket as batsman tends to lose some concentration',
    'Ball goes like a tracer bullet',
    'What a catch!',
    'From the middle of the bat and taken',
    'In the airrrr.. XYZ takes it!',
    'Bowled him',
    'Excellent delivery']
    print(random.choice(com_for_wick))


for_batting  = ['Good cricket all round','……..And he makes no mistake.','That’s a screamer',]

def for_bowling():
    com_for_bowling = ['It depends on how well the spinners bowl',
    'Good cricket all round','Did it pitch in line',
    'Excellent effort on the boundary','He has a go at the stumps',
    'Direct hits are always dangerous',
    'Thats sloppy work by the fielder.',
    'Hes Bowling a Good Line and Length','……..And he makes no mistake.',
    'Beautiful spell']
    print(random.choice(com_for_bowling))

def for_misc() :
    com_for_misc = ['School boy stuff (Sunil Gavaskar’s favourite when the batsman doesnt drag his bat in the crease)',
    'We are up for a treat!','Cricket Is the Winner.',
    'The Key Will Be Early Wickets.',
    'The next few overs would be crucial.',
    'They need to go for wickets now.',
    'Stopping runs should be the topmost priority']
    print(random.choice(for_misc))

def dot_line(x,y) :
    var = ' WICKET '
    var2 = ' '
    print(var.center(35,'-'))
    print(('wicket no {} gone').format(x))
    print(('Ball remaining  {}').format(y))
    print(var2.center(35,'-'))




###first batting 

def battingfirst() :
    usr_score = []
    com_score = []
    ##total
    wick = 10
    over = int(input('enter the overs u need to play = ',))
    ball = over*6

    ##count 
    wick_c = 0
    ball_c = 0
    run_c = 0



    ##range(globa for battingfirst function)
    rran = range(0,ball)

    while True :
        if wick_c > 9 :
            break
        if ball_c == ball :
            break

        usr_inp = input('on strike',)

        if  usr_inp == ' ' :
            print('enter 0-6 to score')
            continue
        if int(usr_inp) not in range(0,7):
            print('enter 0-6 to score')
            continue 
        usr_inp = int(usr_inp)
        ball_c += 1
        ball_r = ball - ball_c

        comp_inp = random.randint(0,6)
        com_score.append(comp_inp)

        if usr_inp == comp_inp :
            wick_c += 1
            for_wickt()
            dot_line(wick_c,ball_r)
            #print(('wicket no {} gone,ball remaining {}').format(wick_c,ball_r))
            continue

        if usr_inp != comp_inp :
            run_c += usr_inp
            usr_score.append(usr_inp)
        
            if usr_inp == 6 :
                for_six ()
            if usr_inp == 4 :    
                for_boundary()
            if usr_inp == 1 :
                for_single ()

        #    print(('the score is {}-{}').format(run_c,wick_c))
        if ball_c / 6 in rran :
            print(('the score is {}-{}').format(run_c,wick_c))

    player_score = run_c
    print(('Player{}-{} in {}').format(run_c,wick_c,ball_c))



    busr_score = []
    bcom_score = []
    ##total
    bwick = 10
    bover = over
    #bover = int(input('enter the overs u need to play',))
    bball = bover*6

    ##count 
    bwick_c = 0
    bball_c = 0
    brun_c = 0

    while True :
        if bwick_c > 9 :
            break
        if bball_c == bball :
            break
        if brun_c > player_score :
            break

        busr_inpb = input('bowl',)

        if busr_inpb == '  ' :
            pass

        if int(busr_inpb) not in range(0,7) :
            print('enter 0-6 to bowl')
            continue
        busr_inpb = int(busr_inpb)
        bball_c += 1
        bball_r = bball - bball_c

        bcomp_inp = random.randint(0,6)
        bcom_score.append(bcomp_inp)

        if busr_inpb == bcomp_inp :
            bwick_c += 1
            for_wickt()
            dot_line(bwick_c,bball_r)
            #print(('wicket no {} gone,bball remaining {}').format(bwick_c,bball_r))
            

        if busr_inpb != bcomp_inp :
            brun_c += bcomp_inp
            busr_score.append(bcomp_inp)
            if usr_inp == 6 :
                for_six()
            if usr_inp == 4 :
                for_boundary()
            if usr_inp == 1 :
                for_single ()

        if bball_c / 6 in rran :
            print(('the score is {}-{}').format(brun_c,bwick_c))
        #    print(('the score is {}-{}').format(brun_c,bwick_c))
        computer_score = brun_c
    print(('{}-{} in {}balls ').format(brun_c,bwick_c,bball_c))


    #############Result
    if computer_score > player_score :
        print(('Computer won the match by {}').format(computer_score-player_score))
    if computer_score < player_score :
        print(('You won the match by {}').format(player_score - computer_score))
    if computer_score == player_score :
        print('Scores are Level -- Matchs Draw')





#####first     bowling fucntion 

def bowlingfirst () :

    busr_score = []
    bcom_score = []
    ##total
    bwick = 10
    bover = int(input('enter the overs u need to play = ',))
    bball = bover*6

    ##count 
    bwick_c = 0
    bball_c = 0
    brun_c = 0

    ##range(globa for ##bowlingfirst function)
    rran = range(0,bball)

    while True :
        if bwick_c > 9 :
            break
        if bball_c == bball :
            break

        busr_inpb = input('bowl',)

        if busr_inpb == ' ' :
            print('enter 0-6 to bowl')
            continue
        if int(busr_inpb) not in range(0,7) :
            print('enter 0-6 to bowl')
            continue
        busr_inpb = int(busr_inpb)
        bball_c += 1
        bball_r = bball - bball_c

        bcomp_inp = random.randint(0,6)
        bcom_score.append(bcomp_inp)

        if busr_inpb == bcomp_inp :
            bwick_c += 1
            for_wickt()
            dot_line(bwick_c,bball_r)
            #print(('wicket no {} gone,bball remaining {}').format(bwick_c,bball_r))
            

        if busr_inpb != bcomp_inp :
            brun_c += bcomp_inp

            if bcomp_inp == 6 :
                for_six()
            if bcomp_inp == 4 :
                for_boundary()
            if bcomp_inp == 1 :
                for_single ()

            busr_score.append(busr_inpb)
        if bball_c / 6 in rran :
            print(('the score is {}-{}').format(brun_c,bwick_c))
        #    print(('the score is {}-{}').format(brun_c,bwick_c))
    computer_score = brun_c
    print(('{}-{} in {}balls ').format(brun_c,bwick_c,bball_c))

    ###bat2

    usr_score = []
    com_score = []
    ##total
    wick = 10
    #over = int(input('enter the overs u need to play',))
    over = bover
    ball = over*6

    ##count 
    wick_c = 0
    ball_c = 0
    run_c = 0

    while True :
        if wick_c > 9 :
            break
        if ball_c == ball :
            break
        if run_c > computer_score :
            break 

        usr_inp = input('on strike',)

        if  usr_inp == str() :
            pass

        if int(usr_inp) not in range(0,7):
            print('enter 0-6 to score')
            continue 
        usr_inp = int(usr_inp)
        ball_c += 1
        ball_r = ball - ball_c

        comp_inp = random.randint(0,6)
        com_score.append(comp_inp)

        if usr_inp == comp_inp :
            wick_c += 1
            for_wickt()
            dot_line(wick_c,ball_r)
            #print(('wicket no {} gone,ball remaining {}').format(wick_c,ball_r))
            

        if usr_inp != comp_inp :
            run_c += usr_inp
            usr_score.append(usr_inp)

            if usr_inp == 6 :
                for_six()
            if usr_inp == 4 :
                for_boundary()
            if usr_inp == 1 :
                for_single ()

        if ball_c / 6 in rran :
            print(('the score is {}-{}').format(run_c,wick_c))


        #    print(('the score is {}-{}').format(run_c,wick_c))
    player_score = run_c
    print(('Player{}-{} in {}').format(run_c,wick_c,ball_c))

    if computer_score > player_score :
        print(('Computer won the match by {}').format(computer_score-player_score))
    if computer_score < player_score :
        print(('You won the match by {}').format(player_score - computer_score))


###############toss###########

coin = ['head','tail']
play_selection = ['batting', 'bowling']

coin_random = random.choice(coin)



usr_in =  input('Head or Tail == ' ,)
usr_in = usr_in.lower()
if usr_in == coin_random :
    print('You won the toss')
    usr_selection = input('Batting or Bowling ==')
    usr_selection = usr_selection.lower()
    if usr_selection == play_selection[0] :
        print('Your opt yo Bat')
        ###Batting function
        battingfirst()
    else :
        print('Your opt to bowl')
        #####bowling function
        bowlingfirst()

else :
    print('Computer won the toss')
    play_random = random.choice(play_selection)
    if play_random == play_selection[0] :
        print('Computer choses the Bat') 
        #####bowling function
        bowlingfirst()

    else :
        print('Computer choses the Bowl')
        ####batting fuction
        battingfirst()

