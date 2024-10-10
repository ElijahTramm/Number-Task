#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Oct  8 14:27:48 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from startScreenCode
# Preset end code (press 'e' to go to end screen)
key_pressed = False

# Set accuracy counts to zero
number_total = 0
number_correct = 0
number_incorrect = 0
number_firstcorrect = 0
incorrect_at_first = 0
incorrect_at_second = 0
incorrect_at_third = 0
incorrect_at_fourth = 0

# Hard code feeder and turn on*
#import sys
#sys.path.append(r'C:\Users\uwpsy\mcculw')
#import feeder_api
#feeder_api.initialize_usb_dio(True)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'phase1Prototype'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/elijahtramm/Desktop/numberTask/phase5_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "startScreen" ---
# Run 'Begin Experiment' code from startScreenCode
#Import code for turning mouse off
#from psychopy import core

#Timer for experiment
#myClock = clore.Clock()
startScreenText = visual.TextStim(win=win, name='startScreenText',
    text='Click anywhere to start\n\nPlease check that the touchscreen is working',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
startScreenMouse = event.Mouse(win=win)
x, y = [None, None]
startScreenMouse.mouseClock = core.Clock()

# --- Initialize components for Routine "startBox" ---
# Run 'Begin Experiment' code from startBoxCode
firstArrayRand = []
secondArrayRand = []


# --- Initialize components for Routine "locationRandomization" ---

# --- Initialize components for Routine "firstArray" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
pinkOne = visual.ImageStim(
    win=win,
    name='pinkOne', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
pinkTwo = visual.ImageStim(
    win=win,
    name='pinkTwo', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
pinkThree = visual.ImageStim(
    win=win,
    name='pinkThree', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
pinkFour = visual.ImageStim(
    win=win,
    name='pinkFour', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "firstFeedback" ---
feedbackStim = visual.ImageStim(
    win=win,
    name='feedbackStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
feedbackAudio = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='feedbackAudio')
feedbackAudio.setVolume(1.0)

# --- Initialize components for Routine "pause" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "locationRandomization" ---

# --- Initialize components for Routine "secondArray" ---
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
greenOne = visual.ImageStim(
    win=win,
    name='greenOne', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
greenTwo = visual.ImageStim(
    win=win,
    name='greenTwo', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
greenThree = visual.ImageStim(
    win=win,
    name='greenThree', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
greenFour = visual.ImageStim(
    win=win,
    name='greenFour', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)

# --- Initialize components for Routine "secondFeedback" ---
secondFeedbackStim = visual.ImageStim(
    win=win,
    name='secondFeedbackStim', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
secondFeedbackAudio = sound.Sound('A', secs=2, stereo=True, hamming=True,
    name='secondFeedbackAudio')
secondFeedbackAudio.setVolume(1.0)

# --- Initialize components for Routine "pause" ---
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "endScreen" ---
endScreenText = visual.TextStim(win=win, name='endScreenText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "End" ---

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "startScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from startScreenCode
#Hide mouse on screen
#event.mouse(visible = False)
# setup some python lists for storing info about the startScreenMouse
startScreenMouse.x = []
startScreenMouse.y = []
startScreenMouse.leftButton = []
startScreenMouse.midButton = []
startScreenMouse.rightButton = []
startScreenMouse.time = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
startScreenComponents = [startScreenText, startScreenMouse]
for thisComponent in startScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "startScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startScreenText* updates
    if startScreenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startScreenText.frameNStart = frameN  # exact frame index
        startScreenText.tStart = t  # local t and not account for scr refresh
        startScreenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startScreenText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startScreenText.started')
        startScreenText.setAutoDraw(True)
    # *startScreenMouse* updates
    if startScreenMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startScreenMouse.frameNStart = frameN  # exact frame index
        startScreenMouse.tStart = t  # local t and not account for scr refresh
        startScreenMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startScreenMouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('startScreenMouse.started', t)
        startScreenMouse.status = STARTED
        startScreenMouse.mouseClock.reset()
        prevButtonState = startScreenMouse.getPressed()  # if button is down already this ISN'T a new click
    if startScreenMouse.status == STARTED:  # only update if started and not finished!
        buttons = startScreenMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                x, y = startScreenMouse.getPos()
                startScreenMouse.x.append(x)
                startScreenMouse.y.append(y)
                buttons = startScreenMouse.getPressed()
                startScreenMouse.leftButton.append(buttons[0])
                startScreenMouse.midButton.append(buttons[1])
                startScreenMouse.rightButton.append(buttons[2])
                startScreenMouse.time.append(startScreenMouse.mouseClock.getTime())
                
                continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "startScreen" ---
for thisComponent in startScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('startScreenMouse.x', startScreenMouse.x)
thisExp.addData('startScreenMouse.y', startScreenMouse.y)
thisExp.addData('startScreenMouse.leftButton', startScreenMouse.leftButton)
thisExp.addData('startScreenMouse.midButton', startScreenMouse.midButton)
thisExp.addData('startScreenMouse.rightButton', startScreenMouse.rightButton)
thisExp.addData('startScreenMouse.time', startScreenMouse.time)
thisExp.nextEntry()
# the Routine "startScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
arrayLoop = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('phase5Randomizer.csv'),
    seed=None, name='arrayLoop')
thisExp.addLoop(arrayLoop)  # add the loop to the experiment
thisArrayLoop = arrayLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisArrayLoop.rgb)
if thisArrayLoop != None:
    for paramName in thisArrayLoop:
        exec('{} = thisArrayLoop[paramName]'.format(paramName))

for thisArrayLoop in arrayLoop:
    currentLoop = arrayLoop
    # abbreviate parameter names if possible (e.g. rgb = thisArrayLoop.rgb)
    if thisArrayLoop != None:
        for paramName in thisArrayLoop:
            exec('{} = thisArrayLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "startBox" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from startBoxCode
    #Mouse not visible
    #event.Mouse(visible=False)
    
    #Experiment ends after 4 hours
    #if myClock.getTime() > 14400:
        #trials.finished = True
        #continueRoutine = False
    
    firstArrayRand.clear()
    firstArrayRand.append(randint(0,5))
    
    secondArrayRand.clear()
    secondArrayRand.append(randint(0,5))
    # keep track of which components have finished
    startBoxComponents = []
    for thisComponent in startBoxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "startBox" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from startBoxCode
        #keys = event.getKeys()
        #if 'e' in keys:
        #    key_pressed = True
        #if key_pressed == True:
        #    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startBoxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startBox" ---
    for thisComponent in startBoxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "startBox" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    firstLoop = data.TrialHandler(nReps=playfirstArray * firstArrayRand[0], method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='firstLoop')
    thisExp.addLoop(firstLoop)  # add the loop to the experiment
    thisFirstLoop = firstLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFirstLoop.rgb)
    if thisFirstLoop != None:
        for paramName in thisFirstLoop:
            exec('{} = thisFirstLoop[paramName]'.format(paramName))
    
    for thisFirstLoop in firstLoop:
        currentLoop = firstLoop
        # abbreviate parameter names if possible (e.g. rgb = thisFirstLoop.rgb)
        if thisFirstLoop != None:
            for paramName in thisFirstLoop:
                exec('{} = thisFirstLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "locationRandomization" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from locationRandomizationCode
        # Set grid of possible positions
        xys = [[-.5, .275], [0, .275], [.5, .275], [-.5, 0], [.5, 0], [-.5, -.275], [0, -.275], [.5, -.275], [0, 0]]
        # randomize the coordinates
        shuffle(xys)
        # keep track of which components have finished
        locationRandomizationComponents = []
        for thisComponent in locationRandomizationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "locationRandomization" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in locationRandomizationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "locationRandomization" ---
        for thisComponent in locationRandomizationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "locationRandomization" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "firstArray" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from firstArrayCode
        
        clickableStims = [pinkOne, pinkTwo, pinkThree, pinkFour]
        for stim in clickableStims:
            stim.opacity = 1
        
        clickedStims = []
        
        clickCounter = 0
        
        timer = core.Clock()
        #playFirstTouch = []
        pinkOne.setPos([xys[0]])
        pinkOne.setImage('stimuli/pinkOne.png')
        pinkTwo.setPos([xys[2]])
        pinkTwo.setImage('stimuli/pinkTwo.png')
        pinkThree.setPos([xys[3]])
        pinkThree.setImage('stimuli/pinkThree.png')
        pinkFour.setPos([xys[1]])
        pinkFour.setImage('stimuli/pinkFour.png')
        # keep track of which components have finished
        firstArrayComponents = [mouse, pinkOne, pinkTwo, pinkThree, pinkFour]
        for thisComponent in firstArrayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "firstArray" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(clickableStims)
                            clickableList = clickableStims
                        except:
                            clickableList = [clickableStims]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse.getPos()
                            mouse.x.append(x)
                            mouse.y.append(y)
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
            # Run 'Each Frame' code from firstArrayCode
            
            #record clicks
            for stim in clickableStims:
                if mouse.isPressedIn(stim):
                    clickedStims.append(stim.name)
                    clickCounter += 1
                    if len(mouse.clicked_name) == clickCounter:
                        timer.reset()
                        if timer.getTime() < 3:
                            clickableStims = []
                            stim.opacity = .5
            
            if timer.getTime() >= 3:
                clickableStims = [pinkOne, pinkTwo, pinkThree, pinkFour]
                for stim in clickableStims:
                    stim.opacity = 1
                #playFirstTouch = []
            
            #Check correctness
            if len(mouse.clicked_name) == 1 and mouse.clicked_name[0] != 'pinkOne':
                incorrect_at_first += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            if len(mouse.clicked_name) == 2 and mouse.clicked_name[1] != 'pinkTwo':
                incorrect_at_second += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            if len(mouse.clicked_name) == 3 and mouse.clicked_name[2] != 'pinkThree':
                incorrect_at_third += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            #end
            if len(mouse.clicked_name) == 4 and mouse.clicked_name[3] != 'pinkFour':
                continueRoutine = False
                for stim in clickableStims:
                    stim.opacity = 1
            elif len(mouse.clicked_name) == 4 and mouse.clicked_name[3] == 'pinkFour':
                continueRoutine = False
                for stim in clickableStims:
                    stim.opacity = 1
            
            # *pinkOne* updates
            if pinkOne.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pinkOne.frameNStart = frameN  # exact frame index
                pinkOne.tStart = t  # local t and not account for scr refresh
                pinkOne.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pinkOne, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pinkOne.started')
                pinkOne.setAutoDraw(True)
            
            # *pinkTwo* updates
            if pinkTwo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pinkTwo.frameNStart = frameN  # exact frame index
                pinkTwo.tStart = t  # local t and not account for scr refresh
                pinkTwo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pinkTwo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pinkTwo.started')
                pinkTwo.setAutoDraw(True)
            
            # *pinkThree* updates
            if pinkThree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pinkThree.frameNStart = frameN  # exact frame index
                pinkThree.tStart = t  # local t and not account for scr refresh
                pinkThree.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pinkThree, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pinkThree.started')
                pinkThree.setAutoDraw(True)
            
            # *pinkFour* updates
            if pinkFour.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pinkFour.frameNStart = frameN  # exact frame index
                pinkFour.tStart = t  # local t and not account for scr refresh
                pinkFour.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pinkFour, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pinkFour.started')
                pinkFour.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstArrayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "firstArray" ---
        for thisComponent in firstArrayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for firstLoop (TrialHandler)
        firstLoop.addData('mouse.x', mouse.x)
        firstLoop.addData('mouse.y', mouse.y)
        firstLoop.addData('mouse.leftButton', mouse.leftButton)
        firstLoop.addData('mouse.midButton', mouse.midButton)
        firstLoop.addData('mouse.rightButton', mouse.rightButton)
        firstLoop.addData('mouse.time', mouse.time)
        firstLoop.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "firstArray" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "firstFeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from firstFeedbackCode
        #keys = event.getKeys()
        #if 'e' in keys:
        #    key_pressed = True
        #if key_pressed == True:
        #    continueRoutine = False
        
        if mouse.clicked_name == ['pinkOne', 'pinkTwo', 'pinkThree', 'pinkFour']:
            feedbackColor = "stimuli/GreenCorrectScreen.png"
            feedbackSound = "stimuli/Positive.wav"
            #feeder_api.pulse_feeder(1, True)
            number_correct += 1
            number_total += 1
            correct = 1
        
        else:
            feedbackColor = "stimuli/solid-red-background.jpg"
            feedbackSound = "stimuli/Negative.wav"
            number_incorrect +=1
            number_total += 1
        
            correct = 0
        
        thisExp.addData('correct_answer', correct)
        feedbackStim.setImage(feedbackColor)
        feedbackAudio.setSound(feedbackSound, secs=2, hamming=True)
        feedbackAudio.setVolume(1.0, log=False)
        # keep track of which components have finished
        firstFeedbackComponents = [feedbackStim, feedbackAudio]
        for thisComponent in firstFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "firstFeedback" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackStim* updates
            if feedbackStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackStim.frameNStart = frameN  # exact frame index
                feedbackStim.tStart = t  # local t and not account for scr refresh
                feedbackStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackStim.started')
                feedbackStim.setAutoDraw(True)
            if feedbackStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackStim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackStim.tStop = t  # not accounting for scr refresh
                    feedbackStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackStim.stopped')
                    feedbackStim.setAutoDraw(False)
            # start/stop feedbackAudio
            if feedbackAudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackAudio.frameNStart = frameN  # exact frame index
                feedbackAudio.tStart = t  # local t and not account for scr refresh
                feedbackAudio.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('feedbackAudio.started', tThisFlipGlobal)
                feedbackAudio.play(when=win)  # sync with win flip
            if feedbackAudio.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackAudio.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackAudio.tStop = t  # not accounting for scr refresh
                    feedbackAudio.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedbackAudio.stopped')
                    feedbackAudio.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "firstFeedback" ---
        for thisComponent in firstFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedbackAudio.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "pause" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        pauseComponents = [text]
        for thisComponent in pauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed playfirstArray * firstArrayRand[0] repeats of 'firstLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    secondLoop = data.TrialHandler(nReps=playsecondArray * secondArrayRand[0], method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='secondLoop')
    thisExp.addLoop(secondLoop)  # add the loop to the experiment
    thisSecondLoop = secondLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSecondLoop.rgb)
    if thisSecondLoop != None:
        for paramName in thisSecondLoop:
            exec('{} = thisSecondLoop[paramName]'.format(paramName))
    
    for thisSecondLoop in secondLoop:
        currentLoop = secondLoop
        # abbreviate parameter names if possible (e.g. rgb = thisSecondLoop.rgb)
        if thisSecondLoop != None:
            for paramName in thisSecondLoop:
                exec('{} = thisSecondLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "locationRandomization" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from locationRandomizationCode
        # Set grid of possible positions
        xys = [[-.5, .275], [0, .275], [.5, .275], [-.5, 0], [.5, 0], [-.5, -.275], [0, -.275], [.5, -.275], [0, 0]]
        # randomize the coordinates
        shuffle(xys)
        # keep track of which components have finished
        locationRandomizationComponents = []
        for thisComponent in locationRandomizationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "locationRandomization" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in locationRandomizationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "locationRandomization" ---
        for thisComponent in locationRandomizationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "locationRandomization" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "secondArray" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse_2
        mouse_2.x = []
        mouse_2.y = []
        mouse_2.leftButton = []
        mouse_2.midButton = []
        mouse_2.rightButton = []
        mouse_2.time = []
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from secondArrayCode
        #keys = event.getKeys()
        #if 'e' in keys:
        #    key_pressed = True
        #if key_pressed == True:
        #    #exit trial does not count
        #    number_total -= 1
        #    trials.finished = True
        #    continueRoutine = False
        
        clickableStims = [greenOne, greenTwo, greenThree, greenFour]
        for stim in clickableStims:
            stim.opacity = 1
        
        clickedStims = []
        
        secondTimer = core.Clock()
        #playFirstTouch = []
        greenOne.setPos([xys[0]])
        greenOne.setImage('stimuli/greenOne.png')
        greenTwo.setPos([xys[2]])
        greenTwo.setImage('stimuli/greenTwo.png')
        greenThree.setPos([xys[3]])
        greenThree.setImage('stimuli/greenThree.png')
        greenFour.setPos([xys[1]])
        greenFour.setImage('stimuli/greenFour.png')
        # keep track of which components have finished
        secondArrayComponents = [mouse_2, greenOne, greenTwo, greenThree, greenFour]
        for thisComponent in secondArrayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "secondArray" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse_2* updates
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_2.started', t)
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(clickableStims)
                            clickableList = clickableStims
                        except:
                            clickableList = [clickableStims]
                        for obj in clickableList:
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_2.getPos()
                            mouse_2.x.append(x)
                            mouse_2.y.append(y)
                            buttons = mouse_2.getPressed()
                            mouse_2.leftButton.append(buttons[0])
                            mouse_2.midButton.append(buttons[1])
                            mouse_2.rightButton.append(buttons[2])
                            mouse_2.time.append(mouse_2.mouseClock.getTime())
            # Run 'Each Frame' code from secondArrayCode
            
            #record clicks
            for stim in clickableStims:
                if mouse.isPressedIn(stim):
                    clickedStims.append(stim.name)
                    secondTimer.reset()
                    if secondTimer.getTime() < 3:
                        clickableStims = []
                        stim.opacity = .5
            
            if secondTimer.getTime() >= 3:
                clickableStims = [greenOne, greenTwo, greenThree, greenFour]
                for stim in clickableStims:
                    stim.opacity = .8
                #playFirstTouch = []
            
            #Check correctness
            if len(mouse_2.clicked_name) == 1 and mouse_2.clicked_name[0] != 'greenFour':
                incorrect_at_first += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            if len(mouse_2.clicked_name) == 2 and mouse_2.clicked_name[1] != 'greenThree':
                incorrect_at_second += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            if len(mouse_2.clicked_name) == 3 and mouse_2.clicked_name[2] != 'greenTwo':
                incorrect_at_third += 1
                number_incorrect +=1
                for stim in clickableStims:
                    stim.opacity = 1
                continueRoutine = False
            
            #end
            if len(mouse_2.clicked_name) == 4 and mouse_2.clicked_name[3] != 'greenOne':
                continueRoutine = False
                for stim in clickableStims:
                    stim.opacity = 1
            elif len(mouse_2.clicked_name) == 4 and mouse_2.clicked_name[3] == 'greenOne':
                continueRoutine = False
                for stim in clickableStims:
                    stim.opacity = 1
            
            # *greenOne* updates
            if greenOne.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                greenOne.frameNStart = frameN  # exact frame index
                greenOne.tStart = t  # local t and not account for scr refresh
                greenOne.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(greenOne, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'greenOne.started')
                greenOne.setAutoDraw(True)
            
            # *greenTwo* updates
            if greenTwo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                greenTwo.frameNStart = frameN  # exact frame index
                greenTwo.tStart = t  # local t and not account for scr refresh
                greenTwo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(greenTwo, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'greenTwo.started')
                greenTwo.setAutoDraw(True)
            
            # *greenThree* updates
            if greenThree.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                greenThree.frameNStart = frameN  # exact frame index
                greenThree.tStart = t  # local t and not account for scr refresh
                greenThree.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(greenThree, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'greenThree.started')
                greenThree.setAutoDraw(True)
            
            # *greenFour* updates
            if greenFour.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                greenFour.frameNStart = frameN  # exact frame index
                greenFour.tStart = t  # local t and not account for scr refresh
                greenFour.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(greenFour, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'greenFour.started')
                greenFour.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in secondArrayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "secondArray" ---
        for thisComponent in secondArrayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for secondLoop (TrialHandler)
        secondLoop.addData('mouse_2.x', mouse_2.x)
        secondLoop.addData('mouse_2.y', mouse_2.y)
        secondLoop.addData('mouse_2.leftButton', mouse_2.leftButton)
        secondLoop.addData('mouse_2.midButton', mouse_2.midButton)
        secondLoop.addData('mouse_2.rightButton', mouse_2.rightButton)
        secondLoop.addData('mouse_2.time', mouse_2.time)
        secondLoop.addData('mouse_2.clicked_name', mouse_2.clicked_name)
        # the Routine "secondArray" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "secondFeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from secondFeedbackCode
        #keys = event.getKeys()
        #if 'e' in keys:
        #    key_pressed = True
        #if key_pressed == True:
        #    continueRoutine = False
        
        if mouse_2.clicked_name == ['greenFour', 'greenThree', 'greenTwo', 'greenOne']:
            feedbackColor = "stimuli/GreenCorrectScreen.png"
            feedbackSound = "stimuli/Positive.wav"
            #feeder_api.pulse_feeder(1, True)
            number_correct += 1
            number_total += 1
        
        else:
            feedbackColor = "stimuli/solid-red-background.jpg"
            feedbackSound = "stimuli/Negative.wav"
            number_incorrect +=1
            number_total += 1
        
        secondFeedbackStim.setImage(feedbackColor)
        secondFeedbackAudio.setSound(feedbackSound, secs=2, hamming=True)
        secondFeedbackAudio.setVolume(1.0, log=False)
        # keep track of which components have finished
        secondFeedbackComponents = [secondFeedbackStim, secondFeedbackAudio]
        for thisComponent in secondFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "secondFeedback" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *secondFeedbackStim* updates
            if secondFeedbackStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                secondFeedbackStim.frameNStart = frameN  # exact frame index
                secondFeedbackStim.tStart = t  # local t and not account for scr refresh
                secondFeedbackStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(secondFeedbackStim, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'secondFeedbackStim.started')
                secondFeedbackStim.setAutoDraw(True)
            if secondFeedbackStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > secondFeedbackStim.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    secondFeedbackStim.tStop = t  # not accounting for scr refresh
                    secondFeedbackStim.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'secondFeedbackStim.stopped')
                    secondFeedbackStim.setAutoDraw(False)
            # start/stop secondFeedbackAudio
            if secondFeedbackAudio.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                secondFeedbackAudio.frameNStart = frameN  # exact frame index
                secondFeedbackAudio.tStart = t  # local t and not account for scr refresh
                secondFeedbackAudio.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('secondFeedbackAudio.started', tThisFlipGlobal)
                secondFeedbackAudio.play(when=win)  # sync with win flip
            if secondFeedbackAudio.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > secondFeedbackAudio.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    secondFeedbackAudio.tStop = t  # not accounting for scr refresh
                    secondFeedbackAudio.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'secondFeedbackAudio.stopped')
                    secondFeedbackAudio.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in secondFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "secondFeedback" ---
        for thisComponent in secondFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        secondFeedbackAudio.stop()  # ensure sound has stopped at end of routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "pause" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        pauseComponents = [text]
        for thisComponent in pauseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pause" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed playsecondArray * secondArrayRand[0] repeats of 'secondLoop'
    
# completed 5.0 repeats of 'arrayLoop'


# --- Prepare to start Routine "endScreen" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
endScreenText.setText('Monkey ran on AGL phase 3 task!! ' +str(number_correct) + ' correct out of ' + str(number_total) + ' Must be X for X days in a row to pass.')
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
endScreenComponents = [endScreenText, key_resp]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "endScreen" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endScreenText* updates
    if endScreenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endScreenText.frameNStart = frameN  # exact frame index
        endScreenText.tStart = t  # local t and not account for scr refresh
        endScreenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endScreenText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'endScreenText.started')
        endScreenText.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "endScreen" ---
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "endScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "End" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "End" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "End" ---
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
