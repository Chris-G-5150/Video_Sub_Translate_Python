from dataclasses import dataclass
from pydub import AudioSegment, silence
from data_classes.speech_chunk import SpeechChunk
from data_enums.iso_3166_regions import ISO3166Regions
from data_enums.iso_639_languages import ISO639Language
from helper_functions.enum_evaluator import evaluate_enum
from modules.file_manager import FileManager
from modules.media_manager import MediaManager

@dataclass
class SeparateAndRemoveAudioSilienceParams:
    media_manager: MediaManager # All properties are here, just wanted to separate concerns and only update when a step in the process complete
    file_manager: FileManager
    
class SeparateAndRemoveAudioSilience:
    def __init__(self, params: SeparateAndRemoveAudioSilienceParams):
        self.media_manager = params.media_manager
        self.file_manager = params.file_manager
        self.user_silence_offset = params.media_manager.user_silence_offset
        self.user_silence_duration = params.media_manager.user_silence_duration
        self.source_language = evaluate_enum(params.media_manager.source_language, ISO639Language)
        self.source_language_dialect = evaluate_enum(params.media_manager.source_language_dialect, ISO3166Regions)
        self.process_step = "2"

    def split_audio_remove_silence(self):
        file_manager = self.file_manager
        media_manager = self.media_manager
        app_params = file_manager.app_params
        directories = file_manager.directories
        audio_format = media_manager.extracted_audio_format
        extracted_audio_path = file_manager.extracted_audio_path
        audio_segment = AudioSegment.from_file(extracted_audio_path, audio_format)
        silence_threshold = audio_segment.dBFS - self.user_silence_offset
        output_directory = directories.silence_removed_chunks_dir

        try:
            file_manager.check_directroy_exists(output_directory)
        except Exception:
            raise Exception('Cannot find directory to place silence removed audio')

        speech_chunks = silence.split_on_silence(
            audio_segment,
            min_silence_len = 1500,
            silence_thresh = silence_threshold,
            keep_silence = self.user_silence_duration,
            seek_step = 10
        )

        speech_chunks_silence_removed = []
        # Very doubtful actual speech sections will be less than two seconds, cuts out loud breathing/background sections
        for chunk in speech_chunks:
            if not chunk.duration_seconds < 2:
                speech_chunks_silence_removed.append(chunk)
        #   Filters speech chunks out less than 2 seconds long out before writing to disk, makes sure that the indexes are in
        #   the correct order for the sub files instead of having 1: some dialogue 2: **nothing** 3: some dialogue.
        #   This keeps sub files concise and no longer than they need to be.

        time_accumulator = 0.0

        for index, chunk in enumerate(speech_chunks_silence_removed):
            print(f"Exporting chunk {index} ({len(chunk) / 1000:.2f}s)")
            start_point_seconds = time_accumulator + 0.1
            end_point_seconds = start_point_seconds + chunk.duration_seconds

            chunk_file_path = file_manager.build_file_os_path(
                directories.silence_removed_chunks_dir,
                f"{index}-{app_params.project_title}-silence_removbed_chunk.{audio_format}"
            )

            new_speech_chunk = SpeechChunk(
                project_title=self.media_manager.project_title,
                clip_srt_index=index,
                speech_chunk_path=chunk_file_path,
                duration_in_miliseconds=int(chunk.duration_seconds / 1000),
                milisecond_start=int(start_point_seconds / 1000),
                milisecond_end=int(end_point_seconds / 1000),
                audio_format=audio_format,
                source_language=self.source_language,
            )

            file_manager.write_speech_chunk_to_disk(segment=audio_segment, chunk=new_speech_chunk, chunk_file_path=chunk_file_path)
            self.media_manager.add_speech_chunk(new_speech_chunk)


        return 'Complete'









