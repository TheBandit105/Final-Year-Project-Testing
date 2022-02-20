# Individual Project

This is my individual project for vision-based emotion detection.

## Patch Notes

3 October 2021 - As of currently, the application has not been made yet.

15 October 2021 - Have started working on creating the application for the emotion recognition software for the final year project.

22 October 2021 - Have got a basic menu setup completed where the user can select one of 3 options in the software, which are to run the ERS itself, view the credits of the application and quit the application entirely. Upon clicking the run button for the ERS, the user will be taken to another window, which is currently blank at the moment. The user can now quit the entire application from this window as well.

12 November 2021 - Looked into getting the face detection working first. This was done by getting OpenCV to activate the webcam that was built into my computer. Afterwards, using haarcascade as a reference point for the faces, the rectangle is drawn on the webcam application when a face is detected in range of the camera. It currently works well, but has a bit of a difficult time detecting faces that have obstructions in the way, such as glasses.

19 January 2022 - After struggling to get the emotion detection aspect of the program to work, the program can now detect the emotions when a face comes into view of the webcam. The emotions are displayed on the top left hand corner of the window and are displayed as floating point values in order to get a more accurate reading on the emotions registered. This means that the extent of the types of emotions presented can be more easily deduced and thus make a more accurate judgment on the measurement that was returned at that point.

22 January 2022 - Updated the credits page and added new options for about and the external camera option, but still need to add the functionality for those options.

20 February 2022 - The first prototype of the Emotion Recognition System is officially ready for a quick demo for poster week. Simplified into one start button, so will now detect whether there is an external webcam or not before running. Prints emotions as percentages on the frame, but in the console, will print emotions as decimals to 8 decimal places, as well as frame number and the current time and date. Will now warn the user if they are getting too angry during gameplay. ABOUT page has been updated. Currently working on trying to turn the program into a functional app.