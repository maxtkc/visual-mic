from argparse import ArgumentParser
# import cv2 as cv
import matplotlib.pyplot as plt
# from os import path
from scipy.io import wavfile

# from visualmic.sound_from_video import sound_from_video
# from visualmic.sound_spectral_subtraction import get_soud_spec_sub


def parse_args():
  parser = ArgumentParser()
  # parser.add_argument('input_video', help='The path of the input video')
  parser.add_argument('-o', '--output', help='The path of the output file', default='recoveredsound.wav')
  # parser.add_argument('-s', '--sampling-rate', help='The video frame rate', type=int, default=None)

  return parser.parse_args()


def plot_specgram(sound, sampling_rate, fp, scale=1):
  plt.figure()
  plt.specgram(sound[::scale], Fs=sampling_rate/scale, cmap=plt.get_cmap('jet'))
  plt.xlabel('Time (sec)')
  plt.ylabel('Frequency (Hz)')
  plt.colorbar().set_label('PSD (dB)')
  # plt.show()
  plt.savefig(fp)


if __name__ == '__main__':
  args = parse_args()

  # video = cv.VideoCapture(args.input_video)
  # sr = round(video.get(cv.CAP_PROP_FPS)) if args.sampling_rate is None else args.sampling_rate

  # sound = sound_from_video(video, 1, 2, downsample_factor=1)

  sr, sound = wavfile.read(args.output)

  scale = 1
  if sr > 1000:
      scale = 22
  print(sr, scale)

  plot_specgram(sound, sr, f"{args.output}.png", scale)
