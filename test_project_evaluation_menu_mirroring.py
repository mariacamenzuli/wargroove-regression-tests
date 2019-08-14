import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationMenuMirroring(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/menus/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_mercia_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_emeric_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_caesar_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar-mirrored.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(153)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(224)
        assert_that(match.bottom_right[1]).is_equal_to(86)
