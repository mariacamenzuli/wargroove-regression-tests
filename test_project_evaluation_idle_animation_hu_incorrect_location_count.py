import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationHuMomentsILC(unittest.TestCase):
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

            if match is not None:
                if (match.top_left[0] < (354 - 6) or match.top_left[0] > (354 + 6)) or (match.top_left[1] < (122 - 6) or match.top_left[1] > (122 + 6)) or (match.bottom_right[0] > (392 + 6) or match.bottom_right[0] < (392 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (360 - 6) or match.top_left[0] > (360 + 6)) or (match.top_left[1] < (220 - 6) or match.top_left[1] > (220 + 6)) or (match.bottom_right[0] > (390 + 6) or match.bottom_right[0] < (390 - 6)) or (match.bottom_right[1] > (274 + 6) or match.bottom_right[1] < (274 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (360 - 6) or match.top_left[0] > (360 + 6)) or (match.top_left[1] < (220 - 6) or match.top_left[1] > (220 + 6)) or (match.bottom_right[0] > (390 + 6) or match.bottom_right[0] < (390 - 6)) or (match.bottom_right[1] > (274 + 6) or match.bottom_right[1] < (274 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (360 - 6) or match.top_left[0] > (360 + 6)) or (match.top_left[1] < (220 - 6) or match.top_left[1] > (220 + 6)) or (match.bottom_right[0] > (390 + 6) or match.bottom_right[0] < (390 - 6)) or (match.bottom_right[1] > (274 + 6) or match.bottom_right[1] < (274 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (354 - 6) or match.top_left[0] > (354 + 6)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (404 + 6) or match.bottom_right[0] < (404 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (354 - 6) or match.top_left[0] > (354 + 6)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (404 + 6) or match.bottom_right[0] < (404 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (354 - 6) or match.top_left[0] > (354 + 6)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (404 + 6) or match.bottom_right[0] < (404 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (506 - 6) or match.top_left[0] > (506 + 6)) or (match.top_left[1] < (124 - 6) or match.top_left[1] > (124 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (506 - 6) or match.top_left[0] > (506 + 6)) or (match.top_left[1] < (124 - 6) or match.top_left[1] > (124 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (506 - 6) or match.top_left[0] > (506 + 6)) or (match.top_left[1] < (124 - 6) or match.top_left[1] > (124 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (500 - 6) or match.top_left[0] > (500 + 6)) or (match.top_left[1] < (218 - 6) or match.top_left[1] > (218 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (500 - 6) or match.top_left[0] > (500 + 6)) or (match.top_left[1] < (218 - 6) or match.top_left[1] > (218 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (500 - 6) or match.top_left[0] > (500 + 6)) or (match.top_left[1] < (218 - 6) or match.top_left[1] > (218 + 6)) or (match.bottom_right[0] > (536 + 6) or match.bottom_right[0] < (536 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (502 - 6) or match.top_left[0] > (502 + 6)) or (match.top_left[1] < (324 - 6) or match.top_left[1] > (324 + 6)) or (match.bottom_right[0] > (554 + 6) or match.bottom_right[0] < (554 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (502 - 6) or match.top_left[0] > (502 + 6)) or (match.top_left[1] < (324 - 6) or match.top_left[1] > (324 + 6)) or (match.bottom_right[0] > (554 + 6) or match.bottom_right[0] < (554 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (502 - 6) or match.top_left[0] > (502 + 6)) or (match.top_left[1] < (324 - 6) or match.top_left[1] > (324 + 6)) or (match.bottom_right[0] > (554 + 6) or match.bottom_right[0] < (554 - 6)) or (match.bottom_right[1] > (368 + 6) or match.bottom_right[1] < (368 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (596 - 6) or match.top_left[0] > (596 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (642 + 6) or match.bottom_right[0] < (642 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (596 - 6) or match.top_left[0] > (596 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (642 + 6) or match.bottom_right[0] < (642 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (596 - 6) or match.top_left[0] > (596 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (642 + 6) or match.bottom_right[0] < (642 - 6)) or (match.bottom_right[1] > (176 + 6) or match.bottom_right[1] < (176 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (592 - 6) or match.top_left[0] > (592 + 6)) or (match.top_left[1] < (222 - 6) or match.top_left[1] > (222 + 6)) or (match.bottom_right[0] > (636 + 6) or match.bottom_right[0] < (636 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (592 - 6) or match.top_left[0] > (592 + 6)) or (match.top_left[1] < (222 - 6) or match.top_left[1] > (222 + 6)) or (match.bottom_right[0] > (636 + 6) or match.bottom_right[0] < (636 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (592 - 6) or match.top_left[0] > (592 + 6)) or (match.top_left[1] < (222 - 6) or match.top_left[1] > (222 + 6)) or (match.bottom_right[0] > (636 + 6) or match.bottom_right[0] < (636 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (590 - 6) or match.top_left[0] > (590 + 6)) or (match.top_left[1] < (314 - 6) or match.top_left[1] > (314 + 6)) or (match.bottom_right[0] > (634 + 6) or match.bottom_right[0] < (634 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (590 - 6) or match.top_left[0] > (590 + 6)) or (match.top_left[1] < (314 - 6) or match.top_left[1] > (314 + 6)) or (match.bottom_right[0] > (634 + 6) or match.bottom_right[0] < (634 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (590 - 6) or match.top_left[0] > (590 + 6)) or (match.top_left[1] < (314 - 6) or match.top_left[1] > (314 + 6)) or (match.bottom_right[0] > (634 + 6) or match.bottom_right[0] < (634 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (692 - 6) or match.top_left[0] > (692 + 6)) or (match.top_left[1] < (108 - 6) or match.top_left[1] > (108 + 6)) or (match.bottom_right[0] > (732 + 6) or match.bottom_right[0] < (732 - 6)) or (match.bottom_right[1] > (178 + 6) or match.bottom_right[1] < (178 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (692 - 6) or match.top_left[0] > (692 + 6)) or (match.top_left[1] < (108 - 6) or match.top_left[1] > (108 + 6)) or (match.bottom_right[0] > (732 + 6) or match.bottom_right[0] < (732 - 6)) or (match.bottom_right[1] > (178 + 6) or match.bottom_right[1] < (178 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (692 - 6) or match.top_left[0] > (692 + 6)) or (match.top_left[1] < (108 - 6) or match.top_left[1] > (108 + 6)) or (match.bottom_right[0] > (732 + 6) or match.bottom_right[0] < (732 - 6)) or (match.bottom_right[1] > (178 + 6) or match.bottom_right[1] < (178 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (693 - 6) or match.top_left[0] > (693 + 6)) or (match.top_left[1] < (208 - 6) or match.top_left[1] > (208 + 6)) or (match.bottom_right[0] > (744 + 6) or match.bottom_right[0] < (744 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (693 - 6) or match.top_left[0] > (693 + 6)) or (match.top_left[1] < (208 - 6) or match.top_left[1] > (208 + 6)) or (match.bottom_right[0] > (744 + 6) or match.bottom_right[0] < (744 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (693 - 6) or match.top_left[0] > (693 + 6)) or (match.top_left[1] < (208 - 6) or match.top_left[1] > (208 + 6)) or (match.bottom_right[0] > (744 + 6) or match.bottom_right[0] < (744 - 6)) or (match.bottom_right[1] > (272 + 6) or match.bottom_right[1] < (272 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (686 - 6) or match.top_left[0] > (686 + 6)) or (match.top_left[1] < (319 - 6) or match.top_left[1] > (319 + 6)) or (match.bottom_right[0] > (742 + 6) or match.bottom_right[0] < (742 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (686 - 6) or match.top_left[0] > (686 + 6)) or (match.top_left[1] < (319 - 6) or match.top_left[1] > (319 + 6)) or (match.bottom_right[0] > (742 + 6) or match.bottom_right[0] < (742 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (686 - 6) or match.top_left[0] > (686 + 6)) or (match.top_left[1] < (319 - 6) or match.top_left[1] > (319 + 6)) or (match.bottom_right[0] > (742 + 6) or match.bottom_right[0] < (742 - 6)) or (match.bottom_right[1] > (370 + 6) or match.bottom_right[1] < (370 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (842 + 6) or match.bottom_right[0] < (842 - 6)) or (match.bottom_right[1] > (180 + 6) or match.bottom_right[1] < (180 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (842 + 6) or match.bottom_right[0] < (842 - 6)) or (match.bottom_right[1] > (180 + 6) or match.bottom_right[1] < (180 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (138 - 6) or match.top_left[1] > (138 + 6)) or (match.bottom_right[0] > (842 + 6) or match.bottom_right[0] < (842 - 6)) or (match.bottom_right[1] > (180 + 6) or match.bottom_right[1] < (180 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (226 - 6) or match.top_left[1] > (226 + 6)) or (match.bottom_right[0] > (844 + 6) or match.bottom_right[0] < (844 - 6)) or (match.bottom_right[1] > (276 + 6) or match.bottom_right[1] < (276 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (226 - 6) or match.top_left[1] > (226 + 6)) or (match.bottom_right[0] > (844 + 6) or match.bottom_right[0] < (844 - 6)) or (match.bottom_right[1] > (276 + 6) or match.bottom_right[1] < (276 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (782 - 6) or match.top_left[0] > (782 + 6)) or (match.top_left[1] < (226 - 6) or match.top_left[1] > (226 + 6)) or (match.bottom_right[0] > (844 + 6) or match.bottom_right[0] < (844 - 6)) or (match.bottom_right[1] > (276 + 6) or match.bottom_right[1] < (276 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (770 - 6) or match.top_left[0] > (770 + 6)) or (match.top_left[1] < (300 - 6) or match.top_left[1] > (300 + 6)) or (match.bottom_right[0] > (830 + 6) or match.bottom_right[0] < (830 - 6)) or (match.bottom_right[1] > (362 + 6) or match.bottom_right[1] < (362 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (770 - 6) or match.top_left[0] > (770 + 6)) or (match.top_left[1] < (300 - 6) or match.top_left[1] > (300 + 6)) or (match.bottom_right[0] > (830 + 6) or match.bottom_right[0] < (830 - 6)) or (match.bottom_right[1] > (362 + 6) or match.bottom_right[1] < (362 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (770 - 6) or match.top_left[0] > (770 + 6)) or (match.top_left[1] < (300 - 6) or match.top_left[1] > (300 + 6)) or (match.bottom_right[0] > (830 + 6) or match.bottom_right[0] < (830 - 6)) or (match.bottom_right[1] > (362 + 6) or match.bottom_right[1] < (362 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 6) or match.top_left[1] > (112 + 6)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 6) or match.bottom_right[1] < (168 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 6) or match.top_left[1] > (112 + 6)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 6) or match.bottom_right[1] < (168 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (876 - 6) or match.top_left[0] > (876 + 6)) or (match.top_left[1] < (112 - 6) or match.top_left[1] > (112 + 6)) or (match.bottom_right[0] > (938 + 6) or match.bottom_right[0] < (938 - 6)) or (match.bottom_right[1] > (168 + 6) or match.bottom_right[1] < (168 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (878 - 6) or match.top_left[0] > (878 + 6)) or (match.top_left[1] < (214 - 6) or match.top_left[1] > (214 + 6)) or (match.bottom_right[0] > (926 + 6) or match.bottom_right[0] < (926 - 6)) or (match.bottom_right[1] > (264 + 6) or match.bottom_right[1] < (264 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (878 - 6) or match.top_left[0] > (878 + 6)) or (match.top_left[1] < (214 - 6) or match.top_left[1] > (214 + 6)) or (match.bottom_right[0] > (926 + 6) or match.bottom_right[0] < (926 - 6)) or (match.bottom_right[1] > (264 + 6) or match.bottom_right[1] < (264 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (878 - 6) or match.top_left[0] > (878 + 6)) or (match.top_left[1] < (214 - 6) or match.top_left[1] > (214 + 6)) or (match.bottom_right[0] > (926 + 6) or match.bottom_right[0] < (926 - 6)) or (match.bottom_right[1] > (264 + 6) or match.bottom_right[1] < (264 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 6) or match.bottom_right[1] < (354 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 6) or match.bottom_right[1] < (354 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (872 - 8) or match.top_left[0] > (872 + 8)) or (match.top_left[1] < (320 - 6) or match.top_left[1] > (320 + 6)) or (match.bottom_right[0] > (934 + 8) or match.bottom_right[0] < (934 - 8)) or (match.bottom_right[1] > (354 + 6) or match.bottom_right[1] < (354 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (450 - 6) or match.top_left[0] > (450 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (502 + 6) or match.bottom_right[0] < (502 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (450 - 6) or match.top_left[0] > (450 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (502 + 6) or match.bottom_right[0] < (502 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (450 - 6) or match.top_left[0] > (450 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (502 + 6) or match.bottom_right[0] < (502 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (544 - 6) or match.top_left[0] > (544 + 6)) or (match.top_left[1] < (530 - 6) or match.top_left[1] > (530 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (544 - 6) or match.top_left[0] > (544 + 6)) or (match.top_left[1] < (530 - 6) or match.top_left[1] > (530 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (544 - 6) or match.top_left[0] > (544 + 6)) or (match.top_left[1] < (530 - 6) or match.top_left[1] > (530 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (560 + 6) or match.bottom_right[1] < (560 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (641 - 6) or match.top_left[0] > (641 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (695 + 6) or match.bottom_right[0] < (695 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (641 - 6) or match.top_left[0] > (641 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (695 + 6) or match.bottom_right[0] < (695 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (641 - 6) or match.top_left[0] > (641 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (695 + 6) or match.bottom_right[0] < (695 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (732 - 6) or match.top_left[0] > (732 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (794 + 6) or match.bottom_right[0] < (794 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (732 - 6) or match.top_left[0] > (732 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (794 + 6) or match.bottom_right[0] < (794 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (732 - 6) or match.top_left[0] > (732 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (794 + 6) or match.bottom_right[0] < (794 - 6)) or (match.bottom_right[1] > (564 + 6) or match.bottom_right[1] < (564 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (840 - 6) or match.top_left[0] > (840 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (886 + 6) or match.bottom_right[0] < (886 - 6)) or (match.bottom_right[1] > (562 + 6) or match.bottom_right[1] < (562 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (840 - 6) or match.top_left[0] > (840 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (886 + 6) or match.bottom_right[0] < (886 - 6)) or (match.bottom_right[1] > (562 + 6) or match.bottom_right[1] < (562 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (840 - 6) or match.top_left[0] > (840 + 6)) or (match.top_left[1] < (520 - 6) or match.top_left[1] > (520 + 6)) or (match.bottom_right[0] > (886 + 6) or match.bottom_right[0] < (886 - 6)) or (match.bottom_right[1] > (562 + 6) or match.bottom_right[1] < (562 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (546 - 6) or match.top_left[0] > (546 + 6)) or (match.top_left[1] < (420 - 6) or match.top_left[1] > (420 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (546 - 6) or match.top_left[0] > (546 + 6)) or (match.top_left[1] < (420 - 6) or match.top_left[1] > (420 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (546 - 6) or match.top_left[0] > (546 + 6)) or (match.top_left[1] < (420 - 6) or match.top_left[1] > (420 + 6)) or (match.bottom_right[0] > (596 + 6) or match.bottom_right[0] < (596 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (972 - 6) or match.top_left[0] > (972 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (1026 + 6) or match.bottom_right[0] < (1026 - 6)) or (match.bottom_right[1] > (578 + 6) or match.bottom_right[1] < (578 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (972 - 6) or match.top_left[0] > (972 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (1026 + 6) or match.bottom_right[0] < (1026 - 6)) or (match.bottom_right[1] > (578 + 6) or match.bottom_right[1] < (578 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (972 - 6) or match.top_left[0] > (972 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (1026 + 6) or match.bottom_right[0] < (1026 - 6)) or (match.bottom_right[1] > (578 + 6) or match.bottom_right[1] < (578 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (446 - 6) or match.top_left[0] > (446 + 6)) or (match.top_left[1] < (402 - 6) or match.top_left[1] > (402 + 6)) or (match.bottom_right[0] > (496 + 6) or match.bottom_right[0] < (496 - 6)) or (match.bottom_right[1] > (482 + 6) or match.bottom_right[1] < (482 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (446 - 6) or match.top_left[0] > (446 + 6)) or (match.top_left[1] < (402 - 6) or match.top_left[1] > (402 + 6)) or (match.bottom_right[0] > (496 + 6) or match.bottom_right[0] < (496 - 6)) or (match.bottom_right[1] > (482 + 6) or match.bottom_right[1] < (482 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (446 - 6) or match.top_left[0] > (446 + 6)) or (match.top_left[1] < (402 - 6) or match.top_left[1] > (402 + 6)) or (match.bottom_right[0] > (496 + 6) or match.bottom_right[0] < (496 - 6)) or (match.bottom_right[1] > (482 + 6) or match.bottom_right[1] < (482 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (738 - 6) or match.top_left[0] > (738 + 6)) or (match.top_left[1] < (416 - 6) or match.top_left[1] > (416 + 6)) or (match.bottom_right[0] > (784 + 6) or match.bottom_right[0] < (784 - 6)) or (match.bottom_right[1] > (476 + 6) or match.bottom_right[1] < (476 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (738 - 6) or match.top_left[0] > (738 + 6)) or (match.top_left[1] < (416 - 6) or match.top_left[1] > (416 + 6)) or (match.bottom_right[0] > (784 + 6) or match.bottom_right[0] < (784 - 6)) or (match.bottom_right[1] > (476 + 6) or match.bottom_right[1] < (476 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (738 - 6) or match.top_left[0] > (738 + 6)) or (match.top_left[1] < (416 - 6) or match.top_left[1] > (416 + 6)) or (match.bottom_right[0] > (784 + 6) or match.bottom_right[0] < (784 - 6)) or (match.bottom_right[1] > (476 + 6) or match.bottom_right[1] < (476 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (638 - 6) or match.top_left[0] > (638 + 6)) or (match.top_left[1] < (424 - 6) or match.top_left[1] > (424 + 6)) or (match.bottom_right[0] > (690 + 6) or match.bottom_right[0] < (690 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (638 - 6) or match.top_left[0] > (638 + 6)) or (match.top_left[1] < (424 - 6) or match.top_left[1] > (424 + 6)) or (match.bottom_right[0] > (690 + 6) or match.bottom_right[0] < (690 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (638 - 6) or match.top_left[0] > (638 + 6)) or (match.top_left[1] < (424 - 6) or match.top_left[1] > (424 + 6)) or (match.bottom_right[0] > (690 + 6) or match.bottom_right[0] < (690 - 6)) or (match.bottom_right[1] > (480 + 6) or match.bottom_right[1] < (480 - 6)):
                    assert_that(1).is_equal_to(0)

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

            if match is not None:
                if (match.top_left[0] < (302 - 6) or match.top_left[0] > (302 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (352 + 6) or match.bottom_right[0] < (352 - 6)) or (match.bottom_right[1] > (574 + 6) or match.bottom_right[1] < (574 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (302 - 6) or match.top_left[0] > (302 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (352 + 6) or match.bottom_right[0] < (352 - 6)) or (match.bottom_right[1] > (574 + 6) or match.bottom_right[1] < (574 - 6)):
                    assert_that(1).is_equal_to(0)

    def test_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                                  threshold=threshold,
                                                                                  method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                                  binarization_threshold=unit_constants.hu_moment_binarization_threshold)

            if match is not None:
                if (match.top_left[0] < (302 - 6) or match.top_left[0] > (302 + 6)) or (match.top_left[1] < (516 - 6) or match.top_left[1] > (516 + 6)) or (match.bottom_right[0] > (352 + 6) or match.bottom_right[0] < (352 - 6)) or (match.bottom_right[1] > (574 + 6) or match.bottom_right[1] < (574 - 6)):
                    assert_that(1).is_equal_to(0)
