from datetime import datetime
import unittest

from inzidenzvergleich import set_date


class TestDateAdded(unittest.TestCase):
    
    def test_add_date_one_city(self):
        test_city_dict = [{'city_name': 'Munich', 'incidence': 1.75}]
        now = datetime.now()

        cities_with_date = set_date(test_city_dict, now)

        munich = cities_with_date[0]
        self.assertEqual(munich['city_name'], 'Munich')
        self.assertEqual(munich['incidence'], 1.75)
        self.assertEqual(munich['date'], now)

    def test_add_date_multiple_city(self):   
        test_city_dict = [
            {},
            {}
            ]
        now = datetime.now()

        cities_with_date = set_date(test_city_dict, now)

        for c in cities_with_date:
            self.assertEqual(c['date'], now, "Date was not today everywhere")

            # city_name und incidencewird nicht verändert (1.)
            # für eine Stadt wird "date" hinzugefügt (2.)
            # für alle Städte wird "date" hinzugefügt (3.)
            # wie mathematische Induktion
            # Also: date_add_date_one_city(self) - Test in zwei Tests aufspalten
            # BDD, hoare_logic, unittest.html
            # Immer nur ein Kommando pro Test testen klappt am besten in Unit-Tests. 
            # https://docs.python.org/3/library/unittest.html 
            # https://en.wikipedia.org/wiki/Hoare_logic
            # https://en.wikipedia.org/wiki/Behavior-driven_development 

