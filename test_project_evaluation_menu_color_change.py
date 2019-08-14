import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationMenu(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/menus/'

    def test_close_button_standard_template_matching_cross_corr(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('close_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(620)
        assert_that(match.top_left[1]).is_equal_to(498)
        assert_that(match.bottom_right[0]).is_equal_to(660)
        assert_that(match.bottom_right[1]).is_equal_to(532)

    def test_play_map_button_standard_template_matching_cross_corr(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('play_map_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(600)
        assert_that(match.top_left[1]).is_equal_to(414)
        assert_that(match.bottom_right[0]).is_equal_to(678)
        assert_that(match.bottom_right[1]).is_equal_to(448)

    def test_save_and_exit_button_standard_template_matching_cross_corr(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('save_and_exit_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(450)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(484)

    def test_event_editor_button_standard_template_matching_cross_corr(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('event_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(588)
        assert_that(match.top_left[1]).is_equal_to(366)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(400)

    def test_cutscene_editor_button_standard_template_matching_cross_corr(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('cutscene_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CROSS_CORRELATION_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(574)
        assert_that(match.top_left[1]).is_equal_to(330)
        assert_that(match.bottom_right[0]).is_equal_to(704)
        assert_that(match.bottom_right[1]).is_equal_to(364)

    def test_close_button_standard_template_matching_corr_coeff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('close_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(620)
        assert_that(match.top_left[1]).is_equal_to(498)
        assert_that(match.bottom_right[0]).is_equal_to(660)
        assert_that(match.bottom_right[1]).is_equal_to(532)

    def test_play_map_button_standard_template_matching_corr_coeff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('play_map_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(600)
        assert_that(match.top_left[1]).is_equal_to(414)
        assert_that(match.bottom_right[0]).is_equal_to(678)
        assert_that(match.bottom_right[1]).is_equal_to(448)

    def test_save_and_exit_button_standard_template_matching_corr_coeff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('save_and_exit_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(450)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(484)

    def test_event_editor_button_standard_template_matching_corr_coeff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('event_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(588)
        assert_that(match.top_left[1]).is_equal_to(366)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(400)

    def test_cutscene_editor_button_standard_template_matching_corr_coeff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('cutscene_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(574)
        assert_that(match.top_left[1]).is_equal_to(330)
        assert_that(match.bottom_right[0]).is_equal_to(704)
        assert_that(match.bottom_right[1]).is_equal_to(364)

    def test_close_button_standard_template_matching_square_diff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('close_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(620)
        assert_that(match.top_left[1]).is_equal_to(498)
        assert_that(match.bottom_right[0]).is_equal_to(660)
        assert_that(match.bottom_right[1]).is_equal_to(532)

    def test_play_map_button_standard_template_matching_square_diff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('play_map_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(600)
        assert_that(match.top_left[1]).is_equal_to(414)
        assert_that(match.bottom_right[0]).is_equal_to(678)
        assert_that(match.bottom_right[1]).is_equal_to(448)

    def test_save_and_exit_button_standard_template_matching_square_diff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('save_and_exit_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(450)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(484)

    def test_event_editor_button_standard_template_matching_square_diff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('event_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(588)
        assert_that(match.top_left[1]).is_equal_to(366)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(400)

    def test_cutscene_editor_button_standard_template_matching_square_diff(self):
        pre_process = cmp504.image_processing.ImageProcessingStepChain()
        pre_process.append(cmp504.image_processing.BGR2Grayscale())
        pre_process.append(cmp504.image_processing.Threshold(200))

        threshold = unit_constants.ui_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + 'change-color.png')
        match = wargroove_ctrl.find_ui_item_with_template_matching('cutscene_editor_button',
                                                                   threshold=threshold,
                                                                   template_pre_processing_chain=pre_process,
                                                                   frame_pre_processing_chain=pre_process,
                                                                   method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(574)
        assert_that(match.top_left[1]).is_equal_to(330)
        assert_that(match.bottom_right[0]).is_equal_to(704)
        assert_that(match.bottom_right[1]).is_equal_to(364)


