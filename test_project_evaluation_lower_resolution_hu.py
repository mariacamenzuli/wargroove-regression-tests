import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationLowerResolutionHuMoments(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/change-in-resolution/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(122 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(392 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)

    def test_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)

    def test_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(360 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(220 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(390 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(274 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(354 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(404 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(506 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(124 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(500 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(218 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(536 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)

    def test_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(324 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(554 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(368 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    def test_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(642 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(176 * 1.5), 1)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(592 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(222 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(636 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(590 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(314 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(634 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)

    def test_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)

    def test_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(692 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(108 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(178 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)

    def test_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(693 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(208 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(744 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(272 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)

    def test_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(686 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(319 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(742 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(370 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)

    def test_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)

    def test_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(138 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(842 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(180 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)

    def test_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)

    def test_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(782 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(226 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(844 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(276 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)

    def test_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)

    def test_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(770 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(300 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(830 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(362 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)

    def test_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)

    def test_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(876 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(112 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(938 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(168 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)

    def test_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)

    def test_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(878 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(214 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(926 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(264 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)

    def test_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)

    def test_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(872 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(320 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(934 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(354 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(450 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(502 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)

    def test_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(544 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(530 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(560 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(641 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(695 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)

    def test_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(732 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(794 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(564 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)

    def test_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)

    def test_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(840 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(520 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(886 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(562 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(546 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(420 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(596 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)

    def test_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)

    def test_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(972 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(1026 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(578 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)

    def test_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)

    def test_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(446 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(402 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(496 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(482 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)

    def test_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)

    def test_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(738 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(416 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(784 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(476 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)

    def test_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(638 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(424 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(690 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(480 * 1.5), 1)


    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

    def test_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

    def test_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '640x360.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(int(302 * 1.5), 1)
        assert_that(match.top_left[1]).is_close_to(int(516 * 1.5), 1)
        assert_that(match.bottom_right[0]).is_close_to(int(352 * 1.5), 1)
        assert_that(match.bottom_right[1]).is_close_to(int(574 * 1.5), 1)

