# Green Gardens


## The goal of this e-commerce website is to sell garden products to users and provide a blog displaying users with tips and tricks uploaded by the owner. The user will have the ability to login/create an account profile and save their personal information for future purchases and faster checkout.

### User Experience (UX)

#### The user goals will be to:
* Easily navigate through the website.
* Access the website using multiple devices.
* Register and create an account profile to store personal information for future login and faster checkout.
* Buy gardening products.
* Update shopping basket.
* Delete products from shopping basket.
* Checkout and receive confirmation that the order has been placed
* View a blog tips and tricks.


### User Stories

#### As a user, I want - 
* the navigation bar clearly visible, displaying products by category and sub category so I can easily navigate the website.
* the website responsive across devices so I can swap and change devices.
* the page laid out neatly so that I can find information effortlessly with a search bar allowing me to search for product items by name or product detail.
* to create an account profile that will store my personal information for speedy transactions.
* a page displaying all products by sub category.
* the ability to update and remove items from my shopping basket.
* receive confirmation that my order has been placed.
* view tips and tricks on a blog page.

### Site owner goals

#### As the site owner, I want - 
* to provide a simple navigation display making it easy for users to navigate through the website with search bar for users to search items by by name or product detail.
* the website responsive across all major devices.
* to display all products by category and sub categories contained in an expanded navigation bar.
* to give functionality for users to register and create an account profile to store their personal information for speedy transactions.
* to allow users to update and remove items from their shopping bag.
* to give users confirmation that their orders have been placed.
* to provide a blog with gardening tips and tricks.

### Design

#### Colour Scheme
 - The Green color used across the website fits perfectly as the website is selling gardening products and is universally associated with nature. The Yellow was chosen symbolises happiness, warmth and sunshine and brightens up the page as well as making certain elements in the website stand out. The off Black and basic Black were then used for text and borders.

    ![](readme-images-docs/color-scheme.jpg)

#### Typography
 - The font used across the website is 'Monserrat' because it's simple and legible with 'Sans Serif' as the fall back font. The font 'Are You Serious' was used for the Green Gardens name in the header.

 #### Imagery
 - The main image on the website is of foliage and tells in itself what the website sells. The product images were scraped from the Johnstown Garden Centre website.

### Existing Features
   * The website is responsive across all devices.
   * A navbar with Home, Bulbs & Seeds, Garden Care, Plants & Flowers, Pots & Containers dropdown into a mega menu features across all pages listing products by sub-category and collapses to a hamburger button for smaller screen sizes medium and below.
   * The blog nav item brings the user directly to the blog page.
   * A search bar appears in the header across all screen sizes making it simple for users to navigate.
   * The Green Gardens logo also features along the navigation that's visible on every page and when clicked, brings the user back to the home page.
   * An account button gives users the ability to register or login.
   * The basket icon links to the bag/basket page with text beneath calculating the sum as each time an item is added to the bag.
   * A banner displays to users that delivery is free on orders over €30 across all pages.
>>
 * #### Home page
   * A background image takes up the screen below the banner with inspirational text.
   ![Home page responsive image](readme-images-docs/home-responsive-image.png)
 * #### Login page
   * The Login page uses allauth to verify that the user exists by adding the users name/email and password
 * #### Profile page
   * The profile page allows users to store their personal details for speedy checkout or update if required.
   * The stored personal information carries to the checkout page where all they're left to do is enter their name.
 * #### Register page
   * The Register page uses allauth and requires that users enter their email and password twice for verification and also enter a username.
 * #### Products page
   * The products page display each product in cards displaying the product name, image, price with category and sub-category tags.
   * The category/sub-category tags bring the user to all the products the the same either category or sub-category depending on the users need.
   * Clicking on the product image brings the user to the product-info page
 * #### Product-info page
   * The product-info page displays a larger product image with name, price, category/subcategory tags and information about the selected product.
   * An input field with the default value of 1 can be updated depending on the users requirement.
   * Two buttons appear on the page with the 'Continue shopping' button sending the user back to a page displaying all products and an 'Add to basket' button that adds the selected quantity of product to the basket.
   * Once the user adds an item, a sweetify message pops up informing the user that their chosen product has been added to the basket.
   * The product quantity multiplied by the price adds to the current value of the basket and displays below the basket icon in the header.
   * The page is fully responsive and the layout changes on smaller screens.
 * #### Bag/basket page
   * The bag/basket page displays each product image, name, price, quantity within an input depending on the users selection and a subtotal which is based on the quantity multiplied by the price.
   * The user has the ability to update or delete each product in the bag using the buttons below the quantity input field.
   * If either the update or delete button is clicked, the user receives a confirmation Sweetify popup that their chosen action was successful.
   * At the bottom of the page, the sub-total, delivery cost and total to pay is displayed.
   * If the users bag/basket is less than €30, the user is displayed message informing them how much needs to be spend to get free delivery.
   * Two buttons appear on the page with the 'Continue shopping' button sending the user back to a page displaying all products and a 'Secure Checkout' button that adds brings the user to the checkout page.
 * #### Checkout page
   * The checkout page calls for the user to fill in the form
   * The form asks for the users full name. email, phone number, Address line 1 & 2, City or Town, County or State, Postcode or Zipcode.
   * All forms are text inputs but the country field is an option box that requires the user to select their country.
   * Text beneath the form informs the informs the user that in order to save their personal information they should create a new account or login.
   * A stripe payment input appears where the user must enter their card details.
   * If the card details are entered incorrectly for whatever reason a message displays below the card input field.
   * Text appears below the below the card input field as default informing the user how much their card will be charged.
   * Two buttons appear on the checkout page with the 'Back to bag' button sending the user back to their bag page displaying their chosen products and a 'Complete order' button that sends the payment request to Stripe to charge the users card and the user is then directed to the checkout-success page.
 * #### Checkout Success page
   * The checkout success page displays a Sweetify popup confirming that the users order has been successful and this is re-iterated on the page by thanking the user for the order.
   * Text also appears informing the user that their order will be delivered within 5 x business days.
   * A 'continue shopping' button brings the user back to the home page.

### Features for future implimentation
 * Email capabilities to verify email account registration and order confirmations
 * A contact page

## Information Architecture

### Data Storage

![](readme-images-docs/information-architecture/category.JPG)
![](readme-images-docs/information-architecture/subcategory.JPG)
![](readme-images-docs/information-architecture/product.JPG)
>>
![](readme-images-docs/information-architecture/order.JPG)
![](readme-images-docs/information-architecture/orderlineitem.JPG)
![](readme-images-docs/information-architecture/userprofile.JPG)
>>
![](readme-images-docs/information-architecture/blog.JPG)





## Technology Used

### Languages used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

### Frameworks/Libraries and Programs used
1.  [Balsamiq](https://balsamiq.com/)
    - Balsamic was used to build wireframes for the website pages.
2.  [Font Awesome](https://fontawesome.com/)
    - Font awesome was used for the base.html header icons.
3.  [Google fonts](https://fonts.google.com/)
    - The Monserrat & Are You Serious fonts that i used are from Google fonts.
4.  [Istockphoto](https://www.istockphoto.com/)
    - Istockphoto was used for the main background website image.
5.  [Octoparse](https://www.octoparse.com/)
    - Octoparse was used to scrape data from Johnstown Garden Centre to create json database files.
6.  [Befunky photo editor](https://www.befunky.com/)
    - Befunky photo editor was used to resize images.
7.  [Bootstrap](https://getbootstrap.com/)
    - Bootstrap was used across the full website to style and make the website responsive across different device sizes.
8.  [Coolers](https://coolors.co/)
    - Coolers was used to help generate a colour palette for the entire site.
9.  [Favicon](https://favicon.io/)
    - Favicon.io was used to create the website favicon.
10. [Bootstrap Menu](https://bootstrap-menu.com/detail-megamenu.html)
    - Bootstrap Menu was used to help create a mega menu within the header.
11. [Gitpod](https://gitpod.io/)
    - Gitpod was used to write the website code.
12. [GitHub](https://github.com/)
    - GitHub was used to host the code and website contents.