"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():

	a = "the house that Jack built."
	b = "the malt" 
	c = "the rat,"
	d = "the cat,"
	e = "the dog,"
	f = "the cow with the crumpled horn,"
	g = "the maiden all forlorn,"
	h = "the man all tattered and torn,"
	j = "the priest all shaven and shorn,"
	p = "the cock that crowed in the morn,"
	m = "the farmer sowing his corn," 

	a1 = "That lay in "
	b1 = "That ate "
	c1 = "That killed "
	d1 = "That worried "
	e1 = "That tossed "
	f1 = "That milked "
	g1 = "That kissed "
	h1 = "That married "
	j1 = "That waked "
	p1 = "That kept "
	m1 = "This is "
	 
	str_poem = [a, b, c, d, e, f, g, h, j, p, m]
	str_poem1 = [a1, b1, c1, d1, e1, f1, g1, h1, j1, p1, m1]

	
	return(f"{m1}{a}\n\n{m1}{b}\n{a1}{a}\n\n{m1}{c}\n{b1}{b}\n{a1}{a}\n\n\
{m1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n\
{a1}{a}\n\n{m1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{g}\n\
{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{h}\n{g1}{g}\n\
{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{j}\n{h1}{h}\n\
{g1}{g}\n{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n\n{m1}{p}\n\
{j1}{j}\n{h1}{h}\n{g1}{g}\n{f1}{f}\n{e1}{e}\n{d1}{d}\n{c1}{c}\n{b1}{b}\n\
{a1}{a}\n\n{m1}{m}\n{p1}{p}\n{j1}{j}\n{h1}{h}\n{g1}{g}\n{f1}{f}\n{e1}{e}\n\
{d1}{d}\n{c1}{c}\n{b1}{b}\n{a1}{a}\n")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
