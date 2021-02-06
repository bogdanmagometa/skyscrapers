# skyscrapers

### Project for checking winning combinations in skyscrapers game.

<br>

<b>skyscrapers</b> project provides their users with the module <a href="https://github.com/bogdanmagometa/skyscrapers/blob/main/skyscrapers.py">skyscrapers.py</a> contatining the function check_skyscrapers(input_path). Import and invoke check_skyscrapers with the argument (list of string) representing a board in order to check if this board is a winning combination.

The board is considered to be a winning combination iff all of the following conditions are satisfied:
<ul>
<li>No two numbers in each row are equal</li>
<li>No two numbers in each column are equal</li>
<li>The number of visible skyscrapers in any direction is equal to the number given in the hint</li>
</ul>

<br>

The example of the board satisfying these conditions:
```
***21**
412453*
423145*
*543215
*35214*
*41532*
*2*1***
```

<br>

The example of the board not satisfying some of the conditions:
```
***21**
4?????*
4?????*
*?????5
*?????*
*?????*
*2*1***
```
