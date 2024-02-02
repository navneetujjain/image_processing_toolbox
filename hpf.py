import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_noise(image, noise_level=25):
    noise = np.random.normal(0, noise_level, image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8)

def create_high_pass_kernel(size):
    kernel = np.ones((size, size), np.float32) / (size * size)
    center = (size - 1) // 2
    kernel[center, center] = -1
    return kernel

def apply_high_pass_filter(image, kernel):
    return cv2.filter2D(image, -1, kernel)

def highpass_image(image_path, filter_size=15, noise_level=25):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    noisy_image = add_noise(original_image, noise_level)

    high_pass_kernel = create_high_pass_kernel(filter_size)

    filtered_image = apply_high_pass_filter(noisy_image, high_pass_kernel)

    plt.figure(figsize=(7, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 3, 2)
    plt.imshow(noisy_image, cmap='gray')
    plt.title('Noisy Image')

    plt.subplot(1, 3, 3)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Filtered Image')

    plt.tight_layout()

    plt.show()
