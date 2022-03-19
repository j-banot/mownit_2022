# Zestaw 1 - Arytmetyka komputerowa

## Zadania
1. Napisać program liczący kolejne wyrazy ciągu:
x{n+1}= x{n} + 3.0 * x{n} * (1 - x{n})
startując z punktu x{0} = 0.01. Wykonać to zadanie dla różnych reprezentacji liczb (float, double). Dlaczego wyniki się rozbiegają?
Uwaga: Nalezy wprowadzić zmienne pomocnicze, aby uniknąć obliczeć w rejestrach procesora.

2. Napisać program liczący ciąg z wcześniejszego zadania, ale wg wzoru:
x{n+1} = 4.0 * x{n} - 3.0 * x{n} * x{n}
- porównać z wynikami z wcześniejszego zadania.

3. Znaleźć "maszynowe epsilon", czyli najmniejszą liczbę a, taką że a+1>1