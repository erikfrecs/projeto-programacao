# projeto-programacao
CentralRecursivaRobusta

Erik Alves de Sousa - 26.1.19172

Fernando Lemke da Silveira - 26.1.18620

Descrição do projeto

O projeto é uma aplicação que realiza duas operações matemáticas usando recursividade. A primeira calcula o Máximo Divisor Comum (MDC) entre dois números e a segunda calcula a soma dos dígitos de um número. O programa também verifica quando a operação ou os valores informados são inválidos.

Instruções para execução

Para executar o projeto é necessário ter o Python instalado.

Depois, basta abrir o arquivo TED2Alex.py e executar o programa. Primeiro é informada a quantidade de operações e depois os dados de cada operação.

Módulos desenvolvidos

O programa foi dividido em algumas funções para organizar melhor o código:

mdc_recursivo: faz o cálculo do MDC.
soma_digitos_recursiva: faz a soma dos dígitos.
processar_linha: verifica os dados informados e realiza a operação.
main: recebe as operações e mostra os resultados.
Algoritmos recursivos
MDC

Para calcular o MDC foi utilizado o algoritmo de Euclides. A função vai chamando ela mesma usando o resto da divisão até chegar ao resultado.

Soma dos dígitos

Nesse cálculo, a função pega o último dígito do número e depois continua com o restante do número, chamando a própria função até terminar.

Exceções personalizadas

Foram utilizadas duas exceções personalizadas:

OperacaoInvalidaError: usada quando é informada uma operação diferente de M ou S.
EntradaInvalidaError: usada quando os valores informados não estão de acordo com as regras da operação.
