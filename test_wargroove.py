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

    match2 = computer_vision_ctrl.find_template_match("data/cherrystone_stronghold.png")

    assert_that(match2).is_not_none()
