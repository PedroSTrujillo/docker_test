from flask import Flask, request, jsonify
import os
import math

app = Flask(__name__)

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

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <title>Docker Test App - Prime Calculator</title>
        </head>
        <body>
            <h1>Bienvenido a la aplicación de cálculo de números primos</h1>
            <p>Usa los siguientes endpoints:</p>
            <ul>
                <li><a href="/prime/check/&lt;number&gt;">/prime/check/&lt;number&gt;</a> - Verifica si un número es primo</li>
                <li><a href="/prime/generate/&lt;limit&gt;">/prime/generate/&lt;limit&gt;</a> - Genera números primos hasta un límite</li>
            </ul>
        </body>
    </html>
    """

@app.route('/prime/check/<int:number>')
def check_prime_api(number):
    """API endpoint to check if a number is prime"""
    result = is_prime(number)
    return jsonify({
        'number': number,
        'is_prime': result,
        'message': f'{number} {"es" if result else "no es"} un número primo'
    })

@app.route('/prime/generate/<int:limit>')
def generate_primes_api(limit):
    """API endpoint to generate prime numbers up to a limit"""
    if limit > 10000:
        return jsonify({
            'error': 'El límite no puede ser mayor a 10,000 para evitar sobrecarga del servidor'
        }), 400
    
    primes = generate_primes(limit)
    return jsonify({
        'limit': limit,
        'count': len(primes),
        'primes': primes
    })

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False)
