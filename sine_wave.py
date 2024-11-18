# File: sine_wave.py

import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=1.0, amplitude=1.0, duration=2.0, sampling_rate=1000):
    """
    Plots a sine wave based on the given parameters.

    :param frequency: Frequency of the sine wave in Hz.
    :param amplitude: Amplitude of the sine wave.
    :param duration: Duration of the wave in seconds.
    :param sampling_rate: Number of samples per second.
    """
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    plt.figure(figsize=(8, 4))
    plt.plot(t, y)
    plt.title(f"Sine Wave: Frequency={frequency}Hz, Amplitude={amplitude}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_sine_wave(frequency=5.0)
