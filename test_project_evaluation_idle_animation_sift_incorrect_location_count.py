import wargroove_ctrl
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationAnimationSiftILC(unittest.TestCase):
    frame_count = 75

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/idle-animation/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 354 or match.location[0] > 392 or match.location[1] < 122 or match.location[1] > 176:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 360 or match.location[0] > 390 or match.location[1] < 220 or match.location[1] > 274:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 354 or match.location[0] > 404 or match.location[1] < 320 or match.location[1] > 368:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 506 or match.location[0] > 536 or match.location[1] < 124 or match.location[1] > 176:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 500 or match.location[0] > 536 or match.location[1] < 218 or match.location[1] > 272:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 502 or match.location[0] > 554 or match.location[1] < 324 or match.location[1] > 368:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 596 or match.location[0] > 642 or match.location[1] < 138 or match.location[1] > 176:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 592 or match.location[0] > 636 or match.location[1] < 222 or match.location[1] > 272:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 590 or match.location[0] > 634 or match.location[1] < 314 or match.location[1] > 370:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 692 or match.location[0] > 732 or match.location[1] < 108 or match.location[1] > 178:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 693 or match.location[0] > 744 or match.location[1] < 208 or match.location[1] > 272:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 686 or match.location[0] > 742 or match.location[1] < 319 or match.location[1] > 370:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 782 or match.location[0] > 842 or match.location[1] < 138 or match.location[1] > 180:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 782 or match.location[0] > 844 or match.location[1] < 226 or match.location[1] > 276:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 770 or match.location[0] > 830 or match.location[1] < 300 or match.location[1] > 362:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 870 or match.location[0] > 944 or match.location[1] < 108 or match.location[1] > 172:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 878 or match.location[0] > 926 or match.location[1] < 214 or match.location[1] > 264:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 872 or match.location[0] > 934 or match.location[1] < 320 or match.location[1] > 354:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 450 or match.location[0] > 502 or match.location[1] < 520 or match.location[1] > 560:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 544 or match.location[0] > 596 or match.location[1] < 530 or match.location[1] > 569:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 641 or match.location[0] > 695 or match.location[1] < 516 or match.location[1] > 564:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 732 or match.location[0] > 794 or match.location[1] < 516 or match.location[1] > 564:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                       threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 840 or match.location[0] > 886 or match.location[1] < 520 or match.location[1] > 562:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 546 or match.location[0] > 596 or match.location[1] < 420 or match.location[1] > 480:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 972 or match.location[0] > 1026 or match.location[1] < 516 or match.location[1] > 578:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 446 or match.location[0] > 496 or match.location[1] < 402 or match.location[1] > 482:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 738 or match.location[0] > 784 or match.location[1] < 416 or match.location[1] > 476:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 638 or match.location[0] > 690 or match.location[1] < 424 or match.location[1] > 480:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        incorrect_location_count = 0
        for frame in range(self.frame_count):
            wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + str(frame) + '.png')
            match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                           threshold=threshold)

            wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

            if match is not None:
                if match.location[0] < 302 or match.location[0] > 354 or match.location[1] < 516 or match.location[1] > 574:
                    incorrect_location_count = incorrect_location_count + 1
        assert_that(incorrect_location_count).is_equal_to(0)
