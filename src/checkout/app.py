
@app.route('/checkout_sca')
def checkout():
  intent = # ... Fetch or create the PaymentIntent
  return render_template('checkout_sca.html', client_secret=intent.client_secret)