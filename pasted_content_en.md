## Flutter Application Development

The goal of this project is to implement an application with the following characteristics:

*   It should implement the presented low-fidelity prototype.
*   It should follow a commercial design system (Google Material Design).
*   The application should be delivered as a GitHub repository.
*   It should interact with an API (this doesn't need to be implemented; interaction can be mocked using Faker.js or JSON Placeholder).

### Data Server Suggestion

For testing, I suggest using a REST API: Json-Server.

On the product display screen, it must necessarily display 10,000 items. These can be Lego pieces or any other web API we can find (the main objective here is to verify the pagination strategy you are using).

*   It should be possible to use the device's camera.
*   It should be possible to share images with the application.
*   The application should have some type of user control (registration/login/password recovery).
*   The application should have a notification system (notifications implemented only when the application is open).

### Screen and Functionality Suggestions

#### Login / Authentication

The objective of this screen is to allow the user to log in to the application. For this, they must provide their email and password. If the user does not have an account, they should be redirected to the registration screen. This implies the creation of a registration screen as well!

It's interesting that the user can reset their password if they have forgotten it. For this, they must provide their email, and the system should send an email to the user with instructions on how to reset the password. This is one of the possible solutions for the forgotten password problem. My suggestion is to use the OTP (One Time Password) mechanism for sending the email.

#### Main / Product List (Home)

The objective of the Home screen is to display a welcome screen. Think of this screen as the initial screen of a shopping application. It should display a general list of products. Here, the goal is for your application to be able to display up to 10,000 products, but certainly not all at once. I believe the ideal here would be to display 10 products as a suggestion criterion, and a screen to display the products, with the possibility of adding filters, would be interesting.

This screen is also where the user is directed after logging in. It's interesting that they can access other functionalities of the application from this screen.

#### Product Details

On the product details screen, a descriptive text about the product, along with its image, should be displayed to the user. Here, the objective is for the user to be able to view product information, such as price, description, etc. This screen should be accessed from the product list screen.

#### Camera / Add Item

This screen, as simple as it may seem, has several functionalities. First, it offers the possibility of adding a new item to the product list. This functionality alone has a great impact on the application's design, as it requires your application, which will function as a backend, to be able to receive new products. This can be done through an API, which can be implemented with Python, using only the device's local storage to store the products.

Another objective of this screen is to allow the user to take a photo of the product. This can be done using the device's camera. Interacting with the device's hardware is one of the interesting functionalities of application creation.
It's interesting to put some energy into studying how to store the uploaded images. My suggestion is to store them locally in this first iteration.

#### Profile

Here, user information should be displayed. The objective is for the user to be able to view their profile information, such as name, email, phone, etc. This screen should be accessed from the Home screen. However, other navigation strategies can be used. The user should be able to edit their profile information. This can be done through a button that the user can click to edit their profile information. This functionality is not mandatory, but it is interesting for the user. The user should be able to change their password and profile picture.

#### Notifications

Here, the objective is to work with in-app notifications. Any type of notification can be used, such as a notification of a new product added. The objective is for the user to be able to view received notifications. It is up to the developer how the notifications will be displayed. The user should be able to view received notifications.


