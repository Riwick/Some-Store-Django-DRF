import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

DB_NAME = env.get_value("DB_NAME")
DB_HOST = env.get_value("DB_HOST")
DB_PORT = env.get_value("DB_PORT")
DB_USER = env.get_value("DB_USER")
DB_PASS = env.get_value("DB_PASS")
