# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import sys

# EXCEÇÕES PERSONALIZADAS
class OperacaoInvalidaError(Exception):
    """Exceção lançada para operações desconhecidas (diferentes de M ou S)."""
    def __init__(self, mensagem="ERRO: OperacaoInvalida"):
        super().__init__(mensagem)


class EntradaInvalidaError(Exception):
    """Exceção lançada para entradas malformadas ou com valores fora dos domínios válidos."""
    def __init__(self, mensagem="ERRO: EntradaInvalida"):
        super().__init__(mensagem)


# ALGORITMOS RECURSIVOS
def mdc_recursivo(a: int, b: int) -> int:
    """Calcula o Máximo Divisor Comum (MDC) utilizando o algoritmo recursivo de Euclides."""
    if b == 0:
        return a
    return mdc_recursivo(b, a % b)


def soma_digitos_recursiva(n: int) -> int:
    """Calcula a soma dos algarismos de um número inteiro de forma recursiva."""
    if n < 10:
        return n
    return (n % 10) + soma_digitos_recursiva(n // 10)

def processar_linha(linha: str) -> str:
    """
    Analisa a linha fornecida, valida os parâmetros e executa a operação.
    Lança exceções personalizadas em caso de entradas ou operações inválidas.
    """
    partes = linha.strip().split()
    if not partes:
        raise EntradaInvalidaError()

    codigo_op = partes[0]

    if codigo_op not in ('M', 'S'):
        raise OperacaoInvalidaError()

    if codigo_op == 'M':
        if len(partes) != 3:
            raise EntradaInvalidaError()
        try:
            a = int(partes[1])
            b = int(partes[2])
        except ValueError:
            raise EntradaInvalidaError()

        if a <= 0 or b <= 0:
            raise EntradaInvalidaError()

        resultado = mdc_recursivo(a, b)
        return f"MDC = {resultado}"

    elif codigo_op == 'S':
        if len(partes) != 2:
            raise EntradaInvalidaError()
        try:
            n = int(partes[1])
        except ValueError:
            raise EntradaInvalidaError()

        if n < 0:
            raise EntradaInvalidaError()

        resultado = soma_digitos_recursiva(n)
        return f"SOMA = {resultado}"


def main():
    try:
        linha_q = sys.stdin.readline()
        if not linha_q:
            return
        q = int(linha_q.strip())
    except ValueError:
        return

    for _ in range(q):
        linha = sys.stdin.readline()
        if not linha:
            break

        try:
            resultado = processar_linha(linha)
            print(resultado)
        except OperacaoInvalidaError as err:
            print(str(err))
        except EntradaInvalidaError as err:
            print(str(err))
        finally:
            # Bloco finallly executado ao fim de cada ciclo de processamento
            pass


if __name__ == "__main__":
    main()