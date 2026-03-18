def eh_palindromo(arr):
    if len(arr) <= 1:
        return True
    
    if arr[0] == arr[-1]:
        return eh_palindromo(arr[1:-1])
    
    return False

testes = [
    [0, 1, 2, 3, 2, 1, 0],
    ["R", "A", "D", "A", "R"],
    [10, 20, 30, 10],
    ["P", "Y", "T", "H", "O", "N"],
]

for t in testes:
    print(f"O array {t} é palíndromo? {eh_palindromo(t)}")