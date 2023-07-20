<script src="https://js.stripe.com/v3/">
  import { enhance } from "$app/forms";
  import { loadStripe } from "@stripe/stripe-js";

  let stripePromise = loadStripe(
    "sk_test_51NVJiRGxLFc3zCwXgKNjIQd7MVZ7v7DYXWDic8fwAhbKmU2EKFVEiuzIHofq4wWG22GWVTCQYqg0fyOM2DQQBLAw00i07d5S17"
  );

  async function handleSubmit(event) {
    event.preventDefault();
    const stripe = await stripePromise;
    const response = await fetch("/", { method: "POST" });
    const { sessionId } = await response.json();
    stripe.redirectToCheckout({ sessionId });
  }
</script>

<div class="content">
  <aside />
  <main class="order-form">
    <h2>Place Your Order</h2>
    <form action="?/pay" method="post" use:enhance>
      <label>
        Name:
        <input name="name" autocomplete="off" />
      </label>
      <button on:submit={handleSubmit} type="submit">Pay</button>
    </form>
  </main>
  <aside />
</div>

<style>
  .content {
    display: flex;
  }
  .order-form {
    flex: 3;
    display: flex;
    flex-direction: column;
    align-items: center;
    /* justify-content: center; */
    background-color: gainsboro;
  }
  aside {
    flex: 1;
  }
</style>
