# Specification Document for Insect Language

Grammar describes the grammars used in this specification to define the lexical and syntactic structure of a program:


Grammar for an Insect language with 6 levels of precedence:

```

1)	<program> -> begin <stmt_list> end
2)	<stmt_list> -> <stmt> ;
			| <stmt> ; <stmt_list>
3)	<stmt> -> <either_or>; | <loop>; | <declaration>; | <assignment>;
4)	<either_or> ->  either (<expr>) <stmt>
 			| either (<expr>) <stmt> or <stmt>
5)	<loop> -> loop (<expr>) <stmt>
6)	<declaration> -> ant <ID>
7)	<assignment> -> <ID> = <expr>
8)	<expr> -> | <expr> == <term1> | <expr> != <term1> | <expr> < <term1> | < expr > <= <term1> | <expr> > <term1> |  <expr> >= <term1> | <term1>
9)	<term1> -> <term1> - <term2> | <term2>
10)	<term2> -> <term2> + <term3> | <term3>
11)	<term3> -> <term3> / <term4> | <term3> % <term4> | <term4>
12)	<term4> -> <term4> * <factor> | <factor>
13)	<factor> -> (<expr>) | <var>
14)	<var> -> <ID> | <NUMBER>

```
## Keywords:

9 character sequences, formed from ASCII characters, are reserved for use as keywords and cannot be used as identifiers (3).
ReservedKeyword:

1. begin
   - defines the beginning of the program
2. loop
   - defines the loop structure 
3. either
   - defines the beginning of the conditional statement
4. or
   - defines the extension of the conditional statement
5. ant
   - defines integer literal
6. bee
   - defines boolean literal
7. caterpillar
   - defines string literal
8. fly
   - defines the float literal 
9. end
   - defines the end of the program

true and false are not keywords, but rather boolean literals (2.3)


## Special Symbols:

1. (
   - defines the beginning of the separation of the expression in conditional statement and loop structure
   - defines the beginning of the highest order of the procedure in the expression
2. )
   - defines the closing of the separation of the expression in conditional statement and loop structure
   - defines the closing of the highest order of the procedure in the expression
3. ;
   - defines the termination symbol of the statement in a program

## Literals

2.1 IntegerLiterals

An integer literal may be expressed as regular expression:
```
'([0-9]*\$1)|([0-9]*\$2)|([0-9]*\$4)|([0-9]*\$8)'
```
Number after symbol $ defines how integer literal is saved in memory as one byte, two bytes, four bytes or eight bytes e.g., $1, $2, $3, $4.

2.2 FloatLiterals

A floating-point literal has the following parts: a whole-number part, a decimal point (represented by an ASCII period character), a fraction part.

Float literal may be expressed as regular expression:
```
'[0-9]+.[0-9]+'
```

2.3 BooleanLiterals

The boolean type has two values, represented by the boolean literals true and false, formed from ASCII letters.

Boolean literal may be expressed as regular expression:
```
'(true)|(false)'
```

2.4 StringLiterals

A string literal consists of zero or more characters enclosed in double quotes. Characters such as a quote may be represented by backslash and a quote inside enclosed double quotes.

String literal may be expressed as regular expression:
```
'"[^"]*"'
```
## Identifiers

An identifier is a limited-length sequence of 6-8 letters and cannot contain digits, but may contain underscore(s).

Identifier may be expressed as regular expression:
```
r'[a-zA-Z_]{6,8}'
```
An identifier cannot have the same spelling (Unicode character sequence) as a keyword (1) or boolean literal (2.3)

## Operators

12 tokens, formed from ASCII characters, are the operators:
```
1. =
2. ==
3. +
4. -
5. *
6. /
7. %
8. <
9. >
10. <=
11. >=
12. !=
```
## Data types and values

A data type is predefined by the Insect programming language and named by its reserved keyword (1):
- ant
- bee
- fly
- caterpillar

The numeric types are the integral types and the floating-point types.

The integral type is ant, whose values are 8-bit, 16-bit, 32-bit and 64-bit signed two's-complement integers.

Number after symbol $ defines how integer literal (2.1) is saved in memory as on 1-byte, 2-bytes, 4-bytes or 8-bytes e.g., $1, $2, $3, $4.

The values of the integral type are integers in the following ranges:
- For $1, from -128 to 127, inclusive
- For $2, from -32768 to 32767, inclusive
- For $4, from -2147483648 to 2147483647, inclusive
- For $8, from -9223372036854775808 to 9223372036854775807, inclusive

The floating-point type is fly, whose values include the floating-point numbers.
The bee type has exactly two values: true and false.
The caterpillar type is an arbitrarily long sequence of characters enclosed in double quotes (“). Backslash with a single quote may be used to insert a single quote in a sequence of characters enclosed in double quotes


## How to write a program?

### The base rule for that is
```
<program> -> begin <stmt_list> end
```

### Any program written in Insect language should start from the begin, <stmt_list> and closed with end.
```
<stmt_list> is explained by the following rule:

<stmt_list> -> <stmt> ;
		| <stmt> ; <stmt_list>
```
Statement <stmt> in Insect language can be a conditional statement <either_or>, loop structure <loop>, declaration of a variable <declaration> or assignment of a variable <assignment>:
```
<stmt> -> <either_or>; | <loop>; | <declaration>; | <assignment>;
```

### Conditional statement <either_or> is possible in two variations:
```
1. <either_or> ->  either (<expr>) <stmt>
Keyword either, expression <expr> of type bee that evaluates to true or false, statement <stmt>. If expression <expr> evaluates true, then <stmt> will be executed.

2. <either_or> -> either (<expr>) <stmt> or <stmt>
```
Keyword either, expression <expr> of type bee that evaluates to true or false, statement <stmt1>, keyword or statement <stmt2>. If expression <expr> evaluates true, then <stmt1> will be executed, else <stmt2> will be executed.

### Insect language allow to create loop structures.

Loop structure is a feature to execute a particular part of the program repeatedly if a given <expr> evaluates to be true.
```
<loop> -> loop (<expr>) <stmt>
```
### Declaration in Insect language:
```
<declaration> -> ant <ID> | bee <ID> | fly <ID> | caterpillar <ID>
```
A declaration introduces an entity into a program and includes an identifier (3) that can be used in a name to refer to this entity.
A declared entity should be declared on separate line and is one of the following:
```
1)	ant <ID>
2)	bee <ID>
3)	fly <ID>
4)	caterpillar <ID>
```
### Assignment in Insect language:

Assignment allows the value of an expression to be assigned to a variable on the separate line; the type of the expression must be converted to the type of the variable.
```
<assignment> -> <ID> = <expr>
```
### Expressions in Insect language

An expression is a construct made up of variables and operators, which are constructed according to the syntax of the Insect language, that evaluates to a single value.

The Insect language has a proper evaluation order, 6 level of precedence, that conforms to the real-life principles of mathematics for in order operations

Relational operators are the lowest precedence 6th level of operations. Expression <expr> evaluates to true or false:
```
<expr> -> | <expr> == <term1> | <expr> != <term1> | <expr> < <term1> | < expr > <= <term1> | <expr> > <term1> |  <expr> >= <term1> | <term1>
```
The 5th level of precedence. Term <term1> opens with term <term1> minus term <term2> or term <term2>:
```
<term1> -> <term1> - <term2> | <term2>
```
The 4th level of precedence. Term <term2> opens with term <term2> plus term <term3> or term <term3>:
```
<term2> -> <term2> + <term3> | <term3>
```
The 3rd level of precedence. Term <term3> opens with term <term3> div term <term4> or term <term3> mod term <term4> or <term4>:
```
<term3> -> <term3> / <term4> | <term3> % <term4> | <term4>
```
The 2nd level of precedence. Term <term4> opens with term <term4> multiplication with factor <factor> or factor <factor>:
```
<term4> -> <term4> * <factor> | <factor>
```
The highest level of precedence. Factor <factor> opens as expression enclosed in round parentheses (<expr>) or variable <var>:
```
<factor> -> (<expr>) | <var>
```
Variable opens as identifier <ID> or number <NUMBER>
```
<var> -> <ID> | <NUMBER>
```
## Description of integral operations

The Insect programming language provides a number of operators that act on integral values:
1. The comparison operators, which result in a value of type bee:
   - The numerical comparison operators <, <=, >, and >=
   - The numerical equality operators == and !=
2. The numerical operators, which result in a value of type ant:
   - The multiplicative operators *, /, and %
   - The additive operators + and -

## Description of floating operations

The Insect programming language provides a number of operators that act on floating values:
1. The comparison operators, which result in a value of type bee:
   - The numerical comparison operators <, <=, >, and >=
   - The numerical equality operators == and !=
2. The numerical operators, which result in a value of type fly:
   - The multiplicative operators *, /, and %
   - The additive operators + and -


https://jsmachines.sourceforge.net/machines/lr1.html

```
program -> begin stmt_list end
stmt_list -> stmt ;
stmt_list -> stmt ; stmt_list
stmt -> either_or
stmt -> cycle
stmt -> declaration
stmt -> assignment
either_or -> either ( expr ) stmt
either_or -> either ( expr ) stmt or stmt
cycle -> loop ( expr ) stmt
declaration -> ant ID
assignment -> ID = expr
expr -> expr == term1
expr -> expr != term1
expr -> expr < term1
expr -> expr <= term1
expr -> expr > term1
expr -> expr >= term1
expr -> expr >= term1
expr -> term1
term1 -> term1 - term2
term1 -> term2
term2 -> term2 + term3
term2 -> term3
term3 -> term3 / term4
term3 -> term3 % term4
term3 -> term4
term4 -> term4 * factor
term4 -> factor
factor -> ( expr )
factor -> var
var -> ID
var -> NUMBER
```
Strings:
```
String 1

begin ID = NUMBER ; end

String 2

begin ant ID ; end

String 3

begin ant ID = NUMBER ; end

String 4

begin loop ( expr ) stmt ; ; end

```



