# Image-Kernel-Applier
Written in Python 3.8 and PyGame 2. Handles the application of Image Kernels, there are a couple preset kernels but adding custom ones is super simple. Since this app is written in Python, the kernels take a really long while to get applied. Untill I find a faster method, this is not for real time use.

The preset kernels are under ```kernel_manager.PresetKernels.<kernel_of_choice>```<br>
**The following kernels can be found in the Presets**
 - identity
 - blur
 - outline
 - sharpen
 - denoise
 - highpass
 - lowpass
 
 **Creating a new kernel**
```python
identity = Kernel(
    0, 0, 0,
    0, 1, 0,
    0, 0, 0
)
```

<strong>Required</strong><br>
Python 2.7-3.8<br>
Pygame 2.0.0.dev6<br>

To use this script use the following commands:
```
pip install pygame

git clone <URL>
cd <REPO NAME>
python main.py
```

If you do not want to install any packages, you can also use repl.it to run PyGame scripts!

Please create issues to tell me what you like/don't like about this project.
If I missed anything please create an issue too!

 - Hamolicious
