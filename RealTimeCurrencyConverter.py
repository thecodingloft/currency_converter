import requests
import datetime


class RealTimeCurrencyConverter():

    def convert_currencies(amount, currency_1, currency_2):
        base_url = "https://v6.exchangerate-api.com/v6/"
        api_key = "0dcc14bc61d5e00d1cd437da"
        mode = "/latest/"
        currency = f"{currency_1}"
        date = datetime.datetime.today().date()

        full_url = base_url + api_key + mode + currency

        r = requests.get(full_url)
        results = r.json()

        exchange_rate = results["conversion_rates"][f"{currency_2}"]
        converted_amount = round((amount * exchange_rate), 2)
        print(exchange_rate)
        print(converted_amount)
        print(
            f"{date}: {amount} {currency_1} converts to {converted_amount} {currency_2}")
        return exchange_rate, converted_amount

    def convert_pair(currency_1, currency_2):
        base_url = "https://v6.exchangerate-api.com/v6/"
        api_key = "0dcc14bc61d5e00d1cd437da"
        mode = "/pair/"
        currencies = f"{currency_1}/{currency_2}"

        full_url = base_url + api_key + mode + currencies

        r = requests.get(full_url)
        response = r.json()

        exchange_rate = response["conversion_rate"]

        return exchange_rate


if __name__ == "__main__":
    value = RealTimeCurrencyConverter.convert_currencies(10, "USD", "THB")
    print(value[0])

    exchange_rate = RealTimeCurrencyConverter.convert_pair("EUR", "JPY")
    print(exchange_rate)
