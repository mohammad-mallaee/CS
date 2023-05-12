class DateError(Exception):
    pass


class Date:
    MAX_DAYS_PER_MONTH = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    MILADI_DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    DAYS_PER_YEAR = 365

    def __init__(self, year=1, month=1, day=1):
        if year < 1 or month < 1 or day < 1 or month > 12:
            raise DateError("Out of range value")

        if day > Date.MAX_DAYS_PER_MONTH[month - 1]:
            raise DateError("Out of range value")

        self.__year = year
        self.__month = month
        self.__day = day

    def total_days(self):
        days = self.__year * Date.DAYS_PER_YEAR
        for i in range(self.__month - 1):
            days += Date.MAX_DAYS_PER_MONTH[i]
        days += self.__day
        return days

    @staticmethod
    def days_to_date(days):
        year = days // Date.DAYS_PER_YEAR
        days = days % Date.DAYS_PER_YEAR
        month_index = 0
        month = 1
        while days > Date.MAX_DAYS_PER_MONTH[month_index]:
            days -= Date.MAX_DAYS_PER_MONTH[month_index]
            month += 1
            month_index += 1
        days = 1 if days == 0 else days
        year = 1 if year == 0 else year
        return Date(year, month, days)

    @staticmethod
    def days_to_miladi_date(days):
        year = days // Date.DAYS_PER_YEAR
        days = days % Date.DAYS_PER_YEAR
        month_index = 0
        month = 1
        while days > Date.MILADI_DAYS_PER_MONTH[month_index]:
            days -= Date.MILADI_DAYS_PER_MONTH[month_index]
            month += 1
            month_index += 1
        days = 1 if days == 0 else days
        return year, month, days

    def convert2miladi(self):
        difference_year = 621
        if self.__month >= 10 and self.__day >= 10:
            difference_year += 1
        passed_date = Date(self.__year + difference_year, self.__month, self.__day)
        days = passed_date.total_days() + 31 + 28 + 20
        year, month, day = Date.days_to_miladi_date(days)
        return f"{month}.{day}.{year}"

    def __add__(self, other):
        if isinstance(other, int):
            return Date.days_to_date(self.total_days() + other)
        elif isinstance(other, Date):
            return Date.days_to_date(self.total_days() + other.total_days())
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, int):
            return self.total_days() - other
        elif isinstance(other, Date):
            return self.total_days() - other.total_days()
        else:
            raise TypeError

    def __iter__(self):
        self.__iter_days = self.__year * Date.DAYS_PER_YEAR
        return self

    def __next__(self):
        if self.__iter_days >= self.total_days():
            raise StopIteration
        self.__iter_days += 1
        return Date.days_to_date(self.__iter_days)

    def __str__(self):
        return f"{self.__year}/{self.__month}/{self.__day}"
