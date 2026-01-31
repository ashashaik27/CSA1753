bestfs(Node,Goal) :-
    Node = Goal,
    write('Goal reached').

bestfs(Node,Goal) :-
    move(Node,Next),
    bestfs(Next,Goal).
