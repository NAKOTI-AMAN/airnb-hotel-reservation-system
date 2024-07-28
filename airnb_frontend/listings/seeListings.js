let listings = document.querySelector(".listings");
let booking_page = document.querySelector(".booking-page");
let check_in = document.querySelector(".check-in-date");
let check_out = document.querySelector(".check-out-date");
let guests = document.querySelector(".guests");
let token = localStorage.getItem("token");
let user_id = localStorage.getItem("user_id");
let listingId;

async function payment(token, booking_id) {
  const response = await fetch("http://0.0.0.0:5500/API/V1/payments", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: token },
    body: JSON.stringify({
      booking_id: booking_id,
    }),
  });
  if (response.ok) {
    const data = await response.json();
    if (data.payment_url) {
      window.location.href = data.payment_url;
    }
  }
}
async function create_booking(
  token,
  user_id,
  place_id,
  check_in,
  check_out,
  guests
) {
  const response = await fetch("http://0.0.0.0:5500/API/V1/book-place", {
    method: "POST",
    headers: { "Content-Type": "application/json", Authorization: token },
    body: JSON.stringify({
      guest_id: user_id,
      place_id: place_id,
      check_in: check_in,
      check_out: check_out,
      guests: guests,
    }),
  });
  if (response.ok) {
    const data = await response.json();

    payment(token, data.booking_id);
  }
}

async function show_listings() {
  try {
    const response = await fetch(
      "http://0.0.0.0:5500/API/V1/show-all-listings",
      {
        method: "GET",
      }
    );

    if (response.ok) {
      const data = await response.json();
      console.log(data);
      display_listings(data);
    } else {
      console.error("Failed to fetch listings:", response.status);
    }
  } catch (error) {
    console.error("Error fetching listings:", error);
  }
}

function display_listings(listingsData) {
  const listingsContainer = document.querySelector(".listings");

  listingsData.forEach((listing) => {
    const listingElement = create_listing_element(listing);
    listingsContainer.appendChild(listingElement);
  });
}

function create_listing_element(listing) {
  const listingElement = document.createElement("div");
  listingElement.classList.add("listing");

  listingElement.dataset.listingId = listing.listing_id;

  const listingElementLeft = document.createElement("div");
  listingElementLeft.classList.add("listing-left");
  listingElement.appendChild(listingElementLeft);

  const listingElementRight = document.createElement("div");
  listingElementRight.classList.add("listing-right");
  listingElement.appendChild(listingElementRight);

  const image = document.createElement("img");
  image.src = `../../airnb_backend/${listing.image}`;
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
  rate.innerText = `₹${listing.rate}/day`;
  listingElementRight.appendChild(rate);

  const book = document.createElement("button");
  book.innerText = "Book";
  book.classList.add("book-button");
  listingElementRight.appendChild(book);

  return listingElement;
}

document.addEventListener("DOMContentLoaded", () => {
  show_listings();
  document.querySelector(".listings").addEventListener("click", (event) => {
    if (event.target.classList.contains("book-button")) {
      const listingElement = event.target.closest(".listing");
      if (listingElement) {
        listingId = listingElement.dataset.listingId;
        if (localStorage.getItem("token")) {
          booking_page.style.display = "flex";
        } else {
          alert("please login first");
        }
      }
    }
  });
  document.querySelector(".close-book").addEventListener("click", () => {
    booking_page.style.display = "none";
    check_in.innerHTML = "";
    check_out.innerHTML = "";
    guests.innerHTML = "";
  });
});
function book() {
  create_booking(
    token,
    parseInt(user_id),
    parseInt(listingId),
    check_in.value,
    check_out.value,
    parseInt(guests.value)
  );
  check_in.innerHTML = "";
  check_out.innerHTML = "";
  guests.innerHTML = "";
  booking_page.style.display = "none";
}