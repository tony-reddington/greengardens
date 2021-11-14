let public_key_for_stripe = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(public_key_for_stripe);
let elements = stripe.elements();


let card = elements.create('card', {
    style: {
      base: {
        iconColor: '#393D3F',
        color: '#393D3F',
        fontWeight: '500',
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#393D3F',
        },
      },
      invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
      },
    },
  });

card.mount('#card-element');

// Handles card element validation errors
card.addEventListener('change', function (event) {
    let errorLine = document.getElementById('card-errors');
    if (event.error) {
        let html = 
        `<span>
        <p class="text-danger fw-bolder">${event.error.message}</p>
        </span>`;
        $(errorLine).html(html);
    } else {
        errorLine.textContent = '';
    }
});
