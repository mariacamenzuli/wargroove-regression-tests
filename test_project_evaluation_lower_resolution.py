import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationLowerResolution(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/change-in-resolution/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354 * 0.5, 392 * 0.5)
        assert_that(match.location[1]).is_between(122 * 0.5, 176 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 0.5), 1)

    def test_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 0.5), 1)

    def test_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 0.5), 1)

    def test_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(360 * 0.5, 390 * 0.5)
        assert_that(match.location[1]).is_between(220 * 0.5, 274 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354 * 0.5, 404 * 0.5)
        assert_that(match.location[1]).is_between(320 * 0.5, 368 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506 * 0.5, 536 * 0.5)
        assert_that(match.location[1]).is_between(124 * 0.5, 176 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500 * 0.5, 536 * 0.5)
        assert_that(match.location[1]).is_between(218 * 0.5, 272 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 0.5), 1)

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502 * 0.5, 554 * 0.5)
        assert_that(match.location[1]).is_between(324 * 0.5, 368 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 0.5), 1)

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596 * 0.5, 642 * 0.5)
        assert_that(match.location[1]).is_between(138 * 0.5, 176 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592 * 0.5, 636 * 0.5)
        assert_that(match.location[1]).is_between(222 * 0.5, 272 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590 * 0.5, 634 * 0.5)
        assert_that(match.location[1]).is_between(314 * 0.5, 370 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 0.5), 1)

    def test_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 0.5), 1)

    def test_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 0.5), 1)

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692 * 0.5, 732 * 0.5)
        assert_that(match.location[1]).is_between(108 * 0.5, 178 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 0.5), 1)

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693 * 0.5, 744 * 0.5)
        assert_that(match.location[1]).is_between(208 * 0.5, 272 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 0.5), 1)

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686 * 0.5, 742 * 0.5)
        assert_that(match.location[1]).is_between(319 * 0.5, 370 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 0.5), 1)

    def test_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 0.5), 1)

    def test_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 0.5), 1)

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782 * 0.5, 842 * 0.5)
        assert_that(match.location[1]).is_between(138 * 0.5, 180 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 0.5), 1)

    def test_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 0.5), 1)

    def test_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 0.5), 1)

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782 * 0.5, 844 * 0.5)
        assert_that(match.location[1]).is_between(226 * 0.5, 276 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 0.5), 1)

    def test_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 0.5), 1)

    def test_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 0.5), 1)

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770 * 0.5, 830 * 0.5)
        assert_that(match.location[1]).is_between(300 * 0.5, 362 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 0.5), 1)

    def test_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 0.5), 1)

    def test_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 0.5), 1)

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876 * 0.5, 938 * 0.5)
        assert_that(match.location[1]).is_between(112 * 0.5, 168 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 0.5), 1)

    def test_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 0.5), 1)

    def test_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 0.5), 1)

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878 * 0.5, 926 * 0.5)
        assert_that(match.location[1]).is_between(214 * 0.5, 264 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 0.5), 1)

    def test_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 0.5), 1)

    def test_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 0.5), 1)

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872 * 0.5, 934 * 0.5)
        assert_that(match.location[1]).is_between(320 * 0.5, 354 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(450 * 0.5, 502 * 0.5)
        assert_that(match.location[1]).is_between(520 * 0.5, 560 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 0.5), 1)

    def test_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(544 * 0.5, 596 * 0.5)
        assert_that(match.location[1]).is_between(530 * 0.5, 569 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(641 * 0.5, 695 * 0.5)
        assert_that(match.location[1]).is_between(516 * 0.5, 564 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 0.5), 1)

    def test_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(732 * 0.5, 794 * 0.5)
        assert_that(match.location[1]).is_between(516 * 0.5, 564 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 0.5), 1)

    def test_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 0.5), 1)

    def test_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 0.5), 1)

    def test_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(840 * 0.5, 886 * 0.5)
        assert_that(match.location[1]).is_between(520 * 0.5, 562 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                        threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(546 * 0.5, 596 * 0.5)
        assert_that(match.location[1]).is_between(420 * 0.5, 480 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 0.5), 1)

    def test_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 0.5), 1)

    def test_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 0.5), 1)

    def test_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(972 * 0.5, 1026 * 0.5)
        assert_that(match.location[1]).is_between(516 * 0.5, 578 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 0.5), 1)

    def test_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 0.5), 1)

    def test_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 0.5), 1)

    def test_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446 * 0.5, 496 * 0.5)
        assert_that(match.location[1]).is_between(402 * 0.5, 482 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 0.5), 1)

    def test_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 0.5), 1)

    def test_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 0.5), 1)

    def test_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(738 * 0.5, 784 * 0.5)
        assert_that(match.location[1]).is_between(416 * 0.5, 476 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 0.5), 1)

    def test_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638 * 0.5, 690 * 0.5)
        assert_that(match.location[1]).is_between(424 * 0.5, 480 * 0.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 0.5), 1)

    def test_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 0.5), 1)

    def test_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 0.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 0.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 0.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 0.5), 1)

    def test_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(302 * 0.5, 354 * 0.5)
        assert_that(match.location[1]).is_between(516 * 0.5, 574 * 0.5)
