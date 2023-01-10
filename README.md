# Envision

## Introduction:
This application allows you to experiment with different color schemes and see how they look together in real-time. Whether you are a designer looking to create a cohesive palette for your latest project or a homeowner trying to find the perfect paint colors for your living room, this application will help you visualize how it looks which just a few clicks. Finding real-time area is also supported. 

## How it works: 
-> CANNY EDGE DETECTION 
-> FLOOD FILLING (BFS Approach) 
-> MASK ENHANCEMENT (3x3 min and 9x9 max filters to smoothen out edges)
-> APLHA BLENDING 

For area, asking user to provide reference length on the image using which area per pixel is calculated. Then summation pixel color swapped * area per pixel is used to find out the area of the region color swapped.   

## Use Case # 1:
A painting company can use it to: 

``Interior design``: can be used to help homeowners and interior designers select colors for a room or an entire house. The application can allow users to upload a photo of a room and then "paint" the walls, floor, and other surfaces with different colors to see how the room would look before any actual painting is done.

``Painting and architecture``: can be used by painters and architects to experiment with different color schemes for building exteriors and other large-scale structures.

``Cost Calculation``: the area calculated by application can be used to give an estimate of the cost of the painting, saving a lot of time. 

## Use Case # 2:
An ecommerce website that sells paint or other home improvement products can use application to enhance the customer experience and drive sales. Here are a few ways this can be done:

``Virtual Room Designer``: The application can allow customers to upload a photo of a room they want to paint and then experiment with different colors and paint types to see what the room will look like before they make a purchase. This can help customers make more informed decisions about their paint choices and increase their confidence in their purchase.

``Color Matching``: The application can be integrated with the website's product catalog, allowing customers to take a photo of a color they see in another setting, such as on a piece of furniture or in nature, and the application will match the color to the closest paint shades and provide details such as product name and price.

``Save and Share``: The application can allow customers to save and share the virtual room designs they create. This can allow them to easily share their design with friends and family or with a professional designer to get feedback or make suggestions.

``Color Palette``: The application can allow customers to create color palettes and save them for future use. They can also browse pre-existing color palettes created by design experts and other users to get inspiration for their project.

``Special Offers``: The application can provide personalized offers to the customers based on their selection like a bundle of rollers, brushes etc. or a discount on their paint purchase.

Integrating a wall painting application on an ecommerce website can help to increase customer engagement and drive sales by making it easier for customers to visualize the end result of their home improvement projects and make more informed decisions about their paint choices.

## User Interfacec:
<img src="/Images/UI.PNG" width="360"/> <img src="/Images/UI2.png" width="360"/>

## Tests:
<img src="/Images/architecture-building-house.jpg" width="240"/> <img src="/Images/architecture-render-external-design.jpg" width="240"/> <img src="/Images/wall1.jpg" width="240"/> <img src="/Images/wall2.jpg" width="240"/>  <img src="/Images/wall3.jpg" width="240"/> 

## Results:
<img src="/results/image 2.jpg" width="240"/> <img src="/results/image1.jpg" width="240"/> <img src="/results/wall1.png" width="240"/> <img src="/results/wall2.png" width="240"/>  <img src="/results/wall3.png" width="240"/> 


## Area Calculation
This is a test case for calculation area of a small object(sticky notes) whose actual area is about 35 cm square. We will be using the application to find the area closest to the actual value. 

->First the user have to draw a line on the image.

<img src="/Images/reference length.PNG" width="240"/>

-> Then provide the reference length of that line in order to calculate the area of color swapped region. 

<img src="/Images/providing length.PNG" width="240"/>

The area calculated by the application was 33.23 cm square as shown in above image and actual area is 35 cm square. 

## Strengths:
- Fast 
- Realist Blend 
- Preserve Reflections
- Tweaking Options

## Limitations:
- Doesn’t perform well where there are too many edges. 
- For area calculations, the image should be exactly at the angle of 90 degrees to get accurate results.

## Installation 
``python  main.py`` 
