import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request


def load_dummy_image():
    """Loads a dummy image from the internet and returns a CV2 image."""
    url = "https://via.placeholder.com/600x400"
    resp = urllib.request.urlopen(url)
    img_arr = np.asarray(bytearray(resp.read()), dtype=np.uint8)
    image = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    return image


def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def interactive_edge_detection():
    """Interactive activity for edge detection and filtering."""
    
    # Load dummy image instead of example.jpg
    image = load_dummy_image()
    
    if image is None:
        print("Error: Could not load the image!")
        return

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            # Sobel Edge Detection
            sobelX = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobelY = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined = cv2.bitwise_or(sobelX.astype(np.uint8), sobelY.astype(np.uint8))
            display_image("Sobel Edge Detection", combined)

        elif choice == "2":
            # Canny Edge Detection
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower = int(input("Enter lower threshold: "))
            upper = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower, upper)
            display_image("Canny Edge Detection", edges)

        elif choice == "3":
            # Laplacian Edge Detection
            lap = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(lap).astype(np.uint8))

        elif choice == "4":
            # Gaussian Smoothing
            print("Enter kernel size (must be odd):")
            k = int(input("Kernel size: "))
            blurred = cv2.GaussianBlur(image, (k, k), 0)
            display_image("Gaussian Smoothed Image", blurred)

        elif choice == "5":
            # Median Filtering
            print("Enter kernel size (odd number):")
            k = int(input("Kernel size: "))
            filtered = cv2.medianBlur(image, k)
            display_image("Median Filtered Image", filtered)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Pick 1 to 6.")


# Run the activity
interactive_edge_detection()
