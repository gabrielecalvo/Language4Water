# Setup Guide
This guides describes how to get setup for this course in order to minimise the headaches. For some steps, it assumes you are running Windows.

The setup steps are:

1. Download [Anaconda](https://www.anaconda.com/distribution/#download-section) of the latest python 3.x version for your architecture
    - your architecture is most likely 64-bit, you can check following [these steps](https://support.microsoft.com/en-gb/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64).
    - if you have limited hard disk memory you can try use [Miniconda](https://docs.conda.io/en/latest/miniconda.html) instead of Anaconda.
2. Run the downloaded installer until the end.
    - it's not vital, but choose to add Anaconda to Path if requested.
3. Create a folder that you will use for this course.
    - you can pick where, but a good idea is probably in somewhere like ```C:\Users\<yourusername>\Documents\L4W_Python_Course```.
4. Copy the Jupyter Lab Runner batch script to your folder as follows:
    - going to this [link](https://raw.githubusercontent.com/gabrielecalvo/Language4Water/master/other/jupylab_runner.bat)
    - right clicking the content
    - selecting "Save Page As.." and choosing your folder as the destination.
5. Make a shortcut to the desktop for quicker access as follows:
    - right click on the ```jupylab_runner.bat``` file and select "Send To" > "Desktop (create a shortcut)"

You are all setup now :)

When you want to work on python data analysis all you need to do is go to your desktop and double click the shortcut you created. This will open a command window (that you need to keep open until you are done with the analysis) which, within a few seconds, will open Jupyter Lab in a tab of your default browser.

Notebooks are autosaved every 2 minutes, but you can also click the save button before closing the tab and command window.
