import os
from colorama import Fore, Style
# Arte ASCII principal
print("""
Aquí pon el arte
""")

# Arte ASCII que dice "1882"
print(Fore.RED+"""
 ,-----.--.  ,---.--.   ,---.--.  ,-----,--,   
/` ` - /==/ /  -_ \==\ /  -_ \==\ | '-  -\==\  
`-'-. -|==| |` / \/==/ |` / \/==/ \,--, '/==/  
    | `|==|  \ \ /==/   \ \ /==/     /  /==/   
    | -|==|  /  \==/    /  \==/     / -/==/    
    | `|==| /. / \==\  /. / \==\   / -/==/     
  .-','|==|| _ \_/\==\| _ \_/\==\ / `\==\_,--, 
 /     \==\\ . -  /==/\ . -  /==//` -   ,/==/  
 `-----`---`'----`--`  '----`--` `------`--`   
"""+Style.RESET_ALL)

# Menú de opciones
opciones = {
    "1": "airgeddon.sh",
    "2": "script2.py",
    "3": "script3.py",
    "4": "script4.py",
    "5": "script5.py",
}

while True:
    print("\nMenú de opciones:")
    for key, value in opciones.items():
        print(f"{key}. Ejecutar {value}")

    seleccion = input("\nSelecciona una opción (1-5) o 'q' para salir: ")

    if seleccion == "q":
        print("Saliendo...")
        os.wait(100)
        break
    elif seleccion in opciones:
        archivo = opciones[seleccion]
        if os.path.exists(archivo):
            os.system(f"python {archivo}")  # Ejecuta el archivo
        else:
            print(f"Error: {archivo} no existe.")
    else:
        print("Opción no válida, intenta de nuevo.")