#Causality

[Our facebook page](https://fb.com/kolmogorovtoolbox)

Helegris (**Tímea Fekete**) and I (**Gergely Bencsik**) were on a routine-like ice cream tour in the downtown of Pécs during a break from our weekly rehearsal. We discussed glitch art as we knew it then. The topic was about databending and circuit bending, like when one puts electro-acoustic effects (like reverb, compressor, echo-cancellation etc.) on an analogue encoded video. So we decided to make something similar, with a distortion and a feedback delay. Python and OpenCV were very handy for this stuff, so the final form of the code was complete after approximately three hours of experimenting.

The project is written in _Python_, using the _OpenCV_ Python package. The concept behind it is a feedback webcam stream with some additional filters (_Gaussian_ and _Laplacian_ based variations) to make a glitchy and trippy effect. As you can see on the video, it looks like a monochromatic curve is moving real-time while the distorted texture follows it over and over again and also continuously overwrites itself. In fact, we developed it in a shady room with a very noisy camera built in a Toshiba L300 oldtimer (it’s not tested on other environments yet).
