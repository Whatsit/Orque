import unittest
from player import Player
from room import Room
from map import Map
from item import Item

class PlayerTestCase(unitcase.TestCase):
	def assert_location_equal(self, p, location):
		self.assertEqual(p.location, location)

class PlayerTest(PlayerTestCase):

	def setup(self):
		self.p = Player()
		self.m = Map()
		self.m


	def test_move_into_wall(self):
		p = Player()
		p.location = [0,0]
		p.move(0,False)
		self.assertEqual(p.location == [0,0])

	def test_move_into_door(self):
		pass

	def test_move_into_room(self):
		pass

	def search_empty_room(self):
		pass

	def search_room_with_item(self):
		pass

	def get_item_from_empty_room(self):
		pass

	def get_item_from_room_with_item(self):
		pass

	def use_item_with_empty_inventory(self):
		pass

	def use_item_on_door(self):
		pass

	def use_item_on_door_without_item(self):
		pass

