import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationSTM(unittest.TestCase):
    frame_count = 75

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/idle-animation/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                    threshold=threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 4)

    def test_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 4)

    def test_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    def test_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    def test_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    def test_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    def test_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    def test_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    def test_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    def test_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 4)

    def test_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 4)

    def test_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    def test_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    def test_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    def test_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 4)

    def test_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 4)

    def test_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 4)

    def test_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 4)

    def test_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 4)

    def test_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 4)

    def test_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 4)

    def test_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 4)

    def test_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 4)

    def test_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 4)

    def test_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 4)

    def test_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 4)

    def test_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    def test_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    def test_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    def test_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    def test_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    def test_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    def test_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    def test_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    def test_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 4)

    def test_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 4)

    def test_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    def test_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    def test_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 4)

    def test_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 4)

    def test_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 4)

    def test_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 4)

    def test_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 4)

    def test_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 4)

    def test_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    def test_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    def test_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 4)

    def test_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 4)

    def test_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 4)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 4)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 4)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 4)
