% Rules

sum([], 0).
sum([H|T], Sum) :-
    sum(T, Sum1),
    Sum is H + Sum1.


% sum([1, 2, 3, 5, 17, -4], Sum).

% Sum = 24