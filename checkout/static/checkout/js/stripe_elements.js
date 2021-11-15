let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
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


// Will handle the form submit

let form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            let errorLine = document.getElementById('card-errors');
            let html = 
                `<span>
                <p class="text-danger fw-bolder">${result.error.message}</p>
                </span>`;
            $(errorLine).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit()
            }
        }
    });
});
