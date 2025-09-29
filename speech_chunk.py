from future.backports.datetime import timedelta
import main


#   {
#       clip_srt_index: 1, <- same order that will go into global array for each run of the processing can be used for the SRT files
#       project_title: None
#       clip_name: None <- filename
#       path_to_clip: './xxxxxx' <- reason for both file name and this is just to avoid further processing down the road.
#       audio_file_type: None <- may need this later, remove if not required, saves on processing again.
#       time_stamp_start: SRT compatible time stamp, <- get this processed as the silence is taken out when chunks are being created
#       time_stamp_end: SRT compatible time stamp, <- same here
#       platform_translated_from: None <- this can be updated later through the process but keeps everything in one place.
#       source_language: None <- first work out platform for lang codes, create a list somewhere for each of the platforms,
#       , look up API docs for further info for this, can potentially be called in?
#       detected_language: None <- check see if each platform has different lang codes and update later on in the process
#       transcribed_audio: None <- string with transcribed clip which will be turned into SRT compatible later on, object
#       will have empty properties that will be processed later
#       }

# Class declaration
# TODO - check if there are any sharp edges with Python classes.

class SpeechChunk:
    def __init__(self, clip_srt_index, project_title, chunk_from_audio_silence, milisecond_start, milisecond_end):
        self.project_title = project_title
        self.chunk_from_audio_silence = chunk_from_audio_silence
        self.clip_srt_index = clip_srt_index
        self.clip_name = None
        self.path_to_clip = None
        self.audio_file_type_SRT = None
        # milisecond start and end may not be required but also may be useful later.
        # these are the measurements given in the main chunks
        self.milisecondStart = milisecond_start
        self.milisecondEnd = milisecond_end
        self.time_stamp_start_SRT = timedelta(milliseconds = milisecond_start)
        self.time_stamp_end_SRT = timedelta(milliseconds = milisecond_end)
        # TODO look at how to type from Enums
        self.platform_transcribed_from = None
        self.source_language = None
        self.detected_language = None
        self.transcribed_audio = None


