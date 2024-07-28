let image = document.querySelector("#image");
  let blank= document.querySelector("#blank");
  image.onchange= function(){
    blank.src = URL.createObjectURL(image.files[0]);
  }

function create_listings() {
  let token = localStorage.getItem("token");
  let host_id = localStorage.getItem("user_id");
  let title = document.querySelector("#title").value;
  let subtitle = document.querySelector("#subtitle").value;
  let description = document.querySelector("#description").value;
  let location = document.querySelector("#location").value;
  let rate = document.querySelector("#rate").value;
  let dayDiscount = document.querySelector("#dayDiscount").value;
  let weekDiscount = document.querySelector("#weekDiscount").value;
  let cleaningFee = document.querySelector("#cleaningFee").value;
  let serviceFee = document.querySelector("#serviceFee").value;
  let occupancy = document.querySelector("#occupancy").value;
  let cancellation = document.querySelector('input[name="cancellation"]:checked').value;
  let image = document.querySelector("#image");
  
  generate_listing(
    token,
    host_id,
    title,
    subtitle,
    description,
    location,
    rate,
    dayDiscount,
    weekDiscount,
    cleaningFee,
    serviceFee,
    occupancy,
    cancellation,
    image
  );

}

async function generate_listing(
  token,
  host_id,
  title,
  subtitle,
  description,
  location,
  rate,
  dayDiscount,
  weekDiscount,
  cleaningFee,
  serviceFee,
  occupancy,
  cancellation,
  image
) {
  const formData = new FormData();
  formData.append("host_id", host_id);
  formData.append("title", title);
  formData.append("subtitle", subtitle);
  formData.append("description", description);
  formData.append("location", location);
  formData.append("rate", rate);
  formData.append("dayDiscount", dayDiscount);
  formData.append("weekDiscount", weekDiscount);
  formData.append("cleaningFee", cleaningFee);
  formData.append("serviceFee", serviceFee);
  formData.append("occupancy", occupancy);
  formData.append("cancellation", cancellation);
  formData.append('images',image.files[0]);

  const response = await fetch("http://0.0.0.0:5500/API/V1/create-listing", {
    method: "POST",
    headers: { Authorization: token },
    body: formData
  });
  if (response.ok) {
    const data = await response.json();
  }
  if(data){
    alert(data.status);
  }
}
