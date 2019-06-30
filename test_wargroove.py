import cmp504
import time
from assertpy import assert_that

computer_vision_ctrl = cmp504.computer_vision.CVController()
mouse_ctrl = cmp504.mouse_controller.MouseController()


def test_right_clicking_stronghold_shows_stronghold_info_panel():
    computer_vision_ctrl.capture_frame()
    mouse_over_building("cherrystone_stronghold")
    mouse_ctrl.right_mouse_click()

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_ui_element("building_tile_info_panel_border")

    try:
        text = computer_vision_ctrl.find_text(pre_processing_chain=get_pre_processing_chain_for_tile_info_panel_ocr())

        assert_that(text).contains_ignoring_case("Income")
        assert_that(text).contains_ignoring_case("Stronghold")
    finally:
        mouse_over_ui_element("close_button")
        mouse_ctrl.left_mouse_click()


def test_right_clicking_commander_shows_commander_info_panel():
    computer_vision_ctrl.capture_frame()
    mouse_over_unit("cherrystone_commander_mercia")
    mouse_ctrl.right_mouse_click()

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_ui_element("unit_tile_info_panel_border")

    try:
        text = computer_vision_ctrl.find_text(pre_processing_chain=get_pre_processing_chain_for_tile_info_panel_ocr())

        assert_that(text).contains("Moves")
        assert_that(text).contains("Commander")
        assert_that(text).contains("Captures")
    finally:
        mouse_over_ui_element("close_button")
        mouse_ctrl.left_mouse_click()


def test_cherrystone_stronghold_exists():
    computer_vision_ctrl.capture_frame()

    match = computer_vision_ctrl.find_template_match("data/wargroove-icon.PNG")

    mouse_ctrl.move_mouse(match[0], match[1])
    mouse_ctrl.left_mouse_click()

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_building("cherrystone_stronghold")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit("cherrystone_commander_mercia")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit("cherrystone_soldier")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit("cherrystone_villager")


def mouse_over_unit(unit_template_name, threshold=0.7):
    mouse_over_element("data/units/" + unit_template_name + ".png", threshold)


def mouse_over_building(building_template_name, threshold=0.8):
    mouse_over_element("data/buildings/" + building_template_name + ".png", threshold)


def mouse_over_ui_element(ui_element_template_name, threshold=0.9):
    mouse_over_element("data/ui/" + ui_element_template_name + ".png", threshold)


def mouse_over_element(template_path, threshold=0.9):
    match = computer_vision_ctrl.find_template_match(template_path,
                                                     threshold=threshold,
                                                     method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

    assert_that(match).is_not_none()
    mouse_ctrl.move_mouse(match[0], match[1])


def get_pre_processing_chain_for_tile_info_panel_ocr():
    pre_processing_step_chain = cmp504.image_processing.ImageProcessingStepChain()
    pre_processing_step_chain.append(cmp504.image_processing.BGR2Grayscale())
    pre_processing_step_chain.append(cmp504.image_processing.Resize(3, 3))
    return pre_processing_step_chain
