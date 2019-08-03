import wargroove_ctrl
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationPartialOcclusion(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'D:/Libraries/Dropbox/Abertay University/CMP504 - Masters Project/Evaluation Frames/Units & Buildings Tests/Partial Occlusion/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_standard_template_matching(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 392)
        assert_that(match.location[1]).is_between(122, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_standard_template_matching(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506, 536)
        assert_that(match.location[1]).is_between(124, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_standard_template_matching(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500, 536)
        assert_that(match.location[1]).is_between(218, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_standard_template_matching(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502, 554)
        assert_that(match.location[1]).is_between(324, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_standard_template_matching(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596, 642)
        assert_that(match.location[1]).is_between(138, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_standard_template_matching(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592, 636)
        assert_that(match.location[1]).is_between(222, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_standard_template_matching(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590, 634)
        assert_that(match.location[1]).is_between(314, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_standard_template_matching(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692, 732)
        assert_that(match.location[1]).is_between(108, 178)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_standard_template_matching(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693, 744)
        assert_that(match.location[1]).is_between(208, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686, 742)
        assert_that(match.location[1]).is_between(319, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_standard_template_matching(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 842)
        assert_that(match.location[1]).is_between(138, 180)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_standard_template_matching(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 844)
        assert_that(match.location[1]).is_between(226, 276)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770, 830)
        assert_that(match.location[1]).is_between(300, 362)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_standard_template_matching(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876, 938)
        assert_that(match.location[1]).is_between(112, 168)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_standard_template_matching(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878, 926)
        assert_that(match.location[1]).is_between(214, 264)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_standard_template_matching(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'birds-over-all-things.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872, 934)
        assert_that(match.location[1]).is_between(320, 354)
