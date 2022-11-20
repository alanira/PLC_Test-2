Description of programming language:

a)

tokens = ['NUMBER','ID','LBRACE','RBRACE','SEMI','PLUS','MINUS','TIMES','DIV','MOD', 'LESS', 'GREAT', 'LESSE', 'GREATE'] + \
  list(keywords.values())

keywords = { 'loop': 'LOOP', 'either': 'EITHER', 'or':'OR',
            'ant':'ANT', 'begin':'BEGIN', 'end':'END'} 

Expressed in Regular expressions:

- t_LBRACE = r'\('
- t_RBRACE = r'\)'
- t_SEMI = r';'
- t_PLUS = r'\+'
- t_MINUS = r'-'
- t_TIMES = r'\*'
- t_DIV = r'/'
- t_MOD = r'\%'
- t_LESS = r'<'
- t_GREAT = r'>'
- t_LESSE = r'<='
- t_GREATE = r'>='
- t_EQUAL = r'=='
- t_NEQUAL = r'!='
- t_ASSIGN = r'='
- t_NUMBER = r'([0-9]*\$1)|([0-9]*\$2)|([0-9]*\$4)|([0-9]*\$8)'
- t_ID = r'[a-zA-Z_]{6,8}'
- t_LOOP = r'[l][o][o][p]'
- t_EITHER = r'[e][i][t][h][e][r]'
- t_OR = r'[o][r]'
- t_ANT = r'[a][n][t]'
- t_BEGIN = r'[b][e][g][i][n]'
- t_END = r'[e][n][d]'

b) Grammar

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
c) Show whether every rule set in your language conforms to the standard of an LL Grammar (should pass pairwise disjoint test, no lefthand recursion).

Answer: I do not think so.

Pairwise disjoint test: 

```
1)	<program> -> begin <stmt_list> end
  yes
2)	<stmt_list> -> <stmt>
			| <stmt> ; <stmt_list>

<stmt_list> -> {stmt} | {<stmt> ; <stmt_list>}
  yes
3)	<stmt> -> <either_or>; | <loop>; | <declaration>; | <assignment>;
  yes
4)	<either_or> ->  either (<expr>) <stmt>
 			| either (<expr>) <stmt> or <stmt>

  <either_or> -> {either} | {either}
  no
5)	<loop> -> loop (<expr>) <stmt_list>
  yes
6)	<declaration> -> ant <ID>
  yes
7)	<assignment> -> <ID> = <expr>
  yes
8)	<expr> -> | <expr> == <term1> | <expr> != <term1> | <expr> < <term1> | <expr> <= <term1> | <expr> > <term1> |  <expr> >= <term1> | <term1>
  no, <expr> -> <expr>  
9)	<term1> -> <term1> - <term2> | <term2>
  no, <term1> -> <term1> lefthand recursion
10)	<term2> -> <term2> + <term3> | <term3>
  no, <term2> -> <term2> lefthand recursion
11)	<term3> -> <term3> / <term4> | <term3> % <term4> | <term4>
  no, <term3> -> <term3> lefthand recursion
12)	<term4> -> <term4> * <factor> | <factor>
  no, <term4> -> <term4> lefthand recursion
13)	<factor> -> (<expr>) | <var>
  yes
14)	<var> -> <ID> | <NUMBER>
  yes

```
Lefthand recursion:

Answer: Yes, for the following rules:

```
8) <expr> -> | <expr> == <term1> | <expr> != <term1> | <expr> < <term1> | <expr> <= <term1> | <expr> > <term1> |  <expr> >= <term1> | <term1>
9) <term1> -> <term1> - <term2> | <term2>
10) <term2> -> <term2> + <term3> | <term3>
11) <term3> -> <term3> / <term4> | <term3> % <term4> | <term4>
12) <term4> -> <term4> * <factor> | <factor>

```
Is it ambiguous grammar? No

Aaaaaa = bbbbbb * (aaaaaa – cccccc)
```

Program => begin <stmt_list> end , rule 1

 => begin <stmt_list> end , rule 2

 => begin <stmt> end , rule 3

 => begin <assign> end , rule 7

 => begin <ID> = <expr> end , rule 14

 => begin Aaaaaa = <expr> end , rule 8

 => begin Aaaaaa = <term1> end , rule 9

 => begin Aaaaaa = <term2> end , rule 10

 => begin Aaaaaa = <term3> end , rule 11

 => begin Aaaaaa = <term4> end , rule 12

 => begin Aaaaaa = <term4> * <factor> end , rule 12

 => begin Aaaaaa = <factor> * <factor> end , rule 13

 => begin Aaaaaa = <var> * <factor> end , rule 13, 14

 => begin Aaaaaa = <ID> * (<expr>) end , rule 8, 14 

 => begin Aaaaaa = bbbbbb * (<term1>) end , rule 9 

 => begin Aaaaaa = bbbbbb * (<term1> – <term2>) end , rule 9 

 => begin Aaaaaa = bbbbbb * (<term2> – <term2>) end , rule 10

 => begin Aaaaaa = bbbbbb * (<term3> – <term2>) end , rule 10, 11 
	
 => begin Aaaaaa = bbbbbb * (<term4> – <term3>) end , rule 11, 12 

 => begin Aaaaaa = bbbbbb * (<factor> – <term4>) end , rule 11, 12 

 => begin Aaaaaa = bbbbbb * (<var> – <factor>) end , rule 12, 13 

 => begin Aaaaaa = bbbbbb * (<ID> – <var>) end , rule 12, 13 

 => begin Aaaaaa = bbbbbb * (aaaaaa – <ID>) end , rule 14 

 => begin Aaaaaa = bbbbbb * (aaaaaa – cccccc) end 
```
Rules for RL parser

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



