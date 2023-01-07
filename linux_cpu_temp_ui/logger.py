import atexit
import logging


class Logger:
    """
    Inherit from this class to get logging like this:
    ```
    self.log("My text")
    ```
    """

    logging.basicConfig(
        filename="logs.txt",
        encoding="utf-8",
        format="%(asctime)s -- %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        level=logging.INFO,
    )

    def __init_subclass__(cls):
        Logger.log(f"Class {cls.__name__} got declared on code.")
        super().__init_subclass__()

    @staticmethod
    def log(text: str) -> None:
        logging.info(text)

    @staticmethod
    @atexit.register
    def exit() -> None:
        Logger.log("The program ended.")
