# Verson API
API where companies can manage their products and orders.

## How to run the porject:

First clone the repository:

```$ git clone https://github.com/joaosr/verso_api.git```

```$ cd verso_api```

Create the local environment:

```$ python -m venv venv```

```$ source venv/bin/activate```

Install the dependencies:

```$ pip install -r requirements.txt```

Run the migrations:

```$ python manage.py migrate```

Run the tests:

```$ python manage.py test```

## Data structures diagram

Based on the task description, I'm considering that an Order has a quantity of the same product from one supplier. 

For simplicity, I'm keeping the supplier name as an attribute in the Order table, and an Order can have many items (quantity attribute) of the same product.

<img width="700" alt="Screenshot 2025-05-09 at 14 43 34" src="https://github.com/user-attachments/assets/5e3cfde6-1b08-44f2-8066-7f03b35cb835" />

### Improvements
There are two changes that I can see as potential improvements, but are out of the escope of the task:

- Allow an Order to contain different products
- Move supplier to a separete table connected with Product table