from web.moneyCount.models import User, Money, Category


class MoneyService:
    # Сохраняет операцию с деньгами
    def save_money(self, user: User, category: Category, count: int, comment: str, is_income: bool) -> Money:
        r = Money(count=count, comment=comment, user=user, category=category, is_income=is_income)
        return r.save()

    # Сохраняет приход (пополнение баланса)
    def save_income(self, user: User, category: Category, count: int, comment: str)-> Money:
        return self.save_money(user, category, count, comment, True)

    # Сохраняет расход (уменьшение баланса)
    def save_outcome(self, user: User, category: Category, count: int, comment: str)-> Money:
        return self.save_money(user, category, count, comment, False)
