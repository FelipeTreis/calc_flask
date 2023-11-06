from flask import Flask, request, jsonify

app = Flask(__name__)

# Função para realizar a soma
def add_numbers(a, b):
    return a + b

# Função para realizar a subtração
def subtract_numbers(a, b):
    return a - b

# Função para realizar a multiplicação
def multiply_numbers(a, b):
    return a * b

# Função para realizar a divisão
def divide_numbers(a, b):
    if b == 0:
        return "It's impossible to divide by zero. Try again."
    return a / b

# Function to error 400    
def error_400():
    return jsonify({'error': 'One or more parameters are missing: a, b'}), 400    

# Rota para a soma
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = add_numbers(a, b)
        return jsonify({'result': result})
    else:
        error_400()

# Rota para a subtração
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = subtract_numbers(a, b)
        return jsonify({'result': result})
    else:
        error_400()

# Rota para a multiplicação
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = multiply_numbers(a, b)
        return jsonify({'result': result})
    else:
        error_400()

# Rota para a divisão
@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        result = divide_numbers(a, b)
        return jsonify({'result': result})
    else:
        error_400()

if __name__ == '__main__':
    app.run(debug=True)
