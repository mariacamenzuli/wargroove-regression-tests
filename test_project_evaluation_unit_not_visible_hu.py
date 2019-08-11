import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationUnitNotVisibleHuMoments(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/missing-units/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'mercia-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_mercia_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'mercia-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_mercia_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_mercia_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'mercia-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_mercia',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'emeric-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_emeric_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'emeric-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_emeric_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_emeric_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'emeric-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_emeric',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'caesar-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_caesar_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'caesar-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_caesar_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_caesar_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'caesar-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_commander_caesar',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'villager-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_villager_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'villager-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_villager_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_villager_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'villager-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_villager',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'soldier-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_soldier_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'soldier-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_soldier_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_soldier_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'soldier-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_soldier',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'pikeman-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_pikeman_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'pikeman-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_pikeman_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_pikeman_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'pikeman-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_pikeman',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'battlepup-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_battlepup_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'battlepup-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_battlepup_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_battlepup_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'battlepup-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_battle_pup',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'alchemist-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_alchemist_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'alchemist-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_alchemist_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_alchemist_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'alchemist-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_alchemist',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'archer-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_archer_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'archer-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_archer_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_archer_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'archer-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_archer',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'golem-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_golem_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'golem-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_golem_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_golem_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'golem-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_golem',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'knight-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_knight_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'knight-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_knight_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_knight_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'knight-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_knight',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'wagon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_wagon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'wagon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_wagon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_wagon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'wagon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_wagon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'ballista-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_ballista_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'ballista-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_ballista_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_ballista_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'ballista-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_ballista',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'trebuchet-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_trebuchet_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'trebuchet-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_trebuchet_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_trebuchet_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'trebuchet-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_trebuchet',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'balloon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_balloon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'balloon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_balloon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_balloon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'balloon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_balloon',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpy-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_harpy_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpy-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_harpy_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpy_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpy-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpy',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'witch-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_witch_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'witch-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_witch_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_witch_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'witch-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_witch',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'dragon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_dragon_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'dragon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_dragon_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_dragon_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'dragon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_emberwing',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barge-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_barge_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barge-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_barge_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barge_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barge-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_barge',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'turtle-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_seaturtle_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'turtle-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_seaturtle_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_seaturtle_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'turtle-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_sea_turtle',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpoon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_harpoonship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpoon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_harpoonship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_harpoonship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpoon-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_harpoon_ship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'warship-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_warship_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'warship-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_warship_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_warship_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'warship-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_warship',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'merfolk-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_merfolk_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'merfolk-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_merfolk_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_merfolk_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'merfolk-missing.png')
        match = wargroove_ctrl.find_unit_with_hu_moment_template_matching('cherrystone_merfolk',
                                                                          threshold=threshold,
                                                                          method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                          binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barracks-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_barracks_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barracks-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_barracks_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_barracks_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'barracks-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_barracks',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'port-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_port_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'port-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_port_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_port_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'port-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_port',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'stronghold-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_stronghold_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'stronghold-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_stronghold_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_stronghold_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'stronghold-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_stronghold',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'tower-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_tower_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'tower-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_tower_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_tower_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'tower-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_tower',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_village_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_village_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_village_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_village',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_hu_moment_template_matching_method_1(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'water-village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_1,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_watervillage_hu_moment_template_matching_method_2(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'water-village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_2,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_watervillage_hu_moment_template_matching_method_3(self):
        threshold = unit_constants.cherrystone_watervillage_hu_moment_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'water-village-missing.png')
        match = wargroove_ctrl.find_building_with_hu_moment_template_matching('cherrystone_watervillage',
                                                                              threshold=threshold,
                                                                              method=cmp504.computer_vision.HuTemplateMatchingMethod.METHOD_3,
                                                                              binarization_threshold=unit_constants.hu_moment_binarization_threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()
