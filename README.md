**Computer Vision - Object Detection using Binary Image Processing**

---

The assignment was to create a script to prototype the capabilities of the cv2 library when it comes to performing Morphological Transformations.

---

Running Project3.py will load in neuron.jpg(image1) and blood-cells_12.Red-blood-ce.jpg(image2)
and perform the following Morphological Transformations, using the cv2 library, on the images to find the number of objects each photo:
  - Convert the images to binary.
  - Perform closing using a window of 9x9 pixels, and 3x3 pixels respectively.
  - Open image2 with window of 3x3 pixels.
  - Draw contours on image2.
  - Open image2 again with window of 5x5 pixels.
  - Draw contours on image2 again.

---

The script will display the images after each operation. You can press any button to step through each image transformation.
When the script is finished it will print out the number of objects it has calculated in each image.
