T = [ -10, -8, 0, 1, 2, 5, -2, -4]

def temperaturas(T):
    if not T:
        return "Sem nenhuma temperatura."

minima = min(T)
maxima = max(T)
media = sum(T) / len(T)

print(f"Temperatura mínima : {minima}")
print(f"Temperatura máxima : {maxima}")
print(f"Temperatura média : {media:.2f}")