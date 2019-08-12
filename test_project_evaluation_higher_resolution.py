import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationHigherResolution(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/change-in-resolution/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354 * 1.5, 392 * 1.5)
        assert_that(match.location[1]).is_between(122 * 1.5, 176 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)

    def test_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)

    def test_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)

    def test_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(360 * 1.5, 390 * 1.5)
        assert_that(match.location[1]).is_between(220 * 1.5, 274 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354 * 1.5, 404 * 1.5)
        assert_that(match.location[1]).is_between(320 * 1.5, 368 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506 * 1.5, 536 * 1.5)
        assert_that(match.location[1]).is_between(124 * 1.5, 176 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500 * 1.5, 536 * 1.5)
        assert_that(match.location[1]).is_between(218 * 1.5, 272 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502 * 1.5, 554 * 1.5)
        assert_that(match.location[1]).is_between(324 * 1.5, 368 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596 * 1.5, 642 * 1.5)
        assert_that(match.location[1]).is_between(138 * 1.5, 176 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592 * 1.5, 636 * 1.5)
        assert_that(match.location[1]).is_between(222 * 1.5, 272 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590 * 1.5, 634 * 1.5)
        assert_that(match.location[1]).is_between(314 * 1.5, 370 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)

    def test_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)

    def test_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692 * 1.5, 732 * 1.5)
        assert_that(match.location[1]).is_between(108 * 1.5, 178 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693 * 1.5, 744 * 1.5)
        assert_that(match.location[1]).is_between(208 * 1.5, 272 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686 * 1.5, 742 * 1.5)
        assert_that(match.location[1]).is_between(319 * 1.5, 370 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)

    def test_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)

    def test_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782 * 1.5, 842 * 1.5)
        assert_that(match.location[1]).is_between(138 * 1.5, 180 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)

    def test_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)

    def test_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782 * 1.5, 844 * 1.5)
        assert_that(match.location[1]).is_between(226 * 1.5, 276 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)

    def test_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)

    def test_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770 * 1.5, 830 * 1.5)
        assert_that(match.location[1]).is_between(300 * 1.5, 362 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)

    def test_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)

    def test_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876 * 1.5, 938 * 1.5)
        assert_that(match.location[1]).is_between(112 * 1.5, 168 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)

    def test_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)

    def test_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878 * 1.5, 926 * 1.5)
        assert_that(match.location[1]).is_between(214 * 1.5, 264 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)

    def test_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)

    def test_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872 * 1.5, 934 * 1.5)
        assert_that(match.location[1]).is_between(320 * 1.5, 354 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(450 * 1.5, 502 * 1.5)
        assert_that(match.location[1]).is_between(520 * 1.5, 560 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(544 * 1.5, 596 * 1.5)
        assert_that(match.location[1]).is_between(530 * 1.5, 569 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(641 * 1.5, 695 * 1.5)
        assert_that(match.location[1]).is_between(516 * 1.5, 564 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(732 * 1.5, 794 * 1.5)
        assert_that(match.location[1]).is_between(516 * 1.5, 564 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)

    def test_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)

    def test_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)

    def test_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(840 * 1.5, 886 * 1.5)
        assert_that(match.location[1]).is_between(520 * 1.5, 562 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                        threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(546 * 1.5, 596 * 1.5)
        assert_that(match.location[1]).is_between(420 * 1.5, 480 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)

    def test_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)

    def test_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)

    def test_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(972 * 1.5, 1026 * 1.5)
        assert_that(match.location[1]).is_between(516 * 1.5, 578 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)

    def test_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)

    def test_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)

    def test_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446 * 1.5, 496 * 1.5)
        assert_that(match.location[1]).is_between(402 * 1.5, 482 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)

    def test_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)

    def test_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)

    def test_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(738 * 1.5, 784 * 1.5)
        assert_that(match.location[1]).is_between(416 * 1.5, 476 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638 * 1.5, 690 * 1.5)
        assert_that(match.location[1]).is_between(424 * 1.5, 480 * 1.5)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

    def test_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

    def test_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

    def test_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1920x1080.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(302 * 1.5, 354 * 1.5)
        assert_that(match.location[1]).is_between(516 * 1.5, 574 * 1.5)
