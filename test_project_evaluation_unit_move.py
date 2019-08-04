import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationUnitMove(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/moving-targets/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_mercia_standard_template_matching(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    @unittest.skip("not evaluating custom... at least not for now")
    def test_frame_1_mercia_hu_moment_template_matching_method_custom(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching_custom('cherrystone_commander_mercia',
                                                                                 threshold=threshold,
                                                                                 binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(392, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_1_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(354, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(392, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_1_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 392)
        assert_that(match.location[1]).is_between(122, 176)

    def test_frame_2_mercia_standard_template_matching(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(920)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(882, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(920, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(882, 920)
        assert_that(match.location[1]).is_between(122, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_villager_standard_template_matching(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(506, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_1_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506, 536)
        assert_that(match.location[1]).is_between(124, 176)

    def test_frame_2_villager_standard_template_matching(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(746)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(746, 4)
        assert_that(match.top_left[1]).is_close_to(124, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(746, 776)
        assert_that(match.location[1]).is_between(124, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_soldier_standard_template_matching(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(500, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(536, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_1_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500, 536)
        assert_that(match.location[1]).is_between(218, 272)

    def test_frame_2_soldier_standard_template_matching(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(740)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(740, 4)
        assert_that(match.top_left[1]).is_close_to(218, 4)
        assert_that(match.bottom_right[0]).is_close_to(776, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(740, 776)
        assert_that(match.location[1]).is_between(218, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_pikeman_standard_template_matching(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(502, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(554, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_1_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502, 554)
        assert_that(match.location[1]).is_between(324, 368)

    def test_frame_2_pikeman_standard_template_matching(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(742)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(742, 4)
        assert_that(match.top_left[1]).is_close_to(324, 4)
        assert_that(match.bottom_right[0]).is_close_to(794, 4)
        assert_that(match.bottom_right[1]).is_close_to(368, 4)

    def test_frame_2_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(742, 794)
        assert_that(match.location[1]).is_between(324, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_battlepup_standard_template_matching(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(596, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(642, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_1_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596, 642)
        assert_that(match.location[1]).is_between(138, 176)

    def test_frame_2_battlepup_standard_template_matching(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(644)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(644, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(690, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_frame_2_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(644, 690)
        assert_that(match.location[1]).is_between(138, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_alchemist_standard_template_matching(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(592, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(636, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_1_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592, 636)
        assert_that(match.location[1]).is_between(222, 272)

    def test_frame_2_alchemist_standard_template_matching(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(640)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(684)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(640, 4)
        assert_that(match.top_left[1]).is_close_to(222, 4)
        assert_that(match.bottom_right[0]).is_close_to(684, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(640, 684)
        assert_that(match.location[1]).is_between(222, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_archer_standard_template_matching(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(590, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(634, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_1_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590, 634)
        assert_that(match.location[1]).is_between(314, 370)

    def test_frame_2_archer_standard_template_matching(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(682)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(638, 4)
        assert_that(match.top_left[1]).is_close_to(314, 4)
        assert_that(match.bottom_right[0]).is_close_to(682, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638, 682)
        assert_that(match.location[1]).is_between(314, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_golem_standard_template_matching(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_1_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(692, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(732, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_frame_1_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692, 732)
        assert_that(match.location[1]).is_between(108, 178)

    def test_frame_2_golem_standard_template_matching(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(548)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(588)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_2_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(548, 4)
        assert_that(match.top_left[1]).is_close_to(108, 4)
        assert_that(match.bottom_right[0]).is_close_to(588, 4)
        assert_that(match.bottom_right[1]).is_close_to(178, 4)

    def test_frame_2_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(548, 588)
        assert_that(match.location[1]).is_between(108, 178)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_knight_standard_template_matching(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(693, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(744, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_1_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693, 744)
        assert_that(match.location[1]).is_between(208, 272)

    def test_frame_2_knight_standard_template_matching(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(549)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(600)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(549, 4)
        assert_that(match.top_left[1]).is_close_to(208, 4)
        assert_that(match.bottom_right[0]).is_close_to(600, 4)
        assert_that(match.bottom_right[1]).is_close_to(272, 4)

    def test_frame_2_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(549, 600)
        assert_that(match.location[1]).is_between(208, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_wagon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(686, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(742, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_1_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686, 742)
        assert_that(match.location[1]).is_between(319, 370)

    def test_frame_2_wagon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(598)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(542, 4)
        assert_that(match.top_left[1]).is_close_to(319, 4)
        assert_that(match.bottom_right[0]).is_close_to(598, 4)
        assert_that(match.bottom_right[1]).is_close_to(370, 4)

    def test_frame_2_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(542, 598)
        assert_that(match.location[1]).is_between(319, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_ballista_standard_template_matching(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_1_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(842, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_frame_1_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 842)
        assert_that(match.location[1]).is_between(138, 180)

    def test_frame_2_ballista_standard_template_matching(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(506)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_2_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(138, 4)
        assert_that(match.bottom_right[0]).is_close_to(506, 4)
        assert_that(match.bottom_right[1]).is_close_to(180, 4)

    def test_frame_2_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 506)
        assert_that(match.location[1]).is_between(138, 180)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_trebuchet_standard_template_matching(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_1_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(782, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(844, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_frame_1_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 844)
        assert_that(match.location[1]).is_between(226, 276)

    def test_frame_2_trebuchet_standard_template_matching(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(508)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_2_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(446, 4)
        assert_that(match.top_left[1]).is_close_to(226, 4)
        assert_that(match.bottom_right[0]).is_close_to(508, 4)
        assert_that(match.bottom_right[1]).is_close_to(276, 4)

    def test_frame_2_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 508)
        assert_that(match.location[1]).is_between(226, 276)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_balloon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_1_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(770, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(830, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_frame_1_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770, 830)
        assert_that(match.location[1]).is_between(300, 362)

    def test_frame_2_balloon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(434)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(494)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_2_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(434, 4)
        assert_that(match.top_left[1]).is_close_to(300, 4)
        assert_that(match.bottom_right[0]).is_close_to(494, 4)
        assert_that(match.bottom_right[1]).is_close_to(362, 4)

    def test_frame_2_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(434, 494)
        assert_that(match.location[1]).is_between(300, 362)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_harpy_standard_template_matching(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_1_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(876, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(938, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_frame_1_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876, 938)
        assert_that(match.location[1]).is_between(112, 168)

    def test_frame_2_harpy_standard_template_matching(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(346)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(408)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_2_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(346, 4)
        assert_that(match.top_left[1]).is_close_to(112, 4)
        assert_that(match.bottom_right[0]).is_close_to(408, 4)
        assert_that(match.bottom_right[1]).is_close_to(168, 4)

    def test_frame_2_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(346, 408)
        assert_that(match.location[1]).is_between(112, 168)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_witch_standard_template_matching(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_1_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(878, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(926, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_frame_1_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878, 926)
        assert_that(match.location[1]).is_between(214, 264)

    def test_frame_2_witch_standard_template_matching(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(348)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(396)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_2_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(348, 4)
        assert_that(match.top_left[1]).is_close_to(214, 4)
        assert_that(match.bottom_right[0]).is_close_to(396, 4)
        assert_that(match.bottom_right[1]).is_close_to(264, 4)

    def test_frame_2_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(348, 396)
        assert_that(match.location[1]).is_between(214, 264)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_dragon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_1_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(872, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(934, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_frame_1_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872, 934)
        assert_that(match.location[1]).is_between(320, 354)

    def test_frame_2_dragon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(342)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_2_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

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
                                                                          binarization_threshold=80)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(342, 4)
        assert_that(match.top_left[1]).is_close_to(320, 4)
        assert_that(match.bottom_right[0]).is_close_to(404, 4)
        assert_that(match.bottom_right[1]).is_close_to(354, 4)

    def test_frame_2_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(342, 404)
        assert_that(match.location[1]).is_between(320, 354)
