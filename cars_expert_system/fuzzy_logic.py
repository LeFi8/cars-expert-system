import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyLogic:
    def __init__(self):
        self._define_year()
        self._define_mileage()
        self.car_value_fuzzy = ctrl.Consequent(np.arange(0, 100, 1), "car_value")

        self.car_value_fuzzy["low"] = fuzz.trimf(
            self.car_value_fuzzy.universe, [0, 25, 50]
        )
        self.car_value_fuzzy["medium"] = fuzz.trimf(
            self.car_value_fuzzy.universe, [25, 50, 75]
        )
        self.car_value_fuzzy["high"] = fuzz.trimf(
            self.car_value_fuzzy.universe, [50, 75, 100]
        )

        rule1 = ctrl.Rule(
            self.year["new"] & self.mileage["low"], self.car_value_fuzzy["high"]
        )
        rule2 = ctrl.Rule(
            self.year["medium"] & self.mileage["medium"], self.car_value_fuzzy["medium"]
        )
        rule3 = ctrl.Rule(
            self.year["old"] & self.mileage["high"], self.car_value_fuzzy["low"]
        )
        rule4 = ctrl.Rule(
            self.year["new"] & self.mileage["high"], self.car_value_fuzzy["low"]
        )
        rule5 = ctrl.Rule(
            self.year["old"] & self.mileage["low"], self.car_value_fuzzy["medium"]
        )
        rule6 = ctrl.Rule(
            self.year["medium"] & self.mileage["low"], self.car_value_fuzzy["medium"]
        )
        rule7 = ctrl.Rule(
            self.year["new"] & self.mileage["medium"], self.car_value_fuzzy["high"]
        )
        rule8 = ctrl.Rule(
            self.year["medium"] & self.mileage["high"], self.car_value_fuzzy["low"]
        )

        self.fuzzy_system = ctrl.ControlSystem(
            [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8]
        )
        self.fuzzy_simulation = ctrl.ControlSystemSimulation(self.fuzzy_system)

    def _define_year(self):
        self.year = ctrl.Antecedent(np.arange(1990, 2026, 1), "year")
        self.year["old"] = fuzz.trimf(self.year.universe, [1990, 2000, 2005])
        self.year["medium"] = fuzz.trimf(self.year.universe, [2000, 2010, 2020])
        self.year["new"] = fuzz.trimf(self.year.universe, [2015, 2022, 2026])

    def _define_mileage(self):
        self.mileage = ctrl.Antecedent(np.arange(0, 300000, 1000), "mileage")
        self.mileage["low"] = fuzz.trimf(self.mileage.universe, [0, 50000, 100000])
        self.mileage["medium"] = fuzz.trimf(
            self.mileage.universe, [50000, 150000, 200000]
        )
        self.mileage["high"] = fuzz.trimf(
            self.mileage.universe, [200000, 250000, 300000]
        )

    def compute_car_value(self, year, mileage):
        self.fuzzy_simulation.input["year"] = year
        self.fuzzy_simulation.input["mileage"] = mileage

        self.fuzzy_simulation.compute()
        return self.fuzzy_simulation.output["car_value"]
