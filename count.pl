vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).

count([],0).
count([H|T],N) :-
    vowel(H),
    count(T,N1),
    N is N1+1.

count([H|T],N) :-
    \+ vowel(H),
    count(T,N).
