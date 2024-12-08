# GRAPHQL project in Python

This project implements a basic GraphQL server in Python, using Flask and Ariadne, including a graphical interface for querying the API.

## Instructions to run the project
### Prerequisites
1. Make sure you have Docker installed on your machine.
2. Clone this repository to your local machine:

   ```bash
   git clone  https://github.com/alwxav98/EA2GraphQl.git
   cd  EA2GraphQl
   ```

### Using Docker
1. Clone this repository to your local machine.
2. Build the Docker image with the following command:

   ```bash
   docker build -t python-graphql .
   ```

3. Run the container with:

   ```bash
   docker run -d -p 5000:5000 --name graphql-container python-graphql
   ```
4. Access the application in your browser:
- Home page: http://localhost:5000
- API endpoint: http://http://localhost:5000/graphql_ui

5. Trying the API
You can run queries in the graphical interface of /graphql_ui, for example:
   ```graphql
   query {
     hello
   }
   ```
This should return:
```json
   {
    "data": {
      "hello": "Hola desde GraphQL"
    }
   }
    ```
