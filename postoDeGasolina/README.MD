# [Posto de Gasolina](https://leetcode.com/problems/gas-station/)

**Dificuldade: Médio**

Existem npostos de gasolina ao longo de uma rota circular, onde a quantidade de gasolina no posto é .ithgas[i]

Você tem um carro com um tanque de gasolina ilimitado e custa cost[i]gasolina para viajar do posto até o próximo posto. Você começa a jornada com o tanque vazio em um dos postos de gasolina.ith(i + 1)th

Dadas duas matrizes inteiras gase cost, retorne o índice do posto de gasolina inicial se você puder percorrer o circuito uma vez no sentido horário, caso contrário, retorne -1 . Se existe uma solução, é garantido que ela seja única


**Exemplo 1:**

``` bash
Entrada: gás = [1,2,3,4,5], custo = [3,4,5,1,2]
 Saída: 3
 Explicação:
Comece na estação 3 (índice 3) e encha com 4 unidades de gás. Seu tanque = 0 + 4 = 4
Viaje para a estação 4. Seu tanque = 4 - 1 + 5 = 8
Viaje para a estação 0. Seu tanque = 8 - 2 + 1 = 7
Viaje para a estação 1. Seu tanque = 7 - 3 + 2 = 6
Viaje para a estação 2. Seu tanque = 6 - 4 + 3 = 5
Viaje até o posto 3. O custo é 5. Seu combustível é suficiente para voltar ao posto 3.
Portanto, retorne 3 como o índice inicial.
```````

**Exemplo 2:**

``` bash
Entrada: gás = [2,3,4], custo = [3,4,3]
 Saída: -1
 Explicação:
Você não pode começar na estação 0 ou 1, pois não há combustível suficiente para ir até a próxima estação.
Vamos começar no posto 2 e abastecer com 4 unidades de gasolina. Seu tanque = 0 + 4 = 4
Viaje para a estação 0. Seu tanque = 4 - 3 + 2 = 3
Viaje para a estação 1. Seu tanque = 3 - 3 + 3 = 3
Você não pode voltar ao posto 2, pois requer 4 unidades de gás, mas você só tem 3.
Portanto, você não pode percorrer o circuito uma vez, não importa onde comece.
```

**Restrições**

n == gas.length == cost.length 

1 <= n <= 105

0 <= gas[i], cost[i] <= 104
