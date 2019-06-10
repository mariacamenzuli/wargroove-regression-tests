import cmp504
from assertpy import assert_that


def test_cherrystone_stronghold_exists():
    computer_vision_ctrl = cmp504.computer_vision.CVController()
    computer_vision_ctrl.load_frame("data/test-screenshot.png")
    match = computer_vision_ctrl.find_template_match("data/cherrystone_stronghold.png")

    assert_that(match).is_true()
