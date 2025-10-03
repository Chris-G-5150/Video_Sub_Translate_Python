from pathlib import Path
from data_enums.whisper_local_models import WhisperEnglishModels
from helper_functions.enum_evaluator import evaluate_enum
from module_parameters.app_params import AppParams
from data_enums.compatible_audio_formats import CompatibleAudioFormats
from data_enums.compatible_video_formats import CompatibleVideoFormats
from module_parameters.whisper_local_params import WhisperLocalParams
from modules.file_manager import FileManager
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.iso_639_languages import ISO639Language
from modules.media_manager import MediaManager
from module_parameters.media_manager_params import MediaManagerParams
from modules.separate_and_remove_audio_silence import SeparateAndRemoveAudioSilienceParams, SeparateAndRemoveAudioSilience
from modules.separate_audio_from_video import SeparateAudioFromVideoParams, SeparateAudioFromVideo
from modules.whisper_local import WhisperLocal

BASE_DIRECTORY = Path(__file__).resolve().parent

class App:
    def __init__(self, app_params: AppParams, media_manager_params: MediaManagerParams):
        # Classes that take care of each part of the project
        self.app_params = app_params
        self.media_manager = MediaManager(media_manager_params=media_manager_params, app_params=app_params)
        self.file_manager = FileManager(app_params=app_params, app_base_dir=None)
        self.whisper_local_chosen_model = app_params.whisper_local_chosen_model
        self.separate_audio_from_video = None
        self.separate_and_remove_audio_silience = None
        self.speech_to_text_generator = None
        self.sub_title_file_generator = None
        self.wisper_local = None

    def start(self):
        file_manager = self.file_manager
        file_manager.app_base_dir = self.get_base_dir()
        file_manager.set_directory_paths_in_file_manager()
        file_manager.build_directories_in_file_system()
        self.run_audio_extraction()

    @staticmethod
    def get_base_dir() -> Path:
        return BASE_DIRECTORY

    def run_audio_extraction(self):
        app = self
        params = SeparateAudioFromVideoParams(media_manager=app.media_manager, file_manager=app.file_manager)
        app.separate_audio_from_video = SeparateAudioFromVideo(params)
        status = self.separate_audio_from_video.process_video_to_audio()

        print(status)
        # TODO - Will be updating with events system once every module tested

        if status == 'Complete':
            self.run_separate_and_remove_audio_silience()

    def run_separate_and_remove_audio_silience(self):
        app = self
        params = SeparateAndRemoveAudioSilienceParams(media_manager=app.media_manager, file_manager=app.file_manager)
        app.separate_and_remove_audio_silience = SeparateAndRemoveAudioSilience(params)
        status = app.separate_and_remove_audio_silience.split_audio_remove_silence()

        # TODO - Will be updating with events system once every module tested
        if status == 'Complete':
            print('Silence and Separation Complete')


    def run_audio_transcription(self):
        app = self
        directories = self.file_manager.directories

        params = WhisperLocalParams(media_manager=app.media_manager, file_manager=app.file_manager, chosen_model=app.whisper_local_chosen_model)
        app.whisper_local = WhisperLocal(params)
        speech_to_text_status = app.whisper_local.run_speech_to_text()

        if speech_to_text_status == 'Complete':
            print('Transcription Complete')
            text_to_disk_status = app.wisper_local.write_transcriptions_to_disk()
            if text_to_disk_status == 'Complete':
                print(f"Transcriptions written to disk at: {directories.transcription_source_language_dir}")





test_app_params = AppParams(
    project_title = 'test',
    extracted_audio_format = CompatibleAudioFormats.MP3,
    source_language=ISO639Language.English,
    source_language_dialect = ISO3166Regions.UnitedKingdom,
    target_language = ISO639Language.Spanish,
    source_video_format = CompatibleVideoFormats.MP4,
    source_video_file_name = 'coronationstreet.mp4',
    whisper_local_chosen_model = evaluate_enum(WhisperEnglishModels.BaseEn, WhisperEnglishModels),
)

test_media_params = MediaManagerParams(
    source_video_start_point = '00:00:00',
    user_silence_offset = 15,
    user_silence_duration=500,
    target_language=ISO639Language.English,
)

App(test_app_params, test_media_params).start()
#
#
#
#
#
#
#
#




