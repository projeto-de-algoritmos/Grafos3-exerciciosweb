# [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

**Dificuldade: Difícil**

Dada uma string de entrada ( s) e um padrão ( p), implemente correspondência de padrão curinga com suporte para '?'e '*'onde:

 '?'Corresponde a qualquer caractere único.

'*'Corresponde a qualquer sequência de caracteres (incluindo a sequência vazia).

A correspondência deve abranger toda a string de entrada (não parcial).

 


**Exemplo 1:**

``` bash
Entrada: s = "aa", p = "a"
 Saída: false
 Explicação: "a" não corresponde à string inteira "aa".
```````

**Exemplo 2:**

``` bash
Entrada: s = "aa", p = "*"
 Saída: verdadeiro
 Explicação:  '*' corresponde a qualquer sequência.
```


**Exemplo 3:**

``` bash
Entrada: s = "cb", p = "?a"
 Saída: falso
 Explicação:  '?' corresponde a 'c', mas a segunda letra é 'a', que não corresponde a 'b'.
```


**Restrições**

0 <= s.length, p.length <= 2000

scontém apenas letras minúsculas em inglês.

pcontém apenas letras minúsculas em inglês '?'ou '*'.