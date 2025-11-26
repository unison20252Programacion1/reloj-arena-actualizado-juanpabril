# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    for i in range(1,m+1):
        print((i-1)*" ", end="")
        print((2*(m-i+1)-1)*s)

    for i in range(1,m):
        ind = (m-i)
        print((ind-1)*" ", end="")
        print((2*(m-ind+1)-1)*s)
        
        
