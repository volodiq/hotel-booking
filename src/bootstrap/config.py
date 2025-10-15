import datetime

import environs


environs.env.read_env()

# Common
is_run_as_service = environs.env.bool("APP_RUN_AS_SERVICE", default=False)
secret_key = environs.env.str("SECRET_KEY")

# DB
db_name = environs.env.str("DB_NAME")
db_user = environs.env.str("DB_USER")
db_password = environs.env.str("DB_PASSWORD")

dbms_port = environs.env.int("DBMS_PORT")
dbms_host = environs.env.str("DBMS_HOST") if is_run_as_service else "localhost"

dbms = "postgresql"
dbms_driver = "asyncpg"
db_dsn = f"{dbms}+{dbms_driver}://{db_user}:{db_password}@{dbms_host}:{dbms_port}/{db_name}"

# Auth
access_token_ttl = datetime.timedelta(hours=1)
refresh_token_ttl = datetime.timedelta(weeks=1)
