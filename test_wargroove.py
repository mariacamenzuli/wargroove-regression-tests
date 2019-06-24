import cmp504
import time
from assertpy import assert_that


def test_cherrystone_stronghold_exists():
    computer_vision_ctrl = cmp504.computer_vision.CVController()
    computer_vision_ctrl.capture_frame()

    match = computer_vision_ctrl.find_template_match("data/wargroove-icon.PNG")

    mouse_ctrl = cmp504.mouse_controller.MouseController()
    mouse_ctrl.move_mouse(match[0], match[1])
    mouse_ctrl.left_mouse_click()

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_building(computer_vision_ctrl, mouse_ctrl, "cherrystone_stronghold")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit(computer_vision_ctrl, mouse_ctrl, "cherrystone_commander_mercia")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit(computer_vision_ctrl, mouse_ctrl, "cherrystone_soldier")

    time.sleep(0.5)
    computer_vision_ctrl.capture_frame()
    mouse_over_unit(computer_vision_ctrl, mouse_ctrl, "cherrystone_villager")


def mouse_over_unit(computer_vision_ctrl, mouse_ctrl, unit_template_name):
    match = computer_vision_ctrl.find_template_match("data/units/" + unit_template_name + ".png",
                                                     threshold=0.7,
                                                     method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

    assert_that(match).is_not_none()
    mouse_ctrl.move_mouse(match[0], match[1])


def mouse_over_building(computer_vision_ctrl, mouse_ctrl, building_template_name):
    match = computer_vision_ctrl.find_template_match("data/buildings/" + building_template_name + ".png",
                                                     threshold=0.7,
                                                     method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

    assert_that(match).is_not_none()
    mouse_ctrl.move_mouse(match[0], match[1])
