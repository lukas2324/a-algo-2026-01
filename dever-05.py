import math

def master_theorem(a, b, f_exp):
    log_b_a = math.log(a, b)
    
    if log_b_a > f_exp:
        return f"O(n^{log_b_a:.2f})"
    elif math.isclose(log_b_a, f_exp):
        return f"O(n^{f_exp} * log n)"
    else:
        return f"O(n^{f_exp})"

recorrencias = [
    {"label": "T(n) = 2T(n/4) + sqrt(n)", "a": 2, "b": 4, "exp": 0.5},
    {"label": "T(n) = 2T(n/4) + n",       "a": 2, "b": 4, "exp": 1.0},
    {"label": "T(n) = 16T(n/4) + n^2",   "a": 16, "b": 4, "exp": 2.0}
]

print("### Resolução das Recorrências ###\n")
for rec in recorrencias:
    resultado = master_theorem(rec["a"], rec["b"], rec["exp"])
    print(f"{rec['label']}  =>  Complexidade: {resultado}")