import random as rn
import turtle
import numpy as np
import sys
class Maze(turtle.Turtle):
      width=0
      height=0
      maze=""
      positions={}
      m_distances={}
      move_speed=0
      def __init__(self,speed,width,height):
             turtle.Turtle.__init__(self)
             #turtle.pen(fillcolor="black", pencolor="red", pensize=10)
             #turtle.shapesize(5, 5, 12)
             window=turtle.Screen()
             self.move_speed=speed
             window.title("A Maze")             
             window.setup(width,height)
             window=turtle.Screen()
             window.bgcolor("black")
             self.fillcolor('brown')
             self.shape("square")
             self.shapesize(1,1)
             self.shapesize(outline=1)
             self.penup()
             self.speed(speed)
             self.width=width
             self.height=height
             self.pencolor("Gray")
      def start(self,start_point,goal_point):
             if(self.maze[start_point[0]][start_point[1]] =='#'):
                    raise Exception("maze must have exactly one start point")
                    #sys.exit(1)
             if(self.maze[goal_point[0]][goal_point[1]] =='#'):
                    raise Exception("maze must have exactly one goal")
                    #sys.exit(1)
             self.setup_maze(start_point,goal_point) 
                        
      def setup_maze(self,start_point,goal_point):
             for i in range(len(self.maze)):
                 for j in range(len(self.maze[i])):
                     x=-int(self.width/2)+21*j
                     y=int(self.height/2-11)-21*i
                     self.goto(x,y)
                     if self.maze[i][j]=='#':                      
                       self.stamp()
                     elif self.maze[i][j]=='O':
                       cost=self.manhattan_distance((i,j),goal_point)
                     
                       self.m_distances[(i,j)]=cost
                       self.write(cost)

               
      def manhattan_distance(self,point_A,point_B):
           return (abs(point_A[0]-point_B[0])+abs(point_A[1]-point_B[1]))      
                      
      def random_positions(self):
           
             self.maze=[['#' for i in range(int(self.width/21))] for j in range(int(self.height/21))]
             
             h=len(self.maze)
             w=len(self.maze[0])
             #np.random.seed(1)
             for l in range(int( h*w*0.4)):
                       
                       i=np.random.randint(1,self.height/21-1)
                       j=np.random.randint(2,self.width/21-2)
                       self.maze[i][j]='O'

                       pos=(i,j)   
                       if pos in self.positions.keys():
                          continue
                       self.positions[pos]=[]   
                       step_1=np.random.choice([1,-1])
                       step_2=np.random.choice([1,-1])
                       new_pos_1=(pos[0],pos[1]+step_1)
                       new_pos_2=(pos[0]+step_2,pos[1])

  
                       if (j+step_1) in range(len(self.maze[i])) :
                           self.positions[new_pos_1]=[] 
                           self.maze[i][j+step_1]='O'
                       if (i+step_2) in range(len(self.maze)) :
                           self.positions[new_pos_2]=[] 
                           self.maze[i+step_2][j]='O'

             for i in range(len(self.maze)):
              for j in range(len(self.maze[i])):
                       if self.maze[i][j]=='O': 
                           if (j+1) in range(len(self.maze[0])) and self.maze[i][j+1]=='O'   :
                              self.positions[(i,j)].append((i,j+1))
                           if (j-1) in range(len(self.maze[0])) and self.maze[i][j-1]=='O'   :
                              self.positions[(i,j)].append((i,j-1))
                           if (i-1) in  range(len(self.maze)) and self.maze[i-1][j]=='O'   :
                              self.positions[(i,j)].append((i-1,j))
                           if (i+1) in  range(len(self.maze)) and self.maze[i+1][j]=='O'   :
                              self.positions[(i,j)].append((i+1,j))        
                
             return self.positions
             
      def path_setup(self,path,color="Red"):
             self.speed(0)
             self.shape("classic")
             self.pencolor(color)
             for block in path:

                     x=-int(self.width/2)+21*block[1]
                     y=int(self.height/2-11)-21*block[0]
                     self.goto(x,y)
                     self.write(self.m_distances[block])
             self.speed(self.move_speed)
             
