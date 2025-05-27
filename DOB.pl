% GENDER FACTS
male(john).
male(michael).
male(david).
male(james).
male(robert).

female(mary).
female(susan).
female(linda).
female(elizabeth).

% PARENT RELATIONS
parent(john, michael).
parent(mary, michael).
parent(john, linda).
parent(mary, linda).

parent(michael, david).
parent(susan, david).

parent(michael, elizabeth).
parent(susan, elizabeth).

% RULES

% Father rule
father(X, Y) :-
    male(X),
    parent(X, Y).

% Mother rule
mother(X, Y) :-
    female(X),
    parent(X, Y).

% Sibling rule (excluding self)
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Child rule
child(X, Y) :-
    parent(Y, X).

% Uncle or Aunt
uncle_or_aunt(X, Y) :-
    parent(Z, Y),
    sibling(X, Z).
