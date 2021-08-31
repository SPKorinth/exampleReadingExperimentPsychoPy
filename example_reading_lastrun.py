#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on Juli 08, 2021, at 17:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import pylink
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import monitors
from PIL import Image




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'example_reading'  # from the Builder filename that created this script
expInfo = {'participant_name': 'test', 'participant_number': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant_name'],expInfo['participant_number'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\idea\\Desktop\\exampleReadingExperimentPsychoPy\\example_reading_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=-1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='myMonitor', color=[0.5,0.5,0.5], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "ET_setup"
ET_setupClock = core.Clock()
# open a connection to the tracker
tk = pylink.EyeLink('100.1.1.1')

# Open an EDF data file on the Host and write a file header
# The file name should not exceeds 8 characters
dataFileName = 'tempName.EDF'
tk.openDataFile(dataFileName)

# define screen dimensions
scnWidth, scnHeight = (1680, 1050)

#open a window; set winType='pyglet' 
# for some strange reason PsychoPy Builder starts with a win useFBO = True
win = visual.Window((scnWidth, scnHeight), fullscr=True, monitor='myMonitor', 
                    winType='pyglet', color=[0.5,0.5,0.5], units='pix', allowStencil=True, 
                    allowGUI = False, useFBO = False)


win.mouseVisible = False


### function run when quit button is pressed
def shutDownFunc(): 
   # close the EDF data file and put the tracker in idle mode
   tk.setOfflineMode()
   pylink.pumpDelay(100)
   tk.closeDataFile() 
   # download EDF file to Display PC and put it in local folder ('edfData')
   msg = 'EDF data is transfering from EyeLink Host PC...'
   edfTransfer = visual.TextStim(win, text=msg, color='black')
   edfTransfer.draw()
   win.flip()
   pylink.pumpDelay(500)
   # make sure the 'edfData' folder is there, create one if not
   dataFolder = os.getcwd() + os.sep +'edfData'
   if not os.path.exists(dataFolder):
        os.makedirs(dataFolder)
       
   tk.receiveDataFile(dataFileName, 'edfData' + os.sep + dataFileName)
   # close the connection to tracker
   tk.close()

   # renaming edf file
   os.rename('edfData' + os.sep + dataFileName,'edfData' + os.sep + expInfo['participant_name'] +'_aborted.EDF')
   core.quit()


# since the standard quit key "esc" would interfer with the recalibration routine
#event.globalKeys.add(key='q', func=core.quit, name='shutdown')
event.globalKeys.add(key='q', func=shutDownFunc, name='shutdown')



# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instruc = visual.TextStim(win=win, name='text_instruc',
    text='Dear participant,\n\nDuring the following experiment we will record your eye movements while you are reading ten simple sentences. Before we can start we will have to calibrate the eye tracker. For this purpose you will have to follow the little point that will appear at various positions of the screen. Please direct your gaze at the point until it disappears. It is not important that you do this quickly but it is crucial that you do this as accurately as possible. \n\n1.) Before each trial a little dot will appear at the left side of the screen. Please look at it and press the space bar as soon as you are ready; the sentence will appear.  \n\n2.) Read the sentence at your usual reading speed and fixate the dot at the right side of the screen. Press the space bar again to indicate that you have finished reading.\n\n3.) A very simple question concerning the content of the sentence will appear. For option a) press the arrow key left; for option b) press the arrow key right.\n\nPress the space bar to start the experiment.',
    font='Courier New',
    units='pix', pos=(0, 0), height=22, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_instruction_go = keyboard.Keyboard()

# Initialize components for Routine "ET_calibration"
ET_calibrationClock = core.Clock()

# Initialize components for Routine "ET_backdrop"
ET_backdropClock = core.Clock()

# Initialize components for Routine "ET_drift"
ET_driftClock = core.Clock()

# Initialize components for Routine "sentence"
sentenceClock = core.Clock()
text_sent = visual.TextStim(win=win, name='text_sent',
    text='',
    font='Courier New',
    units='pix', pos=(0, 0), height=22, wrapWidth=1520, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fix_end_point = visual.ShapeStim(
    win=win, name='fix_end_point',units='pix', 
    size=(16,16), vertices='circle',
    ori=0, pos=(760, 0),
    lineWidth=5,     colorSpace='rgb',  lineColor=[-1.000,-1.000,-1.000], fillColor=[0.5,0.5,0.5],
    opacity=1, depth=-1.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "question"
questionClock = core.Clock()
text_quest = visual.TextStim(win=win, name='text_quest',
    text='',
    font='Courier New',
    units='pix', pos=(0, 100), height=22, wrapWidth=800, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_ans_1 = visual.TextStim(win=win, name='text_ans_1',
    text='',
    font='Courier New',
    pos=(0, 50), height=22, wrapWidth=700, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_ans_2 = visual.TextStim(win=win, name='text_ans_2',
    text='',
    font='Courier New',
    pos=(0, 0), height=22, wrapWidth=700, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_quest = keyboard.Keyboard()

# Initialize components for Routine "ET_stop_record"
ET_stop_recordClock = core.Clock()

# Initialize components for Routine "ET_exit"
ET_exitClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Thanks!',
    font='Courier New',
    pos=(0, 0), height=22, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ET_setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ET_setupComponents = []
for thisComponent in ET_setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ET_setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ET_setup"-------
while continueRoutine:
    # get current time
    t = ET_setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ET_setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ET_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ET_setup"-------
for thisComponent in ET_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ET_setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_instruction_go.keys = []
key_instruction_go.rt = []
_key_instruction_go_allKeys = []
text_instruc.alignText='left'
# initiate a mouse instance just to hide it
mouse = event.Mouse(win=win)
# hiding the mouse
mouse.setPos(newPos=(10000,-10000))
# keep track of which components have finished
instructionsComponents = [text_instruc, key_instruction_go]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruc* updates
    if text_instruc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_instruc.frameNStart = frameN  # exact frame index
        text_instruc.tStart = t  # local t and not account for scr refresh
        text_instruc.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instruc, 'tStartRefresh')  # time at next scr refresh
        text_instruc.setAutoDraw(True)
    
    # *key_instruction_go* updates
    waitOnFlip = False
    if key_instruction_go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_instruction_go.frameNStart = frameN  # exact frame index
        key_instruction_go.tStart = t  # local t and not account for scr refresh
        key_instruction_go.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_instruction_go, 'tStartRefresh')  # time at next scr refresh
        key_instruction_go.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_instruction_go.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_instruction_go.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_instruction_go.status == STARTED and not waitOnFlip:
        theseKeys = key_instruction_go.getKeys(keyList=['space'], waitRelease=False)
        _key_instruction_go_allKeys.extend(theseKeys)
        if len(_key_instruction_go_allKeys):
            key_instruction_go.keys = _key_instruction_go_allKeys[-1].name  # just the last key pressed
            key_instruction_go.rt = _key_instruction_go_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ET_calibration"-------
continueRoutine = True
# update component parameters for each repeat

# set up a custom graphics envrionment (EyeLinkCoreGraphicsPsychopy) for calibration
genv = EyeLinkCoreGraphicsPsychoPy(tk, win)

# Beeps to play during calibration, validation and drift correction
# parameters: target, good, error
#     target -- sound to play when target moves
#     good -- sound to play on successful operation
#     error -- sound to play on failure or interruption
# Each parameter could be ''--default sound, 'off'--no sound, or a wav file
genv.setCalibrationSounds('off', 'off', 'off')

# calibration target size 
genv.setTargetSize(20)

# configure the calibration target, could be a 'circle', 
genv.setTargetType('circle')

# open the graphics env
pylink.openGraphicsEx(genv)

# put the tracker in idle mode before we change its parameters
tk.setOfflineMode()
pylink.pumpDelay(100)

# IMPORTANT: send screen resolution to the tracker
# see Eyelink Installation Guide, Section 8.4: Customizing Your PHYSICAL.INI Settings
tk.sendCommand("screen_pixel_coords = 0 0 %d %d" % (scnWidth-1, scnHeight-1))
# save screen resolution in EDF data, so Data Viewer can correctly load experimental graphics
tk.sendMessage("DISPLAY_COORDS = 0 0 %d %d" % (scnWidth-1, scnHeight-1))
# sampling rate, 250, 500, 1000, or 2000; this command is not supported for EyeLInk II/I trackers
tk.sendCommand("sample_rate 500")
# detect eye events based on "GAZE" (or "HREF") data
tk.sendCommand("recording_parse_type = GAZE")
# Saccade detection thresholds: 0-> standard/coginitve, 1-> sensitive/psychophysiological
# see Eyelink User Manual, Section 4.3: EyeLink Parser Configuration
tk.sendCommand("select_parser_configuration 0") 
# choose a calibration type, H3, HV3, HV5, HV13 (HV = horiztonal/vertical), 
# tk.setCalibrationType('HV9') also works, see the Pylink manual
tk.sendCommand("calibration_type = HV5") 

tk.sendMessage('subject_nr %s' % expInfo['participant_number'])
# tracker hardware, 1-EyeLink I, 2-EyeLink II, 3-Newer models (1000/1000Plus/Portable DUO)
hardware_ver = tk.getTrackerVersion()
# tracking software version
software_ver = 0
if hardware_ver == 3:
    tvstr = tk.getTrackerVersionString()
    vindex = tvstr.find("EYELINK CL")
    software_ver = float(tvstr.split()[-1])

# sample and event data saved in EDF data file
# see sectin 4.6 of the EyeLink user manual, software version > 4 adds remote tracking (and thus HTARGET)
tk.sendCommand("file_event_filter = LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT")
if software_ver >= 4:
    tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
else:
    tk.sendCommand("file_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")

# sample and event data available over the link    
tk.sendCommand("link_event_filter = LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT")
if software_ver >= 4:
    tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,HTARGET,INPUT")
else:
    tk.sendCommand("link_sample_data  = LEFT,RIGHT,GAZE,GAZERES,PUPIL,HREF,AREA,STATUS,INPUT")


# instructions for calibration 
msg = visual.TextStim(win, text='Press ENTER twice\n' + 
                                'to start eye-tracker setup')
msg.draw()

win.flip()

event.waitKeys()

# set up the camera and calibrate the tracker
tk.doTrackerSetup()

# hiding the mouse
mouse.setPos(newPos=(10000,-10000))

# keep track of which components have finished
ET_calibrationComponents = []
for thisComponent in ET_calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ET_calibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ET_calibration"-------
while continueRoutine:
    # get current time
    t = ET_calibrationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ET_calibrationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ET_calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ET_calibration"-------
for thisComponent in ET_calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ET_calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('example_sentences.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ET_backdrop"-------
    continueRoutine = True
    # update component parameters for each repeat
    # put the tracker in idle mode before we start recording
    tk.setOfflineMode()
    pylink.pumpDelay(100)
    
    
    # backdrop image on the Host screen
    # this is SLOW and may cause timing problems for some tasks 
    # open image with the PIL Image moduel
    im = Image.open('images' + os.sep + 'trial_%d.png' %trial_index_var) 
    #im = Image.open('images' + os.sep + 'static.png') 
    w,h = im.size
    pixels = im.load()
    # use the list comprehension trick to convert all image pixels into a <pixel> format
    # supported by the Host PC, pixels = [line1, ...lineH], line = [pix1,...pixW], pix=(R,G,B)
    pixels_2transfer = [[pixels[i,j] for i in range(w)] for j in range(h)]
    tk.sendCommand('clear_screen 0') # clear the host screen
    # call the bitmapBackdrop() command to show backdrop image on the Host
    # arguments: width, height, pixel, crop_x, crop_y, crop_width, crop_height, x, y on Host, option
    #tk.bitmapBackdrop(w, h, pixels_2transfer, 0, 0,w,h,0,0,pylink.BX_MAXCONTRAST)
    tk.bitmapSaveAndBackdrop(w, h, pixels_2transfer, 0, 0, w, h, 'tmp_img', 'images'+ os.sep ,
    pylink.SV_NOREPLACE, 0, 0, pylink.BX_MAXCONTRAST)
    
    # keep track of which components have finished
    ET_backdropComponents = []
    for thisComponent in ET_backdropComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ET_backdropClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ET_backdrop"-------
    while continueRoutine:
        # get current time
        t = ET_backdropClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ET_backdropClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ET_backdropComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ET_backdrop"-------
    for thisComponent in ET_backdropComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ET_backdrop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ET_drift"-------
    continueRoutine = True
    # update component parameters for each repeat
    
    # drift check
    # the doDriftCorrect() function requires target position in integers
    # the last two arguments: draw_target (1-default, 0-user draw the target then call this function)
    #                         allow_setup (1-press ESCAPE to recalibrate, 0-not allowed) 
    try:
        err = tk.doDriftCorrect(88,525, 1, 1)
    except:
            tk.doTrackerSetup()
            tk.doDriftCorrect(88,525,1,1)
    
    
    # send the standard "TRIALID" message to mark the start of a trial
    # see Data Viewer User Manual, Section 7: Protocol for EyeLink Data to Viewer Integration
    tk.sendMessage('TRIALID %d' % trial_index_var)
    tk.sendMessage('stimulus %s'% sent_var)
    # record_status_message : show some info on the Host PC - OPTIONAL
    # here we show how many trial has been tested
    #tk.sendCommand("record_status_message 'TRIAL number %s'"% trial_index_var)
    tk.sendCommand("record_status_message 'TRIAL number %s out of 10'"% (trials.thisN +1))
    
    # start recording    
    # arguments: sample_to_file, events_to_file, sample_over_link, event_over_link (1-yes, 0-no)
    err = tk.startRecording(1, 1, 1, 1)
    pylink.pumpDelay(100)  # wait for 100 ms to cache some samples
    tk.sendMessage('start_trial_index %d' % (trials.thisN+1))
    tk.sendMessage('start_stim_id %d' % trial_index_var)
    
    
    # hiding the mouse
    mouse.setPos(newPos=(10000,-10000))
    
    win.flip()
    # keep track of which components have finished
    ET_driftComponents = []
    for thisComponent in ET_driftComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ET_driftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ET_drift"-------
    while continueRoutine:
        # get current time
        t = ET_driftClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ET_driftClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ET_driftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ET_drift"-------
    for thisComponent in ET_driftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ET_drift" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "sentence"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_sent.setText(sent_var)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    text_sent.alignText='left'
    def sendMSGsentStart():
        tk.sendMessage('onset_sentence %d' %trial_index_var)
    win.callOnFlip(sendMSGsentStart)
    
    # hiding the mouse
    mouse.setPos(newPos=(10000,-10000))
    # keep track of which components have finished
    sentenceComponents = [text_sent, fix_end_point, key_resp]
    for thisComponent in sentenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    sentenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "sentence"-------
    while continueRoutine:
        # get current time
        t = sentenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=sentenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sent* updates
        if text_sent.status == NOT_STARTED and frameN >= 0.0:
            # keep track of start time/frame for later
            text_sent.frameNStart = frameN  # exact frame index
            text_sent.tStart = t  # local t and not account for scr refresh
            text_sent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sent, 'tStartRefresh')  # time at next scr refresh
            text_sent.setAutoDraw(True)
        
        # *fix_end_point* updates
        if fix_end_point.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            fix_end_point.frameNStart = frameN  # exact frame index
            fix_end_point.tStart = t  # local t and not account for scr refresh
            fix_end_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_end_point, 'tStartRefresh')  # time at next scr refresh
            fix_end_point.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if len(key_resp.keys)>0:
            tk.sendMessage('finished_reading  %d' % trial_index_var)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sentenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sentence"-------
    for thisComponent in sentenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "sentence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_quest.setText(quest_var)
    text_ans_1.setText(ans_1_var)
    text_ans_2.setText(ans_2_var)
    key_resp_quest.keys = []
    key_resp_quest.rt = []
    _key_resp_quest_allKeys = []
    text_quest.alignText='left'
    text_ans_1.alignText='left'
    text_ans_2.alignText='left'
    
    # hiding the mouse
    mouse.setPos(newPos=(10000,-10000))
    
    def sendMSGquestStart():
        tk.sendMessage('onset_question %d' %trial_index_var)
    win.callOnFlip(sendMSGquestStart)
    # keep track of which components have finished
    questionComponents = [text_quest, text_ans_1, text_ans_2, key_resp_quest]
    for thisComponent in questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "question"-------
    while continueRoutine:
        # get current time
        t = questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_quest* updates
        if text_quest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_quest.frameNStart = frameN  # exact frame index
            text_quest.tStart = t  # local t and not account for scr refresh
            text_quest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_quest, 'tStartRefresh')  # time at next scr refresh
            text_quest.setAutoDraw(True)
        
        # *text_ans_1* updates
        if text_ans_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ans_1.frameNStart = frameN  # exact frame index
            text_ans_1.tStart = t  # local t and not account for scr refresh
            text_ans_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ans_1, 'tStartRefresh')  # time at next scr refresh
            text_ans_1.setAutoDraw(True)
        
        # *text_ans_2* updates
        if text_ans_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ans_2.frameNStart = frameN  # exact frame index
            text_ans_2.tStart = t  # local t and not account for scr refresh
            text_ans_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ans_2, 'tStartRefresh')  # time at next scr refresh
            text_ans_2.setAutoDraw(True)
        
        # *key_resp_quest* updates
        waitOnFlip = False
        if key_resp_quest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_quest.frameNStart = frameN  # exact frame index
            key_resp_quest.tStart = t  # local t and not account for scr refresh
            key_resp_quest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_quest, 'tStartRefresh')  # time at next scr refresh
            key_resp_quest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_quest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_quest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_quest.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_quest.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_quest_allKeys.extend(theseKeys)
            if len(_key_resp_quest_allKeys):
                key_resp_quest.keys = _key_resp_quest_allKeys[-1].name  # just the last key pressed
                key_resp_quest.rt = _key_resp_quest_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        if len(key_resp_quest.keys)>0:
            tk.sendMessage('response %s' %key_resp_quest.keys)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question"-------
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_quest.keys in ['', [], None]:  # No response was made
        key_resp_quest.keys = None
    trials.addData('key_resp_quest.keys',key_resp_quest.keys)
    if key_resp_quest.keys != None:  # we had a response
        trials.addData('key_resp_quest.rt', key_resp_quest.rt)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ET_stop_record"-------
    continueRoutine = True
    # update component parameters for each repeat
    # stop recording
    tk.sendMessage('stop_recording_trial_index %d' % (trials.thisN +1))
    tk.stopRecording() 
    # keep track of which components have finished
    ET_stop_recordComponents = []
    for thisComponent in ET_stop_recordComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ET_stop_recordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ET_stop_record"-------
    while continueRoutine:
        # get current time
        t = ET_stop_recordClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ET_stop_recordClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ET_stop_recordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ET_stop_record"-------
    for thisComponent in ET_stop_recordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ET_stop_record" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "ET_exit"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ET_exitComponents = []
for thisComponent in ET_exitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ET_exitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ET_exit"-------
while continueRoutine:
    # get current time
    t = ET_exitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ET_exitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ET_exitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ET_exit"-------
for thisComponent in ET_exitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ET_exit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_end]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)
# close the EDF data file and put the tracker in idle mode
tk.setOfflineMode()
pylink.pumpDelay(100)
tk.closeDataFile()

# download EDF file to Display PC and put it in local folder ('edfData')
msg = 'EDF data is transfering from EyeLink Host PC...'
edfTransfer = visual.TextStim(win, text=msg, color='black')
edfTransfer.draw()
win.flip()
pylink.pumpDelay(500)

# make sure the 'edfData' folder is there, create one if not
dataFolder = os.getcwd() + os.sep +'edfData'
if not os.path.exists(dataFolder): 
    os.makedirs(dataFolder)
tk.receiveDataFile(dataFileName, 'edfData' + os.sep + dataFileName)

# close the connection to tracker
tk.close()

# renaming edf file
os.rename('edfData' + os.sep + dataFileName,'edfData' + os.sep + expInfo['participant_name'] +'.EDF')

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
