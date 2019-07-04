import wargroove_ctrl
import cmp504
import time
from unittest import skip
from assertpy import assert_that


@skip("due to OCR being flaky")
def test_right_clicking_stronghold_shows_stronghold_info_panel():
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_building("cherrystone_stronghold")
    wargroove_ctrl.mouse.right_mouse_click()

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    panel_location = wargroove_ctrl.mouse_over_ui_element("building_tile_info_panel_border")
    wargroove_ctrl.vision.crop_frame(panel_location.top_left, panel_location.bottom_right)

    try:
        text = wargroove_ctrl.vision.find_text(pre_processing_chain=get_pre_processing_chain_for_tile_info_panel_ocr())

        assert_that(text).contains_ignoring_case("Income")
        assert_that(text).contains_ignoring_case("Stronghold")
    finally:
        wargroove_ctrl.mouse_over_ui_element("close_button",
                                             mouse_move_offset_x=panel_location.top_left[0],
                                             mouse_move_offset_y=panel_location.top_left[1])
        time.sleep(0.1)
        wargroove_ctrl.mouse.left_mouse_click()


@skip("due to OCR being flaky")
def test_right_clicking_commander_shows_commander_info_panel():
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_unit("cherrystone_commander_mercia")
    wargroove_ctrl.mouse.right_mouse_click()

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    panel_location = wargroove_ctrl.mouse_over_ui_element("unit_tile_info_panel_border")
    wargroove_ctrl.vision.crop_frame(panel_location.top_left, panel_location.bottom_right)

    try:
        text = wargroove_ctrl.vision.find_text(pre_processing_chain=get_pre_processing_chain_for_tile_info_panel_ocr())

        assert_that(text).contains("Moves")
        assert_that(text).contains("Commander")
        assert_that(text).contains("Captures")
    finally:
        wargroove_ctrl.mouse_over_ui_element("close_button",
                                             mouse_move_offset_x=panel_location.top_left[0],
                                             mouse_move_offset_y=panel_location.top_left[1])
        wargroove_ctrl.mouse.left_mouse_click()


def test_cherrystone_stronghold_exists():
    wargroove_ctrl.vision.capture_frame()

    match = wargroove_ctrl.vision.find_template_match("data/wargroove-icon.PNG")

    wargroove_ctrl.mouse.move_mouse(match.mid_point[0], match.mid_point[1])
    wargroove_ctrl.mouse.left_mouse_click()

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_building("cherrystone_stronghold")

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_unit("cherrystone_commander_mercia")

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_unit("cherrystone_soldier")

    time.sleep(0.5)
    wargroove_ctrl.vision.capture_frame()
    wargroove_ctrl.mouse_over_unit("cherrystone_villager")


def get_pre_processing_chain_for_tile_info_panel_ocr():
    pre_processing_step_chain = cmp504.image_processing.ImageProcessingStepChain()
    pre_processing_step_chain.append(cmp504.image_processing.BGR2Grayscale())
    pre_processing_step_chain.append(cmp504.image_processing.Resize(3, 3))
    return pre_processing_step_chain
