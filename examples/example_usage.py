from payok_aio import Payok


async def main():
    # Замените на реальные значения своих API ID и API Key
    api_id = 123456
    api_key = "your_api_key"

    # Создаем экземпляр класса Payok
    payok_instance = Payok(api_id=api_id, api_key=api_key)

    # Пример использования метода get_balance
    balance_result = await payok_instance.get_balance()
    if balance_result:
        print(f"Баланс: {balance_result.balance}, Реф. баланс: {balance_result.ref_balance}")
    else:
        print("Не удалось получить баланс.")

    # Пример использования метода get_transactions
    transactions_result = await payok_instance.get_transactions()
    if transactions_result:
        if isinstance(transactions_result, list):
            for transaction in transactions_result:
                print(f"Транзакция {transaction.transaction_id}: {transaction.amount} {transaction.currency}")
        else:
            print(f"Транзакция {transactions_result.transaction_id}: {transactions_result.amount} {transactions_result.currency}")
    else:
        print("Не удалось получить транзакции.")

    # Пример использования метода create_pay
    payment_url = await payok_instance.create_pay(
        amount=100.0,
        payment="order123",
        currency="RUB",
        desc="Оплата заказа",
        email="buyer@example.com",
        success_url="https://example.com/success",
        method="card",
        lang="RU",
        custom="custom_data"
    )

    if payment_url:
        print(f"Ссылка для оплаты: {payment_url}")
    else:
        print("Не удалось создать платеж.")
