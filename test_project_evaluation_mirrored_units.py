import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationMirroredUnits(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/mirrored-targets/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_hu_moment_template_matching_method_custom(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_mirrored_units.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching_custom('cherrystone_commander_mercia',
                                                                                 threshold=threshold,
                                                                                 binarization_threshold=100)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(934, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(974, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_mirrored_units.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=100)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(934, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(974, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_mirrored_units.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(934, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(974, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)

    def test_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_mirrored_units.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_close_to(934, 4)
        assert_that(match.top_left[1]).is_close_to(122, 4)
        assert_that(match.bottom_right[0]).is_close_to(974, 4)
        assert_that(match.bottom_right[1]).is_close_to(176, 4)
