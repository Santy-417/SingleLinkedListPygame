import pygame  # Import the library

pygame.init()  # Initialize the library
pygame.font.init()  # Initialize font

# Screen configuration
font = pygame.font.Font(None, 30)  # Font
screen = pygame.display.set_mode((900, 600))  # Render screen size
pygame.display.set_caption('Linked List')  # Window title

# Color palette
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (167, 241, 241)
TITLE = (133, 193, 233)
COLORBACK = (31, 97, 141)

# Node class which will contain the value and pointer of the node
class Node:
    def __init__(self, value, image):
        self.value = value
        self.image = image
        self.next = None

# SingleLinkedList class which will contain methods to interact with the nodes
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_first(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def add_last(self, value, image):
        new_node = Node(value, image)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.length -= 1

    def remove_last(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node
        self.length -= 1


linked_list = SingleLinkedList()  # Instance of linked_list which contains the SingleLinkedList class
clock = pygame.time.Clock()  # Instance of clock that contains the screen update time

# Constants for button positions
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
BUTTON_Y = 300
BUTTON_X_FIRST = 50
BUTTON_X_LAST = 250
BUTTON_X_REMOVE_FIRST = 450
BUTTON_X_REMOVE_LAST = 650

# Create buttons
Button_AddFirst = pygame.Rect(BUTTON_X_FIRST, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
Button_AddFirst_color = BLUE
Button_AddLast = pygame.Rect(BUTTON_X_LAST, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
Button_AddLast_color = BLUE
Button_RemoveFirst = pygame.Rect(BUTTON_X_REMOVE_FIRST, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
Button_RemoveFirst_color = BLUE
Button_RemoveLast = pygame.Rect(BUTTON_X_REMOVE_LAST, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)
Button_RemoveLast_color = BLUE

# Create buttons that contain numbers
number_1 = pygame.Rect(330, 175, 50, 50)
number_2 = pygame.Rect(430, 175, 50, 50)
number_3 = pygame.Rect(530, 175, 50, 50)

# Create the bar that will contain the list update
status_bar = pygame.Rect(100, 410, 700, 80)

# Load images of the numbers
image_paths = [
    "img/Imagen_1.jpg",
    "img/Imagen_2.jpg",
    "img/Imagen_3.jpg"
]
number_images = {}
for i, path in enumerate(image_paths, start=1):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, (50, 50))  # Scale to a fixed size
    number_images[i] = img

# Initialize the loop, colors, and number selection
running = True
color_n1 = BLACK
color_n2 = BLACK
color_n3 = BLACK
selected_number = 0

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            if number_1.collidepoint(mouse_position):
                color_n1, color_n2, color_n3, selected_number = BLUE, BLACK, BLACK, 1
            elif number_2.collidepoint(mouse_position):
                color_n1, color_n2, color_n3, selected_number = BLACK, BLUE, BLACK, 2
            elif number_3.collidepoint(mouse_position):
                color_n1, color_n2, color_n3, selected_number = BLACK, BLACK, BLUE, 3
            elif Button_AddFirst.collidepoint(mouse_position) and selected_number is not None:
                linked_list.add_first(selected_number, number_images[selected_number])
            elif Button_AddLast.collidepoint(mouse_position) and selected_number is not None:
                linked_list.add_last(selected_number, number_images[selected_number])
            elif Button_RemoveFirst.collidepoint(mouse_position):
                linked_list.remove_first()
            elif Button_RemoveLast.collidepoint(mouse_position):
                linked_list.remove_last()

    text_title = font.render("SINGLE LINKED LIST WITH PYGAME", True, BLACK)  # Program title
    text_info = font.render("Select a number and then a method to add it to the list.", True, BLACK)  # Instructions
    text_status_list = font.render("List status: ", True, BLACK)  # List update
    text_footer = font.render(" Made by Santiago Chavarro Osorio. ", True, BLACK)  # Footer text

    screen.fill(COLORBACK)  # Fill background color
    screen.blit(text_title, (290, 50))  # Show program title
    screen.blit(text_info, (120, 120))  # Show usage instructions
    screen.blit(text_status_list, (100, 375))  # Show the bar that updates the list
    screen.blit(text_footer, (275, 550))  # Show footer

    pygame.draw.rect(screen, Button_AddFirst_color, Button_AddFirst)  # Draw button rectangle
    Button_AddFirst_text = font.render("Add to first", True, BLACK)  # Add text to button
    Button_AddFirst_text_rect = Button_AddFirst_text.get_rect(center=Button_AddFirst.center)  # Center text
    screen.blit(Button_AddFirst_text, Button_AddFirst_text_rect)  # Show it on screen

    pygame.draw.rect(screen, Button_AddLast_color, Button_AddLast)  # Draw button rectangle
    Button_AddLast_text = font.render("Add to last", True, BLACK)  # Add text to button
    Button_AddLast_text_rect = Button_AddLast_text.get_rect(center=Button_AddLast.center)  # Center text
    screen.blit(Button_AddLast_text, Button_AddLast_text_rect)  # Show it on screen

    pygame.draw.rect(screen, Button_RemoveFirst_color, Button_RemoveFirst)  # Draw button rectangle
    Button_RemoveFirst_text = font.render("Remove first", True, BLACK)  # Add text to button
    Button_RemoveFirst_text_rect = Button_RemoveFirst_text.get_rect(center=Button_RemoveFirst.center)  # Center text
    screen.blit(Button_RemoveFirst_text, Button_RemoveFirst_text_rect)  # Show it on screen

    pygame.draw.rect(screen, Button_RemoveLast_color, Button_RemoveLast)  # Draw button rectangle
    Button_RemoveLast_text = font.render("Remove last", True, BLACK)  # Add text to button
    Button_RemoveLast_text_rect = Button_RemoveLast_text.get_rect(center=Button_RemoveLast.center)  # Center text
    screen.blit(Button_RemoveLast_text, Button_RemoveLast_text_rect)  # Show it on screen

    pygame.draw.rect(screen, WHITE, status_bar, 0)  # Draw rectangle where the list is rendered and updated

    pygame.draw.rect(screen, color_n1, number_1, 0)  # Draw rectangles where the number images are (image1)
    screen.blit(number_images[1], (335, 180))
    pygame.draw.rect(screen, color_n2, number_2, 0)  # Draw rectangles where the number images are (image2)
    screen.blit(number_images[2], (435, 180))
    pygame.draw.rect(screen, color_n3, number_3, 0)  # Draw rectangles where the number images are (image3)
    screen.blit(number_images[3], (535, 180))

    space = 0  # Initialize a counter to give space to the images
    current_node = linked_list.head  # Initialize current_node as the head of the list
    while current_node is not None:  # While current_node is not None, continue
        if current_node.image is not None:  # If the current node's image is not None, add a new image
            screen.blit(current_node.image, (120 + space, 420))  # Render the current node's image
        space += 75  # Add 75 pixels for the separation between each image
        current_node = current_node.next  # Update current_node to point to the next node

    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Define how fast we want the screen to update

pygame.quit()  # End the program

#Button_AddFisrt_text_rect = Button_AddFisrt_text.get_rect(center=Button_AddFisrt.center)
""" calculates and saves in the variable Button_AddLast_text_rect the 
    rectangle that represents the position and size of the rendered text 
    centered within the button's rectangle. """