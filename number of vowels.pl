% Check if a character is a vowel


2	+
is_vowel(a).
3	+
is_vowel(e).
4	+
is_vowel(i).
5	+
is_vowel(o).
6	+
is_vowel(u).
7	+
8	+
% Base case: empty list has 0 vowels
9	+
count_vowels([], 0).
10	+
11	+
% If head is a vowel, increment count
12	+
count_vowels([H|T], Count) :-
13	+
    is_vowel(H),
14	+
    count_vowels(T, RestCount),
15	+
    Count is RestCount + 1.
16	+
17	+
% If head is not a vowel, do not increment
18	+
count_vowels([H|T], Count) :-
19	+
    \+ is_vowel(H),
20	+
    count_vowels(T, Count).
