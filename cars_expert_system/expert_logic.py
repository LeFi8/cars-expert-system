from experta import Fact, KnowledgeEngine, Rule, AND, W


# Define facts
class Car(Fact):
    """Represents a car and its attributes."""

    pass


class CarValue(Fact):
    """Represents the value of a car."""

    pass


class CarValueExpertSystem(KnowledgeEngine):
    @Rule(AND(Car(year_category="new"), Car(mileage_category="low")))
    def rule_high_value(self):
        """If the car is new and has low mileage, its value is high."""
        self.declare(CarValue(value="high based on year and mileage"))

    @Rule(AND(Car(year_category="medium"), Car(mileage_category="medium")))
    def rule_medium_value(self):
        """If the car is medium-aged and has medium mileage, its value is medium."""
        self.declare(CarValue(value="medium based on year and mileage"))

    @Rule(AND(Car(year_category="old"), Car(mileage_category="high")))
    def rule_low_value(self):
        """If the car is old and has high mileage, its value is low."""
        self.declare(CarValue(value="low based on year and mileage"))

    @Rule(AND(Car(fuel_type="diesel"), Car(transmission="automatic")))
    def rule_diesel_automatic(self):
        """If the car has a diesel engine and automatic transmission, its value is higher than medium."""
        self.declare(
            CarValue(value="higher than medium based on fuel type and transmission")
        )

    @Rule(AND(Car(number_of_owners=W(lambda x: x > 2)), Car(mileage_category="high")))
    def rule_multiple_owners_high_mileage(self):
        """If the car has had more than 2 owners and high mileage, its value is lower than medium."""
        self.declare(
            CarValue(value="lower than medium based on number of owners and mileage")
        )

    @Rule(AND(Car(year_category="new"), Car(fuel_type="diesel")))
    def rule_new_diesel(self):
        """If the car is new and has a diesel engine, its value is higher than medium."""
        self.declare(CarValue(value="higher than medium based on year and fuel type"))

    @Rule(AND(Car(year_category="new"), Car(fuel_type="petrol")))
    def rule_new_petrol(self):
        """If the car is new and has a petrol engine, its value is lower than medium."""
        self.declare(CarValue(value="lower than medium based on year and fuel type"))

    @Rule(AND(Car(year_category="new"), Car(transmission="automatic")))
    def rule_new_automatic(self):
        """If the car is new and has automatic transmission, its value is higher than medium."""
        self.declare(
            CarValue(value="higher than medium based on year and transmission")
        )

    @Rule(AND(Car(year_category="new"), Car(number_of_owners=W(lambda x: x > 1))))
    def rule_new_multiple_owners(self):
        """If the car is new and has had more than 1 owner, its value is lower than medium."""
        self.declare(
            CarValue(value="lower than medium based on year and number of owners")
        )

    @Rule(AND(Car(year_category="new"), Car(mileage_category="high")))
    def rule_new_high_mileage(self):
        """If the car is new and has high mileage, its value is lower than medium."""
        self.declare(CarValue(value="lower than medium based on year and mileage"))

    @Rule(AND(Car(year_category="old"), Car(fuel_type="diesel")))
    def rule_old_diesel(self):
        """If the car is old and has a diesel engine, its value is higher than medium."""
        self.declare(CarValue(value="higher than medium based on year and fuel type"))

    @Rule(AND(Car(year_category="old"), Car(transmission="automatic")))
    def rule_old_automatic(self):
        """If the car is old and has automatic transmission, its value is higher than medium."""
        self.declare(
            CarValue(value="higher than medium based on year and transmission")
        )

    @Rule(AND(Car(year_category="old"), Car(number_of_owners=W(lambda x: x > 1))))
    def rule_old_multiple_owners(self):
        """If the car is old and has had more than 1 owner, its value is lower than medium."""
        self.declare(
            CarValue(value="lower than medium based on year and number of owners")
        )
