import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationMenu(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/menus/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MAIN MENU BUTTONS ON IMAGE 1 ----------------------------------
    # ----------------------------------------------------------------------------

    def test_main_menu_button_1_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_2_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_3_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_4_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_5_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_6_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/1.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MAIN MENU BUTTONS ON IMAGE 2 ----------------------------------
    # ----------------------------------------------------------------------------

    def test_main_menu_button_1_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_2_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_3_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_4_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_5_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_6_standard_template_matching_cross_corr_img2(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_corr_coeff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_square_diff_img2(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/2.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MAIN MENU BUTTONS ON IMAGE 3 ----------------------------------
    # ----------------------------------------------------------------------------

    def test_main_menu_button_1_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_2_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_3_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_4_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_5_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_6_standard_template_matching_cross_corr_img3(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_corr_coeff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_square_diff_img3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/3.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MAIN MENU BUTTONS ON IMAGE 4 ----------------------------------
    # ----------------------------------------------------------------------------

    def test_main_menu_button_1_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_2_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_3_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_4_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_5_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_6_standard_template_matching_cross_corr_img4(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_corr_coeff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/4.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MAIN MENU BUTTONS ON IMAGE 5 ----------------------------------
    # ----------------------------------------------------------------------------

    def test_main_menu_button_1_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_1_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/single_player_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(584)
        assert_that(match.top_left[1]).is_equal_to(376)
        assert_that(match.bottom_right[0]).is_equal_to(696)
        assert_that(match.bottom_right[1]).is_equal_to(398)

    def test_main_menu_button_2_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_2_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/multiplayer_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(410)
        assert_that(match.bottom_right[0]).is_equal_to(688)
        assert_that(match.bottom_right[1]).is_equal_to(432)

    def test_main_menu_button_3_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_3_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/custom_content_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(572)
        assert_that(match.top_left[1]).is_equal_to(444)
        assert_that(match.bottom_right[0]).is_equal_to(708)
        assert_that(match.bottom_right[1]).is_equal_to(462)

    def test_main_menu_button_4_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_4_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/extras_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(612)
        assert_that(match.top_left[1]).is_equal_to(478)
        assert_that(match.bottom_right[0]).is_equal_to(668)
        assert_that(match.bottom_right[1]).is_equal_to(496)

    def test_main_menu_button_5_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_5_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/options_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(608)
        assert_that(match.top_left[1]).is_equal_to(512)
        assert_that(match.bottom_right[0]).is_equal_to(672)
        assert_that(match.bottom_right[1]).is_equal_to(534)

    def test_main_menu_button_6_standard_template_matching_cross_corr_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_corr_coeff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_main_menu_button_6_standard_template_matching_square_diff_img5(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'main-menu/5.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('main_menu/exit_button',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(624)
        assert_that(match.top_left[1]).is_equal_to(546)
        assert_that(match.bottom_right[0]).is_equal_to(656)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_mercia_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_mercia_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_mercia_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-mercia.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_mercia_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_emeric_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_standard_template_matching_square_diff_img4(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_emeric_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_emeric_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-emeric.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_emeric_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR PORTRAIT INGAME ----------------------------------
    # ----------------------------------------------------------------------------

    def test_in_game_caesar_portrait_standard_template_matching_cross_corr(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_standard_template_matching_square_diff(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('gameplay/wargroove_caesar_portrait',
                                                                   threshold=threshold,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.ui_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)

    def test_in_game_caesar_portrait_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.ui_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'in-game/hud-mirror/portrait-caesar.png')
        match = wargroove_ctrl.find_ui_item_with_hu_moment_template_matching('gameplay/wargroove_caesar_portrait',
                                                                             threshold=threshold,
                                                                             method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(13)
        assert_that(match.top_left[1]).is_equal_to(13)
        assert_that(match.bottom_right[0]).is_equal_to(84)
        assert_that(match.bottom_right[1]).is_equal_to(86)
