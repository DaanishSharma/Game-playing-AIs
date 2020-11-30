#!/usr/bin/env python
# coding: utf-8

# In[1]:


import heapq as hq
import numpy as np
import copy
k = int(input())
box = input()
box = box.split()
box = np.array([int(i) for i in box]).reshape((k,k))

\

box=box.tolist()


# In[3]:


box2 = box


# In[4]:


from queue import PriorityQueue


# In[5]:


def cal_md(box):
    k=len(box)
    r=0
    for i in range(k):
            for j in range(k):
                x = box[i][j]//k
                y = box[i][j]%k
                r+=abs(x-i)+abs(y-j)
    return r


# In[6]:


def mv(move):
    if move == 'UP':
        return 'DOWN'
    elif move == 'DOWN':
        return 'UP'
    elif move == 'LEFT':
        return 'RIGHT'
    elif move == 'RIGHT':
        return 'LEFT'
    


# In[7]:


class node:
    def __init__(self,box,parent,steps,move):
        self.box = box
        self.parent = parent
        self.steps = steps
        self.move = move


# In[8]:


start = node(box,None,0,None)


# In[9]:


def possibleMoves(box,k):
    box = np.array(box)
    indices=np.where(box == 0)
    i=indices[0][0]
    j=indices[1][0]
    ans = ["RIGHT","LEFT","UP","DOWN"]
    if i == 0 :
        ans.remove("UP")
    if i == k-1 :
        ans.remove("DOWN")
    if j == 0 :
        ans.remove("LEFT")
    if j == k-1 :
        ans.remove("RIGHT")    
    return ans


# In[10]:


import copy
def change(box,move):
    box = np.array(box)
    indices=np.where(box == 0)
    i=indices[0][0]
    j=indices[1][0]
    assert(box[i][j]==0)
    if move == "LEFT":
        assert(box[i][j-1]!=0)
        box[i][j]=box[i][j-1]
        box[i][j-1]=0
    elif move == "RIGHT":
        assert(box[i][j+1]!=0)
        box[i][j]=box[i][j+1]
        box[i][j+1]=0
    elif move == "UP":
        assert(box[i-1][j]!=0)
        box[i][j]=box[i-1][j]
        box[i-1][j]=0
    elif move == "DOWN":               #DOWN
        assert(box[i+1][j]!=0)
        box[i][j]=box[i+1][j]
        box[i+1][j]=0 
    return box.tolist()


# In[11]:


def bfs(box,k):
    target = (np.array([i for i in range(k*k)]).reshape((k,k))).tolist()
    queue = PriorityQueue()
    st = set()
    d = dict()
    d[tuple(np.array(box).flatten())] = (None,0)          #(move,depth)
    queue.put((cal_md(box), box))
    op_index = 0            
    while(queue):
        top = queue.get()[1] 
        print(top)
        st.add(tuple(np.array(top).flatten()))
        if top == target:
            return d
        moves = possibleMoves(top,k)
        for move in moves:
            newBox = change(top,move)
            if tuple(np.array(newBox).flatten()) not in st:  
                depth = d[tuple(np.array(top).flatten())][1]+1
                queue.put((cal_md(box)+depth, newBox))
                d[tuple(np.array(newBox).flatten())]=(move,depth)
            


# In[ ]:


l = bfs(box,k)


# In[ ]:


target = (np.array([i for i in range(k*k)]).reshape((k,k))).tolist()
depth = l[tuple(np.array(target).flatten())][1]
print(depth)
mvs = list()
while depth != 0:
    move = l[tuple(np.array(target).flatten())][0]
    depth = l[tuple(np.array(target).flatten())][1]
    target = change(target,mv(move))
    mvs.append(move)
while mvs:
    a = mvs.pop()
    if a != None:
        box2 = change(box2,a)
        print(box2)
        #print(a)


# In[ ]:




