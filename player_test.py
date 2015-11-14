import unittest
from player import Player

class Player_Test(unitcase.TestCase):
	def test_move_into_wall(self):
		p = Player()
		p.location = [0,0]
		p.move(0,False)
		assert(p.location == [0,0])

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

