import wargroove_ctrl
import unittest
from assertpy import assert_that


class TestCherrystoneUnitInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        wargroove_ctrl.game_state.go_to_custom_content()
        wargroove_ctrl.game_state.go_to_custom_content_creation()
        wargroove_ctrl.game_state.go_to_2_player_map_creation()
        wargroove_ctrl.game_state.go_to_3_player_map_creation()
        wargroove_ctrl.game_state.go_to_map_editor(map_name='cherrystone_units_test_map')
        wargroove_ctrl.game_state.go_to_gameplay()

    @classmethod
    def tearDownClass(cls):
        wargroove_ctrl.game_state.reset_to_initial_state()

    def test_thing(self):
        assert_that(wargroove_ctrl.game_state.is_showing_turn_start_banner()).is_true()
