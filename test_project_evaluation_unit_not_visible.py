import wargroove_ctrl
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationUnitNotVisible(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/missing-units/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'mercia-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'mercia-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'villager-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'villager-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'soldier-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'soldier-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'pikeman-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'pikeman-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'battlepup-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'battlepup-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'alchemist-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'alchemist-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'archer-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'archer-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'golem-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'golem-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'knight-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'knight-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'wagon-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'wagon-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'ballista-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'ballista-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'trebuchet-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'trebuchet-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'balloon-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'balloon-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpy-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'harpy-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'witch-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'witch-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'dragon-missing.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'dragon-missing.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_none()
