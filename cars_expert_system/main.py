from cars_expert_system.expert_logic import CarValueExpertSystem, Car, CarValue
from cars_expert_system.fuzzy_logic import FuzzyLogic


def main(car_data):
    print(f"Running expert system for car data: {car_data}")

    fuzzy_logic = FuzzyLogic()
    car_value = fuzzy_logic.compute_car_value(car_data["year"], car_data["mileage"])

    year_category = "new" if car_value > 75 else "medium" if car_value > 50 else "old"
    mileage_category = (
        "low" if car_value > 75 else "medium" if car_value > 50 else "high"
    )

    engine = CarValueExpertSystem()
    engine.reset()

    engine.declare(
        Car(
            year_category=year_category,
            mileage_category=mileage_category,
            fuel_type=car_data["fuel_type"],
            transmission=car_data["transmission"],
            number_of_owners=car_data["number_of_owners"],
        )
    )

    engine.run()

    print(f"Fuzzy Logic Results: {car_value}")

    for fact in engine.facts.values():
        if isinstance(fact, CarValue):
            print(f"Estimated car value: {fact['value']}")


if __name__ == "__main__":
    data = {
        "year": 2025,
        "mileage": 10000,
        "fuel_type": "diesel",
        "transmission": "automatic",
        "number_of_owners": 1,
    }
    main(data)
