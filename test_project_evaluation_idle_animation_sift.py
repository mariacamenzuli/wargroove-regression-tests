import wargroove_ctrl
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationSift(unittest.TestCase):
    frame_count = 75

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/idle-animation/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(354, 392)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(122, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(360, 390)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(220, 274)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(354, 404)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(320, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(506, 536)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(124, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(500, 536)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(218, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(502, 554)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(324, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(596, 642)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(138, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(592, 636)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(222, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(590, 634)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(314, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(692, 732)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(108, 178)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(693, 744)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(208, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(686, 742)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(319, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(782, 842)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(138, 180)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(782, 844)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(226, 276)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(770, 830)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(300, 362)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(876, 938)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(112, 168)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(878, 926)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(214, 264)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(872, 934)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(320, 354)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(450, 502)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(520, 560)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(544, 596)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(530, 569)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(641, 695)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(732, 794)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(840, 886)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(520, 562)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(546, 596)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(420, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(972, 1026)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(516, 578)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(446, 496)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(402, 482)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(738, 784)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(416, 476)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(638, 690)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(424, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            assert_that(match).described_as('match in frame ' + str(frame)).is_not_none()
            assert_that(match.location[0]).described_as('match x value in frame ' + str(frame)).is_between(302, 354)
            assert_that(match.location[1]).described_as('match y value in frame ' + str(frame)).is_between(516, 574)
