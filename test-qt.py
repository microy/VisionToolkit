#! /usr/bin/env python
# -*- coding:utf-8 -*- 



# External dependencies
import sys
from PySide import QtGui
import Vimba
import QtViewer


# Camera serial numbers
camera_1_id = '50-0503323406'
camera_2_id = '50-0503326223'

# Vimba initialization
Vimba.VmbStartup()

# Camera connection
camera_1 = Vimba.VmbCamera( camera_1_id )
camera_2 = Vimba.VmbCamera( camera_2_id )

# Launch QtViewer
app = QtGui.QApplication( sys.argv )
#window = QtViewer.QtStereoViewer( camera_1, camera_2 )
window = QtViewer.QtViewer( camera_1 )
app.exec_()

# Camera disconnection
camera_1.Disconnect()
camera_2.Disconnect()

# Vimba shutdown
Vimba.VmbShutdown()


#~ class Capture( object ) :
#~ 
	#~ def __init__( self ) :
#~ 
		#~ # Vimba initialization
		#~ self.vimba = Vimba.VmbSystem()
		#~ self.vimba.Startup()
#~ 
		#~ # Camera connection
		#~ self.camera = Vimba.VmbCamera( self.vimba )
		#~ self.camera.Connect( '50-0503323406' )
#~ 
		#~ self.capturing = False
#~ 
	#~ def startCapture( self ) :
#~ 
		#~ print "pressed start"
		#~ self.capturing = True
		#~ # Create an OpenCV window
		#~ cv2.namedWindow( self.camera.id_string )
		#~ # Start image acquisition
		#~ self.camera.CaptureStart()
		#~ while self.capturing :
			#~ # Capture an image
			#~ self.camera.CaptureFrame()
			#~ # Resize image for display
			#~ image_live = cv2.resize( self.camera.image, None, fx=0.3, fy=0.3 )
			#~ # Display the image
			#~ cv2.imshow( self.camera.id_string, image_live )
			#~ cv2.waitKey(5)
#~ 
	#~ def endCapture( self ) :
#~ 
		#~ print "pressed End"
		#~ self.capturing = False
		#~ self.camera.CaptureStop()
		#~ cv2.destroyWindow( self.camera.id_string )
#~ 
	#~ def quitCapture( self ) :
#~ 
		#~ print "pressed Quit"
		#~ self.endCapture()
		#~ # Camera disconnection
		#~ self.camera.Disconnect()
		#~ # Vimba shutdown
		#~ self.vimba.Shutdown()
		#~ QtCore.QCoreApplication.quit()
#~ 
#~ 
#~ class Window( QtGui.QWidget ) :
#~ 
	#~ def __init__( self ) :
#~ 
		#~ QtGui.QWidget.__init__( self )
		#~ self.setWindowTitle( 'Camera' )
#~ 
		#~ self.capture = Capture()
#~ 
		#~ self.start_button = QtGui.QPushButton( 'Start', self )
		#~ self.start_button.clicked.connect( self.capture.startCapture )
#~ 
		#~ self.end_button = QtGui.QPushButton( 'End', self )
		#~ self.end_button.clicked.connect( self.capture.endCapture )
#~ 
		#~ self.quit_button = QtGui.QPushButton( 'Quit', self )
		#~ self.quit_button.clicked.connect( self.capture.quitCapture )
#~ 
		#~ vbox = QtGui.QVBoxLayout( self )
		#~ vbox.addWidget( self.start_button )
		#~ vbox.addWidget( self.end_button )
		#~ vbox.addWidget( self.quit_button )
#~ 
		#~ self.setLayout( vbox )
		#~ self.setGeometry( 100, 100, 200, 200 )
		#~ self.show()
