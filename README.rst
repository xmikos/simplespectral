SimpleSpectral
==============

Heavily simplified scipy.signal.spectral module which only depends on NumPy and supports pyFFTW

Requirements
------------

- `Python 3 <https://www.python.org>`_
- `NumPy <http://www.numpy.org>`_
- Optional: `pyFFTW <https://github.com/pyFFTW/pyFFTW>`_ (for fastest FFT calculations with FFTW library)
- Optional: `SciPy <https://www.scipy.org>`_ (for faster FFT calculations with scipy.fftpack library)

SimpleSpectral preferably uses pyfftw for FFT calculations, then scipy.fftpack
and numpy.fft as a last resort.

You should always install SciPy or pyFFTW, because numpy.fft has horrible
memory usage and is also much slower.

Differences
-----------

You can use scipy.signal `tutorial <https://scipy.github.io/devdocs/tutorial/signal.html#spectral-analysis>`_
and `reference guide <https://scipy.github.io/devdocs/signal.html#spectral-analysis>`_ in most cases,
but there are some important differences:

- input data is assumed to be complex and two-sided spectrum is always returned (``return_onesided``
  argument is not implemented)
- length of FFT is always same as length of segment (``nfft`` argument is not implemented)
- functions work always over last axis of array (``axis`` argument is not implemented)
- if you want to have best FFT performance with pyFFTW, you should create arrays with
  ``empty``, ``zeros`` or ``ones`` functions from SimpleSpectral instead of generic versions
  from NumPy (arrays will be byte aligned for your CPU)

*Implemented functions:*

- empty
- zeros
- ones
- fft
- get_window
- get_detrend
- extend_boundaries
- welch
- periodogram
- spectrogram
- stft

*Supported windows:*

- boxcar
- hann
- hamming
- bartlett
- blackman
- kaiser
- tukey

*Supported boundary extensions:*

- even
- odd
- constant
- zeros

*Supported detrending functions:*

- constant

Credits
-------

Based on code from excellent `SciPy <https://www.scipy.org>`_ project.
