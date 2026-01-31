match([X|_],[X|_]).
match([_|T],P) :-
    match(T,P).
