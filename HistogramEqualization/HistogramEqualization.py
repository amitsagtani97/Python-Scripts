from PIL import Image
import sys

def histogramEqualization(argv):
	
	picSource = Image.open(argv)
	picDestination = picSource.copy()
	
	# For the sake of simplicity, the picture gets casted to
	# RGB if it isn't yet 
	if picDestination.mode != 'RGB':
		picDestination = picDestination.convert('RGB')
		
	picDestinationArray = picDestination.load()
	width, height = picSource.size
	
	# Determine the maximum and minimum pixel brightness
	histMax, histMin = 1, 256
	for pixelX in range(width):
		for pixelY in range(height):
		# Even though a greyscale picture is expected the image
		# gets loaded as RGB, thus its needed to access any of the
		# seperate colour values, since they should have the same value.
		# If coloured pictures are given, this will result in a greyscale
		# representation and equalization of the red values.
			if picDestinationArray[pixelX, pixelY][0] < histMin:
				histMin = picDestinationArray[pixelX, pixelY][0]
			if picDestinationArray[pixelX, pixelY][0] > histMax:
				histMax = picDestinationArray[pixelX, pixelY][0]
				
	# Apply histogramm equalization formula to every pixel
	for pixelX in range(width):
		for pixelY in range(height):
			newVal = int(256 * ((picDestinationArray[pixelX, pixelY][0] - histMin) / (histMax - histMin)) - 1)
			# Since the picture is loaded as RGB, we need to set the value thrice
			picDestinationArray[pixelX, pixelY] = (newVal, newVal, newVal)

	return picDestination
	
	
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print('Usage: {} <Image File>'.format(sys.argv[0]))
	else:
		picOut = histogramEqualization(sys.argv[1])
		picOut.save('out.bmp')
