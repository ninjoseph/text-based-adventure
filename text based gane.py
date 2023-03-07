# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:15:43 2023

@author: ttgll
"""
#import math
import random
class player:
    def __init__(self,name,hp,head,chest,legs,Lhand,Rhand):
        self.name = (name)
        self.hp = (hp)
        self.head = (head)
        self.chest = (chest)
        self.legs = (legs)
        self.Lhand = (Lhand)
        self.Rhand = (Rhand)
        
class weapon:
    def __init__(self,name,Range,hit_mod,dmg,effect):
        self.name = (name)
        self.range = (Range)
        self.hit_mod = (hit_mod)
        self.dmg = (dmg)
        self.effect = (effect)
'''       
class head:

class chest:

class legs:
'''
class enemy:
    def __init__(self,name,hp,armor,dmg,effect):
        self.name = (name)
        self.hp = (hp)
        self.armor = (armor)
        self.dmg = (dmg)
        self.effect = (effect)
        
def new_wep():
    n=input('what is the weapon name:   ')
    r=int(input('what is the range:   '))
    hm=int(input('what is the hit mod:   '))
    print('what is the dmg range?')
    dmg=[]
    low=int(input('low:   '))
    high=int(input('high:   '))
    dmgC=low
    while dmgC <= high:
        dmg.append(dmgC)
        dmgC+=1
    e=''
    return(weapon(n,r,hm,dmg,e))
    


def new_char():
    n=input('what is your name:   ')
    hp=int(input('what is your max hp:   '))
    wep=wep_list[0]
    return(player(n, hp, '', '', '', '', wep))

'''
#create a player and weapon and return random damages
player=new_char()
wep=player.Rhand
print(player.name)
print(player.Rhand.name)
print(player.Rhand.dmg)
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
print(random.choice(player.Rhand.dmg))
input('')
'''

def new_enemy():
    n = input('enemy name:   ')
    hp = int(input('max health:   '))
    armor = int(input('armor:   '))
    dmg = int(input('damage:   '))
    eff = ''
    return(enemy(n, hp, armor, dmg, eff))


wep_list=[]
ene_list=[]
char_list=[]


def attack():
    if len(ene_list) == 1:
        t=0
    elif len(ene_list) != 0:
        print('which enemy do you attack?')
        for x in range(len(ene_list)):
            print(f'{x+1} ',ene_list[x].name, ene_list[x].hp,'hp \n')
        t =int(input()) - 1
    else:
        print('you do no see any enemies...')
        t = 'empty'
    if t != 'empty':
        target = ene_list[t]
        roll = random.randint(1, 20) + char_list[0].Rhand.hit_mod
        if roll < target.armor:
            print(f'you miss {target.name}')
        else:
            dmg = random.choice(char_list[0].Rhand.dmg)
            target.hp -= dmg
            if target.hp > 0:
                print(f'you deal {target.name} {dmg} damage, they drop to {target.hp} hp')
            else:
                print(f'{target.name} is dead')
                ene_list.pop(t)
    
    
    
t = 1
while t != 0:
    print('\n')
    action=input('what would you like to do? (new weapon, new character, new enemy, attack, end)   ')
    if action == 'end':
        t = 0
    elif action == 'new weapon':
        wep_list.append(new_wep())
    elif action == 'new character':
        char_list.append(new_char())
    elif action == 'new enemy':
        ene_list.append(new_enemy())
    elif action == 'attack':
        attack()
    else:
        print('you done messed up aaron')
