def load_image(path, size=None):
    """Lataa kuvan ja skaalaa sen tarvittaessa."""
    import pygame
    image = pygame.image.load(path)
    if size:
        image = pygame.transform.scale(image, size)
    return image