import unittest


class Query:
    """
    Base Query class.
    """

    def __init__(self, operand, table):
        self.query = operand
        self.table = table

    def equals(self, operand):
        self.query += ' = ' + str(operand)
        self.table.query += self.query
        return self.table


class UrlQuery(Query):
    """
    Query class for url columns.
    """

    def __init__(self, table):
        super(UrlQuery, self).__init__('url', table=table)


class ComparisonQuery(Query):
    """
    Base class for comparison queries.
    """

    def greater_than(self, operand):
        self.query += ' > ' + str(operand)
        self.table.query += self.query
        return self.table

    def less_than(self, operand):
        self.query += ' < ' + str(operand)
        self.table.query += self.query
        return self.table


class DateQuery(ComparisonQuery):
    """
    Query class for date columns
    """

    def __init__(self, table):
        super(DateQuery, self).__init__('date', table=table)


class RatingQuery(ComparisonQuery):
    """
    Query class for rating columns
    """
    def __init__(self, table):
        super(RatingQuery, self).__init__('rating', table=table)


class IdQuery(ComparisonQuery):
    """
    Query class for id columns
    """

    def __init__(self, table):
        super(IdQuery, self).__init__('id', table=table)

    def in_(self, operand):
        self.query += ' IN ' + str(tuple(operand))
        self.table.query += self.query
        return self.table

    def not_in(self, operand):
        self.query += ' NOTIN ' + str(tuple(operand))
        self.table.query += self.query
        return self.table


class TableQuery:
    """
    Attempt at class to create SQL queries
    for table with columns (id, url, date, rating)
    with fluent-style interface
    """

    def __init__(self, select='*', from_='table'):
        self.query = 'SELECT {} FROM {}'.format(select, from_)

    @property
    def id(self):
        return IdQuery(self)

    @property
    def url(self):
        return UrlQuery(self)

    @property
    def date(self):
        return DateQuery(self)

    @property
    def rating(self):
        return RatingQuery(self)

    @property
    def where(self):
        self.query += ' WHERE '
        return self

    @property
    def and_(self):
        self.query += ' AND '
        return self


class TestTableQuery(unittest.TestCase):
    """
    Test class for TableQuery,
    see here for usage examples.
    """

    def test_basic(self):
        q = TableQuery()
        self.assertEqual('SELECT * FROM table',
                         q.query)

    def test_simple(self):
        q = TableQuery().where.id.greater_than(42)
        self.assertEqual('SELECT * FROM table WHERE id > 42',
                         q.query)

    def test_two_id_filters(self):
        q = TableQuery().where.id.in_(range(3))\
            .and_.id.greater_than(1)
        self.assertEqual('SELECT * FROM table WHERE id IN (0, 1, 2) AND id > 1',
                         q.query)

    def test_verbose(self):
        q = TableQuery().where.id.in_(range(3))\
            .and_.id.greater_than(1)\
            .and_.date.equals('01-01-2019')\
            .and_.url.equals('www.url.com')\
            .and_.rating.less_than(2)
        self.assertEqual('SELECT * FROM table WHERE id IN (0, 1, 2) AND id > 1 AND date = 01-01-2019 AND url = www.url.com AND rating < 2',
                         q.query)

    def test_select_from(self):
        q = TableQuery(select='id, date', from_='foo')
        self.assertEqual('SELECT id, date FROM foo', q.query)


if __name__ == '__main__':
    unittest.main()

