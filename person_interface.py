from abc import ABC, abstractmethod


class PersonInterface(ABC):
    """Interface defining the contract for Person objects."""

    score: int = 0
    
    @abstractmethod
    def get_first_name(self) -> str:
        """Get the first name."""
        pass
    
    @abstractmethod
    def set_first_name(self, first_name: str) -> None:
        """Set the first name."""
        pass
    
    @abstractmethod
    def get_last_name(self) -> str:
        """Get the last name."""
        pass
    
    @abstractmethod
    def set_last_name(self, last_name: str) -> None:
        """Set the last name."""
        pass
    
    @abstractmethod
    def get_age(self) -> int:
        """Get the age."""
        pass
    
    @abstractmethod
    def set_age(self, age: int) -> None:
        """Set the age."""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Return string representation."""
        pass

    def display_score(self) -> None:
        print(f"Score: {self.score}")
