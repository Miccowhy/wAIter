import pandas as pd
import numpy as np
from .entity import Entity
from ai.decision_tree import Dataset, train_model
from constants.images import CUSTOMER_SPRITESHEET
from constants.movement import Direction
from constants.datasets import PIZZAS_DF, PIZZA_COUNT


class Customer(Entity):
    def __init__(self, current_tile, direction=Direction.DOWN):
        super().__init__(current_tile=current_tile, loaded_image=CUSTOMER_SPRITESHEET(),
                         direction=direction)
        self.order_history = self._generate_order_history()
        order_history_dataset = Dataset(self.order_history,
                                        'Good_Pizza?',
                                        ['Bad Pizza', 'Good Pizza'])
        self.decision_tree = train_model(order_history_dataset)
        print('Customer order history: ')
        print(self.order_history.to_string())

    def _generate_order_history(self):
        pizzas_from_menu_num = np.random.randint(6, 12)
        pizzas_from_menu_1 = np.random.randint(0, pizzas_from_menu_num + 1)
        pizzas_from_menu_2 = pizzas_from_menu_num - pizzas_from_menu_1

        random_custom_pizzas = pd.DataFrame(
                                np.random.randint(
                                    0, 2, size=((PIZZA_COUNT - pizzas_from_menu_num), 7)),
                                columns=PIZZAS_DF.columns.values)

        order_history = PIZZAS_DF.sample(pizzas_from_menu_1)
        order_history = order_history.append(PIZZAS_DF.sample(pizzas_from_menu_2))
        order_history = order_history.append(random_custom_pizzas)
        order_history['Good_Pizza?'] = np.random.randint(0, 2, size=len(order_history))
        return order_history
