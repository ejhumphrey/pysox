import os
import sox.transform


def trim(input_file, output_file, start_time, end_time=None, duration=None):
    '''Excerpt a clip from an audio file, given a start and end time.

    Parameters
    ----------
    input_filepath : str
        Path to input audio file.
    output_filepath : str
        Path to desired output file. If a file already exists at the given
        path, the file will be overwritten.
    start_time : float
        Start time of the clip (seconds)
    end_time : float
        End time of the clip (seconds)

    Returns
    -------
    success : bool
        True if the output was successfully created.
    '''
    none_check = [arg is None for arg in (end_time, duration)]
    if all(none_check) or not any(none_check):
        raise ValueError("One of `end_time` or `duration` must be given.")
    elif end_time is None:
        end_time = start_time + duration
    tfm = sox.transform.Transformer()
    tfm.trim(start_time, end_time)
    tfm.build(input_file, output_file)
    return os.path.exists(output_file)
