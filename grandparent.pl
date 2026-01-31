parent(john,mary).
parent(john,paul).
parent(mary,anna).

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).
