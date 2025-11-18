def decorador_com_argumentos(func):
    def wrapper(*args, **kwargs) :
        print("Isto roda antes da função executar.")
        resultado = func(*args, **kwargs)
        print("Isto roda depois da função executar.")
        print(f"O resultado foi: {resultado}")
        return resultado
    return wrapper

@decorador_com_argumentos
def soma(a, b):
    return a + b

print(soma(2, 3))