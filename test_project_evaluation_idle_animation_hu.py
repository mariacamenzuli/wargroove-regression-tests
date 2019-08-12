import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationHuMoments(unittest.TestCase):
    frame_count = 75

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/idle-animation/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(122, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(392, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 6)

    def test_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 6)

    def test_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(360, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(220, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(390, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(274, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    def test_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    def test_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(354, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(404, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(506, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(124, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(500, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(218, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(536, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    def test_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    def test_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(324, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(554, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(368, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    def test_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(642, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(176, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(592, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(222, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(636, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    def test_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    def test_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(590, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(314, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(634, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 6)

    def test_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 6)

    def test_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(692, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(108, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(178, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    def test_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(693, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(208, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(744, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(272, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    def test_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    def test_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(686, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(319, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(742, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(370, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 6)

    def test_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 6)

    def test_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(138, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(842, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(180, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 6)

    def test_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 6)

    def test_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(782, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(226, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(844, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(276, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 6)

    def test_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 6)

    def test_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(770, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(300, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(830, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(362, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 6)

    def test_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 6)

    def test_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(876, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(112, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(938, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(168, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 6)

    def test_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 6)

    def test_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(878, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(214, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(926, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(264, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 6)

    def test_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 6)

    def test_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(872, 8)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(320, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(934, 8)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(354, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    def test_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    def test_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(450, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(502, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    def test_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    def test_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(544, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(530, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(560, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    def test_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    def test_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(641, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(695, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    def test_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    def test_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(732, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(794, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(564, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 6)

    def test_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 6)

    def test_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(840, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(520, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(886, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(562, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    def test_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    def test_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(546, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(420, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(596, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 6)

    def test_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 6)

    def test_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(972, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(1026, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(578, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 6)

    def test_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 6)

    def test_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(446, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(402, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(496, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(482, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 6)

    def test_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 6)

    def test_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(738, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(416, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(784, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(476, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    def test_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    def test_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(638, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(424, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(690, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(480, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 6)

    def test_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 6)

    def test_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.top_left[0]).described_as('top left x value in frame ' + str(frame)).is_close_to(302, 6)
            assert_that(match.top_left[1]).described_as('top left y value in frame ' + str(frame)).is_close_to(516, 6)
            assert_that(match.bottom_right[0]).described_as('bottom left x value in frame ' + str(frame)).is_close_to(352, 6)
            assert_that(match.bottom_right[1]).described_as('bottom left y value in frame ' + str(frame)).is_close_to(574, 6)
