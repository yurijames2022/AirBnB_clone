import unittest
import models.base_model
import models.state
import models.city
import models.amenity
import models.place
import models.review

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.b = models.base_model.BaseModel()

    def test_id_creation(self):
        self.assertIsNotNone(self.b.id)

    def test_to_dict(self):
        self.assertIsInstance(self.b.to_dict(), dict)

    def test_str(self):
        self.assertIsInstance(str(self.b), str)

class TestState(unittest.TestCase):
    def setUp(self):
        self.s = models.state.State()

    def test_attributes(self):
        self.assertEqual(self.s.name, "")

class TestCity(unittest.TestCase):
    def setUp(self):
        self.c = models.city.City()

    def test_attributes(self):
        self.assertEqual(self.c.state_id, "")
        self.assertEqual(self.c.name, "")

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.a = models.amenity.Amenity()

    def test_attributes(self):
        self.assertEqual(self.a.name, "")

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.p = models.place.Place()

    def test_attributes(self):
        self.assertEqual(self.p.city_id, "")
        self.assertEqual(self.p.user_id, "")
        self.assertEqual(self.p.name, "")
        self.assertEqual(self.p.description, "")
        self.assertEqual(self.p.number_rooms, 0)
        self.assertEqual(self.p.number_bathrooms, 0)
        self.assertEqual(self.p.max_guest, 0)
        self.assertEqual(self.p.price_by_night, 0)
        self.assertEqual(self.p.latitude, 0.0)
        self.assertEqual(self.p.longitude, 0.0)
        self.assertEqual(self.p.amenity_ids, [])

class TestReview(unittest.TestCase):
    def setUp(self):
        self.r = models.review.Review()

    def test_attributes(self):
        self.assertEqual(self.r.place_id, "")
        self.assertEqual(self.r.user_id, "")
        self.assertEqual(self.r.text, "")
