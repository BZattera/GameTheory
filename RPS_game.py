import time
import pygame
import random
import pandas as pd
from datetime import datetime
import yagmail
import feather



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def instructions(screen):
    font_heading = pygame.font.SysFont("Arial", 50)
    heading = ("Welcome to the ultimate Rock Paper Scissor game!")

    font_text = pygame.font.SysFont("Arial", 35)
    myText = ("The game it's easy: click on your selected choice. \n \n" \
              "You will receive a feedback: \n" \
              "green = win, \nblue = draw, \nred = lose. \n" \
              "When the feedback disappears, you can do the next trial")

    blit_text(screen, heading, (30, 30), font_heading)
    blit_text(screen, myText, (30, 250), font_text)
    pygame.display.flip()
    f_running = True

    while (f_running):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill([255, 255, 255])
                f_running = False


def win(player_choice, computer):
    final_result = []

    if player_choice == computer:
        #print('repeat game!')
        final_result = 'draw'
    elif (player_choice == 'scissor' and computer == 'paper'
    ) or (player_choice == 'paper' and computer == 'rock'
    ) or (player_choice == 'rock' and computer == 'scissor'):
        #print('Good! You won!')
        final_result = 'win'

    elif (player_choice == 'scissor' and computer == 'rock'
    ) or (player_choice == 'paper' and computer == 'scissor') or (player_choice == 'rock' and computer == 'paper'):
        #print('Try again')
        final_result = 'lose'

    return final_result


def get_x_comp(response, comp, x, distance=180):
    x_comp = []
    if comp == response:
        x_comp = x
    elif ((comp == 'scissor' and response == 'paper') or (comp == 'paper' and response == 'rock')):
        x_comp = x - distance
    elif (comp == 'scissor' and response == 'rock'):
        x_comp = x - (distance * 2)
    elif ((comp == 'paper' and response == 'scissor') or (comp == 'rock' and response == 'paper')):
        x_comp = x + distance
    elif (comp == 'rock' and response == 'scissor'):
        x_comp = x + (distance * 2)

    return x_comp


def display_feedback(response, x_coord, y_coord, comp, screen):
    y_comp = (y_coord / 2) * 0.5
    x_comp = get_x_comp(response, comp, x_coord)
    outcome = []

    if win(response, comp) == 'win':
        outcome = 'win'  # writing the outcome
        pygame.draw.rect(screen, [0, 255, 0], [x_coord, y_coord, pic_dim, pic_dim], 4)  # green outline for the player
        pygame.draw.rect(screen, [255, 0, 0], [x_comp, y_comp, pic_dim, pic_dim], 4)  # red outline for the computer
        pygame.display.flip()
        time.sleep(0.7)
        # display win window
        display_win(screen, width, height, 'u_won.png')
        pygame.draw.rect(screen, [255, 255, 255], [x_coord, y_coord, pic_dim, pic_dim], 4)  # remove player's outline
        pygame.draw.rect(screen, [255, 255, 255], [x_comp, y_comp, pic_dim, pic_dim], 4)  # remove computer's outline
        pygame.display.flip()


    elif win(response, comp) == 'lose':
        outcome = 'lose'  # writing the outcome
        pygame.draw.rect(screen, [255, 0, 0], [x_coord, y_coord, pic_dim, pic_dim], 4)  # red outline for the player
        pygame.draw.rect(screen, [0, 255, 0], [x_comp, y_comp, pic_dim, pic_dim], 4)  # green outline for the computer
        pygame.display.flip()
        time.sleep(0.7)
        # display win window
        display_win(screen, width, height, 'u_lose.jpg')
        pygame.draw.rect(screen, [255, 255, 255], [x_coord, y_coord, pic_dim, pic_dim], 4)  # remove player's outline
        pygame.draw.rect(screen, [255, 255, 255], [x_comp, y_comp, pic_dim, pic_dim], 4)  # remove computer's outline
        pygame.display.flip()
        outcome = 'lose'

    elif win(response, comp) == 'draw':
        outcome = 'draw'  # writing the outcome
        pygame.draw.rect(screen, [0, 0, 255], [x_coord, y_coord, pic_dim, pic_dim], 4)
        pygame.draw.rect(screen, [0, 0, 255], [x_comp, y_comp, pic_dim, pic_dim], 4)  # red outline for the computer
        pygame.display.flip()
        time.sleep(0.7)
        # display win window
        display_win(screen, width, height, 'tie_game.png')
        pygame.draw.rect(screen, [255, 255, 255], [x_coord, y_coord, pic_dim, pic_dim], 4)  # remove player's outline
        pygame.draw.rect(screen, [255, 255, 255], [x_comp, y_comp, pic_dim, pic_dim], 4)  # remove computer's outline
        pygame.display.flip()
    return outcome


def display_win(screen, width, height, img):
    screen.fill([255, 255, 255])
    rew_pic_dim = 250
    x_pos = width/2 + rew_pic_dim/2
    y_pos = height / 2 + rew_pic_dim / 2
    display_img = pygame.transform.scale(pygame.image.load(img).convert(), (x_pos, y_pos))
    screen.blit(display_img, (x, y_computer))  # paint to screen
    pygame.display.flip()  # paint screen one time
    time.sleep(2)
    screen.fill((255, 255, 255))

    pygame.display.flip()  # paint screen one time
    display_choice()



def display_choice():
    # stimuli for the computer
    screen.blit(scissor, (x, y_computer))  # paint to screen
    screen.blit(paper, (x_paper, y_computer))  # paint to screen
    screen.blit(rock, (x_rock, y_computer))  # paint to screen
    font_computer = pygame.font.SysFont("Arial", 50)
    computer = ("Computer's choice")
    blit_text(screen, computer, (x + 100, (y_computer - 80)), font_computer)

    # stimuli for the player
    screen.blit(scissor, (x, y))  # paint to screen
    screen.blit(paper, (x_paper, y_paper))  # paint to screen
    screen.blit(rock, (x_rock, y_rock))  # paint to screen
    font_player = pygame.font.SysFont("Arial", 50)
    player = ("Click on your move")
    blit_text(screen, player, (x + 100, (y - 80)), font_player)

    pygame.display.flip()  # paint screen one time


class MutableSlice(object):
    def __init__(self, baselist, begin, end=None):
        self._base = baselist
        self._begin = begin
        self._end = len(baselist) if end is None else end

    def __len__(self):
        return self._end - self._begin

    def __getitem__(self, i):
        return self._base[self._begin + i]

    def __setitem__(self, i, val):
        self._base[i + self._begin] = val


def weighted_computer_choice(select, all_trial_outcome, all_player_choice):
    # with this first part of the code, I try to anticipate the next player's choice

    # if the player wins, there is higher probability he will repeat the choice
    if all_trial_outcome[-1] == 'win':
        if all_player_choice[-1] == 'scissor':
            # when the player wins with scissor, he's more likely to repeat his choice =>
            # to win, we have to mostly go for rock
            choice = random.choices(select, weights=(0.25, 0.25, 0.5), k=1)
        elif all_player_choice[-1] == 'paper':
            # when the player wins with paper, he's more likely to repeat his choice =>
            # to win, we have to mostly go for scissor
            choice = random.choices(select, weights=(0.5, 0.25, 0.25), k=1)
        elif all_player_choice[-1] == 'rock':
            # when the player wins with rock, he's more likely to repeat his choice =>
            # to win, we have to mostly go for paper
            choice = random.choices(select, weights=(0.25, 0.5, 0.25), k=1)

    # if the player doesn't win, then he won't prefer anything (the choice will be random)
    # in this case, the optimal solution is to go random
    else:
        choice = random.choices(select)

    return choice[0]


pygame.init()
width = 750;
height = 600
pic_dim = 150;

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
# pygame.display.set_caption('clicked on image')
scissor = pygame.transform.scale(pygame.image.load("scissor1.jpg").convert(), (pic_dim, pic_dim))
paper = pygame.transform.scale(pygame.image.load("paper1.jpg").convert(), (pic_dim, pic_dim))
rock = pygame.transform.scale(pygame.image.load("rock1.jpg").convert(), (pic_dim, pic_dim))
# redSquare = pygame.transform.scale(redSquare, (150, 150))

distance = 180;
x = (width - 3 * distance) / 2;  # x coordnate of image

y = (height / 3) * 2;  # y coordinate of image
y_computer = (height / 3) * 0.5;
x_paper = x + distance
x_rock = x + (distance * 2);
y_paper = y
y_rock = y

pygame.init()  # now use display and fonts
screen.fill([255, 255, 255])
instructions(screen)

# stimuli for the computer
screen.blit(scissor, (x, y_computer))  # paint to screen
screen.blit(paper, (x_paper, y_computer))  # paint to screen
screen.blit(rock, (x_rock, y_computer))  # paint to screen
font_computer = pygame.font.SysFont("Arial", 50)
computer = ("Computer's choice")
blit_text(screen, computer, (x + 100, (y_computer - 80)), font_computer)

# stimuli for the player
screen.blit(scissor, (x, y))  # paint to screen
screen.blit(paper, (x_paper, y_paper))  # paint to screen
screen.blit(rock, (x_rock, y_rock))  # paint to screen
font_player = pygame.font.SysFont("Arial", 50)
player = ("Click on your move")
blit_text(screen, player, (x + 100, (y - 80)), font_player)

n_trial = 30;  # number of trials

pygame.display.flip()  # paint screen one time
select = ['scissor', 'paper', 'rock']  # list of possible values
running = 0  # initialization

# initializing the list for the result
all_player_choice = []
all_computer_choice = []
running_trial = []
all_trial_outcome = []

original_list = list(['random_choice', 'weighted_choice'] * n_trial)  # creating a list of 60 elements (50% random, 50% weighted)

slice = MutableSlice(original_list, 1)  # selecting the part of the list I want to shuffle (all but the first element)
random.shuffle(slice)  # shuffleing the slice


while (running < len(original_list)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = n_trial
        if event.type == pygame.MOUSEBUTTONDOWN:
            running_trial.append(running)

            # Randomly selects option for computer. I select this case for the 50% of the case and if the
            if original_list[running] == 'random_choice':
                computer = random.choice(select)
                all_computer_choice.append(computer)
            elif original_list[running] == 'weighted_choice':
                computer = weighted_computer_choice(select, all_trial_outcome, all_player_choice)
                #print(computer)
                all_computer_choice.append(computer)

            # Set the x, y postions of the mouse click
            x_pos, y_pos = pygame.mouse.get_pos()

            if (x_pos > x and x_pos < x + pic_dim and y_pos > y and y_pos < y + pic_dim):
                #print('clicked on scissor')
                all_trial_outcome.append(display_feedback('scissor', x, y, computer, screen))
                all_player_choice.append('scissor')

            elif (x_pos > x_paper and x_pos < x_paper + pic_dim and y_pos > y_paper and y_pos < y_paper + pic_dim):
                #print('clicked on paper')
                all_trial_outcome.append(display_feedback('paper', x_paper, y_paper, computer, screen))
                all_player_choice.append('paper')

            elif (x_pos > x_rock and x_pos < x_rock + pic_dim and y_pos > y_rock and y_pos < y_rock + pic_dim):
                #print('clicked on rock')
                all_trial_outcome.append(display_feedback('rock', x_rock, y_rock, computer, screen))
                all_player_choice.append('rock')
            running += 1  # incrementing the counter

<<<<<<< HEAD
display_bye()
print(len(running_trial))
print(len(all_player_choice))
print(len(all_computer_choice))
print(len(all_trial_outcome))
print(len(original_list))

=======
>>>>>>> parent of 9cfd0f1 (rps update)
df = pd.DataFrame({'trial_numb': running_trial, 'player_choice': all_player_choice,
                   'computer_choice': all_computer_choice, 'outcome': all_trial_outcome,
                   'stimulus_kind': original_list})


datestring = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
df.to_feather(datestring + '.ftr')

sender_email = "felsenberglab@gmail.com"
receiver_email = 'benedetta.zattera@gmail.com'
subject = "A new person player RPS"

sender_password = "Flytrap.1"

yag = yagmail.SMTP(user=sender_email, password=sender_password)
body = [
    "Whohoooo!",
    "\n",
    "You have new data for your RPS experiment!",
    "\n"
    "Hurry up and analyze them!"]

yag.send(
    to=receiver_email,
    subject=subject,
    contents=body,
    attachments=(datestring + '.ftr')
)