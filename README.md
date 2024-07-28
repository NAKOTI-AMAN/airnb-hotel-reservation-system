# Airbnb Hotel Reservation System

This repository contains the code for an Airbnb-like hotel reservation system, with separate frontend and backend components. The frontend is built using HTML, CSS, and JavaScript, while the backend is developed using Python. The system offers features such as user authentication, browsing listings, booking places, managing bookings, and handling payments through Stripe.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Features

### For Guests

- **Booking Accommodations**: Guests can request to stay at any place for their desired duration.
- **Approval Process**: Hosts need to approve guest requests.
- **View Pending Requests**: Guests can view the status of their pending requests.
- **Reviews**: Guests can leave reviews for the places they have booked after their stay.
- **Profile Management**: View and manage profile details.
- **View Bookings**: View all bookings under the bookings section.

### For Hosts

- **Listings Management**: Hosts can create and manage up to 10 listings with essential information such as title, subtitle, description, location, rate per day, discounts, cleaning fee, service fee, occupancy taxes, images, and occupancy capacity.
- **Discounts**: Weekly discounts apply if the guest books for more than 5 days; otherwise, daily discounts.
- **Cancellation Policy**: Hosts can decide whether to allow cancellation by guests.
- **Booking Management**: Hosts can manage bookings from the dashboard, including approving or declining requests.
- **Payment Integration**: Secure payment processing through Stripe.
- **Profile Management**: View and manage profile details.

## Technologies Used

### Frontend

- **HTML**: Used for structuring the web pages.
- **CSS**: Used for styling the user interface.
- **JavaScript**: Used for interactive elements and client-server communication.

### Backend

- **Python**: Core programming language used for backend development.
- **Stripe API**: Integrated for secure payment processing.

## Setup

### Frontend

1. Clone the repository.
2. Navigate to the `frontend` directory.
3. Open `index.html` in your preferred web browser.

### Backend

1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
