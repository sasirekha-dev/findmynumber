------------------------------------------------
knightMove_schroders_test.py
------------------------------------------------
Introduction
------------
Problem:
------------------- 
| A |B  |C  |D  |E |
-------------------
| F |G  |H  |I  |J |
-------------------
| K |L  |M  |N  |O |
-------------------
    |1  |2  |3 |
    ------------

Given the above keypad find all 10 key sequences that can be keyed in given the following
constraints:
1. The initial keypress can be any key.
2. Each subsequent keypress must be a knight move from the previous key.
3. There can be at most 2 vowels in the sequence.

Requirments:
------------
Python - 3.10

testing framework - unittest ( builtin)

Runtime guide:
--------------
Please enter the length of sequence expected. 

Testing:
--------
Unit tested with following combinations done
 keypress    sequence length    vowelsAllowed
   1               1                2
   A               2                2
   A               2                0
   A               3                1
 All keypress      1                2
 All keypress      2                2
 All keypress      3                2
 All keypress      4                2