from flask import Flask, request, jsonify, render_template
from ariadne import QueryType, graphql_sync, make_executable_schema

# Definir el esquema GraphQL
type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hola desde GraphQL"

schema = make_executable_schema(type_defs, query)

# Configurar Flask
app = Flask(__name__)

# Ruta para la interfaz de GraphQL usando Ariadne directamente
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    if data:
        success, result = graphql_sync(schema, data, context_value=request, debug=True)
        status_code = 200 if success else 400
        return jsonify(result), status_code
    return "No query provided", 400

# Ruta para la interfaz de GraphQL Playground
@app.route("/graphql_ui", methods=["GET"])
def graphql_playground():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <title>GraphQL Playground</title>
        <link rel="stylesheet" href="https://unpkg.com/graphql-playground-react/build/static/css/index.css" />
        <script src="https://unpkg.com/graphql-playground-react/build/static/js/middleware.js"></script>
    </head>
    <body>
        <div id="root" style="height: 100vh;"></div>
        <script>
            window.addEventListener('load', function () {
                GraphQLPlayground.init(document.getElementById('root'), {
                    endpoint: '/graphql'
                })
            })
        </script>
    </body>
    </html>
    """, 200

# Ruta para la página principal
@app.route('/')
def home():
    return render_template('index.html', ViewData={"Title": "Aplicacion Web 2"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)