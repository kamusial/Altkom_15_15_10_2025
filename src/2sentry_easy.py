import sentry_sdk
import logging
from sentry_sdk import capture_message, capture_exception, configure_scope

sentry_sdk.init(
    dsn="https://216ddf0e5fbc256481ab5a53d2d747a7@o4510200615993344.ingest.de.sentry.io/4510203931000912",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    traces_sample_rate=1.0,
    environment="development",
    release="1.0.0",
)

def simulate_user_error(user_id):
    with sentry_sdk.configure_scope() as scope:
        scope.set_user({'id': user_id, 'email': f'user{user_id}@firma.com'})
        scope.set_tag('feature', 'user_operations')

    try:
        if user_id == 999:
            raise ValueError("Celowy błąd użytkownika 999")
        data = {'user_id': user_id}
        print(data['nieistniejący_klucz'])
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print(f'Błąd wysłany do Sentry: {e}')

def simulate_performance_issue():
    print('Symulacja problemu z wydajnością')
    import time
    start_time = time.time()

    result = 0
    for i in range(1000000):
        result += i*i

    end_time = time.time()
    duration = end_time - start_time

    if duration > 0.1:
        capture_message(f'Operacja za długa: {duration:.2f}s', level='warning')


def main():
    print('Test SENTRY')
    print("=" * 50)

    for user_id in [123, 565, 999, 467]:
        simulate_user_error(user_id)

    simulate_performance_issue()

    print("\n"+"=" * 50)

if __name__ == '__main__':
    main()