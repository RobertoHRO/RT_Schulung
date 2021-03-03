https://www.wolframcloud.com/
Values for Symbols

When the Wolfram Language transforms an expression such as x+x into 2x, it is treating the variable x in a purely symbolic or formal fashion. In such cases, x is a symbol that can stand for any expression.

Often, however, you need to replace a symbol like x with a definite "value". Sometimes this value will be a number; often it will be another expression.

To take an expression such as 1+2x and replace the symbol x that appears in it with a definite value, you can create a Wolfram Language transformation rule, and then apply this rule to the expression. To replace x with the value 3, you would create the transformation rule x->3. You must type \-> as a pair of characters, with no space in between. You can think of x->3 as being a rule in which "x goes to 3".

To apply a transformation rule to a particular Wolfram Language expression, you type expr/.rule. The "replacement operator" /. is typed as a pair of characters, with no space in between.

This uses the transformation rule x->3 in the expression 1+2x:

``1 + 2 x /. x -> 3``


remove any value defined for x
`x=.`


- Antwort auf anregung mit Sinus: 
> `OutputResponse[TransferFunctionModel[{{{1}}, 1 + s}, s], Sin[10 t], t]`

## Fahrzeug
- Nach Umformung der folgt so: $$\tfrac{d}{d\,t}v(t)  =- \frac{b}{m}\cdot v(t)+  \frac{F_u}{m}$$