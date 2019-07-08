import cmp504
import time
from assertpy import assert_that
from transitions import Machine


vision = cmp504.computer_vision.CVController()
mouse = cmp504.mouse_controller.MouseController()


class GameState(object):
    states = [
        'main menu',
        'custom content menu',
        'creation menu',
        'two player map creation menu',
        'three player map creation menu',
        'map editor',
        'gameplay'
    ]

    def __init__(self):
        self.machine = Machine(model=self, states=GameState.states, initial='main menu')

        self.machine.add_transition(trigger='go_to_custom_content',
                                    source='main menu',
                                    dest='custom content menu',
                                    before='click_custom_content_button')
        self.machine.add_transition(trigger='go_back_to_main_menu',
                                    source='custom content menu',
                                    dest='main menu',
                                    before='click_back')

        self.machine.add_transition(trigger='go_to_custom_content_creation',
                                    source='custom content menu',
                                    dest='creation menu',
                                    before='click_create_button')
        self.machine.add_transition(trigger='go_back_to_custom_content',
                                    source='creation menu',
                                    dest='custom content menu',
                                    before='click_back')

        self.machine.add_transition(trigger='go_to_2_player_map_creation',
                                    source='creation menu',
                                    dest='two player map creation menu',
                                    before='click_map_button')
        self.machine.add_transition(trigger='go_to_3_player_map_creation',
                                    source='two player map creation menu',
                                    dest='three player map creation menu',
                                    before='click_three_player_button')
        self.machine.add_transition(trigger='go_back_to_custom_content_creation',
                                    source=['two player map creation menu', 'three player map creation menu'],
                                    dest='creation menu',
                                    before='click_back')

        self.machine.add_transition(trigger='go_to_map_editor',
                                    source='three player map creation menu',
                                    dest='map editor',
                                    before='click_map_and_edit_buttons')
        self.machine.add_transition(trigger='go_back_to_main_menu',
                                    source='map editor',
                                    dest='main menu',
                                    before='click_editor_menu_and_exit_buttons')

        self.machine.add_transition(trigger='go_to_gameplay',
                                    source='map editor',
                                    dest='gameplay',
                                    before='click_editor_menu_and_play_buttons')
        self.machine.add_transition(trigger='go_back_to_map_editor',
                                    source='gameplay',
                                    dest='map editor',
                                    before='click_mission_and_exit_buttons')

    def reset_to_initial_state(self):
        if self.state == 'gameplay':
            self.go_back_to_map_editor()

        if self.state == 'map editor':
            self.go_back_to_main_menu()

        if self.state == 'two player map creation menu' or self.state == 'three player map creation menu':
            self.go_back_to_custom_content_creation()

        if self.state == 'creation menu':
            self.go_back_to_custom_content()

        if self.state == 'custom content menu':
            self.go_back_to_main_menu()

    def click_long_animation_button(self, button_name, animation_wait_time=1.0):
        mouse.move_mouse(0, 0)
        time.sleep(0.1)
        mouse_over_ui_element(button_name)
        time.sleep(0.1)
        mouse.left_mouse_click()
        mouse.move_mouse(0, 0)
        time.sleep(animation_wait_time)
        vision.capture_frame()

    def click_no_animation_button(self, button_name):
        mouse.move_mouse(0, 0)
        time.sleep(0.1)
        mouse_over_ui_element(button_name)
        time.sleep(0.1)
        mouse.left_mouse_click()
        mouse.move_mouse(0, 0)
        time.sleep(0.1)
        vision.capture_frame()

    def click_tile(self, tile_template_name):
        mouse.move_mouse(0, 0)
        time.sleep(0.1)
        mouse_over_tile(tile_template_name)
        time.sleep(0.1)
        mouse.left_mouse_click()
        mouse.move_mouse(0, 0)
        time.sleep(0.1)
        vision.capture_frame()

    def click_custom_content_button(self):
        self.click_long_animation_button('main_menu/custom_content_button')

    def click_create_button(self):
        self.click_long_animation_button('main_menu/custom_content/create_button')

    def click_back(self):
        self.click_long_animation_button('back_button')

    def click_map_button(self):
        self.click_long_animation_button('main_menu/custom_content/create/map_button')

    def click_three_player_button(self):
        self.click_long_animation_button('main_menu/custom_content/create/map/three_player_button')

    def click_map_and_edit_buttons(self, map_name):
        self.click_no_animation_button('main_menu/custom_content/create/map/' + map_name + '_button')
        self.click_long_animation_button('main_menu/custom_content/create/map/edit_button')

    def click_editor_menu_and_exit_buttons(self):
        self.click_no_animation_button('map_editor/editor_menu_button')
        self.click_long_animation_button('map_editor/save_and_exit_button')

    def click_editor_menu_and_play_buttons(self):
        self.click_no_animation_button('map_editor/editor_menu_button')
        self.click_long_animation_button('map_editor/play_map_button', animation_wait_time=3.0)

    def click_mission_and_exit_buttons(self):
        self.clear_turn_start_banner()
        time.sleep(0.1)
        self.click_tile('empty_water_tile')
        self.click_no_animation_button('gameplay/menu/mission_button')
        self.click_no_animation_button('gameplay/menu/exit_button')
        self.click_long_animation_button('gameplay/menu/ok_button')

    def is_showing_turn_start_banner(self):
        return self.state == 'gameplay' and is_ui_element_visible('gameplay/turn_start_banner')

    def clear_turn_start_banner(self):
        if self.is_showing_turn_start_banner():
            mouse_over_ui_element('gameplay/turn_start_banner')
            mouse.left_mouse_press()
            while self.is_showing_turn_start_banner():
                time.sleep(0.1)
                vision.capture_frame()
            mouse.left_mouse_release()


game_state = GameState()


def mouse_over_unit(unit_template_name, threshold=0.55, render_match: bool = False):
    return mouse_over_bottom_of_element("data/units/" + unit_template_name + ".png",
                                        threshold,
                                        match_horizontal_mirror=True,
                                        render_match=render_match)


def mouse_over_building(building_template_name, threshold=0.8):
    return mouse_over_center_of_element("data/buildings/" + building_template_name + ".png", threshold)


def mouse_over_tile(tile_template_name, threshold=0.9):
    return mouse_over_center_of_element("data/tiles/" + tile_template_name + ".png", threshold)


def mouse_over_ui_element(ui_element_template_name, threshold=0.9, mouse_move_offset_x=0, mouse_move_offset_y=0):
    return mouse_over_center_of_element("data/ui/" + ui_element_template_name + ".png",
                                        threshold,
                                        mouse_move_offset_x,
                                        mouse_move_offset_y)


def mouse_over_center_of_element(template_path,
                                 threshold=0.9,
                                 mouse_move_offset_x=0,
                                 mouse_move_offset_y=0,
                                 template_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                                 frame_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                                 match_horizontal_mirror: bool = False,
                                 render_match: bool = False):
    match = find_element(template_path,
                         threshold=threshold,
                         template_pre_processing_chain=template_pre_processing_chain,
                         frame_pre_processing_chain=frame_pre_processing_chain,
                         match_horizontal_mirror=match_horizontal_mirror,
                         render_match=render_match)

    mouse.move_mouse(match.mid_point[0] + mouse_move_offset_x,
                     match.mid_point[1] + mouse_move_offset_y)
    return match


def mouse_over_bottom_of_element(template_path,
                                 threshold=0.9,
                                 mouse_move_offset_x=0,
                                 mouse_move_offset_y=0,
                                 template_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                                 frame_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                                 match_horizontal_mirror: bool = False,
                                 render_match: bool = False):
    match = find_element(template_path,
                         threshold=threshold,
                         template_pre_processing_chain=template_pre_processing_chain,
                         frame_pre_processing_chain=frame_pre_processing_chain,
                         match_horizontal_mirror=match_horizontal_mirror,
                         render_match=render_match)

    mouse.move_mouse(match.mid_point[0] + mouse_move_offset_x,
                     match.bottom_right[1] + mouse_move_offset_y)
    return match


def find_element(template_path,
                 threshold=0.9,
                 template_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                 frame_pre_processing_chain: cmp504.image_processing.ImageProcessingStepChain = None,
                 match_horizontal_mirror: bool = False,
                 render_match: bool = False):
    match = vision.find_template_match(template_path,
                                       threshold=threshold,
                                       method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED,
                                       template_pre_processing_chain=template_pre_processing_chain,
                                       frame_pre_processing_chain=frame_pre_processing_chain,
                                       match_horizontal_mirror=match_horizontal_mirror,
                                       render_match=render_match)

    assert_that(match).described_as('mouse over target %s' % template_path).is_not_none()
    return match


def is_ui_element_visible(ui_element_template_name, threshold=0.9):
    match = vision.find_template_match("data/ui/" + ui_element_template_name + ".png",
                                       threshold=threshold,
                                       method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)
    return match is not None


def wait_for_screen_update():
    time.sleep(0.1)


vision.capture_frame()
if not is_ui_element_visible('main_menu/wargroove_title'):
    mouse_over_ui_element('wargroove_taskbar_icon')
    mouse.left_mouse_click()
    wait_for_screen_update()
    vision.capture_frame()
    mouse_over_ui_element('main_menu/wargroove_title')
