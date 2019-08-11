import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationUnitMoveHuMoments(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/moving-targets/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(920, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(920, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(920, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(888, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(918, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    def test_frame_2_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(888, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(918, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    def test_frame_2_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(888, 4)
        assert_that(match.top_left[1]).is_close_to(220, 4)
        assert_that(match.bottom_right[0]).is_close_to(918, 4)
        assert_that(match.bottom_right[1]).is_close_to(274, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(932, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_2_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(932, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_2_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(932, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(746, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(746, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(746, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(740, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(740, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(740, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(742, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_2_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(742, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_2_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(742, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(644, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(690, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(644, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(690, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(644, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(690, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(640, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(684, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(640, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(684, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(640, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(684, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(682, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(682, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(682, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(548, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(588, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_frame_2_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(548, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(588, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_frame_2_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(548, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(588, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(549, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(600, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(549, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(600, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(549, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(600, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(598, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(598, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(598, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(506, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_frame_2_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(506, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_frame_2_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(506, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(508, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_frame_2_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(508, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_frame_2_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(508, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(434, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(494, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_frame_2_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(434, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(494, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_frame_2_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(434, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(494, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(346, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(408, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_frame_2_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(346, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(408, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_frame_2_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(346, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(408, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(348, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(396, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_frame_2_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(348, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(396, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_frame_2_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(348, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(396, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(342, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_frame_2_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(342, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_frame_2_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(342, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(786, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(838, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    def test_frame_2_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(786, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(838, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    def test_frame_2_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(786, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(838, 4)
        assert_that(match.bottom_right[1]).is_close_to(560, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(688, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(740, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    def test_frame_2_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(688, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(740, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    def test_frame_2_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(688, 6)
        assert_that(match.top_left[1]).is_close_to(530, 6)
        assert_that(match.bottom_right[0]).is_close_to(740, 6)
        assert_that(match.bottom_right[1]).is_close_to(560, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(593, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(647, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_frame_2_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(593, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(647, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_frame_2_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(593, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(647, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(492, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_frame_2_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(492, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    def test_frame_2_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(492, 4)
        assert_that(match.top_left[1]).is_close_to(516, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(564, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(408, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(454, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    def test_frame_2_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(408, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(454, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    def test_frame_2_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(408, 4)
        assert_that(match.top_left[1]).is_close_to(520, 4)
        assert_that(match.bottom_right[0]).is_close_to(454, 4)
        assert_that(match.bottom_right[1]).is_close_to(562, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(642, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(692, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    def test_frame_2_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(642, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(692, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    def test_frame_2_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(642, 4)
        assert_that(match.top_left[1]).is_close_to(420, 4)
        assert_that(match.bottom_right[0]).is_close_to(692, 4)
        assert_that(match.bottom_right[1]).is_close_to(480, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(299, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(353, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    def test_frame_2_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(299, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(353, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    def test_frame_2_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(299, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(353, 6)
        assert_that(match.bottom_right[1]).is_close_to(578, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(736, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(786, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    def test_frame_2_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(736, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(786, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    def test_frame_2_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(736, 4)
        assert_that(match.top_left[1]).is_close_to(402, 4)
        assert_that(match.bottom_right[0]).is_close_to(786, 4)
        assert_that(match.bottom_right[1]).is_close_to(482, 4)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(496, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    def test_frame_2_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(496, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    def test_frame_2_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(450, 6)
        assert_that(match.top_left[1]).is_close_to(416, 6)
        assert_that(match.bottom_right[0]).is_close_to(496, 6)
        assert_that(match.bottom_right[1]).is_close_to(476, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(594, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    def test_frame_2_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(594, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    def test_frame_2_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 6)
        assert_that(match.top_left[1]).is_close_to(424, 6)
        assert_that(match.bottom_right[0]).is_close_to(594, 6)
        assert_that(match.bottom_right[1]).is_close_to(480, 6)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_1_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
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

    def test_frame_2_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(974, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1024, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)

    def test_frame_2_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(974, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1024, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)

    def test_frame_2_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(974, 6)
        assert_that(match.top_left[1]).is_close_to(516, 6)
        assert_that(match.bottom_right[0]).is_close_to(1024, 6)
        assert_that(match.bottom_right[1]).is_close_to(574, 6)
