from pyfiguration import conf


@conf.addStringField(
    field="db.host",
    description="Location of the database, e.g. localhost",
    default="localhost",
)
@conf.addIntField(
    field="db.port",
    description="Port of the database to connect on",
    minValue=80,
    maxValue=9999,
    default=8000,
)
def test():
    print("Database host:", conf["db"]["host"])
    print("Database port:", conf["db"]["port"])


if __name__ == "__main__":
    test()
