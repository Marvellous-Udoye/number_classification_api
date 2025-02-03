from django.http import JsonResponse
import requests

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, abs(n)) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    return n == sum(d ** len(digits) for d in digits)

def classify_number(request):
    number = request.GET.get('number', None)
    if number is None or not number.lstrip('-').isdigit():
        return JsonResponse({"number": number, "error": True}, status=400)

    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")

    response = requests.get(f'http://numbersapi.com/{number}/math?json')
    fun_fact = response.json().get('text', '')

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": fun_fact
    }
    return JsonResponse(result)

def custom_404(request, exception):
    return JsonResponse({'error': 'Not found'}, status=404)