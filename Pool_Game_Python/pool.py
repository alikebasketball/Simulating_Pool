# Now I will attempt to run a game
# Start with my imports
from ball import Ball, numinput

# Let us get some inputs..
print('Welcome to the thunder dome!!!!')
input()
print('Your fate will be decided by a simple game..')
input()
print('This game is..')
input()
print('POOL!!!')
input()

# Now variables
u = numinput()
v = numinput()

if u and v:
    # Lets get an instance of ball
    game = Ball(u, v)

    while game.status == 'Moving..':
        game.update()
        game.locate_ball()
else:
    print('Try again loser..') 
    
game.status