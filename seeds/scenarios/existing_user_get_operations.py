from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedAccountsPlan, SeedOperationsPlan


class ExistingUserGetOperationsSeedsScenario(SeedsScenario):
    @property
    def plan(self) -> SeedsPlan:
        """
        Возвращает план сидинга для создания пользователей и операций по кредитному счету.
        Мы создаём 300 пользователей, каждый получит дебетовый счет и виртуальную карту.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Создаём 300 пользователей
                credit_card_accounts=SeedAccountsPlan(
                    count=1,
                    purchase_operations=SeedOperationsPlan(count=5),
                    top_up_operations=SeedOperationsPlan(count=1),
                    cash_withdrawal_operations=SeedOperationsPlan(count=1),
                )
            )
        )

    @property
    def scenario(self) -> str:
        """
        Возвращает название сценария сидинга.
        Это имя будет использоваться для сохранения данных сидинга.
        """
        return "existing_user_get_operations"


if __name__ == '__main__':
    """
    Запуск сценария сидинга вручную.
    Создаём объект сценария и вызываем метод build для создания данных.
    """
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()  # Запуск сидинга