"""
Assignment 1-A
==============

"""

a = "the house that Jack built."
b = "the malt" 
c = "the rat,"
d = "the cat,"
e = "the dog,"
f = "the cow with the crumpled horn,"
g = "the maiden all forlorn,"
h = "the man all tatter'd and torn,"
j = "the priest all shaven and shorn,"
p = "the cock that crow'd in the morn,"
m = "the farmer sowing his corn," 

a1 = "That lay in "
b1 = "That ate "
c1 = "That kill'd "
d1 = "That worried "
e1 = "That tossed "
f1 = "That milk'd "
g1 = "That kissed "
h1 = "That married "
j1 = "That waked "
p1 = "That kept "
m1 = "This is "
 
str_poem = [a, b, c, d, e, f, g, h, j, p, m]
str_poem1 = [a1, b1, c1, d1, e1, f1, g1, h1, j1, p1, m1]

'''
#cначала не увидела, что там меняется текст
k = 1
for i in str_poem:
	while (str_poem.index(i))<=k and k<=len(str_poem):
		poem = '\n'.join((str_poem[0:k]))
		print (f"{poem}\n\n")
		k = k+1
	break
'''
print(f"{m1}{a}\n\n{m1}{b}\n{a1}{a}\n\n{m1}{c}\n{b1}{b}\n{a1}{a}\n\n\
{m1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n\
{a1}{a}\n\n{m1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{g}\n\
{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{h}\n{g1}{g}\n\
{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{j}\n{h1}{h}\n\
{g1}{g}\n{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{p}\n\
{j1}{j}\n{h1}{h}\n{g1}{g}\n{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n\
{a1}{a}\n\n{m1}{m}\n{p1}{p}\n{j1}{j}\n{h1}{h}\n{g1}{g}\n{f1}{f}\n{e1}{e}\n\
{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}")
		
	
