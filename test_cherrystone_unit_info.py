import wargroove_ctrl
import unittest
import time
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
        wargroove_ctrl.game_state.clear_turn_start_banner()

    @classmethod
    def tearDownClass(cls):
        wargroove_ctrl.game_state.reset_to_initial_state()

    def test_mercia_info_panel_specifies_movement_walking_4(self):
        def mercia_info_panel_test():
            is_walking_4_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_4',
                                                                          threshold=0.999)
            assert_that(is_walking_4_displayed).described_as('mercia movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_commander_mercia', mercia_info_panel_test)

    def test_emeric_info_panel_specifies_movement_walking_4(self):
        def emeric_info_panel_test():
            is_walking_4_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_4',
                                                                          threshold=0.999)
            assert_that(is_walking_4_displayed).described_as('emeric movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_commander_emeric', emeric_info_panel_test)

    def test_caesar_info_panel_specifies_movement_walking_4(self):
        def caesar_info_panel_test():
            is_walking_4_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_4',
                                                                          threshold=0.999)
            assert_that(is_walking_4_displayed).described_as('caesar movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_commander_caesar', caesar_info_panel_test)

    def test_villager_info_panel_specifies_movement_walking_3(self):
        def villager_info_panel_test():
            is_walking_3_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_3',
                                                                          threshold=0.999)
            assert_that(is_walking_3_displayed).described_as('villager movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_villager', villager_info_panel_test)

    def test_soldier_info_panel_specifies_movement_walking_4(self):
        def soldier_info_panel_test():
            is_walking_4_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_4',
                                                                          threshold=0.999)
            assert_that(is_walking_4_displayed).described_as('soldier movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_soldier', soldier_info_panel_test)

    def test_pikeman_info_panel_specifies_movement_walking_3(self):
        def pikeman_info_panel_test():
            is_walking_3_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_3',
                                                                          threshold=0.999)
            assert_that(is_walking_3_displayed).described_as('pikeman movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_pikeman', pikeman_info_panel_test)

    def test_battle_pup_info_panel_specifies_movement_walking_5(self):
        def battle_pup_info_panel_test():
            is_walking_5_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_5',
                                                                          threshold=0.999)
            assert_that(is_walking_5_displayed).described_as('battle pup movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_battle_pup', battle_pup_info_panel_test)

    def test_alchemist_info_panel_specifies_movement_walking_5(self):
        def alchemist_info_panel_test():
            is_walking_5_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_5',
                                                                          threshold=0.999)
            assert_that(is_walking_5_displayed).described_as('alchemist movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_alchemist', alchemist_info_panel_test)

    def test_archer_info_panel_specifies_movement_walking_3(self):
        def archer_info_panel_test():
            is_walking_3_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_3',
                                                                          threshold=0.999)
            assert_that(is_walking_3_displayed).described_as('archer movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_archer', archer_info_panel_test)

    def test_golem_info_panel_specifies_movement_walking_5(self):
        def golem_info_panel_test():
            is_walking_3_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/walking_5',
                                                                          threshold=0.999)
            assert_that(is_walking_3_displayed).described_as('golem movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_golem', golem_info_panel_test)

    def test_barge_info_panel_specifies_movement_water_10(self):
        def barge_info_panel_test():
            is_water_10_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/water_10',
                                                                         threshold=0.999)
            assert_that(is_water_10_displayed).described_as('barge movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_barge', barge_info_panel_test)

    def test_sea_turtle_info_panel_specifies_movement_water_12(self):
        def sea_turtle_info_panel_test():
            is_water_12_displayed = wargroove_ctrl.is_ui_element_visible('unit_info/movement/water_12',
                                                                         threshold=0.999)
            assert_that(is_water_12_displayed).described_as('sea turtle movement correctly displayed').is_true()

        self.open_unit_info_panel_and_run_test('cherrystone_sea_turtle', sea_turtle_info_panel_test)

    @staticmethod
    def open_unit_info_panel_and_run_test(unit_template_name, panel_test):
        wargroove_ctrl.vision.capture_frame()
        wargroove_ctrl.mouse_over_unit(unit_template_name)
        time.sleep(0.1)
        wargroove_ctrl.mouse.right_mouse_click()

        time.sleep(0.5)
        wargroove_ctrl.mouse.move_mouse(0, 0)
        time.sleep(0.1)
        wargroove_ctrl.vision.capture_frame()
        panel_location = wargroove_ctrl.mouse_over_ui_element("unit_tile_info_panel_border")
        wargroove_ctrl.vision.crop_frame(panel_location.top_left, panel_location.bottom_right)

        try:
            panel_test()
        finally:
            wargroove_ctrl.mouse_over_ui_element("close_button",
                                                 mouse_move_offset_x=panel_location.top_left[0],
                                                 mouse_move_offset_y=panel_location.top_left[1])
            time.sleep(0.1)
            wargroove_ctrl.mouse.left_mouse_click()
            time.sleep(0.1)
            wargroove_ctrl.mouse.move_mouse(0, 0)
            wargroove_ctrl.vision.capture_frame()
