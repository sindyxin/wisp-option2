from flask import Flask, jsonify
app = Flask(__name__)

# customize error message
@app.errorhandler(404)
def not_found(e):
  error_message = {'invalid_parameters': 'After url "http://127.0.0.1:5000/specialmath/", an integer parameter must be added and no other data type parameters can be added', 'example': 'http://127.0.0.1:5000/specialmath/17'}
  return jsonify(error_message), 404


@app.route('/specialmath/90', methods=['GET'])
def special_math_90() -> str:
  result = special_math_formula(90)
  return jsonify(result)


@app.route('/specialmath/<int:n>', methods=['GET'])
def special_math(n:int) -> str:
  result = special_math_formula(n)
  return jsonify(result)


def special_math_formula(n:int, memo = {}) -> int:
  if n == 0 or n == 1:
    return n
  else:
    if n-1 not in memo:     
      memo[n-1] = special_math_formula(n-1,memo)

    if n-2 not in memo:
      memo[n-2] = special_math_formula(n-2,memo)

  result = n + int(memo[n-1]) + int(memo[n-2])
  return result

if __name__ == '__main__':
  app.run(debug=True, port=5000)