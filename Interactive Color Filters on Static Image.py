import cv2
import numpy as np
import urllib.request


def load_dummy_image():
    """Load a dummy image from an online placeholder service."""
    url = "https://via.placeholder.com/600x400"
    resp = urllib.request.urlopen(url)
    img_arr = np.asarray(bytearray(resp.read()), dtype=np.uint8)
    image = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    return image


def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    
    # Create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    if filter_type == "red_tint":
        # Keep only red channel
        filtered_image[:, :, 0] = 0  # Blue
        filtered_image[:, :, 1] = 0  # Green

    elif filter_type == "blue_tint":
        # Keep only blue channel
        filtered_image[:, :, 1] = 0  # Green
        filtered_image[:, :, 2] = 0  # Red

    elif filter_type == "green_tint":
        # Keep only green channel
        filtered_image[:, :, 0] = 0  # Blue
        filtered_image[:, :, 2] = 0  # Red

    elif filter_type == "increase_red":
        # Increase red intensity
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_blue":
        # Decrease blue intensity
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)

    return filtered_image


# Load dummy image instead of example.jpg
image = load_dummy_image()

if image is None:
    print("Error: Could not load image!")
else:
    filter_type = "original"  # starting filter

    print("Press the following keys to apply filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red Intensity")
    print("d - Decrease Blue Intensity")
    print("q - Quit")

    while True:
        # Apply the selected filter
        filtered_image = apply_color_filter(image, filter_type)

        # Display the filtered image
        cv2.imshow("Filtered Image", filtered_image)

        # Wait for key press
        key = cv2.waitKey(0) & 0xFF

        # Map key presses to filter types
        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Use 'r', 'b', 'g', 'i', 'd', or 'q'.")


cv2.destroyAllWindows()

