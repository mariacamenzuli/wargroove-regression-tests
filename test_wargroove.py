import cmp504
import time
from assertpy import assert_that

computer_vision_ctrl = cmp504.computer_vision.CVController()
mouse_ctrl = cmp504.mouse_controller.MouseController()


def test_right_clicking_building_shows_building_info_panel():
    computer_vision_ctrl.capture_frame()
    mouse_over_building("cherrystone_stronghold")
    mouse_ctrl.right_mouse_click()

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_ui_element("tile_info_panel_border")

    text = computer_vision_ctrl.find_text(pre_processing_chain=get_pre_processing_chain_for_tile_info_panel_ocr())

    assert_that(text).contains("Income")
    assert_that(text).contains("Stronghold")

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


def mouse_over_unit(unit_template_name):
    mouse_over_element("data/units/" + unit_template_name + ".png")


def mouse_over_building(building_template_name):
    mouse_over_element("data/buildings/" + building_template_name + ".png")


def mouse_over_ui_element(ui_element_template_name):
    mouse_over_element("data/ui/" + ui_element_template_name + ".png")


def mouse_over_element(template_path):
    match = computer_vision_ctrl.find_template_match(template_path,
                                                     threshold=0.7,
                                                     method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

    assert_that(match).is_not_none()
    mouse_ctrl.move_mouse(match[0], match[1])


def get_pre_processing_chain_for_tile_info_panel_ocr():
    pre_processing_step_chain = cmp504.image_processing.ImageProcessingStepChain()
    pre_processing_step_chain.append(cmp504.image_processing.BGR2Grayscale())
    pre_processing_step_chain.append(cmp504.image_processing.Resize(3, 3))
    return pre_processing_step_chain
