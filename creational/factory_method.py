from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    
    @annotations
    def factory_method(self):
        pass

    def some_opration(self) -> str:
        
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result

class ConcrateCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreator1()

class ConcrateCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreator2()        

class Product(ABC):

    def operation(self) -> str:
        pass

class ConcreteCreator1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteCreator2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())