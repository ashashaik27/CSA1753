goal(X) :- rule(X).
rule(c) :- rule(b).
rule(b) :- fact(a).
fact(a).
