let hamburger = document.querySelector(".hamburger");
let profile_drop = document.querySelector(".profile-drop");
let close_ham = document.querySelector(".close-hamburger");
let logout = document.querySelector("#logout");
const token = localStorage.getItem("token");
const host_id= localStorage.getItem("user_id");
let user_id = document.querySelector(".id-detail");
let user_name = document.querySelector(".name-detail");
let user_mail = document.querySelector(".mail-detail");
let user_type = document.querySelector(".role-detail");
let user_details = document.querySelector(".profile-left-top");
let booking_view = document.querySelector(".profile-left-bottom");
let host_listings=document.querySelector('.host-listings');

user_details.addEventListener("click", () => {
  document.querySelector(".bookings").style.display = "none";
  document.querySelector(".profile-right-details").style.display = "flex";
  document.querySelector(".my-listings").style.display = "none";
  document.querySelector(".profile").style.height="100vh";
  document.querySelector(".profile-left").style.border="1px solid black";
});

booking_view.addEventListener("click", () => {
  document.querySelector(".bookings").style.display = "flex";
  document.querySelector(".profile-right-details").style.display = "none";
});

host_listings.addEventListener('click', ()=>{
  document.querySelector(".profile-right-details").style.display = "none";
  document.querySelector(".my-listings").style.display = "flex";
  document.querySelector(".profile").style.height="auto";
  document.querySelector(".profile-left").style.border="none";
})
logout.addEventListener("click", () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user_id");
  localStorage.removeItem("user_type");
  hamburger.style.display = "none";
});

profile_drop.addEventListener("click", () => {
  hamburger.style.display = "flex";
  logout.style.display = "flex";
});

close_ham.addEventListener("click", () => {
  hamburger.style.display = "none";
});

async function see_bookings() {
  const token = localStorage.getItem("token");
  const guest_id = localStorage.getItem("user_id");
  const response = await fetch(
    `http://0.0.0.0:5500/API/V1/my-bookings?guest_id=${guest_id}`,
    {
      method: "GET",
      headers: { "Content-Type": "application/json", Authorization: token },
    }
  );
  if (response.ok) {
    const data = await response.json();
    console.log(data);
    display_bookings(data);
    
  }
}

function display_bookings(bookingsData) {
  const bookingsContainer = document.querySelector(".booking-bottom");

  bookingsData.forEach((booking) => {
    const bookingElement = create_booking_element(booking);
    bookingsContainer.appendChild(bookingElement);
  });
}

function create_booking_element(booking) {
  const bookingElement = document.createElement("div");
  bookingElement.classList.add("booking-bottom-element");

  const booking_id_field = document.createElement("div");
  booking_id_field.innerHTML = `${booking.booking_id}`;
  bookingElement.appendChild(booking_id_field);

  const hotel_field = document.createElement("div");
  hotel_field.innerHTML = `${booking.place_title}`;
  bookingElement.appendChild(hotel_field);

  const guests_field = document.createElement("div");
  guests_field.innerHTML = `${booking.guests}`;
  bookingElement.appendChild(guests_field);

  const checkin_field = document.createElement("div");
  checkin_field.innerHTML = `${booking.check_in}`;
  bookingElement.appendChild(checkin_field);

  const checkout_field = document.createElement("div");
  checkout_field.innerHTML = `${booking.check_out}`;
  bookingElement.appendChild(checkout_field);

  const amount_field = document.createElement("div");
  amount_field.innerHTML = `${booking.amount_sum}`;
  bookingElement.appendChild(amount_field);

  const status_field = document.createElement("div");
  status_field.innerHTML = `${booking.status}`;
  bookingElement.appendChild(status_field);

  return bookingElement;
}

async function get_details(token) {
  const response = await fetch(
    `http://0.0.0.0:5500//API/V1/get-details?token=${token}`,
    {
      method: "GET",
    }
  );
  if (response.ok) {
    console.log(response);
    const data = await response.json();
    console.log(data);
    user_id.innerHTML = data.user_id;
    user_name.innerHTML = data.username;
    user_mail.innerHTML = data.email;
    user_type.innerHTML = data.user_type;
    
  }
}

function display_listings(listingsData) {
  const listingsContainer = document.querySelector(".my-listings");

  listingsData.forEach((listing) => {
    const listingElement = create_listing_element(listing);
    listingsContainer.appendChild(listingElement);
  });
}

function create_listing_element(listing) {
  const listingElement = document.createElement("div");
  listingElement.classList.add("my-listing");


  const listingElementLeft = document.createElement("div");
  listingElementLeft.classList.add("my-listing-left");
  listingElement.appendChild(listingElementLeft);

  const listingElementRight = document.createElement("div");
  listingElementRight.classList.add("my-listing-right");
  listingElement.appendChild(listingElementRight);

  const image = document.createElement("img");
  image.src = `../../airnb_backend/${listing.images}`;
  listingElementLeft.appendChild(image);

  const title = document.createElement("h2");
  title.innerText = `${listing.title}`;
  listingElementRight.appendChild(title);

  const subtitle = document.createElement("p");
  subtitle.innerText = `${listing.subtitle}`;
  listingElementRight.appendChild(subtitle);

  const description = document.createElement("p");
  description.innerText = `${listing.description}`;
  listingElementRight.appendChild(description);

  const location = document.createElement("p");
  location.innerText = `Location: ${listing.location}`;
  listingElementRight.appendChild(location);

  const rate = document.createElement("p");
  rate.innerText = `Rate: ₹${listing.rate}/day`;
  listingElementRight.appendChild(rate);

  const day_discount=document.createElement("p");
  day_discount.innerText= `Daily Discount: ₹${listing.day_discount}`
  listingElementRight.appendChild(day_discount);

  const weekly_discount=document.createElement("p");
  weekly_discount.innerText= `Weekly Discount: ₹${listing.weekly_discount}`
  listingElementRight.appendChild(weekly_discount);

  const cleaning_fee=document.createElement("p");
  cleaning_fee.innerText= `Cleaning Fee: ₹${listing.cleaning_fee}`
  listingElementRight.appendChild(cleaning_fee);

  const service_fee=document.createElement("p");
  service_fee.innerText= `Service Fee: ₹${listing.service_fee}`
  listingElementRight.appendChild(service_fee);

  const occupancy=document.createElement("p");
  occupancy.innerText= `Occupancy: ₹${listing.occupancy}`
  listingElementRight.appendChild(occupancy);

  const cancellation=document.createElement("p");
  cancellation.innerText= `Cancellation: ${listing.Cancellation}`
  listingElementRight.appendChild(cancellation);



  return listingElement;
}
async function my_listings(host_id,token){
  const response= await fetch(`http://0.0.0.0:5500/API/V1/my-listings?host_id=${host_id}`,{
    method: 'GET',
    headers: {'Content-Type': 'application/json', Authorization: token},
  })
  if(response.ok){
    const data = await response.json();
    console.log(data)
    display_listings(data)
  }
}
document.addEventListener("DOMContentLoaded", () => {
  see_bookings();
  get_details(token);
  my_listings(host_id,token);
  document.querySelector(".bookings").style.display = "none";
  document.querySelector(".profile-right-details").style.display = "flex";
  document.querySelector(".my-listings").style.display = "none";
  if(localStorage.getItem("user_type") ==="Guest"){
    host_listings.style.display= "none";
  }
  else if(localStorage.getItem("user_type")==="Host"){
    booking_view.style.display="none";
  }
});
