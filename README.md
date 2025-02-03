# HNG Number Classification API

This is a public API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Technology Stack
- Programming Language: Python
- Framework: Django

## Information Returned
- Number properties (prime, perfect, Armstrong, odd/even)
- Digit sum
- Fun fact from Numbers API

## Endpoint
- **GET** `/api/classify-number?number=371`

## Response Format (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

## Response Format (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true
}
```

## Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/Marvellous-Udoye/number_classification_api.git
    cd number_classification_api
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```sh
    python manage.py migrate
    ```

5. Start the server:
    ```sh
    python manage.py runserver
    ```

The API will be accessible at `https://number-classification-api-sspp.onrender.com/api/classify-number?number=371`.

## Example Usage
```sh
curl https://number-classification-api-sspp.onrender.com/api/classify-number?number=371
```

## Project Structure
```
number_classification_api/
├── manage.py
├── number_classification_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
└── README.md
```

## Requirements
- Python 3.6+
- Django 3.2+
- Django REST framework
- django-cors-headers

## Testing the Endpoint
You can test the endpoint using curl or any API testing tool like Postman.

```sh
curl https://number-classification-api-sspp.onrender.com/api/classify-number?number=371
```

This will return the JSON response with the number properties, digit sum, and fun fact.