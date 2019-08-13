import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationSTMILC(unittest.TestCase):
    frame_count = 75

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/idle-animation/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        incorrect_location_count = 0
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
        incorrect_location_count = 0
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
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (354 - 4) or match.top_left[0] > (354 + 4)) or (match.top_left[1] < (122 - 4) or match.top_left[1] > (122 + 4)) or (match.bottom_right[0] > (392 + 4) or match.bottom_right[0] < (392 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (360 - 4) or match.top_left[0] > (360 + 4)) or (match.top_left[1] < (220 - 4) or match.top_left[1] > (220 + 4)) or (match.bottom_right[0] > (390 + 4) or match.bottom_right[0] < (390 - 4)) or (match.bottom_right[1] > (274 + 4) or match.bottom_right[1] < (274 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (360 - 4) or match.top_left[0] > (360 + 4)) or (match.top_left[1] < (220 - 4) or match.top_left[1] > (220 + 4)) or (match.bottom_right[0] > (390 + 4) or match.bottom_right[0] < (390 - 4)) or (match.bottom_right[1] > (274 + 4) or match.bottom_right[1] < (274 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (360 - 4) or match.top_left[0] > (360 + 4)) or (match.top_left[1] < (220 - 4) or match.top_left[1] > (220 + 4)) or (match.bottom_right[0] > (390 + 4) or match.bottom_right[0] < (390 - 4)) or (match.bottom_right[1] > (274 + 4) or match.bottom_right[1] < (274 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (354 - 4) or match.top_left[0] > (354 + 4)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (404 + 4) or match.bottom_right[0] < (404 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (354 - 4) or match.top_left[0] > (354 + 4)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (404 + 4) or match.bottom_right[0] < (404 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (354 - 4) or match.top_left[0] > (354 + 4)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (404 + 4) or match.bottom_right[0] < (404 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (506 - 4) or match.top_left[0] > (506 + 4)) or (match.top_left[1] < (124 - 4) or match.top_left[1] > (124 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (506 - 4) or match.top_left[0] > (506 + 4)) or (match.top_left[1] < (124 - 4) or match.top_left[1] > (124 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (506 - 4) or match.top_left[0] > (506 + 4)) or (match.top_left[1] < (124 - 4) or match.top_left[1] > (124 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (500 - 4) or match.top_left[0] > (500 + 4)) or (match.top_left[1] < (218 - 4) or match.top_left[1] > (218 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (500 - 4) or match.top_left[0] > (500 + 4)) or (match.top_left[1] < (218 - 4) or match.top_left[1] > (218 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (500 - 4) or match.top_left[0] > (500 + 4)) or (match.top_left[1] < (218 - 4) or match.top_left[1] > (218 + 4)) or (match.bottom_right[0] > (536 + 4) or match.bottom_right[0] < (536 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (502 - 4) or match.top_left[0] > (502 + 4)) or (match.top_left[1] < (324 - 4) or match.top_left[1] > (324 + 4)) or (match.bottom_right[0] > (554 + 4) or match.bottom_right[0] < (554 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (502 - 4) or match.top_left[0] > (502 + 4)) or (match.top_left[1] < (324 - 4) or match.top_left[1] > (324 + 4)) or (match.bottom_right[0] > (554 + 4) or match.bottom_right[0] < (554 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (502 - 4) or match.top_left[0] > (502 + 4)) or (match.top_left[1] < (324 - 4) or match.top_left[1] > (324 + 4)) or (match.bottom_right[0] > (554 + 4) or match.bottom_right[0] < (554 - 4)) or (match.bottom_right[1] > (368 + 4) or match.bottom_right[1] < (368 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (596 - 4) or match.top_left[0] > (596 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (642 + 4) or match.bottom_right[0] < (642 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (596 - 4) or match.top_left[0] > (596 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (642 + 4) or match.bottom_right[0] < (642 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (596 - 4) or match.top_left[0] > (596 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (642 + 4) or match.bottom_right[0] < (642 - 4)) or (match.bottom_right[1] > (176 + 4) or match.bottom_right[1] < (176 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (592 - 4) or match.top_left[0] > (592 + 4)) or (match.top_left[1] < (222 - 4) or match.top_left[1] > (222 + 4)) or (match.bottom_right[0] > (636 + 4) or match.bottom_right[0] < (636 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (592 - 4) or match.top_left[0] > (592 + 4)) or (match.top_left[1] < (222 - 4) or match.top_left[1] > (222 + 4)) or (match.bottom_right[0] > (636 + 4) or match.bottom_right[0] < (636 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (592 - 4) or match.top_left[0] > (592 + 4)) or (match.top_left[1] < (222 - 4) or match.top_left[1] > (222 + 4)) or (match.bottom_right[0] > (636 + 4) or match.bottom_right[0] < (636 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (590 - 4) or match.top_left[0] > (590 + 4)) or (match.top_left[1] < (314 - 4) or match.top_left[1] > (314 + 4)) or (match.bottom_right[0] > (634 + 4) or match.bottom_right[0] < (634 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (590 - 4) or match.top_left[0] > (590 + 4)) or (match.top_left[1] < (314 - 4) or match.top_left[1] > (314 + 4)) or (match.bottom_right[0] > (634 + 4) or match.bottom_right[0] < (634 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (590 - 4) or match.top_left[0] > (590 + 4)) or (match.top_left[1] < (314 - 4) or match.top_left[1] > (314 + 4)) or (match.bottom_right[0] > (634 + 4) or match.bottom_right[0] < (634 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (692 - 4) or match.top_left[0] > (692 + 4)) or (match.top_left[1] < (108 - 4) or match.top_left[1] > (108 + 4)) or (match.bottom_right[0] > (732 + 4) or match.bottom_right[0] < (732 - 4)) or (match.bottom_right[1] > (178 + 4) or match.bottom_right[1] < (178 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (692 - 4) or match.top_left[0] > (692 + 4)) or (match.top_left[1] < (108 - 4) or match.top_left[1] > (108 + 4)) or (match.bottom_right[0] > (732 + 4) or match.bottom_right[0] < (732 - 4)) or (match.bottom_right[1] > (178 + 4) or match.bottom_right[1] < (178 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (692 - 4) or match.top_left[0] > (692 + 4)) or (match.top_left[1] < (108 - 4) or match.top_left[1] > (108 + 4)) or (match.bottom_right[0] > (732 + 4) or match.bottom_right[0] < (732 - 4)) or (match.bottom_right[1] > (178 + 4) or match.bottom_right[1] < (178 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (693 - 4) or match.top_left[0] > (693 + 4)) or (match.top_left[1] < (208 - 4) or match.top_left[1] > (208 + 4)) or (match.bottom_right[0] > (744 + 4) or match.bottom_right[0] < (744 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (693 - 4) or match.top_left[0] > (693 + 4)) or (match.top_left[1] < (208 - 4) or match.top_left[1] > (208 + 4)) or (match.bottom_right[0] > (744 + 4) or match.bottom_right[0] < (744 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (693 - 4) or match.top_left[0] > (693 + 4)) or (match.top_left[1] < (208 - 4) or match.top_left[1] > (208 + 4)) or (match.bottom_right[0] > (744 + 4) or match.bottom_right[0] < (744 - 4)) or (match.bottom_right[1] > (272 + 4) or match.bottom_right[1] < (272 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (686 - 4) or match.top_left[0] > (686 + 4)) or (match.top_left[1] < (319 - 4) or match.top_left[1] > (319 + 4)) or (match.bottom_right[0] > (742 + 4) or match.bottom_right[0] < (742 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (686 - 4) or match.top_left[0] > (686 + 4)) or (match.top_left[1] < (319 - 4) or match.top_left[1] > (319 + 4)) or (match.bottom_right[0] > (742 + 4) or match.bottom_right[0] < (742 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (686 - 4) or match.top_left[0] > (686 + 4)) or (match.top_left[1] < (319 - 4) or match.top_left[1] > (319 + 4)) or (match.bottom_right[0] > (742 + 4) or match.bottom_right[0] < (742 - 4)) or (match.bottom_right[1] > (370 + 4) or match.bottom_right[1] < (370 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (842 + 4) or match.bottom_right[0] < (842 - 4)) or (match.bottom_right[1] > (180 + 4) or match.bottom_right[1] < (180 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (842 + 4) or match.bottom_right[0] < (842 - 4)) or (match.bottom_right[1] > (180 + 4) or match.bottom_right[1] < (180 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (138 - 4) or match.top_left[1] > (138 + 4)) or (match.bottom_right[0] > (842 + 4) or match.bottom_right[0] < (842 - 4)) or (match.bottom_right[1] > (180 + 4) or match.bottom_right[1] < (180 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (226 - 4) or match.top_left[1] > (226 + 4)) or (match.bottom_right[0] > (844 + 4) or match.bottom_right[0] < (844 - 4)) or (match.bottom_right[1] > (276 + 4) or match.bottom_right[1] < (276 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (226 - 4) or match.top_left[1] > (226 + 4)) or (match.bottom_right[0] > (844 + 4) or match.bottom_right[0] < (844 - 4)) or (match.bottom_right[1] > (276 + 4) or match.bottom_right[1] < (276 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (782 - 4) or match.top_left[0] > (782 + 4)) or (match.top_left[1] < (226 - 4) or match.top_left[1] > (226 + 4)) or (match.bottom_right[0] > (844 + 4) or match.bottom_right[0] < (844 - 4)) or (match.bottom_right[1] > (276 + 4) or match.bottom_right[1] < (276 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (770 - 4) or match.top_left[0] > (770 + 4)) or (match.top_left[1] < (300 - 4) or match.top_left[1] > (300 + 4)) or (match.bottom_right[0] > (830 + 4) or match.bottom_right[0] < (830 - 4)) or (match.bottom_right[1] > (362 + 4) or match.bottom_right[1] < (362 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (770 - 4) or match.top_left[0] > (770 + 4)) or (match.top_left[1] < (300 - 4) or match.top_left[1] > (300 + 4)) or (match.bottom_right[0] > (830 + 4) or match.bottom_right[0] < (830 - 4)) or (match.bottom_right[1] > (362 + 4) or match.bottom_right[1] < (362 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (770 - 4) or match.top_left[0] > (770 + 4)) or (match.top_left[1] < (300 - 4) or match.top_left[1] > (300 + 4)) or (match.bottom_right[0] > (830 + 4) or match.bottom_right[0] < (830 - 4)) or (match.bottom_right[1] > (362 + 4) or match.bottom_right[1] < (362 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 4) or match.top_left[1] > (112 + 4)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 4) or match.bottom_right[1] < (168 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 4) or match.top_left[1] > (112 + 4)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 4) or match.bottom_right[1] < (168 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 4) or match.top_left[1] > (112 + 4)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 4) or match.bottom_right[1] < (168 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (878 - 4) or match.top_left[0] > (878 + 4)) or (match.top_left[1] < (214 - 4) or match.top_left[1] > (214 + 4)) or (match.bottom_right[0] > (926 + 4) or match.bottom_right[0] < (926 - 4)) or (match.bottom_right[1] > (264 + 4) or match.bottom_right[1] < (264 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (878 - 4) or match.top_left[0] > (878 + 4)) or (match.top_left[1] < (214 - 4) or match.top_left[1] > (214 + 4)) or (match.bottom_right[0] > (926 + 4) or match.bottom_right[0] < (926 - 4)) or (match.bottom_right[1] > (264 + 4) or match.bottom_right[1] < (264 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (878 - 4) or match.top_left[0] > (878 + 4)) or (match.top_left[1] < (214 - 4) or match.top_left[1] > (214 + 4)) or (match.bottom_right[0] > (926 + 4) or match.bottom_right[0] < (926 - 4)) or (match.bottom_right[1] > (264 + 4) or match.bottom_right[1] < (264 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 4) or match.bottom_right[1] < (354 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 4) or match.bottom_right[1] < (354 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 4) or match.top_left[1] > (320 + 4)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 4) or match.bottom_right[1] < (354 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (450 - 4) or match.top_left[0] > (450 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (502 + 4) or match.bottom_right[0] < (502 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (450 - 4) or match.top_left[0] > (450 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (502 + 4) or match.bottom_right[0] < (502 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (450 - 4) or match.top_left[0] > (450 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (502 + 4) or match.bottom_right[0] < (502 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (544 - 4) or match.top_left[0] > (544 + 4)) or (match.top_left[1] < (530 - 4) or match.top_left[1] > (530 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (544 - 4) or match.top_left[0] > (544 + 4)) or (match.top_left[1] < (530 - 4) or match.top_left[1] > (530 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (544 - 4) or match.top_left[0] > (544 + 4)) or (match.top_left[1] < (530 - 4) or match.top_left[1] > (530 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (560 + 4) or match.bottom_right[1] < (560 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (641 - 4) or match.top_left[0] > (641 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (695 + 4) or match.bottom_right[0] < (695 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (641 - 4) or match.top_left[0] > (641 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (695 + 4) or match.bottom_right[0] < (695 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (641 - 4) or match.top_left[0] > (641 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (695 + 4) or match.bottom_right[0] < (695 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (732 - 4) or match.top_left[0] > (732 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (794 + 4) or match.bottom_right[0] < (794 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (732 - 4) or match.top_left[0] > (732 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (794 + 4) or match.bottom_right[0] < (794 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (732 - 4) or match.top_left[0] > (732 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (794 + 4) or match.bottom_right[0] < (794 - 4)) or (match.bottom_right[1] > (564 + 4) or match.bottom_right[1] < (564 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (840 - 4) or match.top_left[0] > (840 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (886 + 4) or match.bottom_right[0] < (886 - 4)) or (match.bottom_right[1] > (562 + 4) or match.bottom_right[1] < (562 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (840 - 4) or match.top_left[0] > (840 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (886 + 4) or match.bottom_right[0] < (886 - 4)) or (match.bottom_right[1] > (562 + 4) or match.bottom_right[1] < (562 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (840 - 4) or match.top_left[0] > (840 + 4)) or (match.top_left[1] < (520 - 4) or match.top_left[1] > (520 + 4)) or (match.bottom_right[0] > (886 + 4) or match.bottom_right[0] < (886 - 4)) or (match.bottom_right[1] > (562 + 4) or match.bottom_right[1] < (562 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (546 - 4) or match.top_left[0] > (546 + 4)) or (match.top_left[1] < (420 - 4) or match.top_left[1] > (420 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (546 - 4) or match.top_left[0] > (546 + 4)) or (match.top_left[1] < (420 - 4) or match.top_left[1] > (420 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (546 - 4) or match.top_left[0] > (546 + 4)) or (match.top_left[1] < (420 - 4) or match.top_left[1] > (420 + 4)) or (match.bottom_right[0] > (596 + 4) or match.bottom_right[0] < (596 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (972 - 4) or match.top_left[0] > (972 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (1026 + 4) or match.bottom_right[0] < (1026 - 4)) or (match.bottom_right[1] > (578 + 4) or match.bottom_right[1] < (578 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (972 - 4) or match.top_left[0] > (972 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (1026 + 4) or match.bottom_right[0] < (1026 - 4)) or (match.bottom_right[1] > (578 + 4) or match.bottom_right[1] < (578 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (972 - 4) or match.top_left[0] > (972 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (1026 + 4) or match.bottom_right[0] < (1026 - 4)) or (match.bottom_right[1] > (578 + 4) or match.bottom_right[1] < (578 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (446 - 4) or match.top_left[0] > (446 + 4)) or (match.top_left[1] < (402 - 4) or match.top_left[1] > (402 + 4)) or (match.bottom_right[0] > (496 + 4) or match.bottom_right[0] < (496 - 4)) or (match.bottom_right[1] > (482 + 4) or match.bottom_right[1] < (482 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (446 - 4) or match.top_left[0] > (446 + 4)) or (match.top_left[1] < (402 - 4) or match.top_left[1] > (402 + 4)) or (match.bottom_right[0] > (496 + 4) or match.bottom_right[0] < (496 - 4)) or (match.bottom_right[1] > (482 + 4) or match.bottom_right[1] < (482 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (446 - 4) or match.top_left[0] > (446 + 4)) or (match.top_left[1] < (402 - 4) or match.top_left[1] > (402 + 4)) or (match.bottom_right[0] > (496 + 4) or match.bottom_right[0] < (496 - 4)) or (match.bottom_right[1] > (482 + 4) or match.bottom_right[1] < (482 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (738 - 4) or match.top_left[0] > (738 + 4)) or (match.top_left[1] < (416 - 4) or match.top_left[1] > (416 + 4)) or (match.bottom_right[0] > (784 + 4) or match.bottom_right[0] < (784 - 4)) or (match.bottom_right[1] > (476 + 4) or match.bottom_right[1] < (476 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (738 - 4) or match.top_left[0] > (738 + 4)) or (match.top_left[1] < (416 - 4) or match.top_left[1] > (416 + 4)) or (match.bottom_right[0] > (784 + 4) or match.bottom_right[0] < (784 - 4)) or (match.bottom_right[1] > (476 + 4) or match.bottom_right[1] < (476 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (738 - 4) or match.top_left[0] > (738 + 4)) or (match.top_left[1] < (416 - 4) or match.top_left[1] > (416 + 4)) or (match.bottom_right[0] > (784 + 4) or match.bottom_right[0] < (784 - 4)) or (match.bottom_right[1] > (476 + 4) or match.bottom_right[1] < (476 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (638 - 4) or match.top_left[0] > (638 + 4)) or (match.top_left[1] < (424 - 4) or match.top_left[1] > (424 + 4)) or (match.bottom_right[0] > (690 + 4) or match.bottom_right[0] < (690 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (638 - 4) or match.top_left[0] > (638 + 4)) or (match.top_left[1] < (424 - 4) or match.top_left[1] > (424 + 4)) or (match.bottom_right[0] > (690 + 4) or match.bottom_right[0] < (690 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (638 - 4) or match.top_left[0] > (638 + 4)) or (match.top_left[1] < (424 - 4) or match.top_left[1] > (424 + 4)) or (match.bottom_right[0] > (690 + 4) or match.bottom_right[0] < (690 - 4)) or (match.bottom_right[1] > (480 + 4) or match.bottom_right[1] < (480 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold)

            if match is not None:
                if (match.top_left[0] < (302 - 4) or match.top_left[0] > (302 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (352 + 4) or match.bottom_right[0] < (352 - 4)) or (match.bottom_right[1] > (574 + 4) or match.bottom_right[1] < (574 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (302 - 4) or match.top_left[0] > (302 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (352 + 4) or match.bottom_right[0] < (352 - 4)) or (match.bottom_right[1] > (574 + 4) or match.bottom_right[1] < (574 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    def test_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                        threshold=threshold,
                                                                        method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

            if match is not None:
                if (match.top_left[0] < (302 - 4) or match.top_left[0] > (302 + 4)) or (match.top_left[1] < (516 - 4) or match.top_left[1] > (516 + 4)) or (match.bottom_right[0] > (352 + 4) or match.bottom_right[0] < (352 - 4)) or (match.bottom_right[1] > (574 + 4) or match.bottom_right[1] < (574 - 4)):
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)
