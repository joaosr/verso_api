# Verson API
API where companies can manage their products and orders.

## How to run the porject:

First clone the repository:

```$ git clone https://github.com/joaosr/verso_api.git```

```$ cd verso_api```

Create the local environment (Python 3.12):

```$ python -m venv venv```

```$ source venv/bin/activate```

Install the dependencies:

```$ pip install -r requirements.txt```

Run the migrations:

```$ python manage.py migrate```

Run the tests:

```$ python manage.py test```

Run local server:

```$ python manage.py runserver```

Local API docs:

http://127.0.0.1:8000/api/schema/redoc/

## Data structures diagram

Based on the task description, I'm considering that an Order has a quantity of the same product from one supplier. 

For simplicity, I'm keeping the supplier name as an attribute in the Order table, and an Order can have many items (quantity attribute) of the same product.

<img width="741" alt="Screenshot 2025-05-09 at 21 53 10" src="https://github.com/user-attachments/assets/276f1cc3-fb70-4803-a457-c424c0531d87" />

### Improvements
There are two changes that I can see as potential improvements, but are out of the escope of the task:

- Allow an Order to contain different products
- Move supplier to a separete table connected with Product table
