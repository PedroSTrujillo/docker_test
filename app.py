import os
import math
import sys

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers up to the given limit"""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def print_welcome():
    """Print welcome message and instructions"""
    print("===== CALCULADORA DE NUMEROS PRIMOS =====")
    print("Ejecutandose en Docker")
    print(f"Hostname: {os.getenv('HOSTNAME', 'unknown')}")
    print("=" * 45)
    print()

def print_menu():
    """Print the main menu options"""
    print("MENU PRINCIPAL:")
    print("1. Verificar si un numero es primo")
    print("2. Generar numeros primos hasta un limite")
    print("3. Salir")
    print("-" * 30)

def get_user_input(prompt, input_type=int, min_value=None, max_value=None):
    """Get and validate user input"""
    while True:
        try:
            value = input_type(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Error: El valor debe ser mayor o igual a {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Error: El valor debe ser menor o igual a {max_value}")
                continue
            return value
        except ValueError:
            print(f"Error: Por favor ingresa un valor valido ({input_type.__name__})")
        except KeyboardInterrupt:
            print("\nSaliendo...")
            sys.exit(0)

def check_single_prime():
    """Check if a single number is prime"""
    print("\nVERIFICAR NUMERO PRIMO")
    print("-" * 25)
    
    number = get_user_input("Ingresa un numero entero positivo: ", int, 1)
    
    result = is_prime(number)
    
    print(f"\nRESULTADO:")
    print(f"Numero: {number}")
    if result:
        print(f"Estado: ES PRIMO")
    else:
        print(f"Estado: NO ES PRIMO")
    print()

def generate_primes_menu():
    """Generate prime numbers up to a limit"""
    print("\nGENERAR NUMEROS PRIMOS")
    print("-" * 26)
    
    limit = get_user_input("Ingresa el limite maximo (2-10000): ", int, 2, 10000)
    
    print(f"\nGenerando numeros primos hasta {limit}...")
    primes = generate_primes(limit)
    
    print(f"\nRESULTADOS:")
    print(f"Limite: {limit}")
    print(f"Cantidad de primos: {len(primes)}")
    
    if len(primes) <= 50:
        print(f"Numeros primos: {', '.join(map(str, primes))}")
    else:
        print(f"Primeros 10: {', '.join(map(str, primes[:10]))}")
        print(f"Ultimos 10: {', '.join(map(str, primes[-10:]))}")
        print(f"(Se omitieron {len(primes)-20} numeros)")
    
    print()

def main():
    """Main function - console application entry point"""
    print_welcome()
    
    while True:
        try:
            print_menu()
            choice = get_user_input("Selecciona una opcion (1-3): ", int, 1, 3)
            
            if choice == 1:
                check_single_prime()
            elif choice == 2:
                generate_primes_menu()
            elif choice == 3:
                print("\nGracias por usar la Calculadora de Numeros Primos!")
                print("Saliendo...")
                break
                
            input("Presiona Enter para continuar...")
            print("\n" + "="*45 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nSaliendo...")
            break
        except Exception as e:
            print(f"\nError: {e}")
            input("Presiona Enter para continuar...")

if __name__ == '__main__':
    main()
