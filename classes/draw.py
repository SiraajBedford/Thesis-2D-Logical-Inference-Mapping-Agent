# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

class Draw():

    def animate(i):
        graph_data=open('example.txt','r').read()
        lines=graph_data.split('\n')
        xs=[]
        ys=[]
        for line in lines:
            if len(line)>1:
                x,y=line.split(',')
                xs.append(x)
                ys.append(y)
                
        ax1.clear()        
        ax1.plot(xs, ys)
        
    
    ani=animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    
    
# WHITE=(255,255,255)
# BLUE=(0,0,255)

# pygame.init()
# gameDisplay = pygame.display.set_mode((500,500))
# pygame.display.set_caption("BLOCK WORLD")
# x=0
# y=0

# clock=pygame.time.Clock()

# crashed=False


# while not crashed:
    
#     pygame.draw.rect(gameDisplay,WHITE,(y,x,100,50))
    
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True
            
#         if event.type == pygame.K_RIGHT:
#             x=x+20
            
#         if event.type == pygame.K_DOWN:
#             y=y+20
            
#         print(event)
    
#     pygame.display.update()
#     clock.tick(60)

# pygame.quit()
# quit()