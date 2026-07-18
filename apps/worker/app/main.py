import logging


def main() -> None:
    """Worker process placeholder; jobs are introduced by future services."""
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("athena.worker").info("ATHENA worker started")


if __name__ == "__main__":
    main()

