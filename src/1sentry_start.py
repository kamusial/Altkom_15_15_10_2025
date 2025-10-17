import sentry_sdk

sentry_sdk.init(
    dsn="https://216ddf0e5fbc256481ab5a53d2d747a7@o4510200615993344.ingest.de.sentry.io/4510203931000912",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

division_by_zero = 1 / 0
