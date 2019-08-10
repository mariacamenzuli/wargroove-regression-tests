import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationPartialOcclusion(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/partial-occlusion/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(392, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(392, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(392, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 392)
        assert_that(match.location[1]).is_between(122, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(360, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(390, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    def test_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(360, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(390, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    def test_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(360, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(390, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    def test_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(360, 390)
        assert_that(match.location[1]).is_between(220, 274)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 404)
        assert_that(match.location[1]).is_between(320, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(506, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(506, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(506, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506, 536)
        assert_that(match.location[1]).is_between(124, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(500, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(500, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(500, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500, 536)
        assert_that(match.location[1]).is_between(218, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(502, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(502, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(502, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502, 554)
        assert_that(match.location[1]).is_between(324, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(596, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(642, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(596, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(642, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(596, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(642, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596, 642)
        assert_that(match.location[1]).is_between(138, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(592, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(636, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(592, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(636, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(592, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(636, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592, 636)
        assert_that(match.location[1]).is_between(222, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(590, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(634, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(590, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(634, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(590, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(634, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590, 634)
        assert_that(match.location[1]).is_between(314, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(692, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(732, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(692, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(732, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(692, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(732, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692, 732)
        assert_that(match.location[1]).is_between(108, 178)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(693, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(744, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(693, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(744, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(693, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(744, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693, 744)
        assert_that(match.location[1]).is_between(208, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(686, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(742, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(686, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(742, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(686, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(742, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686, 742)
        assert_that(match.location[1]).is_between(319, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(842, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(842, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(842, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 842)
        assert_that(match.location[1]).is_between(138, 180)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(844, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(844, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(844, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 844)
        assert_that(match.location[1]).is_between(226, 276)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(770, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(830, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(770, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(830, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(770, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(830, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770, 830)
        assert_that(match.location[1]).is_between(300, 362)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(876, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(938, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(876, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(938, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(876, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(938, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876, 938)
        assert_that(match.location[1]).is_between(112, 168)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(878, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(926, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(878, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(926, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(878, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(926, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878, 926)
        assert_that(match.location[1]).is_between(214, 264)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(872, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(934, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(872, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(934, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(872, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(934, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872, 934)
        assert_that(match.location[1]).is_between(320, 354)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(502, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    def test_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(502, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    def test_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(502, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    def test_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(450, 502)
        assert_that(match.location[1]).is_between(520, 560)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(544, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(596, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    def test_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(544, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(596, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    def test_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(544, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(596, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    def test_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(544, 596)
        assert_that(match.location[1]).is_between(530, 569)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(641, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(695, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(641, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(695, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(641, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(695, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(641, 695)
        assert_that(match.location[1]).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(732, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(732, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(732, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(732, 794)
        assert_that(match.location[1]).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(840, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(886, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    def test_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(840, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(886, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    def test_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(840, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(886, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    def test_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(840, 886)
        assert_that(match.location[1]).is_between(520, 562)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(546, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(596, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    def test_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(546, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(596, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    def test_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(546, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(596, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    def test_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(546, 596)
        assert_that(match.location[1]).is_between(420, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(972, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1026, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    def test_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(972, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1026, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    def test_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(972, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1026, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    def test_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(972, 1026)
        assert_that(match.location[1]).is_between(516, 578)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(496, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    def test_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(496, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    def test_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(496, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    def test_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 496)
        assert_that(match.location[1]).is_between(402, 482)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(738, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(784, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    def test_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(738, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(784, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    def test_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(738, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(784, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    def test_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(738, 784)
        assert_that(match.location[1]).is_between(416, 476)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(690, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    def test_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(690, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    def test_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(690, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    def test_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638, 690)
        assert_that(match.location[1]).is_between(424, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(302, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(354, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)

    def test_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(302, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(354, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)

    def test_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(302, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(354, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)

    def test_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(302, 354)
        assert_that(match.location[1]).is_between(516, 574)
