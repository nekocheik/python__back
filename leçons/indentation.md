## INDENTATION IN PYTHON
The indentation white a language python is important!
It enables to scoop the code in `if` or `for` or`while`.

### Multi-line statement

In python, end of statement is marked by a newline character.
But we can make a statement extend over multiple lines with the line continuation character (\). For example:

>     1.  `a =  1  +  2  +  3  + \`
>     2.  `4  +  5  +  6  + \`
>     3.  `7  +  8  +  9`
This is explicit line continuation. In Python, line continuation is implied inside parentheses ( ), brackets [ ] and braces { }. For instance, we can implement the above multi-line statement as
> 
>     1.  `a =  (1  +  2  +  3  +`
>     2.  `4  +  5  +  6  +`
>     3.  `7  +  8  +  9)`

Here, the surrounding parentheses ( ) do the line continuation implicitly. Same is the case with [ ] and { }. For example:

>     > 1.  `colors =  ['red',`
>     > 2.  `'blue',`
>     > 3.  `'green']`

We could also put multiple statements in a single line using semicolons, as follows  

>  `a =  1; b =  2; c =  3`
