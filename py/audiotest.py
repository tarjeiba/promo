from array import array
import pygame as pg

class Tone(pg.mixer.Sound):
    """This generates a 'Square wave' with a generator.

    Then creates an array of samples, and passes that into pygame.Sound.
    """

    def __init__(self, frequency, array_type, volume=.1):
        self.frequency = frequency
        if array_type == 'b':
            # we have to convert the 1 byte 'b' samples to 2 byte 'h'.
            samples = self.signed_char_to_signed_short(
                self.make_samples_b()
            )
        elif array_type == 'h':
            samples = self.make_samples_h()
        else:
            raise ValueError('array_type not supported')

        pg.mixer.Sound.__init__(self, buffer=samples)
        self.set_volume(volume)

    def make_samples_b(self):
        """ Builds samples array between -127 and 127.
            Array type 'h'.
        """
        mixer_frequency = pg.mixer.get_init()[0]
        mixer_format = pg.mixer.get_init()[1]
        period = int(round(mixer_frequency / self.frequency))
        max_amplitude = 2 ** (abs(mixer_format) - 1) - 1
        max_amplitude = int(max_amplitude / 256)
        # print(f'mixer_frequency:{mixer_frequency}, mixer_format:{mixer_format}')
        # print(f'period:{period}, max_amplitude:{max_amplitude}')

        # 'b' array is signed char, 1 byte
        # https://docs.python.org/3/library/array.html
        samples = array('b',
            (max_amplitude if time < period / 2 else -max_amplitude
                for time in range(period))
        )
        return samples

    def signed_char_to_signed_short(self, b_samples):
        """ Converts 1 byte signed char samples to 2 byte signed short.

            127 to 32767
        """
        # just a simple linear conversion.
        factor = int(32767 / 127)
        return array('h', (sample * factor for sample in b_samples))

    def make_samples_h(self):
        """ Builds samples array between -32767 snd 32767.
            Array type 'h'.
        """
        mixer_frequency = pg.mixer.get_init()[0]
        mixer_format = pg.mixer.get_init()[1]
        period = int(round(mixer_frequency / self.frequency))
        max_amplitude = 2 ** (abs(mixer_format) - 1) - 1
        # print(f'mixer_frequency:{mixer_frequency}, mixer_format:{mixer_format}')
        # print(f'period:{period}, max_amplitude:{max_amplitude}')

        # 'h' array is signed short, 2 bytes
        # https://docs.python.org/3/library/array.html
        samples = array('h',
            (max_amplitude if time < period / 2 else -max_amplitude
                for time in range(period))
        )
        return samples


class Sample(pg.mixer.Sound):
    """ For playing a sample.

    Takes a file, and reads it in as 8bit signed data.

    Then converts it to the 16bit signed size the pygame.mixer needs.
    """
    def __init__(self, fname, volume=.1):
        with open(fname, 'rb') as f:
            samples = self.signed_char_to_signed_short (
                array('b', f.read())
            )
            pg.mixer.Sound.__init__(self, buffer=samples)
        self.set_volume(volume)

    def signed_char_to_signed_short(self, b_samples):
        """ Converts 1 byte signed char samples to 2 byte signed short.
            127 to 32767
        """
        # just a simple linear conversion.
        import time
        t0=time.time()
        factor = int(32767 / 127)
        samples = array('h', (
            max(sample, -127) * factor if sample < 0 else
            min(sample, 127) * factor
            for sample in b_samples))
        t1=time.time()
        print(t1-t0)
        return samples


def fetch_example_mod_file(mod_fname):
    """ Grab a file that has a sound samples in it from the net.

    'MOD is a computer file format used primarily to represent music,
    and was the first module file format. MOD files use the ".MOD"
    file extension, except on the Amiga which doesn't rely on
    filename extensions, instead it reads a file's header to
    determine filetype. A MOD file contains a set of instruments in
    the form of samples, a number of patterns indicating how and when
    the samples are to be played, and a list of what
    patterns to play in what order.'

    https://en.wikipedia.org/wiki/MOD_(file_format)
    """
    import os
    url = 'https://api.modarchive.org/downloads.php?moduleid=101996'

    if not os.path.exists(mod_fname):
        from urllib.request import urlopen
        print ('Fetching %s .mod into file: %s' % (url, mod_fname))
        data = urlopen(url).read()
        with open(mod_fname, 'w+') as modf:
            modf.write(data)


def resample(mod_fname):
    """ An example of resampling audio to a different framerate.

    eg, from 8363 one byte samples per second to
        44100 two byte samples per second.
    """
    import audioop
    import wave
    from io import BytesIO

    in_framerate = 8363
    in_sampwidth = 1
    in_nchannels = 1

    out_framerate = 44100

    num_seconds = 5
    with open(mod_fname, 'rb') as f:
        # Throw away the start data of this mod file.
        #   Better samples later on.
        f.read(8363*2)
        in_frame_data = f.read(in_framerate * num_seconds)

    # https://docs.python.org/3/library/audioop.html?highlight=audio#audioop.ratecv
    newfragment, newstate = audioop.ratecv(
        in_frame_data,
        in_sampwidth,
        in_nchannels,
        in_framerate,
        out_framerate,
        None)

    # print(f'len(newfragment):{len(newfragment)}')
    # A perfect conversion is not possible, because the sample
    #   rates do not divide equally. However, the number
    #   of samples should be close.
    # assert (out_framerate * num_seconds) - len(newfragment) < 10
    pg.mixer.Sound(buffer=newfragment).play(-1)



# TODO:
# Converting between modo and stereo?
#   audioop.tomono and audioop.tostereo
#   https://docs.python.org/3/library/audioop.html?highlight=audio#audioop.tomono

# How to draw a wave form?
#   using pygame.draw.lines transforming audio into
#   Surface space.
#   Meaning, scaling audio samples into a particular
#   sized part of the screen.

# More sound generator types.
#   Saw tooth.



if __name__ == "__main__":
    # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.init
    pg.mixer.pre_init(44100, -16, 1, 1024)
    pg.init()

    pg.display.set_caption('Playing square wave, 808 frequency')
    pg.display.set_mode((320, 200))

    mod_fname = 'outrun_3.mod'

    fetch_example_mod_file(mod_fname)

    # play on repeat, -1 means loop indefinitely.
    # https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound.play
    if 1:
        g = 444
        g2 = g ** (5 / 12)
        g3 = g ** (8 / 12)
        Tone(frequency=g, array_type='b').play(-1)
        Tone(frequency=g2, array_type='b').play(-1)
        Tone(frequency=g3, array_type='b').play(-1)


    if 0:
        try:
            Sample(mod_fname).play(-1)
        except IOError:
            print ('no %s' % mod_fname)
    if 0:
        pg.mixer.music.load(mod_fname)
        pg.mixer.music.play()

    if 0:
        resample(mod_fname)

    going = True
    while going:
        for e in pg.event.get():
            if e.type in [pg.QUIT, pg.KEYDOWN]:
                going = False

